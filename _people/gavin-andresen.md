---
title:  Gavin Andresen
img: /images/gavin-andresen.jpg
seotitle: Gavin Andresen - Chief Scientist, Bitcoin Foundation
position: Developer
education: BSc. in Computer Science from Princeton University
experience:
short_desc: Gavin Andresen is a developer.
long_desc:
affiliations: [Bitcoin Foundation, Bitcoin XT, Bitcoin Classic, Coinbase]
twitter: gavinandresen
github: gavinandresen
residence:
cats: [ ]
website:
---
Gavin Andresen was an early contributor of code to Bitcoin with [overall GitHub commits](https://github.com/bitcoin/bitcoin/graphs/contributors) to Bitcoin Core around 484.

In 2015, Andresen joined MIT's Digital Currency Initiative. Additionally, he serves as the Chief Scientist of the failed Bitcoin Foundation, and is an advisor to [Coinbase](/coinbase/) and [Zcash](https://z.cash/team.html).

## History with Bitcoin

Andresen and Satoshi Nakamoto communicated often through Bitcointalk in early-2010. In mid-2010, Andresen alerted Satoshi that he had agreed to meet with the CIA to discuss Bitcoin. Satoshi disappeared shortly after. It's not clear, however, whether or not Gavin's meeting had anything to do with Satoshi's departure.

## Bitcoin Core

From mid-2010 until April-2014, Andresen maintained control of the Bitcoin Core GitHub repository. On April 8, 2014, [Andresen stepped down](http://www.coindesk.com/gavin-andresen-steps-bitcoins-lead-developer/) and [Wladimir van der Laan](/wladimir-van-der-laan/) agreed to take over as Lead Maintainer of the Bitcoin Core repo.

## Contributions to Bitcoin

### Multisig (Pay to script hash)

[BIPs 11](https://github.com/bitcoin/bips/blob/master/bip-0011.mediawiki), [13](https://github.com/bitcoin/bips/blob/master/bip-0013.mediawiki), and [16](https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki), published by Andresen in 2011 and 2012, were all part of the addition of multisiganture transactions--also known as Pay to Script Hash or P2SH--to Bitcoin.

### Payment Protocol (BIP 70)

Andresen and Mike Hearn published [BIP 70](https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki), also known as Payment Protocol, which added a new form of communication between merchants and customers. BIP 70 [made Bitcoin payments](https://bitcointalk.org/index.php?topic=300809.0) more secure, seamless and also prevents against man-in-the-middle attacks.

## Bitcoin XT

Andresen has long been critical of Bitcoin's capacity limit of three transactions per-second. He teamed up with Mike Hearn in an attempt to fork Bitcoin and created [Bitcoin XT](https://github.com/bitcoinxt/bitcoinxt). XT, also known as [BIP 101](https://github.com/bitcoin/bips/blob/master/bip-0101.mediawiki), proposed an immediate block size increase to 8 MB, which was to be doubled every two years.

Other Bitcoin developers were critical of Bitcoin XT and BIP 101. Some feared that large blocks could force small miners and nodes to shut down, leading to further centralization of Bitcoin. XT failed to reach consensus. Chinese mining pools, which control most of the Bitcoin network hash rate, also [rejected the proposal](http://cointelegraph.com/news/chinese-mining-pools-call-for-consensus-refuse-switch-to-bitcoin-xt).

## Bitcoin Classic

After Bitcoin XT failed to achieve Andresen's goal of bumping the block size limit, he teamed up with another group of developers to create Bitcoin Classic. Classic proposed a more modest 2 MB block size increase via hardfork.

Bitcoin Classic received initial support from a number of miners--which are required to activate any block size increase via hard fork. A few weeks after Classic's release, however, the majority of Bitcoin miners [agreed to run](https://medium.com/@bitcoinroundtable/bitcoin-roundtable-consensus-266d475a61ff#.iz4wd5t59) only Bitcoin Core compatible software.

## Controversy

Andresen is one of the most controversial figures in Bitcoin. Much of the controversy stems from his desire to increase Bitcoin's block size limit.

While most Bitcoin developers agree that Bitcoin must scale in order to accommodate more users, there is much debate about how to do so. Andresen proposals all aim to increase Bitcoin's capacity with hardforks via a block size increase. Other Bitcoin developers argue that a block size increase is unsafe and that more efficient methods exist to increase Bitcoin's capacity without a hardfork through proposals like [Segregated Witness](/what-are-segwit-benefits/).

## Quotes

[On SPV Mode](http://0bin.net/paste/8YeL12K5CwP26YUP#kSSLpZ2+PC9RqgcbiP0-bYbDhIHAMRCB3t2CpHkxokQ):

> I am willing to run SPV mode because I trust that my customers aren’t going to double spend against me.

[On presenting hard fork risks](http://0bin.net/paste/8YeL12K5CwP26YUP#kSSLpZ2+PC9RqgcbiP0-bYbDhIHAMRCB3t2CpHkxokQ) the same as soft fork risks:

> It doesn’t matter if the software is obsolete because of hard or soft fork, the difference in risks between those two cases will not be understood by the typical full node or SPV node user.

[On the proper block size](https://twitter.com/gavinandresen/status/636569665284775937):

> I think 2MB is absurdly small.

[On Peter Todd](https://www.reddit.com/r/Bitcoin/comments/2lypd1/peter_todd_on_changetip_not_a_real_bitcoin_app/clzd6yb):

> Peter is hung up on the decentralization/privacy aspects of Bitcoin

[On using Bitcoins as a store of value](https://bitcointalk.org/index.php?topic=204.msg1714#msg1714):

> I don’t plan on saving a significant number of Bitcoins as a store of value. I like to invest in people who are doing productive things that grow our economy and make the world a better place, so when Bitcoins replace dollars Wink I’ll lend them to people by buying bonds or stocks.

[On no block limit](https://www.reddit.com/r/Bitcoin/comments/2ighvq/a_scalability_roadmap_the_bitcoin_foundation/cl2b7sg):

> In my heart of hearts I still believe that going back to “no hard-coded maximum block size” would work out just fine.

[On who should run a node](https://www.reddit.com/r/Bitcoin/comments/2cc6ed/it_seems_like_theres_something_missing_in_the/cjegk8j):

> Miners and merchants and wallet services and a small fraction of super-security-conscious people are more than enough for a robust, stable network; I don’t think we need more incentives to run full nodes.

[On Peter Todd](https://www.reddit.com/r/Bitcoin/comments/28jp0y/why_is_peter_todd_wrecking_zeroconf_security/cibr8h2):

> Peter Todd is a very large part of the “Bitcoin Core moves forward too slowly” problem.

[On Peter Vesseness](https://www.reddit.com/r/Bitcoin/comments/1y9akl/mark_karpeles_petition_update/cfiwwyx) (who ran Bitcoin foundation and [stole 5 million](https://www.reddit.com/r/Bitcoin/comments/3y0ewr/forgotten_history_bitcoin_foundation_chairman/)):

> Peter is trustworthy.

[On nodes in data centers](https://www.reddit.com/r/Bitcoin/comments/1scd4z/im_running_a_full_node_and_so_should_you/cdw3lrh):

> Most ordinary folks should NOT be running a full node. We need full nodes that are always on, have more than 8 connections (if you have only 8 then you are part of the problem, not part of the solution), and have a high-bandwidth connection to the Internet. So: if you’ve got an extra virtual machine with enough memory in a data center, then yes, please, run a full node.

[On Peter Todd](https://www.reddit.com/r/Bitcoin/comments/1rqexb/87898_kb_block_just_now/cdpvh9x):

> Maybe I don’t communicate clearly enough, but much of the fear, uncertainty, and doubt about the block size issue comes from people like Peter who want to know exactly how technical problems that MIGHT come up three years from now will be solved TODAY.

[On respect](https://www.reddit.com/r/Bitcoin/comments/1oxn14/gavin_finally_lost_it/ccwqvwt):

> Mmm. If you want my respect, write some code.
