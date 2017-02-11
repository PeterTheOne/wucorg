---
layout: post
title: How to Buy Ether (Ethereum)
author: Melvin Draupnir
authorurl: /melvin-draupnir/
description : In most cases buying bitcoins and trading for ether is the easiest way to get ether.
published: true
seotitle: How to Buy Ether (Ethereum)
---
![how to buy ether](/images/ethkraken.png)

Although [Ethereum](/what-is-ethereum/) has one of the largest cryptocurrency market caps, it's still fairly new. Not all exchanges support direct purchases of ether. In most cases buying bitcoins and trading for ether is the easiest way to get ether.  

With that said, there are still a few exchanges where you can buy ether without bitcoin: 

{% for exchange in site.data.buy_ether %}
{% if exchange.tags == 'fiat' %}
{% include buy-list.html %}
{% endif %}
{% endfor %} 

## Trading Bitcoins for Ether

If using Kraken isn't an option, the second easiest way to get ether is to exchange bitcoins for ether. Many Bitcoin exchanges offer this trading pair:

{% for exchange in site.data.buy_ether %}
{% if exchange.tags == 'btc' %}
{% include buy-list.html %}
{% endif %}
{% endfor %} 

## Completing your Purchase

Once your purchase has been made, [send your ether to a wallet you control](/ethereum-wallets/):

* **Ethereum Wallet** - Desktop Ethereum wallet for Mac, Windows, and Linux. 

* **MyEtherWallet** - Open source Javascript client-side Ether wallet. 

* **EthAddress** - open source Javascript client-side paper wallet generator. 

* **EthereumWallet** - EthereumWallet uses client side Javascript to quickly create Ethereum addresses in web browsers. Still in beta. 
 

## Buy Ether with PayPal

Although not recommended, it’s possible to buy ether with PayPal. First you must buy SLL on [VirWox](https://www.virwox.com?r=fbbb7), then trade SLL for bitcoin. Once you have BTC you can use any of the methods above to trade bitcoin for ether. 

## Buy Ether with Credit Card or Debit Card

There is still no easy way to buy Ether directly with a credit card. The best way is to use an exchange like [Circle](https://www.circle.com/en) (US) or [CoinCorner](https://www.coincorner.com/) (UK & Europe) to buy bitcoins which you can trade for ether. 
