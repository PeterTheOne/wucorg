---
layout: post
title: Video - Random Primality Test Warm Up
description: Video - Random Primality Test Warm Up
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>Introduction to random primality tests & how they will work (warm up). Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/1mjyq51ppT8" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

Voiceover: First, let's build up the conceptual mechanics for these new types of random algorithms which accept some input N and if N is prime, our algorithm will output prime with 100% certainty. It will never label it as composite. However, if N is composite, there will be some tiny chance of error E that it will label it prime. Otherwise, there is a one minus this tiny error probability that it will correctly identify it as composite. 

We will start simple. Out of some universe of integers up to some limit, we grab a number and call this integer N. We input N into our machine. Previously, in our trial division methods, we basically iterated through all values from one to the square root of N and tested if that number divides N. Ideally, we only wanted to check primes to save time. If yes, A divides N, we know that N is a composite number because we found a composite witness. 

If not, we aren't sure. So, we go back and we increment A and we test again. Once we exhaust all possible tests, we can then say yes, N is prime, if we found no divisors. Now, let's be lazy. What if we just pick a few random integers and do a few divisibility tests which you can think of as random questions. We know that some number N, if it is composite, it must have some divisors scattered around. 

At minimum, it has a single divisor. Some composite numbers have many divisors. Anyway, we pick a random integer A between one and the square root of N. That's it. Then we just check if A divides N. As before, if A divides N we know for sure that N is composite, we found a witness. If not, we haven't learned too much except that it could be prime. To be safe, we could generate a few more random As and keep testing. 

Perhaps after 100 or 1,000 iterations, we could stop and say "It's probably prime" with some certainty. Say, for example, 99.9 percent. This is similar to the example game on conditional probability. In the simplest version, we were trying to guess if a coin was fair or if it was a two-headed coin. In this case, tails is like finding a divisor. It's a witness of a fair coin. 

Heads is the case where we might want the person to flip again and iterate. In this case, after around 5 heads, we are more than 90 percent sure so we could stop and say "We think the coin is two-headed." Here is a program I have set up which compares our old trial division methods with this new random division test. I am specifically using the current trial division speed leader, which is a program by Dino. 

I posted the link in the header of the program. To begin, notice the variable number of trials. This is the number of random guesses. We will start at something small, such as three. Notice, even with small input, if the input is prime, the random division algorithm will always output prime. When the input is composite, we see the random division can make mistakes and identify incorrectly as prime. 

However, we can fix this by increasing the number of trials then the probability of an error goes down. We see now that the outputs more or less match. As I test larger input, the error grows again. I need to increase the number of random tests accordingly. When I do, the outputs match very nicely. They seem identical. With huge input size, I need thousands of random tests for this to be accurate. 

We haven't actually improved the number of steps needed. Our trial division method seems better. This is because the error rate of the division test is so high, but we are close. We have the right idea. We need to use another test. We need an equation which is fast to calculate, that can be used to prove whether a number is composite. It must accept not only the input integer N, but also a random integer A and do a random test in the same sort of way.
