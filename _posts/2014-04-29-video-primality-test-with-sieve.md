---
layout: post
title: Video - Primality Test with Sieve
description: Video - Primality Test with Sieve
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>An attempt at an optimal trial division primality test using the Sieve of Eratosthenes. Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/XspzfNSSqyk" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

Now, to recap We are checking if sum number N is prime by doing a trial division. Here is the square root of N and here is three. Starting at three, we are hopping along by two up until the square root of N. At each point in the way, checking if that point divides N. Now so far, people have been trying to reduce the number of steps we take by perhaps starting later and taking larger steps. 

I just want to pause here and let's think about what is the ideal case for a trial division algorithm? What is the best we could possibly do if we got very creative in our stepping? Remember, any number N has some tri-factorization. Let's say the square root of N is here. 

We actually only need to step on prime numbers. That would be the best we could do. We know if we step only on primes, we will eventually find a factor. Tri-factor if it's a composite. The question now is how efficient is this method? It seems like we have a perfect solution now. If we wrote a new algorithm which first called the sieve. Let's say the new algorithm is calculating if N is prime. 

If you call the sieve and generate a nice long list of primes for us. Then, we have our trial division, which would use this list of primes. It would hop along and hit only primes up until the square root of N, wherever that is. What's wrong with this? We can visualize the time complexity or the number of steps taken. Remember I did so by- I quoted up this algorithm and I put a step counter inside each loop so we have- let's just say step plus plus means step plus one here. 

Inside this other loop, there is also a step counter. Step plus plus. These are all constant operations checking if and marking. We just had a step counter inside each loop. Now here is a comparison. On the far left is our old trial division method. In the middle is our algorithm calling the sieve to generate all primes up to N. 

On the right is this proposal where we just call the sieve to generate primes up to the square root of N and then call trial division just on those primes. Let's see what happens with a small input. As we can see initially, the sieve takes many steps. Even the modified version on the right is actually slower than trial division. As the input grows, the number of steps in the sieves grows even faster. 

Let's just forget the middle and compare trial division versus the sieve up to the square root of N plus trial division. Here we can see the old trial division method is much more efficient. The number of steps in our sieve to the square root of N plus trial division is growing much faster. 

It is actually not an improvement. Below is the program I used to do this comparison. There is a recording explaining how I set it up. Now you may be wondering "Well, what if we calculated the primes in advance?" The first step would be to build an array of primes and store it on a hard drive. Then, our algorithm would just do trial division and it would know how to hop on primes only because it would be reading from this proposed prime list. 

Perhaps our prime list stores all primes up to 20 digits or even 100 digits. Why can't we do this? The problem is limitations in memory. When we innumerate lists of numbers, which we will explore next. Just for example, let's say we were doing this by hand. We calculate five was prime, we write five on a piece of paper, and we store it in a filing cabinet. Then we get seven, we store that in the filing cabinet. 

Nine, or 11, sorry, into the filing cabinet. Then we have a filing cabinet full of prime numbers. This is our- think of it as a prime array. How big would this filing cabinet be if, say, we wanted all primes up to 20 digits or all primes up to 100 digits long? Could we even store this array on a hard drive? 

To understand why this actually is not possible we have to dive a little deeper into how large does this actually grow, this prime array, and what is the size limitation of modern-day and even future computer hardware?
