---
layout: post
title: How To Use Bitcoin Anonymously
author: Trace Mayer
authorurl: /trace-mayer-bitcoin-expert/
published: true
---

<p>As you probably already know, bitcoin is not anonymous (this property was never part of its original design). Bitcoin transactions are chained together in a permanent public record.
<p>Analysis of the blockchain may reveal a lot information about your transactions <a href="#references">[1]</a> (e.g., recipients of your payments, addresses in your wallet or the balance of your wallet).
<p>The following sections contains everything you need to know in order to prevent such kind of blockchain analysis.
</p>
<p>There are currently three main methods how you can make your transactions more private. The first method is called <b>CoinJoin</b> <a href="#references">[2]</a> and is based on 'joining' your transactions with transactions of other users.
<p>Most advanced project based on this method is JoinMarket <a href="#references">[3]</a>. This method is very secure, but unfortunately not fully implemented yet. However, the development process continues and the user base is slowly growing.
<p>The second method is called <b>Confidential Transactions</b> <a href="#references">[4]</a>. In simple terms, this method encrypts amounts in your transactions and helps obfuscate chain of the transactions.
<p>This method is not yet part of bitcoin implementation, but may be implemented in the future.
</p>
<br/>
<p class="text-center">
<img src="/images/anonymously/bitcoin-mixing-service-diagram.png" alt="how bitcoin mixing service works"/>
<br/>
<small>Figure 1: Basic workflow of a Bitcoin Mixing Service</small>
</p>
<p>The oldest and most often used method is <b>bitcoin mixing</b> (see Figure 1) which works on similar basis as mix network <a href="#references">[5]</a>. The bitcoin mixer receives bitcoins to input addresses and sends out different amounts from different input address.
<p>This method requires trusting the mixer, but is sufficiently secure when used properly. Many of our users mix their bitcons for the first time. Because mixing your bitcoins properly requires to follow some simple rules, we decided to write a manual that will make this operation much easier.
</p>
<h2>Buying bitcoins</h2>
<p>The first step is of course to get some bitcoins. Unfortunately, there is no easy way to buy bitcoins fully anonymously (we will solve that problem later). Most of the bitcoin exchanges have Know Your Customer (KYC) policy.
<p>That means you have to provide your ID, driver's license or passport before buying some bitcoins. Even when the identity verification is not required your bitcoins will be still linked to your bank account or your face (when buying in person).
<p>Therefore, feel free to chose the service which requires the lowest possible amount of information.
</p>
<p>A good option to use is <a href="http://geni.us/localbitcoins">LocalBitcoins.com</a>, since you can buy bitcoins quickly via this service without identity verification in many countries.
<p>However, we don't recommend using <a href="https://www.torproject.org/projects/torbrowser.html">Tor Browser</a> with this service, because some bitcoin sellers won't sell the bitcoins to you if you are connected via Tor.
<p><a href="http://geni.us/localbitcoins">LocalBitcoins.com</a> is good service, especially if you prefer wire transfer or buying bitcoins in person. It is also possible to buy bitcoins at your <a href="https://coinatmradar.com/countries/">local bitcoin ATM</a> or with debit card via <a href="https://circle.com/">circle.com</a> or <a href="http://geni.us/indacoin">Indacoin</a>.
<p>Unfortunately, not all debit/credit cards are accepted.
</p>
<p class="text-center">
<img src="/images/anonymously/buying-bitcoins.png" class="article-image" alt="buying bitcoins"/>
<br/>
<small>Figure 2: Buying bitcoins via LocalBitcoins.com</small>
</p>
<h2>Anonymous wallet</h2>
<p>Ok, let's assume we already have some fresh bitcoins from the bitcoin exchange. The second step is to create anonymous wallet. We will keep the mixed bitcoins in this wallet and also send anonymous payments from it.
<p>The most secure wallet is full bitcoin client (e.g., <a href="https://bitcoin.org/en/bitcoin-core/">Bitcoin Core</a>). However, this kind of wallet requires over 80 GB of hard drive space, generates a lot of network traffic and may be complicated for new bitcoin users.
</p>
<p>If you cannot afford such luxury there is also <a href="https://electrum.org/">Electrum</a> wallet. The Electrum wallet is an SPV client <a href="#references">[6]</a>. It is also very secure and requires very low amount of space on your hard drive. We will use it as an example in our manual.
<p>Download the Electrum wallet from its official website and install it. Download also standalone version of <a href="https://www.torproject.org/download/download.html.en">Tor</a> (without Tor Browser) and install it. You will need it to connect to Electrum servers via Tor anonymity network.
<p>The Tor will listen on TCP port 9050 after the installation. There is no need to change the default Tor settings, but don't forget to change the configuration of <b>Electrum - Tools Network</b> (for the proper configuration of network see Figure 2).
</p>
<p class="text-center">
<img src="/images/anonymously/tor-config.png" alt="tor configuration in Electrum"/>
<br/>
<small>Figure 3: Tor configuration in Electrum</small>
</p>
<br/>
<p>If you run the Electrum for the first time it will challenge you to create a new wallet. (see Figure 3). <b>Do not create the new wallet before the network is properly configured to use Tor!</b> Give some name to the wallet and continue.</p>
<p class="text-center">
<img src="/images/anonymously/name-wallet.png" alt="create new anonymous Electrum wallet"/>
<br/>
<small>Figure 4: Create new anonymous Electrum wallet</small>
</p>
<br/>
<p>Select the standard kind of the wallet on the next dialog and continue (see Figure 4).
</p>
<p class="text-center">
<img src="/images/anonymously/create-wallet.png" alt="select type of Electrum wallet"/>
<br/>
<small>Figure 5: Select type of Electrum wallet</small>
</p>
<br/>
<p>Electrum will challenge you to save the wallet generation seed in the next step (see Figure 5). You will need the seed if something bad happens to the wallet, so keep it in safe location and <b>private</b> (the seed on the picture is from empty wallet, so we can make it public, but you should not).
</p>
<p class="text-center">
<img src="/images/anonymously/electrum-seed.png" alt="electrum recovery seed"/>
<br/>
<small>Figure 6: Save the wallet generation seed</small>
</p>
<br/>
<p>Great, you are almost done. Switch to <b>Receive</b> tab and create some output addresses for the mixing service. We will use them later to send some bitcoins to the wallet. Optimal number of output addresses is 2-5.
</p>
<p class="text-center">
<img src="/images/anonymously/output-addresses.png" alt="create a few output addresses"/>
<br/>
<small>Figure 7: Create a few output addresses</small>
</p>
<h2>Mixing bitcoins</h2>
<p>The last part is mixing the bitcoins. We will send the bitcoins anonymously from <a href="http://geni.us/localbitcoins">LocalBitcoins.com</a> to the anonymous wallet via CoinMixer.se.
<p>Open our website in the Tor Browser and click on Participate link. Copy the output addresses from the previous step to the output fields. The sum of the output values makes the overall mixed value.
<p>There is also the delay value. The longer delay means that your bitcoins will be mixed with bitcoins of more users (better anonymity, but it takes longer time).
<p>We recommend setting different delay for each output. It is possible to set the delay to 0, but it is not recommend because it reveals in which block the outputs are.
</p>
<p class="text-center">
<img src="/images/anonymously/participation-create.png" class="article-image" alt="create a new participation"/>
<br/>
<small>Figure 8: Create a new participation</small>
</p>
<br/>
<p>The next step is simple. Just rewrite the captcha code and click on the continue button (see Figure 8).
</p>
<p class="text-center">
<img src="/images/anonymously/captcha.png" class="article-image" alt="rewrite the captcha code"/>
<br/>
<small>Figure 9: Rewrite the captcha code</small>
</p>
<br/>
<p>We are almost there. We just need to confirm the participation and the system will take care of the rest. You can chose from three transfer methods.
<p>We will choose Address and Amount, since we need to send the bitcoins from LocalBitcoins.com.
</p>
<p class="text-center">
<img src="/images/anonymously/transfer.png" class="article-image" alt="transfer of bitcoins"/>
<br/>
<small>Figure 10: Transfer of bitcoins</small>
</p>
<br/>
<p>Don't forget to save the Letter of Guarantee. It is important.
</p>
<p class="text-center">
<img src="/images/anonymously/letter-of-guarantee.png" class="article-image" alt="letter of guarantee"/>
<br/>
<small>Figure 11: Letter of guarantee</small>
</p>
<br/>
<p>We will copy the payment information exactly as it is to the LocalBitcoins.com payment form and send it.
</p>
<p class="text-center">
<img src="/images/anonymously/send-bitcoins.png" class="article-image" alt="sending bitcoins from LocalBitcoins.com"/>
<br/>
<small>Figure 12: Sending bitcoins from LocalBitcoins.com</small>
</p>
<br/>
<p>Your participation will be confirmed after 3 confirmations in the blockchain (see Figure 12).
</p>
<p class="text-center">
<img src="/images/anonymously/participation-confirmed.png" class="article-image" alt="participation is confirmed"/>
<br/>
<small>Figure 13: Participation is confirmed</small>
</p>
<br/>
<p>And that is it. Your bitcoins will be send with delay you provided in the participation form (see Figure 13). Thank you for reading this manual.
</p>
<p class="text-center">
<img src="/images/anonymously/received-bitcoins.png" alt="the bitcoins have been received"/>
<br/>
<small>Figure 14: The bitcoins have been received</small>
</p>
<h2>Best practices</h2>
<p>In the end, we present to you list of best practices that will help you to keep your transactions private.</p>
<ul>
<li>Always assume that all transactions from a particular wallet are linkable (never buy anonymous stuff and personal stuff with bitcoins from the same wallet).
</li>
<li>Always use Tor Browser when you are buying something with bitcoins from the anonymous wallet (your real IP address will remain unknown to the merchant).
</li>
<li>Always connect to Electrum servers via Tor (your real IP address will remain unknown to the Electrum server admin).
</li>
<li>Use Tor URL instead of clearnet URL whenever possible (location of hidden service server is harder to find for law enforcement agencies). A Tor URL is <a href="http://coinmixibh45abn7.onion/">http://coinmixibh45abn7.onion/</a>.
</li>
<li>Use the Tor Browser with disabled JavaScript if the mixing service supports it (LE used some JavaScript exploits in the past to deanonymize Tor users).
</li>
<li>Use at least two mixing services in a row to anynimize the bitcoins. Like LocalBitcoins.com mixing service A to mixing service B anoynymous-wallet (your transactions will remain private also in the case when one of the mixing services is compromised).
</li>
<li>If the mixing service requires user registration then use a different account for every mixing operation (this will prevent the mixing service to enumerate all your wallets).
</li>
<li>Use only well established mixing services and look for reviews on the internet before using them. Like <a href="http://bitblendervrfkzr.onion">BitBlender</a> and <a href="http://grams7enufi7jmdl.onion/">Helix by Grams</a>.
</li>
<li>Use only encrypted communication channels to contact the mixing service (unencrypted email can be easily intercepted). Bitmessage for example, is encrypted, anonymous, decentralised and uncensorable.
</li>
</ul>
<h2 id="references">References</h2>
<ol>
<li>Fergal Reid; Martin Harrigan (2011). - <a href="http://anonymity-in-bitcoin.blogspot.com/2011/07/bitcoin-is-not-anonymous.html">An Analysis of Anonymity in the Bitcoin System</a>&quot;</li>
<li>Gregory Maxwell (2013-08-22). - <a href="https://bitcointalk.org/index.php?topic=279249">CoinJoin Bitcoin privacy for the real world</a>. bitcointalk.org.
</li>
<li>Chris Belcher (2015-01-09). - <a href="https://bitcointalk.org/index.php?topic=919116.0">Joinmarket - Coinjoin that people will actually use</a>. bitcointalk.org.
</li>
<li>Gregory Maxwell (2015-06-09). - <a href="https://bitcointalk.org/index.php?topic=1085273.0">Confidential Transactions, Content privacy for Bitcoin transactions</a>. bitcointalk.org.
</li>
<li>David Chaum, Untraceable electronic mail, return addresses, and digital pseudonyms, Comm. ACM, 24, 2 (Feb. 1981); 84-90
</li>
<li><a href="https://en.bitcoin.it/wiki/Thin_Client_Security">Thin Client Security</a> - Bitcoin Wiki</li>
</ol>