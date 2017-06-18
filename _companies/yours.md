---
title: Yours 
seotitle: Yours 
img: /images/company/yours.png
---

## What is Yours?

People who create, discover and moderate good content should be paid for their work, but most social platforms do not have any monetization mechanism for their users. Furthermore, the status quo of free, ad-funded content on the internet has incentivized low quality, false, hateful content and poor curation. Yours is a social platform with peer-to-peer monetization so that our users earn money for creating and discovering good content and consumers can pay for quality and curation. 

We do not have or need advertisements; our business model is to take a percentage of payments. Our payment models are based on market economics analogous to the physical economy. Our technology is based on a smart contract network on bitcoin for truly zero marginal cost non-custodial peer-to-peer micropayments, the first such technology for a consumer application on the web. We have a prototype and are working with our users to help us iterate towards launch.

## The Problem

We are solving two related problems: A product problem and a technology problem.

The Product Problem: Facebook, reddit, and most other social media sites have no monetization mechanism for their users. Most of them that do, like YouTube, are based on ads, which are inappropriate for most content types, often irritate consumers, and incentivize clickbait, fake news and trolling. 

Some creators have success using Patreon as a third-party monetization system, but the barrier to use Patreon is much higher than platforms with monetization built-in, and Patreon is also primarily based on voluntary tipping where the payer does not have a strong incentive to make payments, leading to reduced payments to creators and decreased content value for consumers. 

Yours is a social platform with built-in peer-to-peer payments that provides incentives for consumers to make payments to creators, discoverers, and moderators, so that consumers get higher quality content and the others earn money for the value they create.

The Technology Problem: From the 1970s to the mid-1990s it was not possible to make payments on the internet. In the mid-1990s it became possible to use credit cards on the internet, but credit cards only enabled user-to-merchant payments and not user-to-user payments. PayPal was the first user-to-user payment system and it is still useful today for that purpose. 

However, PayPal has problems that make it inappropriate for most content types: 1) Fees are too high at around 30 cents or more per transaction, and 2) Regulatory burdens and banking partnership limitations prevent many users around the world from sending payments to each other. The latter problem is solved by bitcoin. 

The former problem is solved by building a smart contract network on top of bitcoin that only settles to the blockchain, and therefore incurs a fee, when a user wishes to settle. While off-chain, such a smart contract network has zero fees. That is how the Yours payment system works. It is the first peer-to-peer micropayments system on the web.

There are other problems that are solved by proxy, for example:

Automation is ending many jobs. Yours empowers anyone anywhere to learn entrepreneurship as an alternative to labor.

Many newspapers and other forms of traditional media have not figured out how to monetize in the digital era. Yours provides an alternative to advertisements.

## Payment Models & Market

Yours is similar to other social products in that it allows users to sign up, to post content, curate content, and moderate content. The critical difference is that every user of Yours has a micropayments wallet, and many actions on the product involve payments. We have designed many different payment models suitable for different use cases. 

At launch, we will support only a minimal number of payment models sufficient to satisfy the needs of our early users. The payment models have a strong market component, allowing users to set critical rules such as the quantity of payment since the users know their audience better than we do.

The simplest payment model is the purchase model. Consider an author of a short story. The author has written an engaging short story with a compelling cliff hanger 4/5ths of the way through. The author draws a pay wall at the 4/5ths point and charges 10 cents to read the rest of the story. The author knows their audience and is sure their readers are willing to pay this amount to read the conclusion. 

Readers know the story will cost 10 cents going in, but also expect to be able to read part of the story before committing 10 cents. The author earns money directly from their users via peer-to-peer payments of 10 cents per read. The users can ask for a refund if they did not like the conclusion. The same model can also work for audio and video. It can also work for images if the preview is low resolution, black and white, cropped, or containing a watermark. The consumers are paying for access to the full version of the content.

Another model is the endorsement model. While the purchase model is intended for creators, the endorsement model is intended for discoverers. Next to each piece of content is a button called the endorsement button, analogous to the reddit upvote button. Clicking this button makes a 10 cent payment. If a user is the first endorser, the endorsement goes to the creator. Subsequent endorsements are divided evenly amongst earlier endorsers. 

For instance, the third endorser pays 3.3 cents to the creator, 3.3 cents to the first endorser, and 3.3 cents to the second endorser. The more endorsements a piece of content has, the more visibility it has on the page. Although the creator earns only a small fraction of the payments, the creator benefits from improved visibility if the content is highly endorsed. Endorsers are incentivized to pay because they will profit from endorsing popular content early on.

A third payment model is the comment model. In this model, the creator decides the cost of a comment on their content. The author may choose a cost of zero cents, which is the same as comments on most existing social products, which produces very low quality density comments. The author may choose a minimum fee of 5 cents for a comment, with voluntary higher payments producing higher visibility in the comment section. 

As usual, the author knows their audience better than we do, and they will pick a price suitable to their audience that generates the level of discussion they are looking for. The author will earn more money from content that generates discussion. The incentives in this case are to write either controversial content or very popular content so that commenters gain more from the visibility of their content than their time writing it or the cost of posting it.

It is easy to brainstorm many alternative payment schemes. Who pays? How much do they pay? When do they pay? What are they paying for? All of these variables can be tuned for different use cases. When in doubt, we turn to the market, i.e. our users, to make the decisions about these variables in cases where they know better than we do (which is most of the time). 

Our strongest feature are subcommunities, again analogous to reddit, where moderators have full control over what the allowed payment models are and what portion of the payments they themselves receive, incentivizing a choice of rules appropriate for their community. 

Moderators that pick good rules create more successful communities and earn more money. For instance, a photography community may require that every piece of content is an image, that they cost at least 25 cents to view the full resolution version, endorsing costs at least 10 cents, and comments cost at least 100 cents, to minimize trolling.

We will launch with a subset of payment models and will iterate over time based on the feedback from our community about which models are priorities.

##  Technology

After announcing our first prototype in April, 2016, it was clear we had a problem. The prototype was based on normal bitcoin transactions, not a smart contract network, and bitcoin fees were 5 cents and rising, too high for the expected value of payments on the product. We spent the next nine months developing our micropayments solution on top of bitcoin. As of January, 2017 we have integrated our micropayments solution back into the social product and are beginning to develop and refine the user experience in collaboration with our community to prepare for launch.

The way our solution works is as follows. The smart contract network consists of many nodes. A user is a node. The nodes can open payment channels to each other, which allow one-way payment updates to occur off-chain, but which require an on-chain funding transaction. 

The nodes update the commitment transactions to send larger payments and revoke earlier commitment transactions when they do so so that only the latest commitment transaction is valid. When a user wishes to cash out, they broadcast the latest commitment transaction. They then wait two days to spend the commitment transaction. Our solution is similar to, but not equivalent to, the Lightning Network.

## Company

Yours Cofounder & CEO Ryan X. Charles was the cryptocurrency engineer at reddit during a turbulent period in reddit’s history. The cryptocurrency project at reddit did not work out, but after writing the popular article Fix reddit with bitcoin, it was clear there was interest in the idea outside of reddit. 

The project was initially an open-source community-driven project. After about six months Ryan was joined by Clemens Ley, PhD, as Cofounder & CTO, and Yours was incorporated. Clemens Ley has a PhD in computer science from Oxford and is the founder Hapori, a social product with bitcoin payments, a spiritual predecessor to Yours.

Yours has received angel funding totaling $177.5k from investors including DCG, Boost VC, Gaiax, and a number of individual angels. We have over 6000 people on our mailing list, 2000 followers on Twitter, and 700 people on our Slack group.

## Venture Capital Rounds

{% for company in site.data.companies %}
{% if company.company == 'Yours' %}
{% include company_list.html %}
{% endif %}
{% endfor %}