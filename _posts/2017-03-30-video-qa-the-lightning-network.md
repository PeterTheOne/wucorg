---
layout: post
title: Video - Bitcoin Q and A The Lightning Network
description: Video - Bitcoin Q and A The Lightning Network
author: Andreas M. Antonopoulos
authorurl: /andreas-antonopoulos-bitcoin-expert/
published: true
---

<p>This is part of a keynote talk which took place on October 19th 2016 during the <a href="/what-is-immutability">Bitcoin Wednesday Meetup</a> at the Eye Film Museum in Amsterdam, Netherlands.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/vPnO9ExJ50A?list=PLPQwGV1aLnTsHvzevl9BAUlfsfwFfU7aP" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

1. The Lightning Network's trustless anonymity

Assignment of claims, a series of IOUs / forward-looking promises. You don't have to trust any of the partcipants in between, and if it's implemented properly you have no idea who the other participants are. Onion routing like Tor, i.e. one-hop information, with encrypted connections, with no idea if a person started the transaction or is relaying it from someone else, or if the person you're sending it to is the end or another relay. Increases for privacy and anonymity.

2. Smart contracts using multisignatures, opcodes, hashed timelock contracts (HTLC) 1:58

3. Incentives for intermediaries

Participating in the network, collecting very small fees. Routing to give the lowest fee or lowest latency. Transaction fees will be on a different scale: close to the marginal cost of delivering that service. Anyone charging high fees will be pushed out of the market. 

4. If you use a less costly route with more hops, won't that introduce more settlement costs on the blockchain?

No. By adding more hops, you're cancelling out bilateral obligations for parties involved in the hops. It will reduce settlements on the blockchain.

5. Effect on on-chain transaction fees for miners & decentralisation

Anchor and settlement transactions. This doesn't change that Bitcoin Core layer will need to be scaled - we'll do scaling on both.

6. Will the Lightning Network be compatible with BU?

That is up to them to decide. SegWit. You can also run the Lightning Network on top of Ethereum, or any cryptocurrency that enables the checking of hashes, multisgnature contracts, and time-based controls.
