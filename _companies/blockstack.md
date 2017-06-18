---
title: Blockstack 
seotitle: Blockstack 
img: /images/company/blockstack.png
---

<a href="https://blockstack.org">Blockstack</a> is a new decentralized internet.

With Blockstack, users control their data and apps run on their devices. There are no middlemen, no passwords, no massive data silos to breach, and no services tracking us around the internet.

The applications on blockstack are server-less and decentralized. Developers start by building a single-page application in Javascript, Then, instead of plugging the frontend into a centralized API, they plug into an API run by the user. Developers install a library called 'blockstack.js' and don't have to worry about running servers, maintaining databases, or building out user management systems.

Personal user APIs ship with the Blockstack app and handle everything from identity and authentication to data storage. Applications can request permissions from users and then gain read and write access to user resources.

Data storage is simple and reliable and uses existing cloud infrastructure. Users connect with their Dropbox, Google Drive, etc and data is synced from their local device up to the cloud.

Identity is user-controlled and utilizes the blockchain for secure management of keys, devices and usernames. When users login with apps, they are anonymous by default and use an app-specific key, but their full identity can be revealed and proven at any time. Keys are for signing and encryption and can be changed as devices need to be added or removed.

Under the hood, Blockstack provides a decentralized domain name system (DNS), decentralized public key distribution system, and registry for apps and user identities.

## User empowerment

Build apps that put users in control of their identity and data. Remove data as a liability. Attract users who value their freedom and security.

## No infrastructure

Build apps without databases or server maintainance. Publish apps to the decentralized internet where they will run on user devices and live forever.

## Be paid for open source

New business models enable you to get paid for open source code. Utilize micropayments, blockchain protocols, and more.

## Identity

With Blockstack, users get digital keys that let them own their identity. They sign in to apps locally without remote servers or identity providers.

## Storage

Blockstack's storage system allows users to bring their own storage providers and control their data. Data is encrypted and easily shared between applications.

## Payments

Blockstack uses Bitcoin and other crypto-currencies for simple peer-to-peer payments. Developers can charge for downloads, subscriptions, and more.

## Venture Capital Rounds

{% for company in site.data.companies %}
{% if company.company == 'Blockstack' %}
{% include company_list.html %}
{% endif %}
{% endfor %}