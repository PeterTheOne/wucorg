---
title: Tierion  
seotitle: Tierion  
img: /images/company/tierion.png
---

Tierion turns the blockchain into a global platform for verifying any data, file, or business process. We see a future where the blockchain is used to verify everything from medical records to online purchases. We’ve started by making an API and tools to collect data and anchor it in the blockchain.

## Getting Started

Tierion makes it easy to create applications that record any data or business process in the blockchain. We want to build a platform that customers love. 

## Hash API

Tierion’s Hash API lets you anchor data to the blockchain while keeping your data private. This API operates independently from the main Tierion application and the Data API. Use of the Hash API is free up to 100 records per second and 1,000 records per hour.

## Data API

The Data API is your primary API for collecting data, and managing Datastores and Records in your account. This API also offers tools to validate Blockchain Receipts.

## Explorer API

The Explorer API allows you to publish data. Datastores within Tierion can be made publicly accessible through the Explorer API. This API allows you to retrieve this public data as well as the Blockchain Receipt for validating that data.

## Blockchain Receipt

Tierion records data in the Bitcoin blockchain in accordance with the Chainpoint standard. Tierion generates a blockchain receipt for each record. This receipt provides irrefutable proof that your data was recorded at a specific time. 

## Venture Capital Rounds

{% for company in site.data.companies %}
{% if company.company == 'Tierion' %}
{% include company_list.html %}
{% endif %}
{% endfor %}
