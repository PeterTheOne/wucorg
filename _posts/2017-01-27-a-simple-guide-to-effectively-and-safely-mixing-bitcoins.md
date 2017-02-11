---
layout: post
title: A Simple Guide To Effectively And Safely Mixing Bitcoins
author: Melvin Draupnir
authorurl: /melvin-draupnir/
published: true
---

<p>Bitcoin tumbling, also referred to as Bitcoin mixing or Bitcoin laundering, is the process of using a third party service to break the connection between a <a href="/tumbling-bitcoins-is-a-path-through-the-rinse-cycle/">Bitcoin address sending coins</a> and the address(s) they are sent to. </p>

<p>Since the Bitcoin blockchain is a public ledger that records every transaction, mixing coins is critical for anyone who doesn’t want the entire world to know exactly where they send and store their BTC, or from where they receive it.</p>

<p>Properly mixing coins may seem like a daunting task to those who aren’t very familiar with Bitcoin, but it is actually a simple process that will only take a few minutes of your time for each deposit.</p>

<p>There are good reasons for everyone to mix their coins, but for those who use Darknet Markets in particular, it is a necessity. New tools are being built all the time to increase the ability of the public, as well as private corporations and government agencies, to follow coins through the blockchain and track those who use it. </p>

<p>It may seem like a waste of time now, but in the near future it may be simple for anyone- including friends, relatives, employers, and law enforcement, to track every <a href="/adam-back-confidential-transactions/">Bitcoin transaction</a> you’ve ever made and see exactly where it ended up. Breaking the connection between your addresses and the coins’ destination by mixing them is certainly a precaution that all DNM users should take.</p>

<p>In this guide we attempt to provide the simplest possible step-by-step instructions to help users unfamiliar with the process of Bitcoin tumbling do so effectively. This guide assumes the reader already has a basic understand of how to send Bitcoins and how to use .onion sites.</p>

<p>To mix your coins using this method, you will need:</p>

<p>-Bitcoins, or the ability to buy them.</p>
<p>-The Tor Browser</p>
<p>-The ability to create new Bitcoin wallets, both via Tor and on the clear net. We recommended using Electrum, but any client that functions over Tor will work. Alternately, you could use Blockchain.info and their Tor hidden service to create all or some of your wallets.</p>

<p>NOTE: Always make sure you get the .onion link for this and every hidden service from a safe place (like Darknetmarkets.org), never from Wikipedia, Reddit, or Hidden Wikis! Also make sure that you <a href="/how-banks-can-benefit-from-blockchain/">never use the blockchain</a>.info clearnet url over Tor; doing that opens you up another possible vulnerability (malicious tor exit nodes). A good place to make sure you are using the correct URL is from our Darknet Resources page.</p>

<h2>The Steps</h2>

<p><strong>Step #1:</strong> Create a wallet on the clearnet. (We will refer to this as wallet #1)</p>

<p><strong>Step #2:</strong> Buy Bitcoins, and send the amount you want to mix to wallet #1.</p>

<p><strong>Step #3:</strong> Create a second wallet, this time over the Tor network. (wallet #2)</p>

<p><strong>Step #4:</strong> Send your bitcoins from wallet #1 directly to wallet #2.</p>

<p>The reason for this is to add plausible dependability between your clearnet wallet and in-person purchases. If you are ever investigated by law enforcement or the company from which you are buying coins (this happens with Coinbase especially), you can reasonably claim that you sent them to someone else who controls wallet #2 (for whatever made-up reason you have in mind as your excuse for your BTC purchase). After that you have no idea/don’t care what that person did with them, nor should anyone expect you to.</p>

<p><strong>Step #5:</strong> Create a third wallet, also over the Tor network. (wallet #3).</p>

<p><strong>Step #6:</strong> Select which mixer you will be using, and set up your transaction there using the address(s) from wallet #3. It is best to use multiple addresses, and to set random time delays.</p>

<p>ALWAYS MAKE SURE YOU ARE USING THE CORRECT .ONION LINKS!</p>

<p>Scams are rampant everywhere online, and the darknet is no different. You can choose your mixer(s) and get the correct URLs from our list of darknet Bitcoin mixers.</p>

<p>We recommend Helix by Grams first, and then Bitcoin Blender, as the two seemingly best in a group of imperfect options. They have both been extremely reliable so far while processing millions of dollars. DO NOT use blockchain.info’s shared send or any other coinjoin product as your mixer, as those do not completely hide your trail like the others.</p>

<p>Helix Grams .onion</p>

<p>Bitcoin Blender</p>

<p>NOTE: Turn off JavaScript before doing this step if you are using Helix, Bitcoin Blender, or other mixers that function without it. (Click on the “S!” icon before the address bar in the Tor browser, then >Forbid Scripts Globally”.)</p>

<p>Unfortunately Bitmixer still requires users have JavaScript enabled.</p>

<p>Save the “Letter of Guarantee” if you are using Bitmixer. If you are using Helix, save the URL it sends you to after you enter your address(s). Make a backup of these, or your login details for the other mixers.</p>

<p><strong>Step #7:</strong> Send the coins from wallet #2, over Tor, to the address generated for you by the mixer.</p>

<p><strong>Step #8:</strong> Assuming these coins are going to be sent to a darknet market… if you don’t already have your deposit address, log in and get it while having JavaScript disabled. Never use any market that requires you to enable JS!</p>

<p><strong>Step #9:</strong> You can use Blockchain.info’s Tor hidden service to watch for your coins to arrive from the mixer. Once they have, restart Tor and then send the coins to your market address (or their eventually destination)!</p>

<p>The reason you should create an extra wallet in between your mixer and market account, is in case you ever run in to any type of problem with your account (lost password, hacked/phished, lost PGP key, etc), you can use the fact that you control all of the recent deposit address as proof that you are the rightful owner of this account.</p>

<p>You should also create a wallet you control in between any coins you may ever withdrawal from a market and a mixer. This is far more important than the reverse, in case the market takes a long time to put your deposit through (which happens, trust me). Mixers only keep track of the addresses it generates for you for a set amount of time, usually between 6 and 24 hours. </p>

<p>If you initiate a withdrawal from a market directly to a mixer’s bitcoin address, and the market runs into problems and doesn’t send your withdrawal for 48 hours, you face a very real risk of the mixer not forwarding your coins. This would not be the mixer’s fault, as they are open about how they work. They purge records every X hours for privacy.</p>

<p>TIP: You can use Blockchain.info’s taint analysis to make sure that no trace remains between wallet #2 and wallet #3. Access it like this, replacing 1YOURBITCOINADDRESS (in blue) with yours:</p>

<p>Search this page for your address(s) from wallet #2. If they aren’t there, you’ve successfully performed a zero-taint mix of your Bitcoins! If an address from wallet #2 does show up, there is a problem with the mixer you are using, you should contact them and/or use a different one in the future.</p>

<p>The only weakness remaining is the fact that the mixing company has records of your transactions, and although they all claim to delete them shortly after the transaction is complete, it is possible they could have a trail of where your coins went. You can negate this risk by repeating the process with a second mixing service.</p>

<p>I probably made this sound more complicated than it actually is. In total it should only take about 10-15 minutes, and it is something worth doing if you value your privacy and want to make sure you never lose any coins!</p>

<p>As with anything, you should do your research before using Bitcoin tumbling services and use the ones with the best reviews and highest levels of trust. The tumblers we list as trusted have been around for some time and have had no verifiable complaints against them. The other services listed are either newer, <a href="/bitcoin-privacy-technologies-zerocash-confidential-transactions/">have been hacked</a>, or have had numerous complaints against them. We do not link to mixers that are scams, or that do not function as advertised.</p>


