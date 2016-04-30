---
title: Ciphrex
img: /images/company/ciphrex.png
---
[Ciphrex](https://ciphrex.com/) builds infrastructure and enterprise-grade software for Bitcoin and blockchain technology. It was founded by [Eric Lombrozo](/eric-lombrozo/) and Enrique Lombrozo in 2013. 

## mSIGNA

[mSIGNA](https://ciphrex.com/mSIGNA%20DnLd-MR.pdf) is a secure, multisignature Bitcoin wallet and one of Ciphrex's two products. Using multisig technology, mSIGNA makes it easy to create shared accounts or use the same account across multiple devices. Wallets can be stored on an offline computer, and are easy to backup. It also runs on top of [Bitcoin Core](/bitcoin-core/), meaning it does not rely on external or third-party servers for transaction data. 

## CoinSocket

[CoinSocket](https://ciphrex.com/CoinSocket%20DnLd-MR.pdf) makes it easy to manage and secure multisignature Bitcoin accounts and transactions within organizations and groups. 

## Venture Capital Rounds

{% for company in site.data.companies %}
{% if company.company == 'Ciphrex' %}
{% include company_list.html %}
{% endif %}
{% endfor %}