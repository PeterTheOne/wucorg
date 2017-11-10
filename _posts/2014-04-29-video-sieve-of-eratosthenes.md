---
layout: post
title: Video - Sieve of Eratosthenes
description: Video - Sieve of Eratosthenes
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>Sieve of Eratosthenes allows us to generate a list of primes. Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/klcIklsWzrY" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

I'm now going to introduce an ancient method for generating a list of primes up to some limit N, called the Sieve of Erathosthenes. Now Erathosthenes was born in 276 BC. So this method was over 2200 years old. But it's very simple and elegant and you can teach it to any child. 

Now let's say for example we want to calculate all the primes up to 100, this would work in the same way if we wanted to calculate up to 10,000 or a billion. Proceeds as follows, assume all numbers are unmarked, grey is unmarked. We start at the beginning and if we find a number that is unmarked we know it's prime. So we hit two and we say two is primed because it's unmarked. 

And then the second phase is now we can eliminate all multiples of two because we know their composite. So bam, we jump along and we eliminate all multiples of two, red means composite. And now we repeat. We step along from two to three. Three is unmarked so we mark three as prime. And now we can eliminate all multiples of three. 

And a really simple optimization is, notice six is already crossed off, we actually cross off the multiples starting at the square of that number. So three times three is nine. We start at nine and mark all multiples of three as composite. And then again we go back, we jump along to four. Well four is marked, we know it's composite. We jump along to five, we find an unmarked number, five is prime. 

Now five times five is 25, we go to 25. We mark off 25, 30, 35, 40, 45, and so on. Those are composites. We proceed forward until we hit seven, we know seven is prime because it's unmarked. Seven times seven is 49, we mark 49 and all multiples of seven above it as composite. Now we move along until we hit 11, 11 is prime. Notice now, 11 times 11 is greater than 100, so we can actually stop at this point. 

We could have stopped at 10 even, because now all remaining unmarked numbers, if you'll notice, are prime. And in one swoop we can mark them all as prime. And that's the whole algorithm, it's so simple. And just to generalize how we do this, so we could write up a program to perform this sieve, is if we want to find all the primes up to some number N, we first create a main loop. 

So we have four all numbers A, from two to the square root of N. So notice here, we stopped when we hit 10, I showed it as 11, we actually stop because we have found all primes. So from two to the square root of N, we proceed as follows: If A is unmarked, then we know A is prime and when we find a prime number we mark all multiples of A off it's composite and that's it. 

So, you find a number prime, mark of the multiples, go back to the beginning, increment A by one. So we're at two then we go to three then we go to four, five and so on, and when we're done, we have all primes. Notice here that this is also a loop. So we have a main loop for when we find a prime. 

This marking off of multiples is also a loop. So it's important to notice here that we have a nested loop, we have a loop inside a loop. Here is an example of this logarithm in action, I wrote in JavaScript below. If I put in 100, here are all the primes under 100. And if I put in 200, here are all the primes under 200. And if I put in 700, here are all the primes under 700. And below I have this program with a recording explaining how I set it up.
