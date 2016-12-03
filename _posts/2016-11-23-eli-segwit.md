---
layout: post
title: Segwit ELI5 Misinformation FAQ
author: WeUseCoins
authorurl: /
published: true
---

<p>Seeing as there is a lot of FUD and misinformation being spread about Segwit I thought it would be useful to address some of the “issues” and arguments some people bring up when talking about it.
<p>For more detailed information check out the <a href="/what-are-segwit-benefits/">Segwit Benefits</a> and <a href="https://bitcoincore.org/en/2016/10/28/segwit-costs/">Segwit Costs and Risks</a>. <a href="/segregated-witness/">Many companies</a> are already planning on supporting Segregated Witness.
<h2>Segwit is not really a block size increase</h2>
<p>It is a blocksize increase. Miners produce a block every ~10 minutes containing transactions. Before Segwit the maximum size of all the transactions combined was 1MB, after Segwit it can be a maximum of 4MB (1MB base + 3MB witness).
<p><b>2.</b> 1.7 MB is theoretical, it’s still not 2 MB and it will take a long time before we see it being used.
<p>The actual size of a block under Segwit depends on the kind of transactions being included, however the figure of 1.7MB was based on the average transaction profile in January 2015. At the time of writing (Nov 2016), it would be around 2.1MB.
<center><img src="/images/eli-segwit/bitfury-segwit.jpeg" alt="bitfury segwit segregated witness" /></center>
<p>P2SH transactions are the ones that benefit from Segwit. As you can see they have been increasing over time and now account for ~20% of all the transactions on the blockchain. We did see a drop after August, this is due to the Bitfinex hack, however we’re still a lot higher than the start of the year.
<p>Many wallet providers will actively support Segwit once it activates (see section at the bottom of the article).
<p><b>3.</b> What are P2SH transactions?
<p>P2SH transactions are a special kind of transaction type that can unpack complex spending conditions, like requiring 2 of 3 people to sign a transaction to spend it much like a joint account.
<p><b>4.</b> What changes for me? The normal user with normal transactions?
<p>To take advantage of Segwit transactions, users should use a wallet that supports Segwit. Most of wallets and exchanges intend to support segwit transactions. For normal users, there is nothing else to do.
<p><b>5.</b> How will this affect the economics of Bitcoin?
<p>Segwit will make transactions cheaper for users and allow more transactions to fit in per block. It will slow the UTXO set growth and slow the growing burden on full node operators.
<p><b>6.</b> Segwit is an overly complex solution.
<p>Segwit is not an overly complex solution. At its core, it simply relocates transaction signatures, adds script versioning and fixes some serious bugs that exist in the current transaction types. 
<p>As a result, Segwit fixes the long term problem of transaction malleability which prevents more advanced use cases of Bitcoin. It makes bitcoin script more simple and elegant to upgrade and it reduces some burdens on full nodes.
<center><img src="/images/eli-segwit/why-segwit-first.png" alt="why segregated witness first" /></center>
<p>Some people have called segwit a “hack” because it is implemented as a soft fork. The practical differences between soft and hard fork implementation are very minor; however, under a hard fork, every node must upgrade and every software project must be adapted in order to function at all. As a soft fork, nodes can optionally upgrade. 
<p>Wallets and software projects can upgrade at their leisure (and can opt out entirely), so the disruption to the entire ecosystem using a soft fork is much less and does not enforce a hard deadline to either upgrade or be forced off the network.
<p><b>7.</b> What are the other benefits of Segwit?
<p>Segwit fixes transaction malleability, makes Bitcoin easier to upgrade, fixes serious performance issues and allows for bigger blocks in the future. 
<p>Post Segwit, we can introduce new signature types which will both reduce the size of transactions, as well as improve the privacy of users (using Schnorr and signature aggregation).
<p><b>8.</b> What are sidechains good for?
<p>Sidechains are a particularly good for experimentation because bitcoins can be transferred to the sidechain, and back to Bitcoin. If the project fails, no value is lost because the sidechain coins can be sent back to Bitcoin. Sidechains currently do not have a decentralized security model, so are currently more useful for permissioned blockchain projects that require Bitcoin.
<p>Rather than starting an altcoin with it’s own token and risk, sidechains offer an easy onramp and offramp.
<p><b>9.</b> Who supports Segwit (and why?)
<p>On the Bitcoin core website you can see a <a href="/segregated-witness/">list with companies</a> that are ready or preparing for Segwit.
<p><center><img src="/images/eli-segwit/lb-segwit.png" alt="localbitcoins segregated witness" /></center>
<p><center><img src="/images/eli-segwit/electrum-segwit.png" alt="electrum segregated witness" /></center>
<p><center><img src="/images/eli-segwit/bitcoincore-segwit-1.png" alt="bitcoincore segregated witness" /></center>
<p><center><img src="/images/eli-segwit/bitcoincore-segwit-2.png" alt="bitcoincore segregated witness" /></center>
<p><center><img src="/images/eli-segwit/am-segwit.png" alt="andrew miller segregated witness" /></center>
<p><center><img src="/images/eli-segwit/bitgo-segwit.png" alt="bitgo segregated witness" /></center>
<p><center><img src="/images/eli-segwit/ev-segwit.png" alt="erik voorhees segregated witness" /></center>
<p><center><img src="/images/eli-segwit/bitfinex-segwit.png" alt="bitfinex segregated witness" /></center>
<p><center><img src="/images/eli-segwit/sm-segwit.png" alt="samson mow segregated witness" /></center>
<p><center><img src="/images/eli-segwit/bitcoincore-segwit-3.png" alt="bitcoincore segregated witness" /></center>