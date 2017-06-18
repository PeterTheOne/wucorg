---
title: Brave  
seotitle: Brave
img: /images/company/brave.png
---

##  What is Brave Payments?

<a href="https://brave.com">Brave</a> Payments is a payment system that allows Brave to truly anonymize the data associated with your browsing. This means that Brave does not know which Bitcoin wallet is associated with the lists of sites that you choose to support. In other words - you, the user, have access to your browsing report but Brave (the company) does not have that information.

Brave Payments is more than an anonymization service. It is also the system that does payment reconciliation (makes sure that payments are processed correctly and securely).

## Do I have to pay Brave to go ad-free?

No, you do not have to pay Brave to go ad-free, as we have a complimentary ad-free mode. We do encourage users to support publishers and their favorite sites via our paid ad-free mode, but welcome all user profiles to Brave.

## How much personally identifying information does Brave Payments collect about its users?

None, except for the unlinkable and optional step by a user who verifies their Brave wallet in order to receive payments. They would then need to create an account through our partner BitGo - in that case information such as email and phone number is collected and stored by BitGo in order to authorize your wallet.

Brave Payments uses a technology called Anonize that permits anonymous-but-accountable transactions. Here's an analogy from the real world: someone walks into a polling place, identifies themselves, and gets a ballot and an envelope. They go into a voting booth, mark the ballot, put the ballot in the envelope, and seal it. They then drop the envelope in a ballot box. 

The people running the polling place and counting the ballots know that each person putting an envelope in the ballot box is authorized to vote, but they aren't able to determine which envelope in the ballot box goes with which person. In the case of anonize, a special branch of cryptography called "Zero Knowledge Proofs" are used to get the same functionality.

## How does replacing ads with ads help the user experience?

We block trackers, that’s a big win compared to the status quo. We also block eyesore ads that won’t be replaced (think of those parasite pictures in image grids at the bottom of pages). We currently replace only certain standard-sized ads, and we aim for higher quality than what would have been served in those spaces. 

So we reduce the total number of ads experienced by the user and increase the quality and relevance, while simultaneously blocking trackers that follow your activity across sites.

##  Are you using the "Acceptable Ads" model?

There are two parts to that model, filter rules and business deals. Take the second first:

We do not use the business model of taking annual fees from advertisers to allow their ads (and trackers for confirmation) to pass unblocked. Our business model does not couple our ad and flat fee based revenue to which ads we block.

We do use some of the filter rules that are associated with “Acceptable Ads” to block known-bad domains and URL patterns; and to block and clean up after HTML-native ads.

## Do you require publishers to partner with you before you replace ads, or else block their ads?

No, we block without reference to any business relationships, and our brand value depends on us doing so. We will not take “pay to play” money from advertisers or publishers, or extort publishers with blocking threats. Our goal is to make better revenue for all publishers, and give users better ads and control of their data.

## Why build a browser and not extensions for top browsers?

Extensions face API and performance limits. Our own browser lets us put our best foot forward on speed and deep integration of private ad-tech. We may do extensions if our users find themselves browsing in other browsers often.

## Why aren’t you using Mozilla’s Gecko engine on laptops?

We were, under a partially sandboxed, multi-process architecture called Graphene. But we did a careful head-to-head comparison and by every measure, Electron/chromium won. We wish Mozilla well, but as a startup, we must use all sound leverage available to us. For web compatibility and in particular Chrome compatibility, this means chromium.

## How do you relieve concerns that you are spyware?

We use all-open source, and we welcome help in auditing our source and verifying our binaries on Debian Linux (verified binaries provably derive from a given version of open source). 

Beyond this lower-level auditing, we will need partners to believe in our anonymous ad attribution and conversion confirmation system. More on this as we build it out in near-term milestones on the road to Brave 1.0.

## With whom are you partnering?

BitGo for Bitcoin wallets and identity services. Fastly for edge caching of ads and our site content.

## Venture Capital Rounds

{% for company in site.data.companies %}
{% if company.company == 'Brave' %}
{% include company_list.html %}
{% endif %}
{% endfor %}
