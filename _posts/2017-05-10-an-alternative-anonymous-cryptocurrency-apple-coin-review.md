---
layout: post
title: An Alternative Anonymous Cryptocurrency Apple Coin Review
description: An Alternative Anonymous Cryptocurrency Apple Coin Review
author: Melvin Draupnir
authorurl: /melvin-draupnir/
published: true
---

<p><strong>AppeCoin, Sergio D. Lerner‘s</strong> proposal for an <a href="/a-new-way-for-bitcoin-improvement-introduced-lumino-for-better-scalability/">e-cash scheme</a>, is designed for a peer-to-peer network which does not rely on a Trusted Third Party. Like the cryptocurrencies Monero or Zcash, AppeCoin is a protocol which aims to guarantee to its users full privacy. Lerner’s e-cash scheme leverages coin shuffling. Unlike ZeroCoin, where the monetary units are of a fixed value and so the transaction amount can be deduced from the number of units sent, AppeCoin enables users to truly hide transaction amounts by offering the option to divide and combine coins.</p>

<p>You can find the latest version of the AppeCoin draft here.</p>

<h2>Overview:</h2>

<p>Peers have private accounts and can send monetary units, called bills, to other peers. The amount of a bill is encrypted and is only known to the bill`s owner. Bills can be divided into smaller bills or combined into larger bills. The process of bill splitting and bill combining can be done without revealing the value of the bill or its parts. Zero-knowledge proofs are used to demonstrate correctness: the value of the bill is equal to the sum of its parts. There is a minimum bill value in order to avoid inflation.</p>

<p>Transactions to other peers can be sent without revealing their public addresses by using universal re-encryption. Once a payment is sent, it has to be accepted by the receiver. Payer and payee exchange the secret keys of the encrypted bill. The communication between payer and payee uses hybrid encryption and entity authentication.</p>

<p>The community verifies the validity of transactions and that coins have been divided or combined correctly. In a proof-of-work based framework, these changes are recorded in a ledger maintained by the miners. In order to <a href="/bank-of-canada-studies-digital-currencies/">increase anonymity</a>, AppeCoin provides private, delegated, and public bill shuffling. The correctness of the shuffles is verified by the miners.</p>

<h2>AppeCoin seeks to ensure (see p. 6 in draft):</h2>

Efficiency: low transaction wait-time.
Security: no double-spending, no over-spending, unforgeability (of bills and payment transcripts), authenticity, non-repudiation, portability.
Privacy: anonymity (payer cannot be identified from data exchanged during payment), untraceable (infeasible to follow the history of a bill), unlinkable payments, private account balance, hidden transaction amounts.

<p>The difficulty of the decisional Diffie-Hellman problem and of the representation problem should guarantee security and privacy as long as the encryption scheme used resists Ciphertext-only attacks and Chosen-Plaintext attacks.</p>

<h2>More Details:</h2>

<p>Below, we describe some key cryptographic building blocks and algorithms used in the AppeCoin protocol.</p>

<p><strong>A.1: Universal Re-Encryption of Schnorr Public Keys:</strong> A bill contains the public key of the present bill owner. Universal re-encryption is used to re-encrypt the public key of the bill owner without making him change his private key.</p>

<p><strong>A.2: Bill Shuffle:</strong> The BillShuffle algorithm shuffles the bills and provides a zero-knowledge proof of <a href="/bitcoin-economy-will-be-helpful-to-conceal-greeks-richness/">correctness of the shuffle</a>. The input of the BillShuffle algorithm is a list A = (a1, … , an) of bills ai with i=1, … , n and its output is a list B = (b1, … , bn) where bi is the encryption of  aπ(i) for a permutation π with encryption key k.</p>

<p>Two proof systems are considered in AppeCoin proposal. Both apply the Fiat-Shamir heuristic to an interactive public-coin proof system. The second proof system proposed uses a (pseudo-)random subset test which makes it more efficient. Zero-knowledge is achieved by blinding the encryption key and only showing the verifier the image or preimage of a randomly chosen subset under the given permutation π, but not the subset itself. The prover commits to the encryption of the product of the elements of the subset. The assumed hardness of the representation problem makes it difficult to just guess the product.</p>

<p><strong>A.3: CoinSplitting: </strong>The input of the CoinSplitting algorithm is a bill a and produces an output of two bills b and c whose values add up to the value of bill a. The algorithm provides a zero-knowledge proof for correctness.</p>

<p>The amount v of a bill is hidden in the exponent, i.e. as xv. (Note that in the proposal exponentiation refers to homomorphic encryption). The core idea of the CoinSplitting algorithm for proving balance, i.e. va= vb + vc, is to check the correctness of the equation xva = xvb × xvc.  A blinding factor is used to disguise proportion: xkva  zk= xkvb  zkb × xkvc zkc  with k=kb + kc for random kb and kc. The prover changes exponents or multiplies factors and provides the verifier with proofs of knowledge.</p>

<p><strong>A.4: InRangeProof: </strong>The input for the InRangeProof algorithm is a bill and a range for its value. When the bill is in the given range, the algorithm´s output is 1.</p>

<p><strong>A.5: SendBill:</strong> This action includes two algorithms which produce a public and a private message.</p>

<p>Public message: This message is <a href="/bitcoin-might-be-affect-with-digital-geneva-convention/">spread through the network</a> and contains the hash of the public key of the current bill owner, and the destination address and signature of the sender.</p>

<p>Private message: This message is sent privately from the sender to the receiver of the transaction, and is essentially the encryption of the secret keys of the bill, so that the receiver can verify the amount and modify the bill.</p>

<p><strong>A.6: ReceiveBill: </strong>The receiver checks the sender´s identity, and verifies that the bill and the amount which was sent to him, is correct.</p>

<p><strong>A.7: Public Check of Transaction:</strong> Miners search for the serial number of the bill in the ledger, and verify that the bill is unspent and that the sender´s Schnorr signature is correct. The sender´s public address is temporarily visible, until it is disguised by re-encryption.</p>

<h2>Comments:</h2>

<p>We think the AppeCoin proposal is exciting and would like to comment on some of its strong points and point to places which we think should be filled out more.</p>

<h2>Ad A.1: Universal Re-Encryption:</h2>

<p>a) The decisional Diffie-Hellman (DDH) should be assumed instead of computational Diffie-Hellman (CDH) (AppeCoin draft, p. 8).</p>

<p>b) The AppeCoin draft claims that universal re-encryption is secure for any encryption scheme satisfying indistinguishability, but provides no reference. Young/Yung´s article Semantically Secure Anonymity: Foundations of Re-Encryption demonstrates the security for one such encryption scheme, the ElGamal encryption.</p>

<h2>Ad A.2: BillShuffle:</h2>

<p><strong>a) Security aspects:</strong> Formal proof is needed for the claim that BillShuffle provides a non-interactive zero-knowledge proof.</p>

<p>The Fiat-Shamir heuristic is a common way to transform a constant round interactive proof into a non-interactive proof. The heuristic is proven to be secure, i.e. computationally sound, in the random oracle model. Some examples of insecure transformations exist in the plain model, but the Fiat-Shamir heuristic applied to interactive proofs, not just arguments, was recently  proven secure under some conditions for the hash functions involved. See Tauman-Kalai/Rothblum/Rothblum.</p>

<p>Some evidence is provided for the security of the BillShuffle algorithm, but there is no formal proof of security in the draft. Completeness is straight-forward. The article of Tauman-Kalai/Rothblum/Rothblum may imply that the BillShuffle algorithm satisfies computational soundness even in the plain model: the Fiat-Shamir transform is applied to proofs. Although it seems plausible that zero-knowledge can be deduced from the strength of the encryption scheme, the required zero-knowledge simulator is missing.</p>

<p><strong>b) Performance: </strong>The proof system with the random subset test requires an average of rounds*3/2 exponentiations to prove and verify a shuffle of n bills which results in a very fast run time. [Compare the shuffle protocol by Abe (22*n log⁡(n) exponentiations), Sako-Kilian (642*n exponentiations), Furukawa or Groth or Lipmaa-Fausti/Zajac (using pairings: roughly 3n), Lindell-Pinkas (cut-and-choose on circuits; roughly  15qn + 39n + 10q + 6 exponentiations, where q is a statistical security parameter)].</p>

<p>The private keys of shuffle participants may be vulnerable to side-channel attacks since a participant of a shuffle must decrypt all shuffled bills until he finds his own which causes an average of n/2  calls of his private key.</p>

<p><strong>c) Technical Remarks:</strong></p>
<ul>
<li>In figure 4, the definition of bw as bw:=awk is missing.</li>
<li>In figure 7, p. 13, Blob D should start with s (number of rounds) in order to have the same hash H(C) as in the proof;</li>
<li>In figure 7, p. 13, bj in 8.2.3 should be swapped with aQ(s,i)  in 9.2.3;</li>
<li>In figure 8, p. 14, in 14.1.1.3, ts × k should be replaced by rs × k. Index s should be j. Similarly, this applies to ts × k-1  in 1.4.2.1.1.</li>
</ul>
<h2>Ad A.3: CoinSplitting:</h2>

<p><strong>a) Security aspects:</strong> Formal proof is needed for the claim that CoinSplitting provides a zero-knowledge proof for correctness.</p>

<p>Heuristically, the <a href="/dubai-to-host-a-new-world-blockchain-forum/">Discrete Logarithm Problem</a> makes it hard for the prover to cheat the verifier by changing exponents. The prover could try to push some part of vb into the exponent of the neighboring factor z, but he would have to know the logarithm of the blinding factor  (which should be verifiably chosen at random) with respect to the basepoint or with respect to x. However, the draft lacks a formal proof for soundness. Although we could find no evidence that the proof in CoinSplitting leaks information, the draft does not provide a formal proof for zero-knowledge.</p>

<p><strong>b) Performance:</strong> Proof and verification for two bills requires 12 exponentiations and many zk-proofs of knowledge of encryption keys (e.g. using Schnorr ID protocol in case of a Pohlig-Hellman encryption scheme). The proposal´s author, Sergio Lerner, hopes to improve this in the future.</p>

<p><strong>c) Technical Remarks:</strong></p>
<ul>
<li>In DecompProof1, p. 23, we suggest defining bu as bu=a‘u, i.e., bu= auk qb ; otherwise bt= but does not hold;</li>
<li>In DecompProof1, p. 23, Step 6 should be analogous to step 3.</li>
</ul>
<h2>Additional Resources</h2>

<p>APPECoin, a system with total anonymization – key design points</p>
<p>APPECoin (Anonymous Peer-to-Peer electronic Coin) design (2012)</p>
<p>AppeCoin Anonymous Cryptocurrency Draft (2014)</p>

<h2>If you liked this article, you might also like:</h2>

<p>zk-SNARKs Technically Explained: Basic Principles</p>
<p>Quantum Resistant Public Key Exchange: The Supersingular Isogenous Diffie-Hellman Protocol</p>
<p>Comparison of Cryptocurrency Developments</p>
<p>Some Comments on the Security of ECIES with secp256k1</p>
