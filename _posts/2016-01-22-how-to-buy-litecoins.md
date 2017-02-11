---
layout: post
title: How to Buy Litecoins
author: Melvin Draupnir
authorurl: /melvin-draupnir/
description: Learn how to buy litecoins online, with cash, with bitcoin, or with PayPal.  
published: true
seotitle: How to Buy Litecoins Online, with Cash, or PayPal
---
<p>Buying [litecoin](/what-is-litecoin/) is not any different from purchasing bitcoins: find a Litecoin exchange, convert your local currency to litecoin, and send the litecoins to your wallet.
<p><center><iframe id="widget-ticker-preview" src="//www.coingecko.com/en/widget_component/ticker/litecoin/usd" style="border:none; height:125px; width: 275px;" scrolling="no" frameborder="0" allowtransparency="true"></iframe> <iframe id="widget-ticker-preview" src="//www.coingecko.com/en/widget_component/ticker/litecoin/btc" style="border:none; height:125px; width: 275px;" scrolling="no" frameborder="0" allowtransparency="true"></iframe></center>
<p>Finding a Litecoin exchange can be difficult because most exchanges don’t sell litecoin directly. In most cases customers must [first purchase bitcoins](/en/how-buy-bitcoins-online-best-bitcoin-exchange-rate-bitcoin-price/) and then trade for litecoin. 
<p>With that said, there are a few exchanges where users can purchase litecoins directly, without buying bitcoins first: 

{% for exchange in site.data.buy_litecoin %}
{% if exchange.tags == 'fiat' %}
{% include buy-list.html %}
{% endif %}
{% endfor %}

## Trading Bitcoins for Litecoins

If the options above don’t work, the second easiest way to get litecoins is to exchange bitcoins for litecoin. Many Bitcoin exchanges offer this trading pair:
 
{% for exchange in site.data.buy_litecoin %}
{% if exchange.tags == 'btc' %}
{% include buy-list.html %}
{% endif %}
{% endfor %} 

## Completing your Purchase

Leaving your coins on exchange is a risk that has cost Bitcoin users millions of dollars (e.g. Mt. Gox). Once your purchase has been made, send your litecoins to a wallet you control: 

* **[Electrum-LTC](https://electrum-ltc.org/)** is good choice on desktop computers. 
* **[Litecoin Wallet](https://play.google.com/store/apps/details?id=de.schildbach.wallet_ltc&hl=en)** is the most popular Android wallet.  
* **[Hive Wallet](https://itunes.apple.com/us/app/hive-wallet/id906990301?mt=8)** supports Litecoin and Bitcoin. 

## Buying Litecoins with PayPal
Although not recommended, it’s possible to buy litecoins with PayPal. First you must buy SLL on [VirWox](https://www.virwox.com?r=fbbb7), then trade SLL for bitcoin. Once you have BTC you can use any of the methods above to trade BTC for litecoin. 
