#!/usr/bin/env python3
"""
Fetch public works from ORCID and write _data/publications.json for Jekyll.

- Uses the ORCID Public API endpoint:
  https://pub.orcid.org/v3.0/{orcid}/works  (summary list)
  https://pub.orcid.org/v3.0/{orcid}/work/{put-code}  (details per work)
- Writes a compact JSON file Jekyll can render.
"""

from __future__ import annotations
import json
import os
import re
import sys
import urllib.request
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

ORCID = "0000-0001-8901-4377"
UA = "Saenz-Lab-Website/1.0 (GitHub Actions; publications sync; contact: Saenz-Lab)"

def http_get_json(url: str) -> Dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": UA,
        },
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def safe_get(d: Dict[str, Any], path: List[str], default=None):
    cur: Any = d
    for p in path:
        if not isinstance(cur, dict) or p not in cur:
            return default
        cur = cur[p]
    return cur

def extract_year(work_detail: Dict[str, Any]) -> Optional[int]:
    y = safe_get(work_detail, ["publication-date", "year", "value"])
    if y:
        try:
            return int(y)
        except Exception:
            return None
    return None

def extract_title(work_detail: Dict[str, Any]) -> str:
    title = safe_get(work_detail, ["title", "title", "value"]) or ""
    subtitle = safe_get(work_detail, ["title", "subtitle", "value"]) or ""
    t = title.strip()
    if subtitle.strip():
        t = f"{t}: {subtitle.strip()}"
    return t

def extract_journal(work_detail: Dict[str, Any]) -> str:
    return (safe_get(work_detail, ["journal-title", "value"]) or "").strip()

def extract_type(work_detail: Dict[str, Any]) -> str:
    return (safe_get(work_detail, ["type"]) or "").strip()

def extract_url(work_detail: Dict[str, Any]) -> str:
    return (safe_get(work_detail, ["url", "value"]) or "").strip()

def extract_doi(work_detail: Dict[str, Any]) -> Optional[str]:
    ext_ids = safe_get(work_detail, ["external-ids", "external-id"], default=[]) or []
    for eid in ext_ids:
        if (eid.get("external-id-type") or "").lower() == "doi":
            val = (eid.get("external-id-value") or "").strip()
            if val:
                return val
    return None

def normalize_doi(doi: str) -> str:
    doi = doi.strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.I)
    return doi

def main() -> int:
    # 1) Summary list of works
    works_url = f"https://pub.orcid.org/v3.0/{ORCID}/works"
    works = http_get_json(works_url)

    groups = works.get("group", []) or []
    put_codes: List[int] = []
    for g in groups:
        summaries = g.get("work-summary", []) or []
        for s in summaries:
            pc = s.get("put-code")
            if isinstance(pc, int):
                put_codes.append(pc)

    # 2) Fetch details per put-code (gives DOI, journal, full title, etc.)
    items: List[Dict[str, Any]] = []
    for pc in sorted(set(put_codes), reverse=True):
        detail_url = f"https://pub.orcid.org/v3.0/{ORCID}/work/{pc}"
        try:
            wd = http_get_json(detail_url)
        except Exception:
            # If any single work fails, skip it rather than failing the whole build
            continue

        title = extract_title(wd)
        year = extract_year(wd)
        journal = extract_journal(wd)
        wtype = extract_type(wd)
        url = extract_url(wd)
        doi = extract_doi(wd)
        if doi:
            doi = normalize_doi(doi)

        # Prefer DOI link if URL missing
        link = url
        if not link and doi:
            link = f"https://doi.org/{doi}"

        if not title:
            continue

        items.append(
            {
                "title": title,
                "year": year,
                "journal": journal,
                "type": wtype,
                "doi": doi,
                "link": link,
            }
        )

    # Sort: year desc, then title
    def sort_key(x: Dict[str, Any]) -> Tuple[int, str]:
        y = x.get("year") or 0
        return (y, x.get("title", ""))

    items = sorted(items, key=sort_key, reverse=True)

    out = {
        "orcid": ORCID,
        "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "items": items,
    }

    os.makedirs("_data", exist_ok=True)
    with open("_data/publications.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
