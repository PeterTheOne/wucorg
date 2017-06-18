---
layout: post
title: BIP 148 - The Beginner's Guide To A User Activated Soft Fork (UASF)
description: August 1, 2017 BIP 148 will go into effect and could have serious implications for the Bitcoin community. Learn how to protect yourself and your money.
author: WeUseCoins
authorurl: /
published: true
toc:
  what: "What Is BIP 148?"
  fork: "Hard v. Soft Fork"
  why: "Why BIP 148?"
  optimistic: "Those optimistic towards BIP 148"
  ambivalent: "Those ambivalent towards BIP 148"
  pessimistic: "Those pessimistic towards BIP 148"
  support: "Current BIP 148 Support"
  what-could-happen-on-august-1-2017: "What could happen on August 1, 2017?"
  prepare: "How do I prepare?"
  additional: "Where can I get more information?"
  scenarios: "Possible scenarios from BIP 148"
  signal: "How do I signal support?"
  wallets: "Wallets Supporting BIP 148"
  hodler: "As A Hodler (Long Term Investor)"
  trader: "As A Bitcoin Trader"
  exchanges: "Exchanges Supporting BIP 148"
  spender: "As A Spender"
  receiver: "As A Receiver"
  miner: "As A Miner"
  third-parties: "Warning About Third Parties"
  saying: "What Are Companies Saying About BIP148?"
  as-third-party: "As A Third Party"
  conclusion: "Conclusion"
  exchange-support: "How An Exchange Supports BIP 148"
---

<p>In a few months, <b>beginning 1 August 2017</b>, there <i>may</i> be some turbulence ahead for the Bitcoin network.
<p>Bitcoin Core full-nodes comprise <a href="http://luke.dashjr.org/programs/bitcoin/files/charts/software.html">more than 95% of the Bitcoin network</a> and are susceptible to <a href="https://nvd.nist.gov/vuln/detail/CVE-2017-9230">CVE-2017-9230</a>. BIP 148 upgraded nodes would fix this security vulnerability.
<p>Don't be scared though since this serious CVE bug and security vulnerability is being intensively reviewed by the technical community. If you run and rely on the most recent version of a <a href="https://bitcoin.org/en/bitcoin-core/">Bitcoin Core full-node</a> then you should be 99% safe (<a href="https://www.reddit.com/r/Bitcoin/comments/6dfz0y/bip_148_the_beginners_guide_to_a_user_activated/di2i6a8/">but for the 1% chance</a>)!
<p>The UASF will result from a fork of Bitcoin Core and <a href="/uasf-guide/#exchanges">BIP 148 coins that will be listed by Bitfinex</a>.
<p>To be clear, you will need to be running <b>two</b> full-nodes: <b>(1)</b> legacy Bitcoin Core and <b>(2)</b> BIP 148 enforcing Bitcoin Core fork. We assume you have an understanding of best practices as outlined in the <a href="https://glacierprotocol.org/">Glacier Protocol</a>.
<p>To help you protect your money, this guide will be frequently updated with the latest developments.
<p>Share this guide with your friends by directing them to: <b>www.uasfguide.com</b>

{% include page-toc.html %}

<p><h2 id="what">What is BIP 148?</h2>
<p>Bitcoin Improvement Proposal (BIP) 148 is a User Activated Soft Fork (UASF) that requires that miners signal for Segregated Witness (SegWit). SegWit readiness is signalled by miners by setting the version number of blocks mined.
<p>Signalling this bit does not mean miners support SegWit, but is a signal for readiness that miners are ready to enforce the rules.
<p>Miners are still allowed to mine blocks that do not support SegWit and are only required to not mine non-standard blocks that spend SegWit transactions along with not building on top of blocks that do this.
<p><b>Beginning 1 August 2017</b>, nodes that enforce BIP 148 will reject any block from miners that do not signal SegWit readiness, along with any block that is built on top of a block that does not signal support.

<p><h2 id="fork">Hard Fork v. Soft Fork</h2>
<p>Bitcoin Core developer Eric Lombrozo can help you understand the <a href="http://www.bitcoin.kn/2016/04/ciphrex-ceo-eric-lombrozo-contrasts-hard-soft-forks/">differences between a hard fork and a soft fork</a>.
<p>Many people do not fully understand the difference between hard and soft forks and the implications for the network and ecosystem.
<p>Hard forks is a permanent divergence in the the block chain, commonly occurs when non-upgraded nodes can’t validate blocks created by upgraded nodes that follow newer consensus rules.
<p>Soft forks is a temporary divergence in the block chain caused by non-upgraded nodes not following new consensus rules
<center><iframe width="700" height="394" src="https://www.youtube.com/embed/pdaXY1OOiWQ" frameborder="0" allowfullscreen=""></iframe></center>

<p><h2 id="why">Why BIP 148?</h2>
<p>This guide is about helping you protect your money by providing objective actionable things to do as a result of BIP 148 and not delving into the political, economic or other reasons.
<p>Additionally, <a href="https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-May/014419.html">BIP 148 would patch the CVE-2017-9230</a> that is currently active in the Bitcoin Core software.
<p>If you want a quick background and reasoning then this <a href="https://medium.com/@rusty_lightning/i-support-uasf-for-segregated-witness-75d9ef286fe5">piece</a> by the extremely respected open-source Linux kernal developer, Rusty Russell, who has been working on the Lighting Network should hit the spot.

<p><h2 id="optimistic">Those optimistic towards BIP 148</h2>
<p><a href="https://www.reddit.com/r/Bitcoin/comments/6bryvu/bitpay_show_any_shred_of_evidence_for_accusation/dhp5zhr/">Long-time Bitcoin Core developer Luke Dashjr</a>.
<p><a href="https://twitter.com/orionwl/status/872800291233693696">Lead Maintainer of Bitcoin Core Wladimir J. van der Laan</a> has signed Bitcoin Core based wallet binaries.
<p><a href="https://medium.com/@elombrozo/why-i-support-bip148-4b4c0a9feb4d">Long-time Bitcoin Core developer Eric Lombrozo</a>.
<p>The infamous <a href="https://pastebin.com/Lp5Djs5R">bearwhale is in favor of BIP 148</a>.

<p><h2 id="ambivalent">Those ambivalent towards BIP 148</h2>
<p>It seems that most community members are ambivalent towards BIP 148.
<p>Trace Mayer and Jeff Berwick discuss BIP 148 and both are ambivalent towards it but think and feel it is important to be prepared for it.
<p><center><iframe width="560" height="315" src="https://www.youtube.com/embed/QjZk7N7RXfA" frameborder="0" allowfullscreen></iframe></center>
<p>Here is an interesting analysis by <a href="https://medium.com/@jimmysong/bitcoin-uasf-and-skin-in-the-game-7695031c5689">Jimmy Song on how BIP 148</a> impacts various actors in the Bitcoin ecosystem.
<p>MadBitcoins interviews Jimmy Song about the UASF and BIP 148.
<p><center><iframe width="560" height="315" src="https://www.youtube.com/embed/63baLa1GoX4" frameborder="0" allowfullscreen></iframe></center>
<p>An article by Nicolas Dorier why all users and businesses should <a href="https://medium.com/@nicolasdorier/love-or-hate-it-but-do-not-ignore-it-52f8dd3c72e9">prepare for BIP 148</a> and a <a href="/images/bip148-decision-tree.png">great decision tree</a>.

<p><h2 id="pessimistic">Those pessimistic towards BIP 148</h2>
<p><a href="https://bitcointalk.org/index.php?topic=1870015.0">Greg Maxwell</a>
<p><a href="https://botbot.me/freenode/bitcoin-core-dev/2017-05-25/?msg=86145297&page=4">Bitcoin Core Dev Meeting</a>

<p><h2 id="support">Current BIP 148 Support</h2>
<p>What really matters in a UASF situation is which chain the economic actors like users, institutions, exchanges, payment processors, etc. support. There is no easy way to quantify this with a decentralized peer-to-peer network.
<p>The <a href="http://www.uasfpool.com">UASF Mining Pool</a> is BIP 148 ready.
<p>This graph represents the total number of full nodes currently signaling BIP 148.
<p><center><img src="http://uasf.saltylemon.org/uasf_bips_all.png"></center>
<p>This graph represents the percentage of total number of full nodes currently signaling BIP 148.
<p><center><img src="http://uasf.saltylemon.org/uasf_percent_all.png"></center>
<p><a href="http://uasf.snel.it/">Block Height Differences</a>

<p><h2 id="what-could-happen-on-august-1-2017">What could happen on 1 August 2017?</h2>
<p>If miners activate SegWit prior to 1 August 2017 then BIP 148 will not be enforced. All users of Bitcoin will remain on the same chain no matter what client they use.
<p>If miners do not activate SegWit then there may be a chain split. A chain split will mean that some users will see a different set of transactions than others.
<p>If the majority of miners enforce BIP 148 then these chain splits will be temporary and eventually all clients will see the same chain and SegWit will activate for all SegWit compatible clients (0.13.1+ for Bitcoin Core).
<p>If the majority of miners do not enforce BIP 148, users that enforce BIP 148 will diverge from users that do not enforce it.
<p>If the majority of miners do start enforcing BIP 148 at a later date then the legacy chain (without BIP 148 enforcement) may be reorganized once the BIP 148 chain has more work.
<p>The users who are running BIP 148 would be undisturbed, but users running legacy clients may see a large amount of history re-written and could lose funds.

<p><h2 id="prepare">How do I prepare for BIP 148 if there is a split?</h2>
<p>The most important thing you can do is perform your own network consensus by <a href="/bitcoin-core/">running a full-node</a> and <a href="/what-is-a-private-key/">creating and storing your own private keys</a>.
<p>This means you will need to run a full-node for the legacy chain, likely <a href="https://bitcoin.org/en/bitcoin-core/">Bitcoin Core</a>, and a full-node for the BIP 148 chain, likely a fork of Bitcoin Core with the BIP 148 rules enforced.
<p>This will put you in <b>firm control</b> of all decisions related to how you interact instead of having some third-party make those decisions for you.
<p>Additionally, it is unknown how the legacy chain or the BIP 148 chain will be labeled.
<p>This could lead to significant confusion in the marketplace so it is important for you to know exactly what you are buying or selling.

<p><h2 id="additional">Where can I get more information?</h2>
<p>Another great resource is: <a href="http://www.uasf.co/">uasf.co</a>

<p><h2 id="scenarios">Possible scenarios from BIP 148</h2>
<p>BIP148 requires support from the economic majority, particularly exchanges and wallets. If this does not occur, node software supporting BIP148 should not be run after August 1st as it will cause a chain split leading to the abandonment of BIP148.
<p>There are strong economic incentives in the Bitcoin system for nodes to cooperate and remain in consensus to prevent chain splits. If the economic majority is signalling as of August 1st, miners have many incentives to follow along.
<p>Not following along would make it difficult to sell coins mined after August 1st as the blocks would not be accepted by the economic majority. Essentially, miners would be producing an altcoin not recognized by users and exchanges, making them less useful and in lower demand.
<p>Some miners could opt to ignore the BIP148 rule and attempt to split the chain, but this would require a majority of miners who would be out of consensus from the rest of the economic majority.
<p>If a majority of hash power follows BIP148, all nodes will follow the chain regardless of if they are running BIP148. Non-compliant blocks will be orphaned. All SegWit nodes will eventually activate SegWit.
<p>If a minority of the hash power (under 51%) follows BIP148, nodes running BIP148 will be fine, but those not running BIP148 will be out of consensus with the rest of the economy. In this scenario, the more of the economy that runs BIP148, the better.
<p>Miners will find it difficult to sell their coins leading economically motivated miners to start enforcing BIP148.

<p><h2 id="signal">How do I signal support?</h2>
<p>If you operate a full-node then you can signal support with your current software. This is a way you can show support without actually upgrading to enforcing BIP 148 rules.
<p>Many users are alter their node’s user agent string to include BIP148.
<p>To signal #BIP148 on <b>Linux</b> or <b>Mac</b> on your node before binaries are released go to Help --> Debug Window --> Console:</p>
<p><code class="highlighter-rouge">echo "uacomment=UASF-SegWit-BIP148" &gt;&gt; ~/.bitcoin/bitcoin.conf &amp;&amp; bitcoin-cli stop &amp;&amp; sleep 5 &amp;&amp; bitcoind</code></p>
<p>
<p>To signal #BIP148 on <b>Windows</b>, you can edit the shortcut for Bitcoin as follows:</p>
<p><img src="/images/windows148.png" alt="bip148" /></p>
<p>You can signal your support in person, great for meetups, conferences, etc., with this <a href="https://denarium.com/product/uasf-hat">UASF hat</a>.

<p><h3 id="wallets">Wallets Supporting BIP 148</h3>
<p>A listing of wallets here does not imply any endorsement of the quality or security of the software.
<p>Put on your big boy or big girl pants and use at your own risk.
<ol>
<li>09 Apr 2017 - <a href="https://segwit.org/user-activated-soft-forks-the-bip-148-alternative-28e87ffdb76f">Electrum</a> - UASF Server: 158.69.102.114 port 50002</li>
<li>09 Apr 2017 - <a href="https://twitter.com/SamouraiWallet/status/851005717070917633">Samourai Wallet</a></li>
<li>11 Apr 2017 - <a href="https://twitter.com/coinkite/status/851822761794260992">Coinkite</a></li>
<li>12 Apr 2017 - <a href="https://twitter.com/CoinomiWallet/status/852130791362637825">Coinomi</a></li>
<li>22 May 2017 - <a href="https://github.com/greenaddress/abcore/issues/40#issuecomment-303118439">GreenAddress</a></li>
<li>24 May 2017 - <a href="https://twitter.com/LedgerHQ/status/867438968270450698">Ledger Wallet</a></li>
<li>27 May 2017 - <a href="https://play.google.com/store/apps/details?id=com.mycelium.wallet&reviewId=Z3A6QU9xcFRPR2QxMjZmN2hPZ2dRMGFlV0lQNW5SRUdiZnFlLWlJWVpJQnRnaW5abEJzRVZYYWFXLVlpS3FiM2xId0RPaFFaUHZQbGd1T05nQ1ZNeTduM3c&hl=en">Mycelium - one of the most popular mobile wallets</a></li>
<li>28 May 2017 - <a href="https://twitter.com/electrumwallet/status/868845430947401729">Electrum - one of the most popular desktop wallets</a></li>
<li>29 May 2017 - <a href="https://twitter.com/electrumwallet/status/868845430947401729">Airbitz - popular mobile wallet; guide to change node</a></li>
<li>09 Jun 2017 - <a href="">Bitgo</a> - however this is hearsay</li>
</ol>
<p>Operate an exchange and want to make sure your customer funds are safe and secure? Check out: <a href="/uasf-guide/#exchange-support">How An Exchange Supports BIP 148</a>

<p><h3 id="hodler">As a Hodler (Long Term Investor)</h3>
<p>If a chain split occurs then long term investors will have equal amounts of coins on both sides of the chain.
<p>If a chain split is resolved then they will have their original balance on the unified chain and need to take no actions.

<p><h3 id="trader">As A Bitcoin Trader</h3>
<p>As a trader you will need to find an exchange that supports, preferrably, both the legacy chain and the BIP 148 chain.
<p>Traders may have an opportunity to trade coins from one side to another. If exchanges support both chains then they could sell one and buy on the other.
<p>If sufficient demand exists on the BIP 148 chain, it may encourage miners to mine on that chain, which could eliminate any split.
<p>Traders should excercise caution when trading on the legacy chain as it may be reorganized without warning. Traders should also excercise caution on the BIP 148 chain, as if interest in it is insufficient, it may not hold long term value.
<p>The following is a list of exchanges that have or will support BIP 148.
<p>The list is ordered by date of an unequivocal public announcement for support of BIP 148.

<p><h3 id="exchanges">Exchanges Supporting BIP 148</h3>
<p>A listing of exchanges here does not imply any endorsement of the quality or security of the service.
<p>Put on your big boy or big girl pants and use at your own risk.
<ol>
<li>11 Apr 2017 - <a href="https://twitter.com/bitrefill/status/851818821946048512">Bitrefill</a></li>
<li>12 Apr 2017 - <a href="https://twitter.com/prasosltd/status/852104011767566336">Prasos</a></li>
<li>13 Apr 2017 - <a href="https://twitter.com/francispouliot_/status/852554864144109569">Bylls</a></li>
<li>13 Apr 2017 - <a href="https://twitter.com/francispouliot_/status/852554864144109569">Satoshi Counter</a></li>
<li>21 May 2017 - <a href="https://www.reddit.com/r/Bitcoin/comments/6chx7s/i_have_decided_that_my_node_will_run_bip_148_im/dhuspz3/">Vaultoro - Gold dealer</a></li>
<li>21 May 2017 - <a href="https://twitter.com/MojBitcoin/status/866308792568479745">MojBitcoin - European ATM</a></li>
<li>23 May 2017 - <a href="https://twitter.com/Bittylicious_/status/867305106668224513">Bittylicious</a></li>
<li>25 May 2017 - <a href="https://www.reddit.com/r/Bitcoin/comments/6dbsn8/bitfinex_will_list_bip148_chain_after_uasf/">Bitfinex</a> - one of the largest exchanges</li>
<li>09 Jun 2017 - <a href="">BitStamp</a> - however this is hearsay</li>
<li>16 Jun 2017 - <a href="https://bitonic.nl/en/news/138/our-position-on-scaling-proposals">BitTonic</a></li>
</ol>
<p><center><img src="/images/bitfinex-bip148.png"></center>
<p><center><img src="/images/bitstamp-bip148.png"></center>
<p><center><img src="/images/bitgo-bip148.png"></center>
<p>Operate an exchange and want to make sure your customer funds are safe and secure? Check out: <a href="/uasf-guide/#exchange-support">How An Exchange Supports BIP 148</a>

<p><h3 id="spender">Spending Bitcoins</h3>
<p>If you are spending Bitcoins then you should protect yourself from accidentally spending on both chains.
<p>Since many transactions are valid on both chains, the same transaction could be “replayed” on the other chain, thus making it you spend on the other side as well.
<p>Before you send a transaction, you should split your coins and be sure which chain your receiver honors.
<p>You can either use a coin splitting service or you can split your own coins by creating and broadcasting your own transactions on both chains.

<p><h3 id="receiver">Receiving Bitcoins</h3>
<p>If you are receiving Bitcoins then you need to pick which side of the chain you honor.
<p><b>WARNING:</b> Since the legacy chain could be re-organized then you need to evaluate this risk when you receive coins on the legacy chain.
<p>The common security practice is to wait at least six confirmations before relying on a transaction or block.
<p>If there is a chain split then users should excercise extreme caution and closely monitor the split along with requiring more confirmations because the security of the chain may be weakened.
<p>To be extremely safe we recommend having at <b>least 100-200 confirmations</b> before you rely on the transaction or block.

<p><h3 id="miner">As A Miner</h3>
<p>BIP can easily and cheaply be supported by users, businesses, exchanges, wallets, etc.
<p>However, miners have to <b>make a choice</b> between the legacy chain and the BIP 148 chain and this directly impacts their revenue.
<p>These pools mine the BIP 148 chain.
<ol>
<li><a href="http://www.uasfpool.com">UASF Mining Pool</a></li>
<li><a href="http://pa.xro.ca/">Pa.Xro.Ca</a></li>
<li><a href="https://slushpool.com/news/new-voting-option-bip148-has-been-deployed-feel-free-to-vote/">Slush Pool</a></li>
</ol>

<p><h3 id="third-parties">Storing Bitcoins with Third Parties</h3>
<p>We highly recommend you contact any third-parties to determine whether they will be supporting the legacy chain, BIP 148 or both.
<p>Be sure to get any commitments in writing so that, if needed, your lawyer will have it for any litigation. For example, when something similar happened with <a href="https://www.reddit.com/r/Bitcoin/comments/4ut2iz/coinbase_just_announced_that_they_are_pocketing/">Ethereum there was significant confusion at Coinbase</a>.
<p>If you store your coins with a third party, such as an exchange, then you should understand their policy for which chain they support.
<p>Some custodians may only honor one chain and you may not get the full value of your coins if they only honor on one side.
<p>Under the <a href="https://en.wikipedia.org/wiki/Unjust_enrichment">theory of unjust enrichment</a>, significant legal issues could be raised if third-parties are accuring benefit to themselves that should accure to the benefit of users.
<p>The <b>safest plan</b> for storing coins on August 1, 2017 is to gain control of your coins, operate your own full node<b>(s)</b> and evaluate your options after a potential chain split.

<p><h3 id="saying">What are companies saying about BIP148?</h3>

<ol>
<li><a href="https://twitter.com/billbarhydt/status/851855874855391232">Abra</a></li>
<li><a href="https://twitter.com/francispouliot_/status/852554864144109569">Bitcoin Embassy.io</a></li>
<li><a href="https://www.reddit.com/r/Bitcoin/comments/642n66/bitcoinremindercom_supports_bip148_and_a_fix/">Bitcoin Reminder</a></li>
<li><a href="https://news.bitcoin.com/bitfury-mines-block-signaling-uasf-segwit/">Bitfury</a></li>
<li><a href="https://bitkong.com/segwit.txt">BitKong</a></li>
<li><a href="https://twitter.com/spair/status/852160130296762369">BitPay</a></li>
<li><a href="https://twitter.com/bitrated/status/852414265134907392">Bitrated</a></li>
<li><a href="https://twitter.com/bitrefill/status/851818821946048512">Bitrefill</a></li>
<li><a href="https://bitvest.io/segwit">Bitvest</a></li>
<li><a href="https://twitter.com/blockonomics_co/status/851770427529670658">Blockonomics</a></li>
<li><a href="https://www.reddit.com/r/Bitcoin/comments/63otrp/gregory_maxwell_major_asic_manufacturer_is/dfw02tg/">Bustabit</a></li>
<li><a href="https://twitter.com/francispouliot_/status/852554864144109569">Bylls</a></li>
<li><a href="https://blog.coingate.com/2017/04/coingate-supports-segwit-and-uasf/">CoinGate</a></li>
<li><a href="https://twitter.com/coinkite/status/851822761794260992">Coinkite</a></li>
<li><a href="https://twitter.com/CoinomiWallet/status/852130791362637825">Coinomi</a></li>
<li><a href="https://www.reddit.com/r/Bitcoin/comments/6cna2s/notice_the_debate_is_now_only_about_the_way_of/dhwez9b/">Dark Net Heroes League (DHL)</a></li>
<li><a href="https://freedomnode.com/bitcoin-core-support.txt">Freedom Node</a></li>
<li><a href="https://twitter.com/joinmarket/status/851177740900368385">oin Market</a>J</li>
<li><a href="https://twitter.com/csuwildcat/status/851832163792150528">Microsoft</a></li>
<li><a href="https://twitter.com/prasosltd/status/852104011767566336">Prasos</a></li>
<li><a href="https://twitter.com/SamouraiWallet/status/851005717070917633">Samourai Wallet</a></li>
<li><a href="https://twitter.com/francispouliot_/status/852554864144109569">Satoshi Counter</a></li>
<li><a href="https://twitter.com/francispouliot_/status/850474196635439105">Satoshi Portal</a></li>
<li><a href="https://twitter.com/StamperyCo/status/852097157951873025">Stampery Inc.</a></li>
<li><a href="https://twitter.com/slushcz/status/851502735736418304">Trezor</a></li>
<li><a href="https://twitter.com/Vaultoro/status/851370469018284034">Vaultoro</a></li>
<li><a href="https://pastebin.com/raw/FeNHqySX">Walltime</a></li>
<li><a href="http://srv1.yogh.io/#json:getnetworkinfo">yogh.io</a></li>
</ol>

<p>[Add your business here by <a href="https://github.com/sunnankar/wuc-new/blob/gh-pages/_posts/2017-05-21-uasf-guide.md">creating a pull request</a> (must include public announcement link).

<p><h3 id="as-third-party">As A Third Party</h3>
<p>The safest route would be support both chains.
<p>Operate an exchange and want to make sure your customer funds are safe and secure? Check out: <a href="/uasf-guide/#exchange-support">How An Exchange Supports BIP 148</a>

<p><h2 id="conclusion">Conclusion</h2>
<p>If BIP 148 is successful then little to no action is needed from most users.
<p>However, around August 1, 2017 users should be cautious, especially when receiving coins.
<p>Most users will likely wait until more clear information is available.

<p><h3 id="exchange-support">How An Exchange Supports BIP 148</h3>
<p><a href="https://np.reddit.com/r/Bitcoin/comments/6c7twv/solution_unbiased_trading_of_real_bitcoin/">Credit</a>: This guide to help exchanges support BIP 148.
<p>UTTA - Underlying (or unbiased) Token Trading in Advance:</p>

<p>An Exchange ABC could start trading (1) "Bitcoin-BIP148" SegWit-enabled tokens, as well as (2) "Bitcoin-Old" Non-SegWit tokens, starting 1st July 2017, i.e. one month before BIP148 flag day.
<p>The exchange's customers will find the underlying coins, and not any future, derivative or bet, in their account balances, and can trade them exactly as if the two chains exist already!</p>
<p>This would help gauge the economic support for both chains.

<p>Here is an illustrative and exhaustive guidance on how trading will work for customers on an exchange:</p>
<p>Technically, and practically, it works like this:</p>
<p>Starting 1st July 2017, each customer on Exchange ABC will see 3 Bitcoin accounts:</p>

<ul>
<li><p>(a) The normal Bitcoin account</p></li>
<li><p>(b) An account laballed "Bitcoin-Old-NonSegWit"</p></li>
<li><p>(c) An account labelled "Bitcoin-BIP148-SegWit"</p></li>
</ul>

<p>By default, a customer having 1 BTC on his account will find the follwoing balances, when he logs in on 1st July 2017:</p>

<ul>
<li><p>(a) Bitcoin:     1.00000000 BTC</p></li>
<li><p>(b) Bitcoin-Old: 0.00000000 BTC</p></li>
<li><p>(c) Bitcoin-148: 0.00000000 BTC</p></li>
</ul>

<p>If the customer does nothing special, he can continue trading, withdrawing or loading bitcoins as usual and does not need to change anything. He can just ignore (b) and (c).</p>

<p>Optionally, the customer can move back and forth the balances between (a) and (b) and (c), e.g. as follows:</p>

<ul>
<li><p>(a) Bitcoin:     0.60000000 BTC</p></li>
<li><p>(b) Bitcoin-Old: 0.40000000 BTC</p></li>
<li><p>(c) Bitcoin-148: 0.40000000 BTC</p></li>
</ul>

<p>This means, he now has moved 0.4 BTC from his "default" Bitcoin account (a) to his "new" Bitcoin accounts (b) and (c). This kind of account keeping respects the fact that after a chain split, i.e. after 1st August 2017, each Bitcoin that exists before the chain-split will duplicate into one "Bitcoin-Old" and one "Bitcoin-148".</p>
<p>Let's assume that there are two customers on Exchange ABC, call them Alice and Bob, with the following account balances:</p>
<p><center><img src="/images/uasf-exchange-1.png"></center>

<p>Let's assume that Alice and Bob "re-arrange" their accounts in their account settings, as follows:</p>

<p><center><img src="/images/uasf-exchange-2.png"></center>

<p>Now, Alice and Bob can start trading. Let's assume, for the sake of simplicity and ease of understanding, that 1 BTC is valued == 1000 EUR.
<p>Also, trading fees earned by the Exchange operator are assumed to be 0.00% here for simplicity.</p>
<p>Alice and Bob can now place buy and sell orders for Bitcoin-Old (b) or Bitcoin-148 (c), exactly the same way as for normal Bitcoin (a), or for any other crypto-currency traded on Exchange ABC. For example, Alice places a buy-order for 0.25 tokens of "Bitcoin-148" for 300 EUR, and Bob accepts this order. After settlement, their account balances look like this:</p>

<p><center><img src="/images/uasf-exchange-3.png"></center>

<p>After another trade where Alice is selling 0.2 "Bitcoin Old" tokens to Bob for 150 EUR, their balances read:</p>

<p><center><img src="/images/uasf-exchange-4.png"></center>

<p>Now let's assume Alice wants to withdraw 0.7 BTC (0.8 BTC would be the maximum possible in the current situation for her) to her local Trezor wallet. For this she will first "re-arrange" her account (again via account settings) as follows:</p>

<p><center><img src="/images/uasf-exchange-5.png"></center>

<p>She will now withdraw 0.7 BTC:</p>

<p><center><img src="/images/uasf-exchange-6.png"></center>

<p>Alice couldn't withdraw her remaining 0.45 "Bitcoin-148" tokens, because they do not yet exist on any public blockchain. To withdraw them as well already now, she'd either have to sell the 0.45 Bitcoin-148 tokens on the Exchange ABC and buy legacy Bitcoin tokens from that Fiat money, or she'd buy 0.45 Bitcoin-Old tokens to match her "Bitcoin-148" tokens.
<p>Thereafter she could again "re-arrange" her account and then withdraw all the BTC.</p>
<p>Let's assume that no further activity occurs on Alice's and Bob's accounts for the rest of July 2017.</p>
<p>On 1st August 2017, Bitcoin-BIP148 shall activate. As a result, the legacy account balance (a) ceases to exist, and the Bitcoin balances in the customers' accounts read:</p>

<p><center><img src="/images/uasf-exchange-7.png"></center>

<p>As we can see, Bob's former 0.6 BTC was moved (or "re-arranged") to his "Bitcoin-Old" and "Bitcin-148" balance. This reflects the fact that both chains (b) and (c) have the same pre-decessor chain (a).</p>
<p>Now let's assume that first the "Bitcoin-Old" chain grows faster than the "Bitcoin-148 chain", such that there are indeed TWO public Bitcoin blockchains (in the other case we'd have only one common chain, and we'll come to that scenario later).</p>
<p>From this moment on, trading of Bitcoin-Old tokens and Bitcoin-148 tokens on Exchange ABC works like tokens of any other crypto-currency, they are simply treated as what they are - separate chains.</p>
<p>Alice or Bob could e.g. withdraw "Bitcoin-Old" or "Bitcin-148" tokens. Exchange ABC will make sure that no replay attacks are possible when their customers withdraw tokens.
<p>It can easily guarantee this e.g. by a mechanism as described <a href="https://np.reddit.com/r/ethereum/comments/4t30ew/poloniex_announces_their_plans_regarding_upcoming/d5edz7r/">here</a>.</p>
<p>Also, Alice and Bob can load their account balances with new coins. In this case, of course Exchange ABC cannot guarantee that no replay attack will occur. However, for fairness reasons, Exchange ABC will always monitor the receiving address on BOTH chains, and should coins arrive on the "other chain", the received amount will also be credited to the customer's balance, such that no coins get lost when a customer gets "replay-attacked" when loading coins onto his/her account at Exchange ABC.</p>
<p>Now let's consider what happens if one of the two public blockchains disappears - let's look at different possible scenarios:</p>
<p><b>1.)</b> The blockchain of BIP148 (UASF, SegWit) is not mined at all because of lack of interest, or is slower from the start then "Old-Chain", and gets slower and slower and gets less and less valuation and less and less miners and nodes operate this chain.
<p>At some point, this chain "dies" because no more block is mined on this chain at all.
<p>--> In this case, customer balances for Bitcoin-148 coins will not be withdrawable any more as the chain dies, Exchange ABC will quit support trading its tokens a short time later, and customers will lose their balances for this token, since the coin has become unusable and worthless.</p>
<p><b>2.)</b> After a "slow start" on 1st August 2017, the tokens of Bitcoin-BIP148 (UASF, SegWit) become more and more valuable, more and more miners hence switch to mine them, the BIP-148 chain hence becomes longer and longer and at one point overtakes the "Old-Non-SegWit-Chain".
<p>At this point, the "Old-Non-SegWit-Chain" reorganises and becomes identical to the "BIP148-SegWit-Chain". As a consequence, the "Bitcoin-Old" tokens cannot be withdrawn any more and cannot be traded any more - they will be displayed "grayed-out" in the account balance view, just for information, and will a few days afterwards be removed from the user accounts altogether.</p>
<p><b>3.)</b> On 1st August 2017, if from the first moment on, the BIP-148 SegWit chain is faster than the other "Non-SegWit" chain, then no "Bitcoin-Old" chain will be created in the first place, and the customer balance for "Bitcoin-Old" tokens will not be withdrawable.
<p>These tokens, however, will still be tradeable for the first time starting 1st August, because the initial faster block creation of BIP-148 SegWit blocks might well be a result of statistical coincidence, i.e. the "Bitcoin-Old" chain may still turn out faster and longer and fork-off from the BIP148-chain some time later.
<p>Another reason why there don't immediately have to be two parallel chains is that the "Old-chain" will accept BIP148-blocks (because of the SOFT fork characteristics) such that there is no reason to immediately fork-off. However, injection of SegWit transaction into the "Old chain" that look like "anyone can spend" transactions to the "Old-chain miners", as well as old Non-BIP148 blocks that are rejected by BIP148-miners, should sooner cause a chain-split with Old-chain forking off from BIP148-chain, if "old-chain" miner hash power is greater than "BIP148-chain" hash power.
<p>So trading of Old-Chain tokens will be possible for some time (maybe even some days) on Exchange ABC, in expectation that an Old-chain creation may still happen. In case the Old-Chain should indeed fork-off, as soon as it is [10] blocks longer than BIP148-chain, Exchange ABC will recognize the existence of this Old-Chain and will allow withdrawals of "Bitcoin-Old" tokens.
<p>After this moment, the two chains will either coexist forever, or one of the cases 1.) or 2.) will occur at some point in time, sooner or later.</p>

<p><h3>SUMMARY</h3>
<p>By opening a fair and unbiased market for directly trading "Non-SegWit-Bitcoin" tokens and "BIP148-SegWit-Bitcoin" tokens well in advance before actual BIP148 activation, a market demand for a SegWit-disabled coin on the one hand, and for a SegWit-enabled Bitcoin on the other hand, can be determined in a fair and reliable way, before SegWit activation on 1st August 2017 happens.
<p>This solves the dilemma that nobody knows in advance of 1st August what the actual market/user demand for SegWit is, because today's miner hashrate is not representing real market demands.