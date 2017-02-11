---
layout: post
title: How Bitcoin Unlimited Users May End Up on Different Blockchains
description: How Bitcoin Unlimited Users May End Up on Different Blockchains
author: Melvin Draupnir
authorurl: /melvin-draupnir/
published: true
---

<p><center><img src="/images/unlimited-users.jpg" alt=""/></center></p>


<p>Bitcoin Unlimited, one of the Bitcoin Core <a href="/mtgoxs-new-villain-is-coinlab-ceo-peter-vessenes/">software forks introduced</a> in late 2015, garnered much attention in recent months. The project gained hash power support from several new Bitcoin mining pools, including ViaBTC, GBMiners and BTC.TOP, while node adoption appears to be on the rise as well.</p>

<p>The central idea behind Bitcoin Unlimited — specified in “Bitcoin Unlimited Improvement Proposal 001” (BUIP001) — is to hand control of Bitcoin’s block size limit to users and miners. Or perhaps, more accurately, to make this control more explicit and easier to handle.</p>

<p>However, this control does come at the expense of Bitcoin’s strong and automated consensus mechanism. With BUIP001, there is a number of scenarios in which different users end up on different chains — either temporarily or permanently.</p>

<h2>Here’s a (probably incomplete) overview.</h2>

<p>(Note: If you are not sure how Bitcoin Unlimited works, do make sure to first read “A Closer Look at Bitcoin Unlimited’s Configurable Block Size Proposal.”)</p>

<h2>If Not Everyone Switches to Bitcoin Unlimited</h2>

<p>The first example is also the most obvious one.</p>

<p>It currently seems very unlikely that different Bitcoin implementations — like Bitcoin Core, Libbitcoin, BTCD or Bcoin — will adopt BUIP001, or something compatible. This is especially true because the Bitcoin Unlimited team has not submitted BUIP001 to the cross-implementation Bitcoin Improvement Proposal (BIP) process; most implementations therefore don’t even have the proposal under consideration.</p>

<p>But if not all significant Bitcoin implementations adopt BUIP001 or a compatible solution, the blockchain cannot converge in the way Bitcoin Unlimited proponents envisage. Instead, if a majority of miners (by hash power) increases Maximum Generation Size (MG) and Excessive Block Size (EB) to produce blocks bigger than one megabyte, Bitcoin would split into two incompatible networks and currencies, not unlike Ethereum and Ethereum Classic.</p>

<p>However, because this split would not be coordinated or include safety precautions, the consequences could be much worse than the split between Ethereum and Ethereum Classic.</p>

<p>One megabyte users would experience inconveniences, and even more so if their hash power initially represents a smaller minority. This would include (much) slower block confirmations, perhaps even to the point where their chain becomes almost unusable (at least temporarily). Additionally, they are at risk of replay attacks if they want to use the “Bitcoin Unlimited chain” as well.</p>

<p>Bitcoin Unlimited users would suffer similar inconveniences, though their initial block confirmations wouldn’t be as slow, as they’d have support from the hash-power majority.</p>

<p>To counter that, however, <a href="/your-own-wealth-will-be-controlled-as-a-basic-human-right/">Bitcoin Unlimited users</a> would be unsure as to whether “their” chain would continue to exist at all. If the one megabyte chain should ever overtake the “Bitcoin Unlimited chain” in length (really: total proof of work), Bitcoin Unlimited nodes would automatically switch back to the one megabyte chain. </p>

<p>Accordingly, they would dispose of (“orphan”) the entire “Bitcoin Unlimited chain” since the split, even if that chain is thousands of blocks deep. All “their” transactions would be forgotten, perhaps costing lots of people lots of money.</p>

<p>If a group of hardcore one-megabyte supporters and speculators can make this scenario seem even slightly plausible, self-fulfilling prophecy dynamics can pose an existential threat to the “Bitcoin Unlimited chain”: no one wants to hold value on the chain that may be discarded.</p>

<h2>If Everyone Does Switch to Bitcoin Unlimited</h2>

<p>But let’s assume the switch to BUIP001 goes smoothly. All significant Bitcoin implementations adopt the new configurable options, and all users and miners update their software accordingly.</p>

<p>Once again — even in this scenario — there is no technical reason that all users will converge on a single chain in a meaningful way. Different users can configure their nodes to remain out of consensus for the rest of their lives.</p>

<p>As a simple example, a <a href="/a-simple-guide-to-effectively-and-safely-mixing-bitcoins/">minority of miners</a> can configure both MG and EB to one megabyte, while they set Excessive Acceptance Depth (AD) to 10,000,000. In other words, these nodes will mimic the current one-megabyte block size limit for about two centuries — regardless of what the rest of the network does.</p>

<p>Meanwhile, a majority of miners can set MG and EB to create and accept blocks up to two megabytes.</p>

<p>Now, as soon as one miner mines a two-megabyte block, the majority of miners will build on this block and extend this chain. The minority of miners, however, ignores this chain practically forever: exactly as described in the previous section of this article.</p>

<p>And it would include the same risks as previously described as well. If the one-megabyte chain ever overtakes the two-megabyte chain in length, the two-megabyte chain is completely discarded. Even after thousands of blocks.</p>

<h2>If Everyone Limits AD to Four Confirmations</h2>

<p>Bitcoin Unlimited users can have a stronger degree of convergence on a single chain by technical means, if they keep their AD setting relatively low. The default setting in Bitcoin Unlimited is four: An excessive block requires four blocks mined on top of it to be considered valid.</p>

<h2>But this presents problems as well.</h2>

<p>The first problem is that even with this low default, any transaction with less than five confirmations is much less secure than it is now. Say a transaction shows three confirmations in a user’s wallet. That user has no way of knowing whether an alternative blockchain is being mined with a competing (double-spent) transaction, that already has four confirmations. This could happen at any time.</p>

<p>If that alternative chain reaches its fifth confirmation first, the user’s chain is discarded, and his incoming transaction lost — even though it had three confirmations.</p>

<p>Of course, “orphaned blocks” do already exist, and users that require more security should wait for more confirmations.</p>

<p>But barring exotic and expensive types of malicious attacks, three orphaned blocks can currently really only result from freak coincidence. Different groups of miners must coincidentally find three blocks at almost exactly the same time, three separate and subsequent coincidences, in order for the network to experience that many orphans.</p>

<p>Bitcoin Unlimited, on the other hand, throws a new factor into the mix, adding a reason for the network to experience three orphaned blocks. Miners not only race to extend the longest valid chain, but also vote on protocol rules between chains. This process would also be visible and quite predictable for attackers, and therefore easily exploitable.</p>

<p>The second problem is that having to keep AD at the default of four confirmations for security reasons essentially defeats the purpose of BUIP001. While Bitcoin Unlimited is supposed to hand control of the block size limit over to both users and (all) miners, low AD levels ensure that even the slightest majority of miners can always overrule local block size settings by simply mining a series of bigger blocks. This makes MG and EB meaningless for everyone else: “placebo controls.”</p>

<p>Indeed, AD proposes an odd choice: Either nodes and miners set a high AD for relative autonomy, but risk splitting the network with potentially harmful consequences; or these nodes and miners pick a low AD to improve the level of convergence — but only because they effectively give up control to a majority of miners. (And if the intention is to give up control to a majority of miners, there are more straightforward solutions available.)</p>

<h2>Under Adversarial Conditions</h2>

<p>Things get worse under adversarial conditions.</p>

<p>If not everyone wants what’s best for Bitcoin, and instead some entities — for whatever reason — would rather see Bitcoin fail, the security assumptions of BUIP001 degrade further. And the more funds an adversary has at its disposal to cause turmoil, the worse Bitcoin Unlimited’s convergence mechanism would perform.</p>

<p>First off, node signaling is trivially spoofed. Anyone with the resources to spin up “fake” (economically irrelevant) nodes could pretend that there is widespread user support for a certain block size limit level, while in reality there is not. If miners go by these signals, they may fork the chain with less user support than expected.</p>

<p>Additionally, a malicious miner can often split the network. Such a miner could monitor the EB levels signaled by other miners (which is not as easily spoofed), and intentionally mine a block that falls right in between what these miners will accept. If some 50 percent of hash power accepts blocks up to two megabytes, and the other 50 percent supports bigger blocks, a 2.01 megabyte block would be ignored by the first 50 percent, and accepted by the other 50 percent.</p>

<p>Assuming the default AD of four is maintained, the chain could split for more than an hour. As explained in the previous section, the Bitcoin network(s) would be very unreliable during this period, as the chain on either side of the split may be discarded.</p>

<p>An adversary controlling only 0.7 percent of global hash power could cause this level of turmoil about once every day. And unless the overwhelming majority of miners already agree on their EB anyways, that sweet spot to abuse the network should always exist.</p>
</p>

<p>Now, the malicious miner has about 24 hours to mine an even larger block, that — ironically — only the initially smaller-block side of the chain would accept because their sticky gates are open, and the initially larger-block side of the chain would reject. This would create another split.</p>

<p>Last, if and when this new "sticky gate chain" reaches the AD thresholds of the remaining nodes, all sticky gates are open, and <a href="/new-privacy-feature-ricochet-launched-by-samourai-wallet/">there is no block size limit at all</a>. An adversary can now mine blocks that are so big they may fragment the chain as not all nodes can keep up — perhaps due to bandwidth constraints, latency or other machine limits.</p> 

<h2>Emergent Consensus</h2>

<p>While Bitcoin Unlimited arguably offers more personal autonomy to users, it does not ensure technical blockchain convergence. But this is not new. To some extent, it is even touched on in Bitcoin Unlimited’s FAQ.</p>

<p>Yet, Bitcoin Unlimited proponents do expect users to converge on a single blockchain. This is explained by what is perhaps best considered Bitcoin Unlimited’s underlying philosophy: “Emergent Consensus.”</p>

<p>Rather than a purely technical mechanism, Emergent Consensus is a conviction that all participants in the Bitcoin ecosystem have a strong enough (economic) incentive to find consensus on a single blockchain, even if their software does not do this automatically.</p>

<p>The next article will take a closer look at this Emergent Consensus philosophy.</p>

<p>Author’s note: This article is not a complete overview of all the problems that could result from BUIP001. Most importantly, it ignores trade-offs and weaknesses that derive from an oversized (or floating) block size limit itself, like node centralization, miner centralization, or fee economics, to instead focus on (a lack of) blockchain convergence.</p>