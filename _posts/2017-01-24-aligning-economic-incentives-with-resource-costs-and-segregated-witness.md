---
layout: post
title: Aligning Economic Incentives With Resource Costs And Segregated Witness - Andreas Antonopoulos
author: Andreas Antonopoulos
authorurl: /andreas-antonopoulos-bitcoin-expert/
published: true
---

<p>Bitcoin mining nodes and full nodes incur costs for the resources used to support the <a href="/decrypting-bitcoin-documentary/">bitcoin network and the blockchain</a>. As the scale of bitcoin increases, so does the cost of resources (CPU, network bandwidth, disk space, memory). </p>

<p>Miners are compensated for these costs through fees that are proportional to the size (in bytes) of each transaction. Non-mining full nodes are not compensated, so they incur these costs because they have a need to run an authoritative fully-validating full-index node, perhaps because they use the node to operate a bitcoin business.</p>

<p>Without transaction fees, the growth in bitcoin data would arguably increase dramatically. Fees are intended to align the needs of bitcoin users with the burden their transactions impose on the network, through a market-based price discovery mechanism.</p>

<p>The calculation of fees based on transaction size treats all the data in the transaction as equal in cost. But from the perspective of full nodes and miners, some parts of a transaction carry much higher costs. Every transaction added to the bitcoin network affects the consumption of of four resources on nodes:</p>

<p><strong>Disk Space:</strong> Every <a href="/blockchain-uses/">transaction is stored in the blockchain</a>, adding to the total size of the blockchain. The blockchain is stored on disk, but the storage can be optimized by “pruning” older transactions.</p>

<p><strong>CPU:</strong> Every transaction must be validated, which requires CPU time.</p>

<p><strong>Bandwidth:</strong> Every transaction is transmitted (through flood propagation) across the network at least once. Without optimization, transactions are transmitted again as part of a block, doubling the impact on network capacity</p>

<p><strong>Memory:</strong> Nodes that validate transactions keep the “UTXO set”, the list of all unspent transaction outputs, in memory. Because memory is at least one order of magnitude more expensive than disk, growth of the UTXO set contributes disproportionately to the cost of running a node.</p>

<p>As you can see from the list above, not every part of a transaction has an equal impact on the cost of running a node or on the ability of <a href="/scaling-bitcoin-to-billions-of-transactions-per-day-dryja/">bitcoin to scale to support more transactions</a>. The most expensive part of a transaction are the newly created outputs, as they are added to the in-memory UTXO set. By comparison, signatures (aka witness data) add the least burden to the network and the cost of running a node, because witness data are only validated once and then never used again. </p>

<p>Furthermore, immediately after receiving a new transaction and validating witness data, nodes can discard that witness data. If fees are calculated on transaction size, without discriminating between these two types of data, this does not align the market incentives of fees with the actual costs imposed by a transaction. In fact, the current fee structure actually encourages the opposite behavior, because witness data is the largest part of a transaction.</p>

<p>The incentives created by fees matter because they <a href="/introduction-bitcoin-paper-wallets-cold-storage/">affect the behavior of wallets</a>. All wallets must implement some strategy for assembling transactions that takes into considerations a number of factors, such as privacy (reducing address re-use), fragmentation (making lots of loose change) and fees. If the fees are overwhelmingly motivating wallets to use as few inputs as possible in transactions, this can lead to UTXO picking and change address strategies that inadvertently bloat the UTXO set.</p>

<p>Transactions consume UTXO in their inputs and create new UTXO with their outputs. A transaction, therefore, that has more inputs than outputs will result in a decrease in the UTXO set, whereas a transaction that has more outputs than inputs will result in an increase in the UTXO set. Let’s consider the difference between inputs and output and call that the “Net-new UTXO”. </p>

<p>That’s an important metric, as it tells us what impact a transaction will have on the most expensive network-wide resource, the in-memory UTXO set. A transaction with positive Net-new-UTXO, adds to that burden. A transaction with a negative Net-new-UTXO reduces the burden. We would therefore want to encourage transactions that are either negative Net-new-UTXO or neutral with zero Net-new-UTXO.</p>

<p>Let’s look at an example of what incentives are created by the transaction fee calculation, <a href="/what-are-segwit-benefits/">with and without segregated witness</a>. We will look at two different transactions. Transaction A is a 3-input, 2-output transaction, which has a Net-new-UTXO metric of -1, meaning it consumes one more UTXO than it creates, reducing the UTXO set by one. </p>

<p>Transaction B is a 2-input, 3-output transaction, which has a Net-new-UTXO metric of 1, meaning it adds one UTXO to the UTXO set, imposing additional cost on the entire bitcoin network. Both transactions use multi-signature (2-of-3) scripts, to demonstrate how complex scripts increase the impact of segregated witness on fees. Let’s assume a transaction fee of 30 satoshi per byte and a 75% fee discount on witness data:</p>

<p>Without Segregated Witness</p>

<p>Transaction A fee: 25,710 satoshi</p>

<p>Transaction B fee: 18,990 satoshi</p>

<p>With Segregated Witness</p>

<p>Transaction A fee: 8,130 satoshi</p>

<p>Transaction B fee: 12,045 satoshi</p>

<p>Both transactions are less expensive when segregated witness is implemented. But comparing the costs between the two transactions, we see that before segregated witness, the fee is higher for the transaction that has a negative Net-new-UTXO. After segregated witness, the transaction fees align with the incentive to minimize new UTXO creation, by not inadvertently penalizing transactions with many inputs.</p>

<p>Segregated witness therefore has two main effects on the fees paid by bitcoin users. Firstly, <a href="/segregated-witness/">segregated witness reduces the overall cost</a> of transactions by discounting witness data and increasing the capacity of the bitcoin blockchain. Secondly, segregated witness’ discount on witness data corrects a misalignment of incentives that may have inadvertently created more bloat in the UTXO set.</p>
