---
layout: post
title: Video - Randomized Algorithms Intro
description: Video - Randomized Algorithms Intro
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>How could random numbers speed up a decision algorithm? Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/WGMn16TDTjE" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

Voiceover: I have an update. NASA has said that there will be a hardware random number generator on the Rover that we have access to. After that, they made one more comment, they reminded me that we just need our algorithm to work in practice. For something to work in practice, it means that there's always some possibility of error, but perhaps the possibility is so small that we ignore it in practice, and if this sound crazy, just realize that in the physical world nothing is every certain, there is always chances for error. 

For example, chip packaging contains small amounts of radioactive contaminants, and when these decay, they release alpha particles which can actually flip bits in memory, and perhaps change a number unexpectedly. Even more interesting, cosmic rays can also cause soft errors, we can never remove the chance of error completely. I asked NASA exactly what error probability is acceptable. 

They said, "We just need to make sure that "the probabilty of error, for a given trial, "is less than the odds of "hitting the lottery twice in a row." The odds of hitting the lottery, say 649 twice in a row, is six times ten to the negative fourteen, so let's just be safe and round it down and say our error probability is ten to the minus fifteen. Safe enough; we will not expect to see an error, and it could run hundreds or thousands of times. 

Now my question is would access to randomness help us speed up a decision algorithm such as this primality test? This is a deep question, so let's step back and look at the big picture. Given some collection of integers from one to some limit N say, let's think of it as our universe of integers. We can always divide a collection into two sets. A decision problem can actually be thought of as a partician into two sets. 

For example, provided some N is N less than 100, it will output yes for all integers less than 100. Here is one collection, and no for all others, which is another collection. Okay, so let's now focus on recognizing primes with the decision. Ideally, what we would like is some simply computed criteria that all primes satisfy and no composites satisfy. Now if we knew some simple pattern which describes the location of all primes, and only primes, then given some number N we could simply check if N follows that pattern. 

The problem is that so far no exaustive and simply computed pattern has been found for all primes and no composites, or all composites and no primes. But we do know fast tests for most composite numbers. For example, a simply computed criteria would be a test for evenness, and all even numbers are divisible by two. It's fast because we can tell if something's even by just looking at the last digit, and even as N grows, the problem doesn't get any harder, we just look at that last digit also known as the low order bit. 

Now realize that we can use this evenness test as a low quality composite test. In that we could have some algorithm accept our integer N, and all our algorithm does is check if it's even. If it is even, and greater than two, then we know with 100 percent certainty it is composite because we have proof. Think of two as our composite witness. However if not, then we aren't exactly sure. If it's odd it could be prime since all primes are odd, or it could be one of the many composites which are odds, just nine or fifteen. 

This massive region of odd composites makes for an unacceptable test. Now to be clear, let's draw this. Provided some N, N can be either prime or composite. If N is prime, our algorithm will say prime 100 percent of the time since no primes are even that are greater than two. It will never say composite when a prime is provided. However, if N is composite, our algorithm will say composite about fifty percent of the time, and prime fifty percent of the time. 

This means that if our algorithm outputs composite, it means it found proof of composite witness. However, for our algorithm outputs prime, we know there is an unacceptably large chance of error. Until now, our strategy has dealt with this large, unacceptably large error, by iteration and let's draw the flow of our machine. Given some N, our machine does a series of divisibility tests starting at A is two. It asks does A divide N. If it doesn't divide N, then we can eliminate all of this region. 

Then it asks the next question, does N divide three? If not, then we eliminate that whole section. Does N divide five, seven, and so on. Notice these are disjoint sets which gradually fill up all possible composites. Now if we ever answer yes along the way, then we have proof that N is composite. A, whatever it is at that point, is our witness. We halt N output composite from our algorithm. 

Otherwise, we continue trying until we exhaust all possible composites. Until we hit the square root of N since we know, remember ever composite number N must have a factor less than or equal to the square root of N. This really leads to the final question in our algorithm. If no witnesses are found, and A is greater than the square root of N, then we suddenly have proof and we halt an output prime. 

Realize we have two exit paths through our algorithm. Both paths represent proof of certainty that N is either prime or composite. When N is prime, we try all possible divisors and we basically rule them all out, and that is our proof that N is prime. The problem with this strategy is that our test value A at minimum requires us to cycle through every prime starting from two to the square root of N. 

As N grows, the number of primes grow with it. It results in too many iterations in the worst case such as when we provide a prime to our algorithm. Looking at the big picture now, realize it's providing proof when N is prime. Which we now know we don't exactly need. No one said we needed to prove it. We just needed to be 99.9999 fifteen nine's percent certain. Hmm, so we actually need to think about the composite test that's being used in our algorithm. 

Remember, our fastest trial division primality tests thus far have tried to use prime pattern such as 6K, or all primes are of the form 6K plus or minus one, to help walk along the primes only and eliminate many of the composites to save time. Remember, a test like this can be turned into a composite test. 

That is, given some integer N is of the form 6K plus or minus one, then we can say it's probably prime, but there are many composites still which follow this pattern. It doesn't include primes only, just all primes and some composites, and we can think of these extra composites as a leak and this leak is our source of error. 

Now if we invert it and ask is N not of the form 6K plus or minus one, then we can say with 100 percent certainty it is composite, so the leak is our source of error on the prime side, but in this case it's unacceptable it's not a non-negligible error. There's a much larger probabilty. 

We need to define a new composite testing procedure which is able to shrink this space and make the chance of error negligible. Which means we'll need to review how we can actually shrink errors with iterations. I think we should now post our ideas below regarding what kind of tests might we want to perform and also more importantly how could a random number generator really help us?
