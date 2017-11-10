---
layout: post
title: Video - Time Space Tradeoff
description: Video - Time Space Tradeoff
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>What is our memory limit? How can save time at the expense of space? Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/9YRw0Yk7N8c" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

Voiceover: I have a new update. I contacted the engineering department at NASA and found out the new rover is using the same memory platform used on curiosity. And the curiosity rover was equipped with two computers, but only one was active at a time and it had the following specs. 

Two gigabytes of flash memory, 256 megabytes of random access memory, and 256 kilobytes of read only memory, which held core system routines. We want to be able to store our entire program in RAM, however because we have to share this space with other programs, we are allocated 5% of RAM, which is the maximum we can use. 

This is about 12.8 megabytes total. I bring this up because I want to introduce the idea of time space trade off, or space time trade off, a commonly used term in computer science. I was looking at a program done by IV46 and they had a million prime array so that there algorithm could step along on primes only, as far as possible, when doing a trial division primality test. 

It begs the question, why just not store all the primes we need, up to some limit in an array instead of calculating them on the fly? We mentioned in a previous video that this would be optimal for a trial division algorithm. Although you may see his algorithm does not use many steps, it began to run very slowly and eventually crashed before hitting the step limit. 

So it wasn't able to quickly solve the problem for the sizes I defined earlier. And in this case, they were trading off time in the form of repeated divisibility tests at the expense of space, which is memory to hold the array. Now, why didn't this work? Well, let's do a rough calculation using what we've learned to find out if this method is possible using our memory limit. 

Remember, we must be able to deal with numbers up to just over 9 quadrillion. Our trial division algorithms only need to check for factors up to the square root of a number, and if it hits that point with no factors found, it can say 100% whether or not the number is prime. Now, how many primes up to the square root of this limit, where the square root of 9 quadrillion is 94.9 million? 

How many primes under 95 million? Well, luckily we have learned a mathematical solution to approximate this answer using the prime number theorem. So how many primes are there under x? Well, it's x divided by the natural logarithm of x. And if x is just over 94.9 million, we find the number of primes is approximately 5.1 million. Now because we are storing these primes, we need to know the size of the largest prime, or in this case, the 5.1 millionth prime approximately, which we know will be some number less than 94.9 million. 

Now, I double checked the table, and the actual value of this prime, the largest prime we would need to store under the square root of our limit, is 89,078,611. Now how much memory does this single large prime number require? Well, to find out, let's convert the number into binary notation, which is how the computer will store the number using tiny switches in memory. We learned about this in the computer memory video. In bits, the largest prime looks like this, which is 24 bits or 3 bytes needed to store this single number. 

So let's say we want to store each number in memory and since we know the largest number requires 24 bits, we can just imagine a long list of 24 bit blocks storing each prime number. So how many bits are needed for this entire list? Well the memory needed is the number of values, or the number of primes, times the space per value. So we have around 5.1 million values times 24 bits per value, which is just over 124 million bits, or if we convert it into bytes, it's about 14.7 million bytes. 

Call this almost 15 megabytes. So it is not possible to store even a list of these numbers in memory using our limit. This is just a toy example. It's actually an underestimation of what you'd really need. For example, an array needs space for a pointer to each item, and each pointer on a 32 bit machine is 4 bytes. So the actual amount of memory needed is much more than 15 megabytes. That being said, we know that storing all primes up to the square root of our relatively small limit is not even possible with our memory limit. 

We can't do it this way. Okay, well, what about when prices drop by a factor of a thousand, or ten thousand. Modern day cryptographic systems use 512 bit, or even larger numbers, making search and enumeration impossible. Now for example, if someone asks you to make a list of all prime numbers up to primes which are 200 digits in length, you shouldn't even consider it because the hard drive needed to store all these primes would be heavier than the mass of the observable universe. 

I'll leave the calculations for you to try next time you're at a restaurant with crayons and paper all over the table. But remember, there are around 10 to the 80 atoms in the observable universe. That's an 80 digit number. Realize now, there is a fundamental limit for how much space or memory we have access to. 

Nevermind how much time it would take, but there is always this push and pull between using space or time to solve our problems. So to solve this problem of testing for primality quickly using a small amount of space, and a small amount of time, we are going to have to approach it in an entirely new way.
