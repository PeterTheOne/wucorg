---
layout: post
title: A Quick Tour Of Bitcoin Core
description: A Quick Tour Of Bitcoin Core
author: Melvin Draupnir
authorurl: /melvin-draupnir/
published: true
---

<p>Months ago, when Adam Back posted this tweet calling Bitcoin Classic “semi-tested alpha code”, I ignored it. But today he posted the following nasty-gram on a Reddit AMA with a bitcoin miner:</p>

<p>“Do you understand that BU is non-functional , little tested, partly-implemented, more aspiration than something that could be run. <a href="/amazing-math-bitcoin-private-keys/">with limited developer experience</a>, effectively no QA and bitcoin security management experience and would probably just crash the network for people who followed it’s blocks?…</p>

<p>If you cant provide compelling and convincing arguments to any of these questions I suggest you reach out and talk with developers.” (link)</p>

<p>Adam, unlike your statement (which is full of opinion yet contains zero actual data), I will provide some “compelling and convincing arguments” in this post.</p>

<p>But first I need to say that one of the reasons I started Bitcoin Unlimited was to get away from the dismissive, disrespectful and elitist behavior I see in this post and see in various Core-related forums on a daily basis.</p>

<p>Normally, in Bitcoin Unlimited when we find a Core bug we just fix it and move on. I feel that laying every problem out to the Reddit trolls creates a negative environment that affects the larger Bitcoin effort.</p>

<p>But I feel that the Core team is attempting to create a feeling that they are uniquely qualified to work on Bitcoin and that such work is somehow much more difficult than other mission critical development.</p>

<p>This post should destroy the myth that the Bitcoin Core team is somehow superior or more qualified than other teams, for any engineer who can understand the bugs that I will show. If you are not an engineer, find one (he/she need not be a bitcoiner) and ask them their opinion of this list.</p>

<p>Indeed, Bitcoin Unlimited is building the highest quality, most stable, <a href="/bitcoin-privacy-technologies-zerocash-confidential-transactions/">Bitcoin client available</a>. We have a strong commitment to quality and testing as you will see in the rest of this document. If you are a developer and tired of the Bitcoin Core “brogrammer” mentality, if you are tired of your ideas being unilaterally crushed without recourse by one of the Core committers, I’d urge you to give us a try. </p>

<p>I think you will find the situation to be very different — it is demonstrably so because we follow an organizational system specified in our Articles of Federation that gives members recourse in the case where a developer disagrees with the committer. This process ultimately allows the idea to be voted on by the membership, and quantitatively accepted or rejected.</p>

<p>But back to the bugs: As we mine the garbage in the Bitcoin Core code together, I ask that you remember that nobody is perfect. Be reminded that many of the contributors are volunteers, working on this rather than having fun. And people come from many backgrounds, crypto, networking, white hat, and are liable to make mistakes outside their expertise.</p>

<p>Instead, I want you to realise that these issues are systemic to Core, not any individual. So please refrain from chasing down who actually wrote the code in a particular bug — yes, developer quality can vary by a factor of 100 or more, but discovering this quality needs to be done statistically, not anecdotally. Nobody should be in the crossfire because I chose “their” bug for this post, we’ve found many others.</p>

<p>Finally, please note that we have found these bugs over the past year in various Core releases. While I am linking to the code still existing in the 0.13 releases or master branches, I have neither the time nor the inclination to test each one again to determine whether they are still easily expressed in the current release.</p>

<h2>1. Let’s Lose Some Money</h2>

<p>Summary: If you send money in the QT client and include a very large transaction fee, you get an error dialog box saying that the fee is excessively large, the transaction is not sent but the money is deducted from your wallet.</p>

<p>Ok, ok, you probably haven’t actually lost the bitcoin— if you <a href="/how-to-store-bitcoin-USB-stick/">resync your wallet</a> with the blockchain data your money will reappear. But who knows how to do that, and can we expect the normal user to not panic?</p>

<p>You can see the problem right here in the call to AcceptToMemoryPool in “CommitTransaction”. On line 2460 the transaction is added to the wallet. But its added to the memory pool on line 2481. And look, the developer added a comment “// This must not fail. The transaction has already been signed and recorded.” But what if it DOES fail? If the function never failed, why would it return a boolean?</p>

<p>In fact, it does fail, returning false in many cases. In particular, if the user provides an “absurdly high fee”.</p>

<p>This absurdly high fee check was added over a year ago in the 0.12.0 time frame. Did the developer who added this check search for uses of AcceptToMemoryPool to verify that his return value would be handled properly? Nope, he would have seen the comment. Did he create a unit test? No, he would have seen the bug. Did he even test the code by hand? I doubt it for the same reason. Would I have accepted a “// this must not fail” comment in a pull request for a function that can return “failed”? Absolutely not.</p>

<p>This code has been sitting undetected by Core for over a year. We fixed it last January and the fixed code has been publicly available in our repository for that long. One advantage of the Bitcoin Unlimited process is that we pull the best work from all the other development teams…</p>

<p>UPDATE: There has been a lot of denial-before-validation from Core developers (not a good response from a strong development team, by the way) so I made a video showing the bug running on a stock Bitcoin Core 0.12.1 release binary download. In this video you will see me start with over 110 BTC, send 100 BTC to myself, get an error message, and end up with about 10 BTC.</p>

<h2>2. Global constructor and destructor ordering: fixing garbage with garbage</h2>

<p>Summary: The order of construction and destruction of global variables across “translation units” (files) is undefined in the c++ language, yet the Core code has inter-file inter-dependent global variables. One effect of this problem is “solved” in the latest Core release by the use of additional undefined behavior.</p>

<p>The simplest example of the problem is the mutex locks used by CCriticalSection. These objects need to be constructed before and destructed after any other object that contains a CCriticalSection, yet CCriticalSection global variables are declared in many other modules (net.cpp, main.cpp, and rpcwallet.cpp to grab 3). So the C compiler cannot guarantee that the mutex is available before a CCriticalSection uses it.</p>

<p>In any use of undefined behavior issues are typically seen only on alternative platforms, like Windows and Mac, or alternative architectures (ARM), because if they were seen on the typical development platform they would be fixed or worked around (as we’ll see below). But to produce high quality code that runs consistently across multiple platforms, developers need to remain within the defined boundaries of the programming language.</p>

<p>In the Bitcoin Unlimited group, we have developers working daily on <a href="/how-to-use-mycelium-bitcoin-wallet/">Windows and Linux machines</a>, and I personally have Windows, Linux, Mac and ARM Linux machines in my “lab”, running the client 24x7. We first saw this problem as core dumps on the Mac platform. To solve the problem, we placed all dependent global variables in a dedicated file called “globals.cpp”. Since all dependent globals are now in a single “translation unit”, constructor and destructor order is well-defined. This is a common solution to this well-known problem.</p>

<p>In their latest version, Bitcoin Core has also solved the problem here. First, let’s look at the author’s comment; notice that it explains the problem as “global constructors and destructors run single threaded”. This strongly suggests that he doesn’t actually understand the issue because this “single threaded” fact is irrelevant. Secondly, the author actually identifies this as a “Very Ugly Hack”, yet this code somehow passes review and is placed in a worldwide 10 billion dollar financial network?</p>

<p>Next, let’s examine the solution’s code. The author puts some global variables in a struct alongside a new “available” global variable. If “available” is true, the dd_mutex is used. If it is not, it is ignored. However, note that “available” is set to “false” just before the object is destructed. So the author is relying on the RAM that contained “available” still hold the value “false” AFTER the variable’s own destruction. This is a deliberate use of the well known C/C++ “use after free bug”. The problem is that in C and C++, the value of a variable after destruction is undefined so there is no guarantee that the “available” variable will remain “false” or even that the memory will be accessible.</p>

<p>The Bitcoin Core code is relying on undefined behavior to solve a problem caused by reliance on undefined behavior.
A very simple partial solution would of course be to make the “available” global variable a separate initialized global since primitives are not constructed, yet set it true/false in the ctor/dtor of LockData… one must wonder why this idea wasn’t used.</p>

<p>But this simple solution ignores the fundamental problem — a mutex is needed to protect a critical code section. Its generally not “OK” for the lower layers to choose to skip locking or unlocking a mutex even though the upper layers have called the lock/unlock API. And finally this “solution” solves the problem for just these 3 globals, ignoring all the other dependent global variables…</p>

<h2>3. Crashes</h2>

<p>Summary: I share one of many crashes that is caused by multi-threaded issues when using pointers to CNode objects.</p>

<p>At Bitcoin Unlimited we are testing large blocks so we need to drive bitcoin test networks hundreds of times faster than it is being used today (for example, you can see my work optimising transaction generation here which allows us to generate transactions 1000 times faster than the Core client does today). With this code running on the 10 or so worldwide nodes that Bitcoin Unlimited uses for test, we are driving months of use in hours. This intensity of testing means that rare issues become prevalent.</p>

<p>So yes, there have been a lot of crashes we can directly trace to Core code.</p>

<h2>Let’s go over one:</h2>

<p>In net.cpp there’s a helper function “FindNode” that looks through the node list and returns a matching node. Actually, there are 5 FindNode functions and they all have the same problem. The function properly locks the node mutex (cs_vNodes) while searching through the node list, and then it returns a pointer to the found node, unlocking cs_vNodes. </p>

<p>Unfortunately, this is a multi-threaded application, so as soon as the mutex is unlocked another thread might disconnect the node and delete the node object. This will cause a core dump (or corrupt the heap) as soon as the caller tries to use the deleted object.</p>

<p>There are 7 uses of FindNode in the code. I don’t remember if it was all or just the majority that did not do their own locking of cs_vNodes. For quick reference, here is one.</p>

<p>The correct solution is to either add a reference to the node before unlocking cs_vNodes or to force the caller to lock cs_vNodes by using “AssertLockHeld”.</p>

<p>Due to this bug, and another, it would theoretically be possible for an attacker to crash a <a href="/what-is-immutability">remote node if it disconnected</a> at the exact right moment. However, I was unable to “weaponize” this exploit during my testing so I feel that there is little risk in public disclosure today.</p>

<h2>Conclusion</h2>

<p>I hope when reading these issues, you will realise that the Bitcoin Unlimited team might actually be the most careful committers and testers, with a very broad and dedicated test infrastructure. And I hope that you will see these Bitcoin Core commits— bugs that are not tricky and esoteric, but simple issues that well known to average software engineers —and commits of “Very Ugly Hack” code that do not reflect the care required for an important financial network. </p>

<p>I hope that you will realise that, contrary to statements from Adam Back and others, the Core team does not have unique skills and abilities that qualify them to administer this network.</p>

