---
layout: post
title: Bitcoin Volatility As An Asset Class
author: Arthur Hayes
authorurl: /arthur-hayes/
published: true
---
Volatility is the measurement of a financial instrument’s price variation over time. Volatility as an asset class refers to isolating this variable and trading it as a standalone product. Usually volatility is isolated by the trading of delta hedged call and put options. Currently Bitcoin does not have a liquid options market so this method of isolation does not exist. However this does not preclude the existence of tradable Bitcoin volatility.

<center><img alt="Bitcoin volatility" src="/images/historic-bitcoin-volatility.png"></center>
 
BitMEX is leading the market in innovations around the trading of volatility absent an options market. The BitMEX 30 Day Historical Volatility Index futures contract (BVOL) and the XBT vs. XBU pseudo volatility allow investors to trade Bitcoin volatility on BitMEX.
 
### Why Trade Volatility?

Trading volatility allows investors to profit from the price movements or lack thereof. They need not predict the direction of the Bitcoin price. Event driven traders can profit from price gyrations after major news or market events which increase volatility. Conversely investors anticipating periods of relative inactively can sell volatility and profit from a quiet or sideways market. The addition of Bitcoin volatility adds another weapon to savvy investors’ alpha arsenal.

### BitMEX 30 Day Historical Volatility Index Futures (BVOL)
 
On 5 January 2015, BitMEX launched the world’s first historical volatility index future with the ticker BVOL. The futures contract allows investors to bet on where 30 day volatility will realise. The BitMEX 30 Day Historical Volatility Index tracks the rolling 30 day realised volatility by using daily 10:00 GMT to 12:00 GMT 1 minute Time Weighted Average Prices on Bitfinex for Bitcoin / USD. The product is quoted in annualized volatility % points and investors make or lose 0.01 Bitcoin per 1% point move.

### Forward Starting Historical Volatility

The BVOL futures contracts expire on the previous 30 days realised volatility. However, the contracts are tradable before the 30 day observation period starts. This allows investors to trade their expectation of where future historical volatility will realise. If it is 1 January 2015 and an investor is trading the BVOLG15 contract (27 February 2015 expiry), the observation period does not begin until 29 January 2015 (30 days prior to expiry). The price of BVOLG15 reflects the market’s view on where historical volatility will be in the future.

This has interesting implications for the pricing of other Bitcoin derivatives. Bitcoin by some is viewed as a long dated call option. The most crucial component to valuing an option is the volatility of the underlying asset. On a longer term view, higher the forward expectations of Bitcoin volatility lead to more valuable call options and possibly Bitcoin itself.
 

If there are major market events that will occur at specific dates in the future, the forward expectations of volatility gauge how impactful the market believes these events to be. An investor’s view of the over or under appreciation of the magnitude of the event leads to trading opportunities through the volatility component.

As liquidity and interest grows in the BVOL futures contracts, we will list longer dated maturities. Once complete, investors will have a term structure for expected future Bitcoin historic volatility. This is very useful for options traders pricing longer dated maturities. Using BVOL futures contracts as guide posts, options traders will be able to make markets in over the counter (OTC) options at tighter spreads and larger size.

Once the observation period has begun for a particular BVOL futures contract interesting arbitrage opportunities present themselves. Every day that passes there is more information about where the 30 day historical volatility will realise for a particular contract. BVOL prices too high or too low can be sold or bought vs. a knowledge of the magnitude of impact future prices can mathematically have on realised volatility.

### XBT vs. XBU Pseudo Volatility

BitMEX offers two types of futures contracts, the XBT and XBU chain. The XBT chain is quoted in USD but has a XBT multiplier, a quanto style future. Therefore, buyers of XBT chain contracts have unlimited upside, but can only lose 100%. The XBU chain is worth $100 of Bitcoin at all times and is quoted in USD, an inverse style future. Therefore, sellers of XBU chain contracts have unlimited profit potential on the downside, but can only lose 100% if the price moves higher. The XBT chain is an X function, the XBU chain is a 1/X function. All else being equal, for a given maturity the XBT chain should trade at a greater price than the XBU chain. In USD terms multply each function again by X (Bitcoin / USD exchange rate), what is left is XBT – XBU = X * (X – 1/X) = X2 – 1.

Prices observed for the XBTH15 and XBUH15 contract confirm this theory. XBTH15 has been trading at a $25-$40 premium to XBUH15 on BitMEX. Because both contracts have the same maturity, this difference represents a pseudo strangle. A strangle is an options strategy where one buys a put and a call with the put having a lower strike price than the call, and both options having the same maturity. This is a volatility play; buyers of the strangle hope that realised is greater than implied volatility.

Traders who believe the realised volatility will be less than the pseudo implied volatility should sell XBT and buy XBU; those who believe the opposite should buy XBT and sell XBU. For sellers of pseudo volatility, if spot trades outside the profitable range, losses will accumulate in a non-linear fashion.

In the absence of traditional options straddles and strangles, pseudo volatility is a way for traders to express their views on implied volatility for a particular maturity.

### Combining BVOL and XBT vs. XBU Pseudo Volatility

The difference between same maturity pseudo implied volatility and realised volatility through BVOL presents trading opportunities. If pseudo implied volatility is much higher than BVOL expected realised volatility, sell pseudo implied volatility (sell XBT, buy XBU) and buy BVOL. If pseudo implied volatility is lower than BVOL expected realised volatility, buy pseudo implied volatility (buy XBT, sell XBU) and sell BVOL.

The addition of volatility products on BitMEX has added three new trading strategies for investors. All of which do not call for the prediction of the direction of the Bitcoin / USD exchange rate.