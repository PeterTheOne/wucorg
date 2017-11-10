---
layout: post
title: Video - RSA encryption - Step 3
description: Video - RSA encryption - Step 3
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>RSA Encryption (step 3). Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/cJvoi0LuutQ" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

Over 2,000 years ago, Euclid showed every number has exactly one prime factorization, which we can think of as a secret key. It turns out that prime factorization is a fundamentally hard problem. Let's clarify what we mean by "easy" and "hard", by introducing what's called "time complexity". 

We have all multiplied numbers before, and each of us our own rules for doing so, in order to speed things up. If we program a computer to multiply numbers, it can do so much faster than any human can. Here is a graph that shows the time required for a computer to multiply two numbers. And, of course, the time required to find the answer increases as the numbers get larger. 

Notice that the computation time stays well under one second, even with fairly large numbers. Therefore, it is "easy" to perform. Now, compare this to prime factorization. If someone told you to find the prime factorization of 589, you will notice the problem feels harder. 

No matter what your strategy, it will require some trial and error until you find a number which evenly divides 589. After some struggle, you will find 19 times 31 is the prime factorization. If you were told to find the prime factorization of 437, 231, you'd probably give up and get a computer to help you. 

This works fine for small numbers, though if we try to get a computer to factor larger and larger numbers, there is a runaway effect. The time needed to perform the calculations increases rapidly, as there are more steps involved. As the numbers grow, the computer needs minutes, then hours, and eventually it will require hundreds, or thousands of years to factor huge numbers. 

We therefore say it is a "hard" problem due to this growth rate of time needed to solve it. So factorization is what Cocks used to build the trapdoor solution. Step one, imagine Alice randomly generated a prime number over 150 digits long; call this "p one". 

Then, a second randon prime number roughly the same size; call this "p two". She then multiplies these two primes together to get a composite number, N, which is over 300 digits long. This multiplication step would take less than second; we could even do it in a web browser. 

Then, she takes the factorization of N, p one times p two, and hides it. Now, if she gave N to anyone else, they would have to have a computer running for years to find the solution. Step two, Cocks needed to find a function which depends on knowing the factorization of N. For this, he looked back to work done in 1760 by Swiss mathematician, Leonhard Euler.
