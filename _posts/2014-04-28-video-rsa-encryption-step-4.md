---
layout: post
title: Video - RSA encryption - Step 4
description: Video - RSA encryption - Step 4
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>RSA worked example. Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/UjIPMJd6Xks" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

We now have a trapdoor for solving phi. If you know the factorization for N, then finding phi N is easy. For example, the prime factorization of 77 is seven times 11, so phi of 77, is six times 10, 60 Step three, how to connect the phi function to modular exponentiation. 

For this, he turned to Euler's Theorem, which is a relationship between the phi function and modular exponentiation, as follows: m to the power of phi n, is congruent to one mod n. This means you can pick any two numbers, such that they do not share a common factor, let's call them "m" and "n". 

Say m equals five and n equals eight. Now, when you raise m to the power of phi n, or 4, and divide by n, you will always be left with one. Now, we just need to modify this equation using two simple rules. First, if you raise the number one to any exponent, k, you always get one. 

In the same way, we can multiply the exponent phi n by any number k, and the solution is still one. Second, if you multiply one by any number, say m, it always equals m. In the same way, we can multiply the left side by m, to get m on the right hand side. And this can be simplified as m to the power of k, times phi n, plus one. This is the breakthrough. We now have an equation for finding e times d, which depends on phi n. 

Therefore, it's easy to calculate d, only if the factorization of n is known. Meaning d should be Alice's private key. It's the trapdoor which will allow her to undo the effect of e. Let's do a simple example, to see all of this in action. Say Bob has a message he converted into a number, using a padding scheme. 

Let's call this "m". Then, Alice generates her public and private key as follows: First, she generates two random prime numbers of similar size and multiplies them to get n, 3,127. Then she calculates phi of n easily, since she knows the factorization of n, which turns out to 3,016. 

Next, she picks some small public exponent, e, with the condition that it must be an odd number that does not share a factor with phi n. In this case she picks e equals three. Finally, she finds the value of her private exponent, d, which in this case is two times phi of n, plus one, divided by three, or 2,011. Now, she hides everything except the value of n and e, because n and e make up her public key. 

Think of it as an open lock. She sends this to Bob to lock his message with. Bob locks his message by calculating m to the power of e, mod n. Call this "c", his encrypted message, which he sends back to Alice. Finally, Alice decrypts his message using her private key, d, accessed through her trapdoor. c to the power of d, mod n, equals Bob's original message, m. 

Notice that Eve, or anyone else, with c, n, and e, can only find the exponent d, if they can calculate phi n, which requires that they know the prime factorization of n. If n is large enough, Alice can be sure that this will take hundreds of years, even with the most powerful network of computers. 

This trick was immediately classified after its publication, however, it was independently redisovered in 1977 by Ron Rivest, Adi Shamir and Len Adleman, which is why it's now known as RSA in encryption. RSA is the most widely used public key algorithm in the world, and the most copied software in history. 

Every internet user on earth is using RSA, or some variant of it, whether they realize it or not. Its strength relies on the hardness of prime factorization. which is a result of deep questions about the distribution of prime numbers. A question which has remained unsolved for thousands of years. (dramatic music)
