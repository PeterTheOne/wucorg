---
layout: post
title: Bitcoin Privacy Technologies - Zerocash and Confidential Transactions
author: Zooko Wilcox-O'Hearn
authorurl: https://www.weusecoins.com/zooko-wilcox-ohearn/
published: true
---

<p>At Least Authority, <a class="reference external" href="https://leastauthority.com/about_us">our mission</a> is to bring verifiable end-to-end security to every user of the Internet. As a part of this mission, we are working on something that we can't announce yet, but it involves the <a class="reference external" href="http://zca.sh/">Zerocash</a> protocol for private Bitcoin transactions.</p>
<p>Recently Blockstream announced <a class="reference external" href="http://elementsproject.org/">Sidechains Elements</a>, which includes a privacy protocol named <a class="reference external" href="https://people.xiph.org/~greg/confidential_values.txt">Confidential Transactions</a>. We invited the lead author of Confidential Transactions — <a href="/gregory-maxwell-bitcoin-expert/">Greg Maxwell</a> — and the authors of the Zerocash Protocol to help us explain how Confidential Transactions compares to Zerocash.</p>
<p>In short, Zerocash offers privacy properties that Confidential Transactions does not. Most notably, Confidential Transactions only protects transaction values, whereas Zerocash also protects sender and receiver addresses – but at the cost of extra cryptographic novelty. In addition, there are other engineering and cryptography tradeoffs between the two.</p>
<p>—Zooko Wilcox-O'Hearn, Founder and CEO of LeastAuthority</p>
<h2>Overview</h2>
<p>Zerocash (ZC) and Confidential Transactions (CT) are both ledger protocols: they can be used to improve the privacy of any given ledger system, whether that’s in Bitcoin sidechains, centralized ledgers, or even Bitcoin itself. Zerocash was introduced as a proposed extension to Bitcoin, or a Bitcoin-like system, and Confidential Transactions was introduced as a potential Bitcoin sidechain feature as part of Blockstream Elements.</p>
<p>At a high level, the goal of Confidential Transactions is to hide the value of transactions, but it does <em>not</em> hide the participants of a transaction. The metadata of who-has-paid-whom is often more sensitive than the balances. It is possible to combine CT with other techniques (such as CoinJoin mixing) to improve participant confidentiality, although care must be taken to ensure the two schemes interact securely, and the degree of privacy depends on how many mixing transactions occur.</p>
<p>By contrast, in Zerocash provides full privacy for both transaction value and participants.</p>
<p>Finally, an important high-level distinction between the two protocols is that Confidential Transactions have flexible security parameters per transaction, whereas Zerocash has uniform security across the whole system. This may lead to important systemic impacts.</p>
<table border="1" class="docutils">
<colgroup>
<col width="44%" />
<col width="28%" />
<col width="28%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head" colspan="3"><p class="first last" id="table-1">Table 1. Comparing Ledger Privacy Protocol Characteristics</p>
</th>
</tr>
<tr><th class="head" rowspan="2">Example Protocols</th>
<th class="head" colspan="2">What's Confidential</th>
</tr>
<tr><th class="head">Sender/Receiver</th>
<th class="head">Amount</th>
</tr>
</thead>
<tbody valign="top">
<tr><td>Zerocash</td>
<td><strong>✔</strong></td>
<td><strong>✔</strong></td>
</tr>
<tr><td>Confidential Transactions</td>
<td>&nbsp;</td>
<td><strong>✔</strong></td>
</tr>
<tr><td>CoinJoin, Cryptonote, Bitcoin Mixers</td>
<td><strong>✔?</strong> <a class="footnote-reference" href="#id2" id="id1">[1]</a></td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id2" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id1">[1]</a></td><td>We list several schemes which strive for sender/receiver confidentiality, but do not make claims about their security.</td></tr>
</tbody>
</table>
<h2 id="comparison">Comparison</h2>
<p>Here we briefly compare the two approaches, showing their relative strengths and weaknesses, first in a summary <a class="reference internal" href="#table-2">Table 2</a>, followed by more explanation.</p>
<table border="1" class="docutils">
<colgroup>
<col width="45%" />
<col width="28%" />
<col width="28%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head" colspan="3"><p class="first last" id="table-2">Table 2. Zerocash and Confidential Transactions At A Glance</p>
</th>
</tr>
<tr><th class="head">&nbsp;</th>
<th class="head">Confidential Transactions</th>
<th class="head">Zerocash</th>
</tr>
</thead>
<tbody valign="top">
<tr><td><a class="reference internal" href="#confidentiality">Confidentiality</a></td>
<td>Only Amounts</td>
<td>Participants
and Amounts</td>
</tr>
<tr><td><a class="reference internal" href="#user-flexibility">User Flexibility</a></td>
<td>Fine-Grained</td>
<td>All-or-nothing</td>
</tr>
<tr><td><a class="reference internal" href="#transaction-size">Transaction Size</a> <a class="footnote-reference" href="#id9" id="id3">[2]</a></td>
<td>~5000 bytes</td>
<td>~1000 bytes</td>
</tr>
<tr><td><a class="reference internal" href="#proof-size">Proof Size</a> <a class="footnote-reference" href="#id9" id="id4">[2]</a></td>
<td>~2500 bytes</td>
<td>288 bytes</td>
</tr>
<tr><td><a class="reference internal" href="#proving-cost">Proving Cost</a> <a class="footnote-reference" href="#id10" id="id5">[3]</a></td>
<td>~100's/sec</td>
<td>~one per minute</td>
</tr>
<tr><td><a class="reference internal" href="#verification-cost">Verification Cost</a> <a class="footnote-reference" href="#id10" id="id6">[3]</a></td>
<td>~100's/sec</td>
<td>~100's/sec</td>
</tr>
<tr><td><a class="reference internal" href="#pruning-support">Pruning Support</a></td>
<td>Inherent Support</td>
<td>None Implemented</td>
</tr>
<tr><td><a class="reference internal" href="#cryptographic-basis">Cryptographic Basis</a></td>
<td><a class="reference external" href="https://en.wikipedia.org/wiki/Elliptic_curve_cryptography">ECDLP</a>, Random Oracles</td>
<td>Knowledge of
Exponent, <cite>KEA</cite></td>
</tr>
<tr><td><a class="reference internal" href="#peer-review">Peer Review</a></td>
<td>Community Review</td>
<td>Published peer-reviewed conference proceedings <a class="footnote-reference" href="#id11" id="id7">[4]</a></td>
</tr>
<tr><td><a class="reference internal" href="#code-auditability">Code Auditability</a></td>
<td>Open Source</td>
<td>Not Yet Public</td>
</tr>
<tr><td><a class="reference internal" href="#parameter-setup">Parameter Setup</a></td>
<td>Not Vulnerable</td>
<td>Complex, Potential for Compromise <a class="footnote-reference" href="#id12" id="id8">[5]</a></td>
</tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id9" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label">[2]</td><td><em>(<a class="fn-backref" href="#id3">1</a>, <a class="fn-backref" href="#id4">2</a>)</em> For these sizes we consider a “standard” transaction shape with two inputs and two outputs. There are important caveats, see
<a class="reference internal" href="#transaction-size">Transaction Size</a> and <a class="reference internal" href="#proof-size">Proof Size</a> explanations below.</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id10" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label">[3]</td><td><em>(<a class="fn-backref" href="#id5">1</a>, <a class="fn-backref" href="#id6">2</a>)</em> These are rough approximations of a single core on a relatively recent machine; the important take-away is the large relative cost of Zerocash proofs. See <a class="reference internal" href="#proving-cost">Proving Cost</a> below.</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id11" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id7">[4]</a></td><td>See <a class="reference internal" href="#peer-review">Peer Review</a> below for references.</td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id12" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id8">[5]</a></td><td>New research substantially improves this security, see <a class="reference internal" href="#parameter-setup">Parameter Setup</a> below.</td></tr>
</tbody>
</table>
<h3 id="explanation">Explanation</h3>
<p id="confidentiality"><strong>Confidentiality.</strong> Confidential Transactions hide transaction <em>values</em> whereas Zerocash hides all transaction information (except for timing).</p>
<p>Both Zerocash and Confidential Transactions hide the amount of money transferred in transactions. However, CT does not hide the address of the sender and the receiver. So “Transaction Graph Analysis” techniques like <a class="citation-reference" href="#a" id="id13">[a]</a>, <a class="citation-reference" href="#b" id="id14">[b]</a>, <a class="citation-reference" href="#c" id="id15">[c]</a>, <a class="citation-reference" href="#d" id="id16">[d]</a>, and <a class="citation-reference" href="#e" id="id17">[e]</a> may still potentially be used to connect and trace them to endpoints like exchanges.</p>
<p>Transaction graph analysis can potentially be thwarted by mixing, for example by using CoinJoin. But mixing comes with a variety of other implementation challenges, security hazards, and costs; in particular, mixing adds to blockchain bloat, and mixing is not implemented in Elements.</p>
<p id="user-flexibility"><strong>User Flexibility.</strong> Zerocash is an “all-or-nothing” protocol. There is only one level of security, and that provides confidentiality against unauthorized parties for both amounts and sender/receiver addresses. Users cannot alter this.</p>
<p>(Note: users of Zerocash <em>can</em> make their transaction records transparent to chosen authorized parties. The discussion about security levels here is only about the level of security that the system provides against snooping by <em>unauthorized</em> parties. Zerocash is designed to provide nothing but maximal security against snooping by <em>unauthorized</em> parties.)</p>
<p>By contrast, Confidential Transactions allows per-transaction security tuning, such as by trading off <em>some</em> amount of confidentiality for smaller overhead <a class="footnote-reference" href="#id19" id="id18">[6]</a>.</p>
<p>This is a fundamental difference that affects usability, systemic behavior, and many implementation issues. A usability difference might be that in a CT system, a recipient may need to distinguish “how much privacy” comes with the sender's amount, whereas in Zerocash there is a known “standard amount of privacy”.</p>
<p>There may be systemic impacts: if many users opt to turn down their privacy settings, then the few users who leave them high may draw unwanted attention.</p>
<p>Finally, there are many implementation details this difference affects. For example, all Zerocash transactions have the same <em>shape</em> (number of inputs and outputs) and size to aide in indistinguishability, whereas each CT transaction may have a different shape. This also may have usability impact because if a user wants to split a value into many new values, for example, their software must use multiple Zerocash transactions, whereas CT software may choose to use either a single transaction or more depending on other privacy or performance goals.</p>
<table class="docutils footnote" frame="void" id="id19" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id18">[6]</a></td><td>Note: Even when a protocol is flexible, it's possible to enforce a stricter use of a protocol with the ledger consensus rules, so long as that stricter check relies only on ledger-public information.</td></tr>
</tbody>
</table>
<p id="transaction-size"><strong>Transaction Size.</strong> Both systems use transactions which contain some metadata along with one or more <em>proofs</em> related to the inputs or outputs.</p>
<p>Zerocash has only one transaction shape with 2 inputs and 2 outputs, which is the minimum for splitting and joining values <a class="footnote-reference" href="#id21" id="id20">[7]</a>. Note also that most <em>payments</em> require 2 outputs to account for change back to the sender.</p>
<p>For this standard transaction shape, the on-chain cost (blockchain bloat) of a typical CT transaction is higher than that of Zerocash.</p>
<p>However, for other transactions, especially “sweep” transactions with 1 output and N inputs, a CT transaction is much smaller because range proofs are unneeded.</p>
<p>Additionally, CT supports transactions with any number of inputs or outputs, whereas ZC has a fixed shape.</p>
<table class="docutils footnote" frame="void" id="id21" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id20">[7]</a></td><td>The Zerocash protocol could be extended to allow more inputs and more outputs. This article only considers the current published protocol.</td></tr>
</tbody>
</table>
<p id="proof-size"><strong>Proof Size.</strong> The size of a full CT proof is, by default, 2.5Kb, compared to 288 bytes for Zerocash. However, when a transaction has only a single output, range proofs can be omitted from a transaction, and the remaining proof structure requires only a single 33 byte Pedersen commitment.</p>
<p>The proof size for CT can also be run in ‘reduced size’ modes, although this comes with a privacy tradeoff since it reveals more information about balances. The Zerocash proof size reflects “full privacy” mode, and there is no way to decrease the level of protection.</p>
<p>Finally, some of the CT proof can be recycled for a dual use, since it can contain an encrypted message from the sender to recipient.</p>
<p id="proving-cost"><strong>Proving Cost.</strong> The time it takes to create a transaction is much larger in Zerocash than in CT, although both take longer than ordinary Bitcoin transactions. We believe both are tolerable. Given these two state-of-the-art approaches, there remains a tradeoff between cost and privacy.</p>
<p id="verification-cost"><strong>Verification Cost.</strong> The transaction verification costs for both ZC and CT transactions are higher than for Bitcoin, but both are likely tolerable. On a desktop benchmark, a single thread can validate 175 ZC pour transactions per second.</p>
<p id="pruning-support"><strong>Pruning Support.</strong> CT provides pruning <em>inherently</em>, whereas ZC does not have pruning currently.</p>
<p>Pruning allows a “full node” (i.e. a node that independently validates every new transaction block) to reduce its storage costs by forgetting about previously-spent transactions. In CT, a transaction output is publicly known to be either spent or unspent, just as in Bitcoin, and therefore Bitcoin-style pruning works “out of the box”.</p>
<p>By contrast Zerocash requires verifiers to remember a unique identifier for every spent value, and in the current design this set grows indefinitely. The paper presents potential optimizations which can mitigate these storage requirements by making various tradeoffs (Sections 8.3.1 and 8.3.2 of the <cite>Zerocash</cite> paper in <a class="reference internal" href="#peer-review">Peer Review</a>).</p>
<p>Choices around pruning involve other nuanced trade-offs. For example, systems which allow pruning spent outputs necessarily expose information about the transaction graph and constrain what kinds of sender/receiver graph confidentiality is possible.</p>
<p id="cryptographic-basis"><strong>Cryptographic Basis.</strong> The underlying cryptographic basis of CT is the same as Bitcoin and many other deployed systems, while ZC is one of the first practical applications which relies on a particular assumption.</p>
<p>Specifically, CT relies on a variant of Schnorr signatures, whose security can be based on either the elliptic-curve DL problem (<cite>ECDLP</cite>) and the Random-Oracle (<cite>RO</cite>) assumption. On the other hand, ZC relies on zkSNARKs whose security is based on variants of the Knowledge Of Exponent (<cite>KoE</cite>) assumption for bilinear groups (instantiated via certain pairing-friendly elliptic curves). Both the <cite>RO</cite> and <cite>KoE</cite> assumptions have been studied by cryptographers for over two decades, but only the former has seen widespread deployment in practice.</p>
<p id="peer-review"><strong>Peer Review.</strong> CT is a new application of well-understood cryptographic primitives, and has been reviewed informally by industry experts.</p>
<p>The Zerocash protocol has been published in a peer reviewed academic conference, as well as building on prior published work. Additionally published work on <a class="reference internal" href="#parameter-setup">Parameter Setup</a> was presented at a conference this year:</p>
<ul class="simple">
<li>Primary work: <a class="reference external" href="http://zerocash-project.org/media/pdf/zerocash-extended-20140518.pdf">Zerocash: Decentralized Anonymous Payments from Bitcoin</a>
at <a class="reference external" href="http://www.ieee-security.org/TC/SP2014/program-notabs.html#28">IEEE Security and Privacy (Oakland) 2014</a></li>
<li>Prior work: <a class="reference external" href="http://zerocoin.org/media/pdf/ZerocoinOakland.pdf">Zerocoin: Anonymous Distributed E-Cash from Bitcoin</a>
at <a class="reference external" href="http://www.ieee-security.org/TC/SP2013/program.html">IEEE Security and Privacy (Oakland) 2013</a></li>
<li>More secure setup: <cite>Secure Sampling of Public Parameters for Succinct Zero Knowledge Proofs</cite>
at <cite>IEEE Security and Privacy (Oakland) 2015</cite></li>
</ul>
<p>zkSNARKs have been covered by many <a class="reference external" href="http://www.scipr-lab.org/publications.html">peer-reviewed publications</a>.</p>
<p id="code-auditability"><strong>Code Auditability.</strong> CT is open source. The ZC code is not yet public, although a fundamental component, <a class="reference external" href="https://github.com/scipr-lab/libsnark">libsnark</a> is currently open source.</p>
<p>The community behind these projects highly value open source software. It is crucial that security-related software, especially for critical infrastructure such as global transaction systems, is auditable by the public.</p>
<p>The ZC authors intend to release an open source prototype.</p>
<p id="parameter-setup"><strong>Parameter Setup.</strong> CT has very simple one-time initial parameter selection which is amenable to common “nothing up my sleeve” selection techniques. Zerocash has complex one-time initial parameter setup which is vulnerable to compromise.</p>
<p>The Zerocash authors have presented new research on a secure multi-party computation to improve the parameter setup security. This new setup distributed protocol provides the guarantee that if even one party involved in the setup follows the protocol correctly, then the setup is secure. (Conversely all participants must be compromised for parameter compromise.)</p>
<h2 id="conclusion">Conclusion</h2>
<p>Confidential Transactions and Zerocash are two protocols for augmenting ledgers with better privacy. Confidential Transactions only protects transaction values, whereas Zerocash also protects sender/receiver addresses.</p>
<p>In Zerocash, all coins are equal, and values are truly fungible. Users are presented with an all-or-nothing security choice and only a single security level to understand. In Confidential Transactions, users have more flexibility and can tune privacy knobs for their individual needs, and as a result transactions are distinct and have history, and users (or their software) needs to manage fine-grained security levels.</p>
<p>From a system-wide perspective, Zerocash's all-or-nothing security level means all users have strong privacy, even when it's not critical for them. In Confidential Transactions it may be that only users with strong privacy needs have strong privacy, and if this set of users is small enough it may endanger their privacy.</p>
<p>Each has costs and tradeoffs on top of the underlying ledger, related to fundamental security assumptions, maturity of cryptographic techniques, amount of blockchain bloat, proving and verifying costs, and burdens on senders or recipients.</p>
<p>The authors agree that both Zerocash and Confidential Transactions should be pursued – as well as other future innovations! –  to have the best chance of providing strong financial privacy and fungibility.</p>
<p>— Alessandro Chiesa (Zerocash), Andrew Miller (LeastAuthority), Christina Garman (Zerocash), Eli Ben-Sasson (Zerocash), Eran Tromer (Zerocash), Greg Maxwell (Blockstream), Ian Miers (Zerocash), Madars Virza (Zerocash), Matthew D. Green (Zerocash), Nathan Wilcox (LeastAuthority), Zooko Wilcox-O'Hearn (LeastAuthority)</p>
<p>Thanks to Gordon Mohr for review and comments.</p>
<h2 id="references">References</h2>
<table class="docutils citation" frame="void" id="a" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id13">[a]</a></td><td>Ron, Dorit, and Adi Shamir. Quantitative analysis of the full bitcoin transaction graph. Financial Cryptography and Data Security. 2013. <a class="reference external" href="http://eprint.iacr.org/2012/584">http://eprint.iacr.org/2012/584</a></td></tr>
</tbody>
</table>
<table class="docutils citation" frame="void" id="b" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id14">[b]</a></td><td>Reid, Fergal, and Martin Harrigan. An analysis of anonymity in the bitcoin system. Security and Privacy in Social Networks. 2013. <a class="reference external" href="http://arxiv.org/abs/1107.4524">http://arxiv.org/abs/1107.4524</a></td></tr>
</tbody>
</table>
<table class="docutils citation" frame="void" id="c" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id15">[c]</a></td><td>Spagnuolo, Michele, Federico Maggi, and Stefano Zanero. Bitiodine: Extracting intelligence from the bitcoin network. Financial Cryptography and Data Security. 2014. <a class="reference external" href="http://www.ifca.ai/fc14/papers/fc14_submission_11.pdf">http://www.ifca.ai/fc14/papers/fc14_submission_11.pdf</a></td></tr>
</tbody>
</table>
<table class="docutils citation" frame="void" id="d" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id16">[d]</a></td><td>Ron, Dorit, and Adi Shamir. How Did Dread Pirate Roberts Acquire and Protect His Bitcoin Wealth?. Financial Cryptography and Data Security. 2014. <a class="reference external" href="https://www.ifca.ai/fc14/bitcoin/papers/bitcoin14_submission_2.pdf">https://www.ifca.ai/fc14/bitcoin/papers/bitcoin14_submission_2.pdf</a></td></tr>
</tbody>
</table>
<table class="docutils citation" frame="void" id="e" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id17">[e]</a></td><td>Koshy, Philip, Diana Koshy, and Patrick McDaniel. An analysis of anonymity in bitcoin using p2p network traffic. Financial Cryptography and Data Security. 2014. <a class="reference external" href="https://fc14.ifca.ai/papers/fc14_submission_71.pdf">https://fc14.ifca.ai/papers/fc14_submission_71.pdf</a></td></tr>
</tbody>
</table>
