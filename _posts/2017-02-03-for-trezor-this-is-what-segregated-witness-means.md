---
layout: post
title: For TREZOR This Is What Segregated Witness Means
description: For TREZOR This Is What Segregated Witness Means
author: Melvin Draupnir
authorurl: /melvin-draupnir/
published: true
---

<p>Segregated Witness, also known as SegWit, has been a target of <a href="/dollars-to-bitcoin/">frequent debates online and offline</a>. For some it might be controversial due to its political implications for the Bitcoin ecosystem. However, for the sake of clarity, let’s take a step away from politics. </p>

<p>In other words, this article will not discuss the connotation of SegWit for the blocksize debate. This article will not delve deeply into the actual technology and code behind SegWit either; many articles have been written on the merits of SegWit, and I cannot explain it as well as them. Instead, I will focus exclusively on the positive effects of Segregated Witness on TREZOR, and Bitcoin wallets in general.</p>

<blockquote>SegWit is a blessing for hardware wallets for many reasons. I actually think that rolling out SegWit will increase security, because it will reduce huge complexity in hardware wallets as it is today.
<br/>
— Marek “Slush” Palatinus, CEO of SatoshiLabs</blockquote>

<p><center><img src="/images/trezor-0.jpeg" alt="trezor"/></center></p>

<p>Too Long; Did Not Read version at the end of the article.</p>

<h2>Back to Basics: Bitcoin Transaction</h2>

<p>In Bitcoin, a wallet never stores actual coins, real or virtual. Instead, the wallet carries private keys, which are used to digitally sign transactions. The currency network is held together by these records of transactions, as every transaction is entered into the unchangeable common ledger — the Bitcoin blockchain.</p>

<p>A Bitcoin transaction is composed of inputs, outputs and signature. There can be a single input, or multiple of them; the same applies to outputs. Signature verifies the ability of the user to spend the coins (the user signs using his/her private key, others can verify the signature against his/her public key).</p>

<p>Let’s say Alice wants to send 10 bitcoins to Bob. She will have to create a new transaction with Bob’s address (public key) as the receiver. Alice has previously received three different transactions, with values 3 BTC, 4 BTC and 5 BTC. Let’s label these as N1, N2 and N3. </p>

<p>You can see that the sum of these transactions is larger than the 10 BTC Alice wants to send, and there is no way to <a href="/new-privacy-feature-ricochet-launched-by-samourai-wallet/">combine just two of those transactions</a> to have 10 BTC. What Alice has to do is add another output into the transaction, with her own address. She will state that she wants to send 1.5 BTC back to her own account.</p>

<p>Notice that the sum of outputs (10+1.5=11.5) does not add up to the sum of inputs (3+4+5=12). This by design, as the difference between the two will serve as the transaction fee for the miner who adds this transaction to his/her mined block.</p>

<p><center><img src="/images/trezor-1.jpg" alt="trezor"/></center></p>

<h2>Verifying Inputs</h2>

<p>When composing a new transaction, the wallet has to request the information on previous outputs it received, to use them as inputs. However, the amount in the previous output is not explicitly given to the wallet. Instead, the wallet only knows the Transaction ID of the previous transaction and the position of the previous output inside of that transaction.</p>

<p>Alice’s Transaction will therefore look more like this, with no amounts in the inputs, but rather Transaction IDs and positions of previous outputs:</p>

<p><center><img src="/images/trezor-2.jpg" alt="trezor"/></center></p>

<p>The wallet can stream the value of these inputs/previous outputs from somewhere, but how can it know that the amount is correct? What if it was intercepted and modified by someone?</p>

<p>In addition, you have surely noticed that the transaction fee is not explicitly stated. It is implicitly given by the difference between the sum of all outputs and sum of all inputs. This unfortunately opens up an attack vector, where one of the inputs used is actually larger than the user expects, and thus the user can lose a significant amount of coins to the transaction fee. This is the so-called Fee Attack vector.</p>

<p>There is a way to <a href="/bitcoin-arbitrage-made-easy-lesson-two/">protect your wallet from this attack</a>; TREZOR and many other (hardware) wallets employ this method. Essentially, the wallet depends on cryptographic verification of the input — hashes, to confirm the correctness of the input value supplied.</p>

<p>The wallet calculates the hash of the previous transaction and compares it to the hash published with the transaction in the blockchain. If the hashes match, then the wallet can be certain that the amount to be used as an input was not modified.</p>

<h2>Let’s go slower, one by one.</h2>

<p>Consider the input N1. Assume the input was a part of transaction TXID1 and output #0. The transaction TXID1 might have looked something like this:</p>

<p><center><img src="/images/trezor-3.jpg" alt="trezor"/></center></p>

<p>When composing a new transaction, the wallet will stream the previous transaction (TXID1) from the blockchain, and ask for the specific output #0 (first position) and its value. Once it receives the value, the wallet will start hashing then entire transaction. Only if the hash exactly matches the hash published (34b23ea….), then the wallet can be certain that the amount is correct; in this case 3 BTC.</p>

<p>The wallet has to do this for each and every input to be used for a new transaction.</p>

<h2>Hardware Wallets: Limited Power</h2>

<p>Verifying inputs is, in itself, not a problem. The verification process only reinforces the security of hardware wallets. The issues with this operation only arise when there is a large number of inputs in a new transaction, as the hardware wallet will have to calculate all of the hashes of previous transactions.</p>

<p>Hardware wallets do not, in comparison with a phone or a computer, have sufficient computational power to run through a large number of hashes quickly. This explains why some transactions might take a long time to be processed on TREZOR, especially in accounts with a large amount of small inputs.</p>

<p>This issue with limited power is further exacerbated by the fact that sighash operations (signature-hashing — different operation) scale quadratically and not linearly. This means that a transaction double in size will take four times as long to compute.</p>

<h2>How Will SegWit Change This?</h2>

<p>SegWit transactions are designed in such a way that allows <a href="/sample-bankchain-feature-set/">hardware wallets</a> to get rid of the verification process altogether. Why? Because SegWit transactions will include the value of previous outputs in the signature of the transaction. The wallet thus does not need to request the previous transactions nor hash them anymore, saving precious time for users.</p>

<p>It might seem to be a trivial change, but the security implications are large. The lower the amount of operations the hardware wallets need to do, the lower the probability of something going awry. As the value of the previous output to be used as input is already included in the signature of the previous transaction, there is no possibility of anyone modifying the input value.</p>

<p>Moreover, with SegWit, wallets do not sign each inputs separately anymore, but first they will hash all the inputs, and then sign the hash. With this method, the amount of operations the wallets have to do is decreased, and thus the transaction creation process is sped up. </p>

<p>This also means that the quadratic difficulty of sighash operations is replaced by linear difficulty; doubling the size of the transaction will theoretically only double the computation time.</p>

<h2>Should SegWit Be Activated?</h2>

<p>From a hardware wallet’s perspective there is no reason to delay SegWit activation. In fact, for any user with a hardware wallet, which is probably the most secure device you can use to store your private keys in, the benefits SegWit activation should be obvious.</p>

<p>To reiterate, this article raises the merits of SegWit without mentioning its implications for the Blocksize debate. It also does not discuss the method of implementation: softfork or hardfork. Nonetheless, it is disappointing that this piece of code has not been activated yet due to political disagreements within the Bitcoin ecosystem, in conjunction with the inability to compromise.</p>

<h2>Too Long; Did Not Read</h2>

<p>Currently, transactions do not contain the bitcoin value of inputs. Instead, they enclose the reference to the previous transaction, forcing TREZOR to use a workaround in order to safely retrieve the values and verify them. This process, however, takes precious amount of time. With SegWit, this will no longer be necessary as SW transactions include the value of inputs.</p>

