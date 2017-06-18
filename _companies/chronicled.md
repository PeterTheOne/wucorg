---
title: Chronicled
seotitle: Chronicled
img: /images/company/chronicled.png
---

<a href="https://www.chronicled.com/">Chronicled</a> has Secure identities, trusted IoT data, and automated business logic.

## Trusted Identities

We provision cryptographic identities for physical things

## Data Provenance

We sign sensor data and log to blockchain to secure data provenance

## Automation

We automate business processes with smart contracts

## Venture Capital Rounds

{% for company in site.data.companies %}
{% if company.company == 'Chronicled' %}
{% include company_list.html %}
{% endif %}
{% endfor %}
