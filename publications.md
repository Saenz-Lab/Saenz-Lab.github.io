---
title: Publications
subtitle: Synced from ORCID
layout: page
---

<div class="meta">
  Source: <a href="https://orcid.org/0000-0001-8901-4377" target="_blank" rel="noopener">ORCID 0000-0001-8901-4377</a><br/>
  Last sync: {% if site.data.publications.generated_at %}{{ site.data.publications.generated_at }}{% else %}not yet synced{% endif %}
</div>

<hr/>

{% assign pubs = site.data.publications.items %}
{% if pubs and pubs.size > 0 %}
<table class="table">
  <thead>
    <tr>
      <th style="width:90px;">Year</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
  {% for p in pubs %}
    <tr>
      <td>{{ p.year }}</td>
      <td>
        {% if p.link and p.link != "" %}
          <a href="{{ p.link }}">{{ p.title }}</a>
        {% else %}
          {{ p.title }}
        {% endif %}
        {% if p.journal and p.journal != "" %}
          <div class="meta">{{ p.journal }}</div>
        {% endif %}
        {% if p.doi and p.doi != "" %}
          <div class="meta">DOI: <a href="https://doi.org/{{ p.doi }}">{{ p.doi }}</a></div>
        {% endif %}
      </td>
    </tr>
  {% endfor %}
  </tbody>
</table>
{% else %}
<p>No publications loaded yet. Run the sync workflow once (see below).</p>
{% endif %}
