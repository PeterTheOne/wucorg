---
title: Electrum
seotitle: Electrum Review - Desktop Bitcoin Wallet
img: /images/company/electrum.png
---
Electrum is a desktop Bitcoin wallet for Windows, Mac, and Linux. German computer scientist Thomas Voegtlin created the wallet in 2011. Voegtlin estimates that about 10% of all Bitcoin transactions are sent using Electrum. 

<img src="/images/electrum-wallet.png" alt="electrum-wallet"/>

Electrum is a lightweight wallet. It connects to external servers run by other Electrum users to query blockchain data. While this setup eliminates long sync times, it is less private than full wallet clients like [Bitcoin Core](/bitcoin-core/) or [Armory](/armory/). 

## Features

Electrum is lightweight and syncs fast, but is a feature packed Bitcoin wallet. 

### Cold Storage

Like Armory, Electrum can be used to create secure offline cold storage. An offline computer is used to generate the master public and private keys. The master public key is then scanned into an online computer. The online computer is used to receive payments, while the offline computer securely signs transactions. 

### Integration with Hardware Wallets

Electrum has integration with all major hardware wallets: [Ledger Nano](/bitcoin-ledger-wallet-review/) and HW.1, [Trezor](/trezor-review-bitcoin-hardware-wallet/), and KeepKey. All Electrum features are available when used with any of the hardware wallets listed above. 

### Coin Control - Send From & Freeze 

One of Electrum's unique features is its _send from_ ability. An HD Bitcoin wallet contains many different inputs. When it comes time to spend, it is silly to spend a 1 BTC input if only 0.01 BTC must be spent. The Electrum _send from_ ability allows wallet owners to select which input(s) are used in transactions. 

Selected inputs can also be frozen, and won't be included automatically in any outgoing transactions. 

### Tor Support

Electrum is one of the few Bitcoin wallets to support Tor. While not a complete privacy solution, using Tor with Electrum allows you to block your IP address from external servers. 

### More Features

Electrum supports multisignature wallets and two-factor authentication. The wallet is open source and its source code is available on [GitHub](https://github.com/spesmilo/electrum).  

## Tails Integration

Linux operating system Tails aims to provide its users privacy by automatically routing all internet traffic through Tor. In February 2015, it added Electrum--one of the few Bitcoin wallets with Tor integration--as a pre-installed application. Tails sees Bitcoin as an important part of privacy online and wanted to include a Bitcoin wallet in its software. Because Tails USB drives must be under 4 GB, a lightweight wallet like Electrum was required. 

## Electrum Android Wallet

Electrum launched its [Android wallet](https://play.google.com/store/apps/details?id=org.electrum.electrum&hl=en) in March 2016. The Android version of Electrum offers many of the same features as the desktop version: offline transaction signing using a separate phone, and the same server based verification. Electrum developer Thomas Voegtlin also [claims](https://bitcoinmagazine.com/articles/electrum-launches-mobile-wallet-for-android-ios-coming-1457104408) that users will be able to buy and sell bitcoins from within the Android sometime in 2016. 
