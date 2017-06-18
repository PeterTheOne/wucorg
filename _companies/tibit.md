---
title: Tibit 
seotitle: Tibit 
img: /images/company/tibit.png
---

The web has amazing content, but right now it's hard for creative people to support their work financially.

<a href="https://tibit.com/">Tibit</a> aims to make it possible for anyone to get paid for their work with just a link.

## Venture Capital Rounds

{% for company in site.data.companies %}
{% if company.company == 'Tibit' %}
{% include company_list.html %}
{% endif %}
{% endfor %}
