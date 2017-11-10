---
layout: post
title: Video - RSA encryption - Step 2
description: Video - RSA encryption - Step 2
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>Setting up a trapdoor one-way function. Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/IY8BXNFgnyI" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

The solution was found by another British mathematician and cryptographer, Clifford Cocks. Cocks needed to construct a special kind of one-way function called a trapdoor one-way function. This is a function that is easy to compute in one direction, yet difficult to reverse, unless you have special information, called the trapdoor. 

For this, he turned to modular exponentiation, which we introduced as clock arithmetic, in the Diffie–Hellman key exchange, as follows. Take a number, raise it to some exponent, divide by the modulus and output the remainder. This can be used to encrypt a message as follows: Imagine Bob has a message, which is converted into a number, m. 

He then multiplies his number by itself, e times, where e is a public exponent, then he divides the result by a random number, N, and outputs the remainder of the division. This results in some number, c. This calculation is easy to perform, however, given only c, e, and N, it is much more difficult to determine which m was used, because we'd have to resort to some form of trial and error. 

So, this is our one-way function that we can apply to m, easy to perform, but difficult to reverse. It is our mathematical lock. Now, what about the key? The key is the trapdoor, some piece of information that makes it easy to reverse the encryption. 

We need to raise c to some other exponent, say d, which will undo the initial operation applied to m and return the original message m. So, both operations together, is the same as m to the power of e, all raised to the power of d, which is the same as, m to the power of e times d, e is the encryption, d is the decryption. 

Therefore, we need a way for Alice to construct e and d, which makes it difficult for anyone else to find d This requires a second one-way function which is used for generating d, and for this, he looked back to Euclid.
