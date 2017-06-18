---
title: Shocard
seotitle: Shocard
img: /images/company/shocard.png
---

<a href="https://shocard.com/">ShoCard</a> is digital identity that protects consumer privacy and is as easy to use as showing a;driver’s license. It’s optimized for mobile and so secure that a bank can rely on it.

## Helping banks and online retailers authenticate users

Financial services spend a lot of time and money qualifying individuals–proving a user’s identity online can be a tricky business, passwords are hard to remember and easy to steal. With ShoCard, an institution could qualify an individual for a particular qualification (e.g., credit score > 700). The user is given the credit score and it’s saved locally on their phone and that individual’s certification is hashed and then digitally signed by the banks private key and placed onto the blockchain so that any other associated institution could then be passed that certification by the customer.

## Venture Capital Rounds

{% for company in site.data.companies %}
{% if company.company == 'Shocard' %}
{% include company_list.html %}
{% endif %}
{% endfor %}
