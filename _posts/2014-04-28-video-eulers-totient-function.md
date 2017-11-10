---
layout: post
title: Video - Eulers Totient Function
description: Video - Eulers Totient Function
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>Measuring the divisibility of a number. Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/qa_hksAzpSg" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

Euler continued to investigate properties of numbers, specifically the distribution of prime numbers. One important function he defined is called the phi function. It measures the breakability of a number. So, given a number, say N, it outputs how many integers are less than or equal to N that do not share any common factor with N. 

For example, if we want to find the phi of eight we look at all values from one to eight, then we count how many integers eight does not share a factor greater than one with. Notice six is not counted, because it shares a factor of two, while one, three, five and seven are all counted, because they only share a factor of one. 

Therefore, phi of eight equals four. What's interesting is that calculating the phi function is hard, except in one case. Look at this graph. It is a plot of values of five, over integers from one to 1,000. Now, notice any predictable pattern? The straight line of points along the top represent all the prime numbers. 

Since prime numbers have no factors greater than one, the phi of any prime number, P, is simply P minus one. To calculate phi of seven, a prime number, we count all integers, except seven, since none of them share a factor with seven. Phi of seven equals six. 

So, if you're asked to find phi of 21,377, a prime number, you would only need to subtract one to get the solution, 21,376. Phi of any prime is easy to compute. This leads to an interesting result based on the fact that the phi function is also multiplicative. 

That is, phi A times B equals phi A times phi B. If we know some number N is the product of two primes, P one and P two, then phi of N is just the value of phi for each prime multiplied together, or P one minus one, times P two minus one.
