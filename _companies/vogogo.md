---
title: Vogogo
seotitle: Vogogo
img: /images/company/vogogo.png
---

<a href="https://www.vogogo.com/">Vogogo</a> is a publicly traded technology company on the TSX.V.

## ANNOUNCEMENT

Vogogo has formed a special committee of members from its board of directors to consider strategic alternatives. These may include, but are not limited to: the sale of assets to another firm; a strategic vend-in, amalgamation, reverse amalgamation or similar transaction; or a strategic business combination, or strategic partnership.

## Venture Capital Rounds

{% for company in site.data.companies %}
{% if company.company == 'Vogogo' %}
{% include company_list.html %}
{% endif %}
{% endfor %}
