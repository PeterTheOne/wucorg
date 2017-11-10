---
title: What Is Lisk?
description: What Is Lisk?
name: Lisk
author: WeUseCoins
authorurl: /
published: true
permalink: /what-is-lisk/
toc: 
  what: What Is Lisk?
  getting: Getting Started With Lisk
  howto: How To Get A Lisk Wallet?
  resources: Lisk Resources 
  buy: How To Buy Lisk?
  earn: How To Earn Lisk?
  spend: Where To Spend Lisk?
  mining: What Is Lisk Mining?
  latest: Latest Lisk News
img: lisk.png
category: appcoin
summary: Lisk aims to make Blockchain technology more accessible with an SDK written in JavaScript, special focus on user experience, developer support and in-depth documentation.
---

<h2 id="what">What Is Lisk?</h2>

<p><center><script type="text/javascript" src="https://files.coinmarketcap.com/static/widget/currency.js"></script><div class="coinmarketcap-currency-widget" data-currency="lisk" data-base="USD" data-secondary="BTC" data-ticker="true" data-rank="true" data-marketcap="true" data-volume="true" data-stats="USD" data-statsticker="false"></div></center></p>

<p>Lisk is a <a href="/blockchain-explained-for-normal-people/">Blockchain application platform</a>, established in early 2016. Based on its own <a href="/video-backup-your-pivx-blockchain-files/">Blockchain network</a> and token LSK, Lisk will enable developers to create, distribute and manage decentralized <a href="/video-blockchain-smarttickets-for-the-event-industry/">Blockchain applications</a> by deploying their own sidechain linked to the Lisk network, including a custom token. Thanks to the flexibility of sidechains, developers can implement and customize their Blockchain applications entirely.</p>

<h4>How Lisk Helps?</h4>

<p>In early 2016, after several years participating within the Blockchain industry, Max Kordek and Oliver Beddows saw a lack of developer adoption. With the vision to make Blockchain technology more accessible, they imagined a Blockchain framework which accelerates and simplifies development.</p>

{% include page-toc.html %}

<h4>How Lisk Different From Other Platform?</h4>

<p>Lisk is more than just developer tools. It’s an opportunity to become part of the biggest technological innovation since the Internet. Lisk aims to make Blockchain technology more accessible with an SDK written in JavaScript, special focus on user experience, developer support and in-depth documentation.</p>

<p>The Lisk Foundation set itself the goal to inspire and educate entrepreneurs and developers alike. The ultimate goal is to bring talent into the Blockchain industry by enabling developers to build the decentralized future with our SDK. Hereby, we will provide an easy entry to take people from the idea to the product.</p>

<p>Most alternative solutions are either single Blockchain based or are tailored for private Blockchains. Lisk strives to offer the best of both worlds. The Lisk mainchain offers stability and security while sidechains are utilized to have unlimited flexibility. </p>

<p>This way, Lisk offers developers an environment where they have full control to create their own Blockchain network as a sidechain but don’t have to confront the complexity of creating a Blockchain network from scratch.</p>

<h2 id="getting">Getting Started With Lisk</h2>

<iframe width="700" height="394" src="https://www.youtube.com/embed/HUQQoyv9NpQ" frameborder="0" allowfullscreen></iframe>

<h4>Application Development</h4>

<p>Decentralized applications or Blockchain applications are exactly what the name suggests. Applications of any sort running on many servers, providing unseen security, uptime and entirely new business models. A powerful component of the Lisk application platform is the ability to deploy, distribute and manage decentralized applications all in one place with a seamless user experience.</p>

<p>Decentralized applications include the whole package of front-end (what the user sees) and back-end (the logic behind it). A <a href="/video-ethereum-and-smart-contracts/">smart contract</a> on the other hand, consists only of the back-end, and often only a small part of it. This means that if you want to create a <a href="/video-decentralizing-the-internet-maidsafe/">decentralized application</a> on a smart contract system (i.e. not with Lisk), you have to combine several smart contracts and rely on 3rd party systems for the front-end.</p>

<p>Possible use cases include applications that offer proof-of-ownership, improved online identity verification or asset management.</p>

<p>Lisk strives to make Blockchain technology accessible for everybody. A seamless user experience on the Lisk platform and understandable documentation should make it possible for anyone to send LSK, download applications and educate themselves without being a technical genius.</p>

<p>In order to build your own application it requires a developer to code it in JavaScript. By offering an SDK written in JavaScript, Lisk enables millions of developers around the world an accessible way to create their own decentralized applications by deploying their own Blockchain sidechain next to the Lisk network.</p>

<h2 id="howto">How To Get A Lisk Wallet?</h2>

<h4>Lisk Nano</h4>

<center><img src="/images/lisk-nano.png" alt="lisk nano"></center>

<p>Lisk Nano enables the user to send and receive transactions on the Lisk network and provides a simple user interface for more advanced features like delegate voting or registering a second passphrase. With Lisk Nano, there is no need for blockchain synchronisation as it connects to official Lisk nodes hosted by the Lisk Foundation. For the use of API calls and other advanced features please use Lisk Core.</p>

<h4>Lisk Core</h4>

<center><img src="/images/lisk-core.png" alt="lisk core"></center>

<h4>Binary - Prerequisites</h4>

<p>This details how to prepare a Linux operating system for the installation of Lisk Node. It will guide you through installation of important dependencies and user creation.</p>

<p>Determine if your platform can run Lisk Node</p>

<p><b>Supported Architectures</b></p>
<ul>
<li>Linux (x86_64, i686)</li>
<li>Darwin (x86_64)</li>
</ul>

<p>To complete the installation there are prerequisites that need to be completed. If you have already performed these, please proceed to the installation document for your desired network. Follow these instructions to load required software to your system.</p>

<h4>Linux Installation Pre-Requisites</h4>

<p>Ensure you are logged in as root.</p>

<p><code>whoami</code></p>

<p>Install curl, wget, tar, sudo, unzip, zip</p>

<p><code>if [[ -f "/etc/redhat-release" ]]; then</code></p>
<p><code>  yum update</code></p>
<p><code>  yum install curl wget tar sudo unzip zip</code></p>
<p><code>elif [[ -f "/etc/debian_version" ]]; then</code></p>
<p><code>  apt-get update</code></p>
<p><code>  apt-get install curl wget tar sudo unzip zip</code></p>
<p><code>fi</code></p>

<p>Create a user to run lisk, create sudo group and give the lisk user sudo permissions</p>

<p><code>useradd -d /home/lisk -m lisk</code></p>
<p><code>groupadd sudo</code></p>
<p><code>usermod -a -G sudo lisk</code></p>

<p>Set a password for the lisk user</p>

<p><code>passwd lisk</code></p>

<p>Setup the sudoers file</p>

<p><code>visudo</code></p>

<p>After you've opened the file, paste the following line at the bottom of the file:</p>

<p><code>%sudo   ALL=(ALL:ALL) ALL</code></p>

<p>On Ubuntu: Click Ctrl+ X then: Y to exit the document and save it.</p>

<p>On RHEL: type :wq!</p>

<p>Update the systems Locale</p>

<p><code>if [[ -f "/etc/redhat-release" ]]; then</code></p>
<p><code>  localedef -v -c -i en_US -f UTF-8 en_US.UTF-8</code></p>
<p><code>  localectl set-locale LANG=en_US.UTF-8</code></p>
<p><code>elif [[ -f "/etc/debian_version" ]]; then</code></p>
<p><code>  locale-gen en_US.UTF-8</code></p>
<p><code>  update-locale LANG=en_US.UTF-8</code></p>
<p><code>fi</code></p>

<p>Set the systems operating language to en_US.UTF-8</p>

<p>Reboot your system to apply changes</p>

<p><code>reboot</code></p>

<h4>Docker - Prerequisites</h4>

<p>This describes how to install Lisk Node as a Docker based container. It will guide users to downloading and installing Docker Toolbox or login to a Docker VM through an SSH client.</p>

<p><b>Supported Platforms</b></p>
<ul>
<li>Windows 10</li>
<li>macOS</li>
<li>Ubuntu</li>
<li>Debian</li>
<li>CentOS</li>
<li>Fedora</li>
</ul>

<p><b>Not Supported</b></p>
<ul>
<li>Red Hat Enterprise Linux</li>
<li>Oracle Linux</li>
<li>SUSE Linux Enterprise Server</li>
<li>Microsoft Windows Server 2016</li>
</ul>

<p>Docker is supported on most operating systems. Follow the section below that applies to your operating system to setup Docker.</p>

<p>Windows / Mac OS X</p>

<p>Download and install Docker Toolbox for your operating system.</p>

<p>Open the Docker Quickstart Terminal.</p>

<p>PuTTY / SSH Access</p>

<p>You can optionally login to your Docker virtual machine, using PuTTY or any other SSH client.</p>

<p>To do so, please use the following credentials:</p>

<p><code>Host: 192.168.99.100</code></p>
<p><code>Port: 22</code></p>
<p><code>Login: docker</code></p>
<p><code>Password: tcuser</code></p>

<p>Ubuntu / Debian / CentOS / Fedora</p>

<p>Log onto your Ubuntu based server and enter the following commands:</p>

{% include page-toc.html %}

<p>NOTE: The following information is applicable to: Ubuntu 14.04, 16.04 (LTS) or 16.10 - x86_64.</p>

<p><code>curl -sL https://downloads.lisk.io/scripts/setup_docker.Linux | sudo -E bash -</code></p>
<p><code>sudo apt-get install -y docker-engine</code></p>

<p><b>Post Install</b></p>

<p>Proceed to the Installation Landing Page order to install Lisk using the newly prepared Docker system.</p>

<h4>Source - Prerequisites</h4>

<p>Determine if your platform can install Lisk Core from source</p>

<p><b>Supported Platforms</b></p>
<ul>
<li>Ubuntu 14.04 x86_64</li>
<li>Ubuntu 16.04 (LTS) x86_64</li>
</ul>

<p><b>Prerequisite Program Installations</b></p>

<p>Tool chain components -- Used for compiling dependencies</p>

<p><code>sudo apt-get install -y python build-essential curl automake autoconf libtool</code></p>

<p>Git -- Used for cloning and updating Lisk</p>

<p><code>sudo apt-get install -y git</code></p>

<p>Node.js -- Node.js serves as the underlying engine for code execution.</p>

<p>System wide via package manager</p>

<p><code>curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -</code></p>
<p><code>sudo apt-get install -y nodejs</code></p>

<p>Locally using nvm</p>

<p><code>curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash</code></p>
<p><code>source ~/.bashrc</code></p>
<p><code>nvm install v6.10.1</code></p>

<p>Install PostgreSQL (version 9.6.2)</p>

<p><code>curl -sL "https://downloads.lisk.io/scripts/setup_postgresql.Linux" | bash -</code></p>
<p><code>sudo -u postgres createuser --createdb $USER</code></p>
<p><code>sudo -u postgres createdb lisk_test</code></p>
<p><code>sudo -u postgres createdb lisk_main</code></p>
<p><code>sudo -u postgres psql -d lisk_test -c "alter user "$USER" with password 'password';"</code></p>
<p><code>sudo -u postgres psql -d lisk_main -c "alter user "$USER" with password 'password';"</code></p>

<p>Bower -- Bower helps to install required JavaScript dependencies.</p>

<p><code>npm install -g bower</code></p>

<p>Grunt.js -- Grunt is used to compile the frontend code and serves other functions.</p>

<p><code>npm install -g grunt-cli</code></p>

<p>PM2 -- PM2 manages the node process for Lisk (Optional)</p>

<p><code>npm install -g pm2</code></p>

<h4>Binary - Main Network</h4>

<p>This section describes how to install the Lisk Node using pre-built binary packages. When completed, you will have a functioning installation on the Lisk Main Network.</p>

<p>If you are looking to upgrade your current Lisk Node installation, please see the section Upgrading Binary - Main Network.</p>

<p>Login to the Lisk user</p>

<p>The user was created in the Binary - Prerequisites Section. If you are already logged in to this user, please skip this step.</p>

<p><code>su - lisk</code></p>

<p>Execute the installation script</p>

<p>This will configure the environment, download and install the Lisk client.</p>

<p><code>wget https://downloads.lisk.io/lisk/main/installLisk.sh</code></p>
<p><code>bash installLisk.sh install -r main</code></p>

<p>You will be prompted for your installation directory, pressing enter will choose the default.</p>

<p>Accessing Lisk</p>

<p>If you are running the node locally, you can access the Lisk web client by opening a browser and navigate to the following web address.</p>

<p><code>http://localhost:8000/</code></p>

<p>The Lisk web client should launch successfully.</p>

<p>If you are not running Lisk locally, you will need to follow the Configuration - API document to enable access for yourself.</p>

<p>With all of the above steps complete you are ready to move on to the configuration documentation if you wish to enable forging or SSL. Please see Lisk Client Configuration for more information.</p>

<h4>Docker - Main Network</h4>

<p>Install Lisk through Docker</p>

<p>To install the latest version of Lisk as a docker container, please proceed with the following:</p>

<p>Install the docker image (executed only once per installation)</p>

<p><code>docker run -d --restart=always -p 0.0.0.0:8000:8000 lisk/mainnet</code></p>

<p>NOTE: On Windows or Mac OS X, these commands are issued from within the Docker Quickstart Terminal.
Upon successful completion, you will have a running Lisk node with an up-to-date snapshot of the blockchain. The container is configured to automatically restart upon reboot of the server or any occurrence of an error.</p>

<p>To access the Lisk web client, open: http://localhost:8000/</p>

<p>The Lisk web client should launch successfully.</p>

<h4>Source - Main Network</h4>

<p>Installing Lisk from Source (GitHub)</p>

<p>Clone the Lisk repository using Git and initialize the modules</p>

<p><code>git clone https://github.com/LiskHQ/lisk.git</code></p>

<p><code>cd lisk</code></p>
<p><code>git checkout master</code></p>
<p><code>npm install</code></p>

<p>Install Lisk Node, a specialized version of Node.js used to execute blockchain applications within a virtual machine</p>

<p><code>wget https://downloads.lisk.io/lisk-node/lisk-node-Linux-x86_64.tar.gz</code></p>
<p><code>tar -zxvf lisk-node-Linux-x86_64.tar.gz</code></p>
<p><code>rm -f lisk-node-Linux-x86_64.tar.gz</code></p>

<p>NOTE: Lisk Node has to be in [LISK_DIR]/nodejs/node.</p>
<p>Load required git submodules (lisk-ui and lisk-js)</p>

<p><code>git submodule init</code></p>
<p><code>git submodule update</code></p>
<p><code>Build the Lisk user-interface</code></p>

<p><code>cd public</code></p>
<p><code>npm install</code></p>
<p><code>bower install</code></p>
<p><code>grunt release</code></p>

<p>Initiating Lisk Node Installation</p>

<p>Using PM2 you can start Lisk and allow it to be monitored with the following command:</p>

<p><code>pm2 start --name lisk app.js</code></p>

<p>After the process is started, its runtime status and log location can be retrieved by issuing the following command:</p>

<p><code>pm2 show lisk</code></p>

<p>To stop Lisk after it has been started with pm2, issue the following command:</p>

<p><code>pm2 stop lisk</code></p>

<p>Lisk Core enables delegate forging, provides blockchain synchronisation, and includes the complete API for developers. Please note, installing Lisk Core is for advanced technical users looking to build on top of the Lisk Platform, securing the network infrastructure or attain delegate forging access.</p>

{% include page-toc.html %}

<h4>Lisk Tools</h4>

<ul>

<li><b>Lisk-JS</b> - Lisk JS is a JavaScript library for Lisk - the cryptocurrency and blockchain application platform. It allows developers to create offline transactions and broadcast them onto the network. It also allows developers to interact with the core Lisk API, for retrieval of collections and single records of data located on the Lisk blockchain. 

Its main benefit is that it does not require a locally installed Lisk node, and instead utilizes the existing peers on the network. It can be used from the client as a browserify compiled module, or on the server as a standard Node.js module.</li>

<li><b>Lisky</b> - Lisky allows you to communicate with a remote or local node and carry out Lisk-related functionality using an interactive or non-interactive command line tool.</li>

</ul>

<h2 id="resources">Lisk Resources</h2>
<ul>
<li><a href="https://lisk.io/">Website</a></li>
<li><a href="https://github.com/LiskHQ/lisk">LiskHQ/lisk</a></li>
<li><a href="https://reddit.com/r/lisk">Reddit</a></li>
<li><a href="https://blog.lisk.io/">Blog</a></li>
<li><a href="https://github.com/LiskHQ/lisk-nano">LiskHQ/lisk-nano</a></li>
<li><a href="https://twitter.com/LiskHQ">Twitter</a></li>
<li><a href="https://github.com/LiskHQ">GitHub</a></li>
<li><a href="https://github.com/LiskHQ/lisk-js">LiskHQ/lisk-js</a></li>
<li><a href="https://www.facebook.com/LiskHQ/">Facebook</a></li>
<li><a href="https://github.com/LiskHQ/lisk-explorer">Lisk.Chat</a></li>
<li><a href="https://github.com/LiskHQ/lisk-explorer">LiskHQ/lisk-explorer</a></li>
<li><a href="https://bitcointalk.org/index.php?topic=1346646.0">Bitcointalk</a></li>
<li><a href="https://gitter.im/LiskHQ/lisk">Gitter Chat</a></li>
<li><a href="https://github.com/LiskHQ/lisk-build">LiskHQ/lisk-build</a></li>
<li><a href="https://lisk.io/#newsletter">Newsletter</a></li>
</ul>

<h2 id="buy">How To Buy Lisk?</h2>

<p>LSK tokens can be bought and sold on several major exchanges including Bittrex, Poloniex, YoBit and Jubi. There, LSK tokens can be exchanged for other cryptocurrencies including Bitcoin. </p>

<p>Except for the Chinese Yuan and Japanese Yen, it is currently not possible to buy LSK tokens directly with other FIAT currencies. Our goal is to make this possible in the future.</p>

<p>Exchanges have their own safety measurements before <a href="/confidential-transactions/">accepting incoming transactions</a> or confirming outgoing transactions. Like stated on the previous question, the Lisk Blockchain takes ten seconds for a transaction to go through. However, we have no control over how many confirmations exchanges require.</p>

<p>It is impossible to send tokens other than LSK to your Lisk address. We can’t recover those tokens since it is another Blockchain and therefore out of our control.</p>

<p>We recommend that everybody stores their LSK tokens in our Lisk Nano wallet.</p>

<p>In the event of sending LSK to an incorrect address you will lose access to your funds. There is nothing we can do from our side to help retrieve your tokens.</p>

<h2 id="earn">How To Earn Lisk?</h2>

<p>Lisk is a cryptocurrency that offers a next generation platform that allows for the development and distribution of JavaScript based blockchain applications. Lisk provides an easy to use interface and access full featured ecosystem.</p>
 
<p>Through Lisk, developers can build, publish, distribute, and monetize their applications within a cryptocurrency powered system that allows for the use of <a href="/video-blockchain-smarttickets-for-the-event-industry/">customized blockchains</a>, smart contracts, cloud storage, and computing nodes.</p>

<h2 id="spend">Where To Spend Lisk?</h2>

<p>All cryptocurrencies utilize tokens to create a secure system of utilization. As a result, Lisk offers a cryptocurrency token called LSK. This token is used to pay various fees in order generate transactions and to use the system. </p>

<p>LSK tokens can be acquired through various means, such as purchasing them from an exchange or from another individual using Fiat or Bitcoin (BTC).</p>

<h2 id="mining">What Is Lisk Mining?</h2>

<h4>Technical Background</h4>

<p>Lisk as a software has three major components, the JavaScript code, NodeJS as a compute engine and PostgreSQL as a storage and database solution.</p>

<p><b>JavaScript</b></p>

<p>JavaScript is undeniably the language of the internet. Nearly every website on the Internet uses some form of JavaScript to provide rich functionality for end users. Lisk is written in JavaScript for these same reasons and because the language is very accessible to any developer. </p>

<p>With nearly any browser a user can write and test JavaScript code, and with Lisk's aim to be the premiere blockchain application platform it makes sense to use a language that runs on every desktop machine.</p>

<p><b>NodeJS</b></p>

<p>Lisk utilizes NodeJS as the backend computing engine for JavaScript code. NodeJS itself is extremely flexible and can be deployed to all desktop architectures and many <a href="/video-architecture-for-iot/">IoT (Internet Of Things)</a> devices. This flexibility gives Lisk the ability to run on any device that has the hardware to support the client.</p>

<p><b>PostgreSQL</b></p>

<p>All blockchains preserve data in different ways, some choose to use SQLite while others use LevelDB. These solutions work fine for pure blockchain solutions but don't provide the robust features of PostgreSQL.</p>

<p>PostgreSQL is one of the oldest open source relational database systems. With Postgres, a user can store information of any type, such as binary files or even music files. This makes PostgreSQL a perfect fit for the Lisk system and provides the necessary database engine to support blockchain applications. In addition to these features, the backup functionality and fault tolerance Postgres offers is unmatched in the open source space.</p>

<h4>Security</h4>

<p>Lisk uses cryptographic hashing in order to secure all aspects of the system. The system uses EdDSA as it provides a much faster mechanism for hashing and providing security [see http://cr.yp.to/highspeed/coolnacl-20120725.pdf]; rather than ECDSA which is found in many other cryptocurrencies, such as Bitcoin.</p>

<p><b>Key pair</b></p>

<p>A keypair is consists of a private key and a public key. A private key is a piece of information known only to the owner of the key. The public key is derived from the private key and can be used to validate that the private key belongs to the owner, but not provide access to the owners private key. Elliptic curve cryptography is used to generate cryptographically secure key pairs.</p>

<p>The process used to generate the key pair operates under the following assumptions:</p>

<p>When a user creates an account, a BIP39 [2] mnemonics (the passphrase) is generated for the user. This passphrase is hashed using the SHA-256 hash function into a 256 bits string. This hash is subsequently used as a seed in ed25519 [3] to generate the private key ks and derives its public key kp.</p>

<p><b>key-pair-generation</b></p>

<p>With this <a href="/amazing-math-bitcoin-private-keys/">private key</a>, the user is able to sign transactions into a transaction object and broadcast that object to the network. The public key is included as part of the transaction and the nodes that receive the transaction are able to verify the validity of the signature using kp. This provides effective security for both the user and the network since ks is known only to the user and kp can validate that the signature is valid.</p>

<p><b>Second pass phrase</b></p>

<p>Lisk offers an additional <a href="/bitcoin-security-standards/">layer of security</a> for the user. Using a specific class of transaction, the user can register a second pass phrase that is associated with the kp. This relationship requires that all subsequent transactions to be signed using the second pass phrase in order to be considered valid. The process of generating the second key pair is the same as the one for the main key pair.</p>

<p><b>Multisignature</b></p>

<p>Lisk supports <a href="/how-to-use-multisig-armory-lockbox-with-coinkite/">multisignature accounts</a> as another security system for users requiring even greater security. A multisignature account is an account that requires multiple signers to submit signature transactions. Any user may enable multisignature on their account by issuing a special transaction (See <a href="/video-bitcoin-multisig-p2sh-transactions/">Multisignature Registration Transaction</a>) specifying a group of ksn and the require minimum amount of signatures required to confirm a transaction as valid. </p>

{% include page-toc.html %}

<p>It is then mandated in the blockchain that any transactions originating from this account must be signed by a minimum quorum of associated accounts before any transaction from the account may be processed.</p>

<p><b>Address</b></p>

<p>An address or the <a href="/introduction-bitcoin-paper-wallets-cold-storage/">wallet ID</a> is derived from the public key. The <a href="/video-generating-public-key-python/">public key</a> is hashed using SHA-256 then the first 8 bytes of the hash are reversed. The account ID is the numerical representation of those 8 bytes, with the ’L’ character appended at the end. The following figure is the representation of an address and its associated account details.</p>

JSON

<p><code>{</code></p>
<p><code>    "address": "16009998050678037905L",</code></p>
<p><code>    "unconfirmedBalance": "0",</code></p>
<p><code>    "balance": "0",</code></p>
<p><code>    "publicKey": "73ec4adbd8f99f0d46794aeda3c3d86b245bd9d27be2b282cdd38ad21988556b",</code></p>
<p><code>    "unconfirmedSignature": 0,</code></p>
<p><code>    "secondSignature": 0,</code></p>
<p><code>    "secondPublicKey": null,</code></p>
<p><code>    "multisignatures": [],</code></p>
<p><code>    "u_multisignatures": []</code></p>
<p><code>  }</code></p>

<h4>Blocks</h4>

<p>A blockchain is <a href="/video-qa-scaling-and-the-block-size-debate/">composed of blocks</a>, and a block is composed of a header and a list of confirmed transactions. When a delegate is assigned a slot and has a node running, that delegate generates the next block and confirms up to 25 transactions from the transaction pool. These confirmed transactions will be added the payload of the block and subsequently signed into that block.</p>

<p><b>Block Header</b></p>

<p>The block header contains all the information about the block. The following fields compose the block header:</p>

<p>A 32 bit integer identifying the version of the block</p>
<p>A 32 bit epoch timestamp of when the block was created</p>

<p>The 64 bit Id of the previous block</p>

<p>A 32 bit integer corresponding to the number of transactions processed in the block</p>
<p>A 64 bit integer corresponding to the total amount of Lisk transferred</p>
<p>A 64 bit integer corresponding to the total amount of fees associated with the block</p>
<p>A 64 bit integer corresponding to the Lisk reward for the delegate</p>
<p>A 32 bit integer corresponding to the length the payload</p>

<p>The 256 bit hash of the payload</p>
<p>The 256 bit public key of the delegate who generated the block</p>
<p>The following figure is the representation of the complete structure of a block header:</p>

<p><b>Block-Header</b></p>

<p>JSON Representation:</p>

JSON
<code>
     {
      "id": "15787022670460703397",
      "version": 0,
      "timestamp": 23039010,
      "height": 1574052,
      "previousBlock": "4576781903037947065",
      "numberOfTransactions": 0,
      "totalAmount": 0,
      "totalFee": 0,
      "reward": 500000000,
      "payloadLength": 0,
      "payloadHash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "generatorPublicKey": "c0ab189f5a4746725415b17f8092edd3c266d1e758e840f02a3c99547b3a527f",
      "blockSignature": "c6b2bcc960066be078efbfffed625f61553a7bc18ebde3892636c2f36850de234a9c70ba3e33b606db2eff724398026984e4d391c1fbbe70c94dd9d07ff0060b",
      "totalForged": "500000000"
    }
</code>

<p>The process for signing the block header is the same as the process for signing a transaction. A SHA-256 hash of the block header is generated, and signed using the key secret of the delegate. Once the block header has been signed, the system generates the blockId following the same logic as transactions. </p>

<p>The completed <a href="/8-problems-with-bitcoin-to-solve-before-block-size/">block header</a> is hashed using SHA-256 and the first 8 bytes of the hash are reversed and used as the blockId. A signed block generates its blockId using the following flow:</p>

<p><b>Signed-Block</b></p>

<p><b>Block Payload</b></p>

<p>The payload of the block is comprised of up to 25 unconfirmed transactions present on the system signing the block. The maximum number of available transactions up to this limit will be included, provided that the payload for a transaction doesn’t exceed the max size for each transaction type. These max sizes are listed below:</p>

<center><img src="/images/lisk-block-payload.jpg" alt="lisk block payload"></center>

<p>The max size of a block payload can then be determined as 58150 bytes with if every transaction is type 3 and contains the maximum number of assets. A data block is composed using the gathered unconfirmed transactions’ data <a href="/bitcoin-multi-signature-fragmented-backups/">blocks and signatures</a>. The system then hashes the combined transactional data blocks to generate the block payload.</p>

<p>Block Generation</p>

<p>Block Generation occurs every 10 seconds within the Lisk network using DPoS consensus, as described in Consensus. A delegate is an account that has been given the right to generate blocks by a process of election from other Lisk holders. </p>

<p>Block generation requires 51% of peers to maintain broadhash consensus which is described in Broadhash Consensus. Once broadhash consensus is established the node will generate a block using the techniques described in Blocks.</p>

<p>In Lisk, transactions are designated by type. These transaction types include:</p>

<center><img src="/images/lisk-block-transaction.jpg" alt="lisk block transaction type"></center>

<h4>Transaction Signing</h4>

<p>Every transaction, regardless of the type, must be signed by the sender prior to being accepted by the network. The process of signing the transaction is identical for every transaction. First, a data block representing the transaction must be generated. </p>

<p>Each data block contains a specific set of standardized information. Additional information contained in the data block will differ depending on the type of the transaction. The following fields must be present in all types of transactions:</p>

<p>A 8 bit integer identifying the type of the transaction</p>
<p>A 32 bit epoch timestamp of when the transaction has been created</p>
<p>The 256 bit public key of the issuer of the transaction</p>
<p>A 64 bit integer representing the amount of Lisk to be transferred</p>

<p>The other fields will be added to this schema depending on the transaction type. Once the data block has been generated, it is hashed using the <a href="/how-to-mine-bitcoins/">SHA-256 algorithm</a>, and this hash is signed using the key pair of the issuer. If the issuer has enabled a second pass phrase, the first signature is appended at the end of the data block, and the process is repeated, generating a second signature. </p>

<p>The same concept applies to multisignature accounts. The transactionId is generated from the data block. In order to compute the transactionId the system takes the data block with the completed signature information and hashes this block using SHA-256 and the first 8 bytes of the hash are reversed and which is then used as the transactionId. A signed transaction uses the following flow:</p>

<p><b>Signed-Transaction</b></p>

<p>With a second signature the flow looks like this:</p>

<p>signed-second-signature-transaction</p>

<p>Balance Transfer Transaction</p>

<p>A balance transfer transaction (type 0) is a transfer of Lisk from one account to another account. In order to issue a balance transfer transaction, the following fields must be specified:</p>

<p>The account Id of the recipient</p>
<p>The amount of LSK to transfer</p>
<p>The secret of the account</p>

<p>Once those three fields have been specified, the system will begin building the transaction object. First, the public key of the sender is computed using their secret. Following this, the data block is created using the process outlined in Transaction Signing and the additional field, recipientId, is added the to object. The resulting data block is 53 bytes.</p>

<p>This block is then signed using the method described in section 2.1. The final step of the transaction generation process is to compute the fee of the transaction. In the current system, the fee is fixed at 0.1 Lisk. Once all these steps have been completed and the transaction validated, the transaction may be broadcast on the network. </p>

<p>While the transaction may be present on the network, it will remain in unconfirmed status until it has been processed by a delegate. When the transaction is broadcast to the network and it is sent as a JSON object using the HTTP API. The following figure is a representation of a transaction object:</p>

<p><b>Balance-Transfer-Transaction</b></p>

<p>The following figure is a representation of the JSON.</p>

JSON
<code>
 {
    "type": 0,
    "amount": Amount,
    "senderPublicKey": Public key of the sender,
    "timestamp": Timestamp,
    "recipientId": Id of the recipient,
    "signature": Signature of the data block,
    "id": Id of the transaction,
    "fee": 10000000,
    "senderId": Id of the sender,
    ...
}
</code>

<p>The final size of a balance transfer transaction with no second pass phrase is 117 bytes, and 181 bytes with a second pass phrase.</p>

<p><b>Second Signature Registration Transaction</b></p>

<p>A second signature registration transaction (type 1) is used to register a second passphrase on the blockchain. In order to issue this type of transaction the following fields must be specified:</p>

<p>secret: The secret of the account.</p>
<p>secondSecret: The desired second pass phrase.</p>

<p>Once those two fields have been specified the system will begin building the transaction. The process outlined in section 5.1 is followed for this process. The second public key is generated from the second pass phrase, and the system builds the data block of 85 bytes.</p>

<p>This data block is then signed using the user’s secret ks, and the signature is appended to the object. Following this the computation of the <a href="/crypsa-future-of-bitcoin/">fee is performed</a> for the transaction type. In the existing implementation the fee for a signature transaction is fixed at 5 Lisk. The resulting object is represented by the following diagram:</p>

<p>Second-Signature-Registration</p>

<p>The JSON object that will be broadcast on the network is represented by the following diagram:</p>

JSON
 {
    "type": 1,
    "amount": 0,
    "senderPublicKey": Public key of the sender,
    "timestamp": Timestamp,
    "recipientId": null,
    "signature": Signature of the data block,
    "id": Id of the transaction,
    "fee": 500000000,
    "senderId": Id of the sender,
    "asset": {
        "signature": {
            "publicKey": The public key associated with the second passphrase
        }
    }
    ...
}

<p>The final size of the transaction, with the signature, is 149 bytes.</p>

<h4>Delegate Registration Transaction</h4>

<p>A delegate transaction (type 2) is used to register the account as a delegate. Refer to section 6.1 for more information about delegates. In order to issue a delegate registration transaction the following fields are required:</p>

<p>secret: The secret of the account.</p>
<p>username: The delegate’s username.</p>

<p>The length of the username must be at least one character and at most twenty characters. Once those fields have been specified, the system can then compute the account's public key, and begin building the transaction’s data block with a maximum 73 bytes.</p>

<p>This <a href="/use-bitcoin-anonymously/">data block</a> is then signed using the account's secret, and the signature is appended to the transaction object. The system then computes the fee of the transaction. In the present implementation, the fee for a signature transaction is fixed and costs 25 Lisk. The resulting object is represented by the following diagram:</p>

<p>Delegate-Registration</p>

<p>The JSON object that will be broadcast to the network is the follows the format below:</p>

JSON

 {
    "type": 2,
    "amount": 0,
    "senderPublicKey": Public key of the sender,
    "timestamp": Timestamp,
    "recipientId": null,
    "signature": Signature of the data block,
    "id": Id of the transaction,
    "fee": 10000000000,
    "senderId": Id of the sender,
    "asset": {
        "delegate": {
            "username": The chosen username
            "publicKey": The public key of the delegate (the sender)
        }
    }
    ...
}

<p>The final maximum size of the transaction, with the signature, is 137 bytes, and with a second signature, 201 bytes.</p>

<p><b>Vote Transaction</b></p>

<p>A vote transaction (type 3) is a transaction used to vote for delegates. In order to issue a vote transaction, the following two fields are required:</p>

<p>secret: The secret of the account.</p>
<p>delegates: An array of votes.</p>

{% include page-toc.html %}

<p>A vote is prepended with a ’+’ for adding stake to the delegate’s public key, and a ’-’ is prepended to the delegate’s public key if the account wants to remove the vote for the delegate. The maximum number of vote applications in one transaction is 33. Once those fields have been specified, the system can then compute the account's public key, and start building the transaction’s data block with a maximum 2198 bytes.</p>

<p>This data block is then signed using the account's secret, and the signature is appended to the transaction object. The system will then <a href="/video-bitcoinshop-mexbt-airbitz-chamber-of-digital-commerce/">compute the fee of the transaction</a>. In the current implementation, the fee for a vote transaction is fixed at 1 Lisk. The resulting object is represented by the following diagram:</p>

<p><b>Delegate-Vote-Transaction</b></p>

<p>The JSON object that will be broadcast to the network is the follows the format below:</p>

JSON
<code>
 {
    "type": 3,
    "amount": 0,
    "senderPublicKey": Public key of the sender,
    "timestamp": Timestamp,
    "recipientId": Id of the sender,
    "signature": Signature of the data block,
    "id": Id of the transaction,
    "fee": 100000000,
    "senderId": Id of the sender,
    "asset": {
        "votes": Array of votes
    }
    ...
}
</code>

<p>The final maximum size of the transaction, with the signature is 2262 bytes, and with the second signature is 2326 bytes.</p>

<h4>Multisignature Registration Transaction</h4>

<p>A multisignature registration transaction (type 4) is a transaction used to add a multisignature to an account. Refer to section 3.3 for more information about multisignatures. The following fields are needed in order to issue a multisignature registration transaction:</p>

<p>secret: The secret of the account the multisignature will be applied to.</p>
<p>keysgroup: The array of keys to add or remove from the multisignature account.</p>

<p>min: The minimum amount of signature required to validate a transaction. (Minimum of 2)</p>

<p>lifetime: The time to wait for enough signatures before removing the transaction.</p>

<p>Each public key in the keys group is prepended with a ’+’ then the public key to be added to the multisignature account. The minimum amount of signature required to validate a transaction must be at least 2 and at most 16. The minimum amount of keys in the keysgroup is two. The lifetime is specified in hours and a must be at least 1 hour and at most 24 hours. </p>

<p>Once those fields have been specified, the system will then compute the account's public key, and start building the transaction’s data block. The size of the data block depends on the amount of keys added to the multisignature registration transaction. Each key is 65 bytes due to the addition of the modifier.</p>

<p>This data block is then signed using the user’s secret, and the signature is appended to the transaction object. The system will then compute the fee of the transaction. In the present implementation the fee for a multisignature registration transaction is 5 Lisk per key in the keygsgroup. Note that the key of the account issuing the transaction is implicitly added in the multisignature. The resulting object is represented by the following diagram:</p>

<p>The JSON object that will be broadcast to the network is the follows the format below:</p>

JSON
<code>
 {
    "type": 4,
    "amount": 0,
    "senderPublicKey": Public key of the sender,
    "timestamp": Timestamp,
    "recipientId": null,
    "signature": Signature of the data block,
    "id": Id of the transaction,
    "fee": Transaction fee,
    "senderId": Id of the sender,
    "asset": {
        "multisignature": {
            "min": The minimum of signature required,
            "lifetime": The lifetime of the transaction,
            "keysgroup": Array of keys to add in the multisignature
        }
    }
    ...
}
</code>
<p>The final size of a transaction with two keys in the keys group is 249 bytes, and 313 bytes if the account has a second pass phrase enabled.</p>

<h4>Consensus</h4>

<p>Lisk uses Delegated Proof of Stake (DPoS) [4] as the consensus system. Delegates generate all of the blocks within the system and these delegates are chosen through a highly competitive election system driven by stakeholders. The number N (currently N = 101) of delegates are chosen to forge by all stakeholders. </p>

<p>Each stake holder may vote for up to 101 delegates, and the weight of the vote depends on the amount of Lisk the stake holder possess. A stake holder can vote for a delegate using a vote transaction (See Vote Transaction).</p>

<p>Consensus is a required aspect of any <a href="/video-qa-immutability-as-an-anchor-for-other-systems/">blockchain system</a>. It serves a vital purpose for the system where there are many nodes and all nodes must agree on the integrity of the data. All nodes participating must agree on what transactional data is legitimate in order to move the blockchain forward.</p>

<p><b>Delegates</b></p>

<p>A delegate is a type of account that has registered using a delegate registration transaction, mentioned in section 5.4. These accounts have a special purpose within Lisk as they are allowed to generate blocks for the system provided that the delegate has been allocated enough stake by other users of the system. Any account may become a delegate, but only accounts with the required stake are allowed to generate blocks.</p>

<p><b>Delegate Round</b></p>

<p>A round within the system is exactly N blocks in length (N is identical to the total forging delegates). During one round, each delegate will forge <a href="/video-qa-blockchains-are-created-equal/">exactly one block</a>. If an elected delegate cannot forge during a round another delegate will forge their block instead. </p>

<p>At the beginning of each round, each delegate is assigned a slot indicating their position in the block generation process. Once a node with an enabled active delegate has forged a block, the node associated with the delegate includes up to 25 transactions into the block, signs it and broadcasts that block to the network. Once the block has reached the network, the next delegate will forge in the slot assigned to them.</p>

<p>In Lisk, there are various incentives provided to make running a node appealing. The first of these is the block generation reward and the other reward is the accrual of fees for securing the network as an active delegate for the round in which that delegate participates.</p>

<h4>Block Rewards</h4>

<p>As with bitcoin and nearly all other blockchain systems, Lisk rewards the block generator a fixed amount of tokens per block successfully generated and accepted by the system. In Lisk's system, all active delegates that successfully participate are rewarded for securing the network. The timeline for these block rewards are represented in the following figure:</p>

<center><img src="/images/lisk-reward-reduction.jpg" alt="lisk reward reduction"></center>

<p>The block reward linearly decreases over the lifetime of the network, providing significant incentive to actively participate as an active delegate. The reward will decrease every 3.000.000 blocks from the initial reward block.</p>

<p><b>Round Fees</b></p>

<p>The second incentive provided by the system comes in the form of round fees. A round, described in section 6.1, comes to a close after the number of specified blocks has been generated. During this closure process, all transactional fees are aggregated and subsequently split between all active participates in the round. </p>

<p>These fees can provide significant reward for each participant outside of the block generation reward, provided there is significant transactional activity present in the system.</p>

<p>It is possible for a delegate to earn multiple shares of these fees. This may occur if a delegate forges multiple blocks within a round. In most circumstances this will not occur, however occasionally another delegate node may be offline during the delegate's assigned slot and subsequently will be unable to generate a block for the assigned slot. This means that the delegate misses its slot and another delegate will therefor generate multiple blocks during the round instead.</p>

<h4>Peers Communication</h4>

<p>Peers communication serves a vital function within the Lisk network. The peering mechanisms provide the required architecture to facilitate network consensus, block propagation and transaction propagation.</p>

{% include page-toc.html %}

<p><b>System Headers</b></p>

<p>Within the Lisk network system headers are used to identify full nodes and provide a basic set of information about the software running on the system. During <a href="/video-qa-resist-financial-surveillance/">peers communications</a> these headers are added to all messages sent between peers. The following JSON object is generated from system data for this purpose and will be broadcast to the network during all communications:</p>

JSON
<code>
 {
  "os":"darwin16.3.0",
  "version":"0.6.0a",
  "port":7000,
  "height":1574654,
  "nethash":"da3ed6a45429278bac2666961289ca17ad86595d33b31037615d4b8e8f158bba",
  "broadhash":"c7e0902a7016205d456a427edda2b09f4b875f98ef40a224018a0274347146ac",
  "minVersion":">=0.5.0"
}
</code>
<p><b>Broadhash Consensus</b></p>

<p>Broadhash consensus serves a vital function for the Lisk network in order to prevent forks. In the DPoS system, delegates are assigned slots based on timestamp and will attempt to forge a block when the system designates that delegate slot as ready. Broadhash consensus ensures that a majority of available peers agree that it is acceptable to forge.</p>

<p>Broadhash is established as an aggregated rolling hash of the past five blocks present in the database. All peers with the same blocks will produce the same broadhash and propagate that information via the system headers described in section 8.1.</p>

<p><b>Block Propagation</b></p>

<p><a href="/blockchain-uses/">Block propagation</a> serves a vital function within the Lisk network. Blocks are made in a decentralized fashion and must be sent to all nodes found on the network in order to establish consensus. When a block is generated, it is broadcast to peers which broadcast that block to other peers. Without block propagation, the system would grind to a halt and the blockchain would cease to be functional.</p>

<p><b>Broadcast Queue</b></p>

<p>The broadcast queue serves a fundamental role for the Lisk network. Transactions must move from one node to all other nodes in order to be included in blocks. The broadcast queue works by grabbing up to 25 transactions from the transactions pool and aggregating them into a bundle. </p>

<p>This bundle is then broadcast to the network on an interval, which is currently specified as every 5 seconds. In addition to broadcasting the object, the bundle is given a relay limit to prevent over broadcasting of data. In the current implementation the relay limit is set as 2, which means every bundle will be broadcast once from the originating node, and twice more from receiving nodes.</p>

<h4>Transaction Pool</h4>

<p>The transaction pool provides the Lisk network a very robust solution for preserving unconfirmed transactions that have overflowed into the next block. As mentioned in section 6, each block may only include 25 transactions and the transaction pool allows for up to 5.000 transactions to remain queued for the next block(s). The transaction pool could be thought of as a memory pool keeping transactions ready until they are signed into a block.</p>

<p>The second usage of the transaction pool is to provide a mechanism for propagating transactions. When a node prepares a transaction bundle, that node draws up to 25 transactions from the pool and performs validation on those transactions. These transactions are then broadcast to other nodes in a bundled JSON object. This can be represented as an array of objects of every transaction type listed in section 5.</p>

<p>In order to keep the transaction pool tidy, all transactions are given a time to live. This time to live is defined as 10800 seconds, or 1080 blocks.</p>

<p>The final use for the transaction pool is to house transactions with pending signatures. These transactions with pending signatures following the same model as unconfirmed transactions. This way multisignature transactions that are isolated as incomplete within the transaction pool. Like unconfirmed transactions, these transactions will expire out of the pool based on the lifetime specified when the transaction is first generated.</p>

<h2 id="latest">Latest Lisk News</h2>

<h4>Lisk Rebrand — Development Timeline</h4>

<p>Identity and positioning are essential components of a strong brand strategy. They define how the company communicates with its key stakeholders at every touchpoint. Here at Lisk, we treat these values with utmost importance and have been working tirelessly since the beginning of the year to clearly articulate our vision and ambitions.</p>

<center><img src="/images/lisk-brand.jpg" alt="what is Lisk"/></center>

Introducing Six New Lisk Team Members

<p>As the summer comes to a close, great changes are abound here at Lisk. Max and Thomas kicked off their Asia tour in Shanghai with Seoul, Tokyo and Mumbai up next. Be sure to follow Lisk on Twitter and Facebook for updates from their trip. To accommodate the rapid growth Lisk is experiencing, we have hired new talent and are working hard to implement more comprehensive resources for the Lisk community.</p>

{% include page-toc.html %}

<p>Product development is at the top of our priority list so you will see continued growth of our development team over the next months. From a business perspective, one of our biggest endeavours is to help educate people about <a href="/the-best-bitcoin-casinos/">Blockchain technology</a>, therefore we now have dedicated marketing resources to Lisk Academy.</p>

<p>It is often asked how serious we are about expanding the team. The headcount of our Berlin office has grown by six in the last two weeks alone. These new team members will help promote Lisk’s accelerated growth.</p>

<center><img src="/images/lisk-team.jpg" alt="what is Lisk"/></center>
