---
layout: post
title: Video - Diffie-hellman Key Exchange
description: Video - Diffie-hellman Key Exchange
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>Walkthrough of Diffie-Hellman Key Exchange. Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/M-0qt6tdHzk" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

Now this is our solution. First Alice and Bob agree publicly on a prime modulus and a generator, in this case 17 and 3. Then Alice selects a private random number, say 15, and calculates three to the power 15 mod 17 and sends this result publicly to Bob. 

Then Bob selects his private random number, say 13, and calculates 3 to the power 13 mod 17 and sends this result publicly to Alice. And now the heart of the trick; Alice takes Bob's public result and raises it to the power of her private number to obtain the shared secret, which in this case is 10. 

Bob takes Alice's public result and raises it to the power of his private number resulting in the same shared secret. Notice they did the same calculation, though it may not look like it at first. Consider Alice, the 12 she received from Bob was calculated as 3 to the power 13 mod 17. So her calculation was the same as 3 to the power 13 to the power 15 mod 17. 

Now consider Bob, the 6 he received from Alice was calculated as 3 to the power 15 mod 17. So his calculation was the same as 3 to the power 15 to the power 13. Notice they did the same calculation with the exponents in a different order. When you flip the exponent the result doesn't change. 

So they both calculated 3 raised to the power of their private numbers. Without one of these private numbers, 15 or 13, Eve will not be able to find the solution. And this is how it's done; 

While Eve is stuck grinding away at the discrete logarithm problem, and with large enough numbers, we can say it's practically impossible for her to break the encryption in a reasonable amount of time. This solves the Key Exchange problem. It can be used in conjunction with a pseudorandom generator to encrypt messages between people who have never met.
