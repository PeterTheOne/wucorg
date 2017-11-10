---
layout: post
title: Video - RSA encryption - Step 1
description: Video - RSA encryption - Step 1
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>Introduction to why we would need RSA. Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/EPXilYOa71c" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

Up until the 1970s, cryptography had been based on symmetric keys. That is, the sender encrypts their message using a specific key, and the receiver decrypts using an identical key. (lock clinking) As you may recall, encryption is a mapping from some message using a specific key, to a ciphertext message. To decrypt a ciphertex, you use the same key to reverse the mapping. 

So for Alice and Bob to communicate securely, they must first share identical keys. However, establishing a shared key is often impossible if Alice and Bob can't physically meet or requires extra communications overhead when using the Diffy-Hellman key exchange. 

Plus, if Alice needs to communicate with multiple people, perhaps she's a bank, then she's going to have exchange distinct keys with each person. Now she'll have to manage all of these keys and send thousands of messages just to establish them. Could there be a simpler way? In 1970, James Ellis, a British engineer and mathematician, was working on an idea for non-secret encryption. 

It's based on a simple, yet clever concept: Lock and unlock are inverse operations. Alice could buy a lock, keep the key, and send the open lock to Bob. Bob then locks his message and sends it back to Alice. No keys are exchanged. This means she could publish the lock widely and let anyone in the world use it to send her a message. And she now only needs to keep track of a single key. 

Ellis never arrived at a mathematical solution, though he had an intuitive sense of how it should work. The idea is based on splitting a key into two parts, an encryption key and a decryption key. The decryption key performs the inverse or undo operation which was applied by the encryption key. 

To see how inverse keys could work, let's do a simplified exampled with colors. How could Bob send Alice a specific color, without Eve, who is always listening, intercepting it? The inverse of some color is called a complimentary color, which when added to it, produces white, undoing the effect of the first color. 

In this example, we assume that mixing colors is a one-way function because it's fast to mix colors and output a third, and it's much slower to undo. Alice first generates her private key by randomly selecting a color, say red. Next, assume Alice uses a secret color machine to find the exact compliment of her red and nobody else has access to this. 

This results in cyan, which she sends to Bob as her public key. Let's say Bob wants to send a secret yellow to Alice. He mixes this with her public color and sends the resulting mixture back to Alice. Now Alice adds her private color to Bob's mixture. 

This undoes the effect of her public color, leaving her with Bob's secret color. Notice Eve has no easy way to find Bob's yellow, since she needs Alice's private red to do so. This is how it should work. However, a mathematical solution was needed to make this work in practice.
