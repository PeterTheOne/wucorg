---
layout: post
title: Video - The Prime Number Theorem
description: Video - The Prime Number Theorem
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>How can we estimate the number of primes up to x? Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/7jzCJJIc59E" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

Voiceover: Imagine we listed all integers in a growing spiral, and colored the prime numbers blue, and left the composite numbers black. One interesting question we may ask is, "How many primes are there compared to composites?" First, let's zoom out to see the big picture. Notice the prime color is dense in the center, and slowly drops off in the distance but never seems to end. 

One way I like to think about this is as follows: Imagine there is a tree at the center which is infinitely high. The leaves which drop from this tree represent prime numbers, which are scattered unpredictably below, dense near the base of the tree, and as we walk away from this tree, we find fewer leaves, though we always find them. This is exactly what happens when we look at larger and larger integers. 

We always find more primes, though the number of primes we find gradually drops, the further we look. So let's return to our question. How many primes are there less than some integer x? If we make a table, we see the number of primes is always increasing. Though as we search further, we find fewer and fewer. Let's graph the number of primes found on the vertical axis, and the search size x on the horizontal. As we zoom out to include billions of numbers, notice the curve never flat lines. It's always rising, albeit gradually. 

First, let's think about the density of primes less than some integer x. We can find the density by dividing the number of primes found by the search size. For the first 100 integers, we find 25 primes, therefore 25% are prime. Of the first 1000 integers, we find 1229 primes, 12.29% are prime. Of the first 1 million integers, 7.84% are prime. And the first 100 million integers contain 5.76% prime. 

As we search further, this density continues to drop, though the speed at which it drops slows down. Here is a graph of the search size on the horizontal axis and the prime density on the vertical. Notice that as we zoom out, the primes are a vanishing proportion of all integers. Amazingly, we find this formula in nature. We see it in galaxies, storms, flowers, and even inside our bodies as the design of least resistance, known as the logarithmic spiral. Notice that as the spiral rotates, it gets further and further away from the center. 

Incredibly, the rotation rate of a logarithmic spiral is related to the density of primes as follows: We have the number of rotations, call this phi. and the distance from the center, call this r. If we graph phi against r, and zoom out, we see they are related according to the natural logarithm. This means the natural logarithm of the distance is related to the number of rotations. The graph of the natural logarithm is commonly written using the variable names y and x as y equals the natural logarithm of x. 

Notice the graph tapers off in the same way the density of primes gradually decreases. The final step is to invert this by changing the y axis to 1 divided by the natural logarithm of x. And when we zoom out, we find the exact same curve generated when we plot the density of primes. Let's confirm this by overlapping the two plots. In green, is a graph of the line y equals 1 over the natural logarithm of x. 

And in red is the plot of prime number density up to x. As we zoom out, they approach each other. The further we zoom out, the more accurate the green estimate becomes. This is known as the asymptotic law of distribution of prime numbers. We now have a formula to accurately tell us the density of primes without counting. The density of primes up to some integer x is approximately 1 divided by the natural logarithm of x or lawn x. So let's say you need to know the density of primes between 1 and 100 trillion. Simple. 

1 divided by lawn of 100 trillion equals 3.1%. Compare this to the actual result from counting all primes which is 3.2%. This is off by 0.1%. And as we check larger and larger numbers, the difference approaches zero. Realize now that we can use this formula for prime density to estimate the number of primes up to x. The number of primes is the area under the density curve for which we can simplify by assuming density is constant. So number of primes equals size times density or x divided by lawn x. 

This is the prime number theorem. Here is a graph of y equals x divided by lawn x in blue, and in yellow, is a plot of an actual count of primes. Notice as we zoom out, these lines eventually overlap as we look to infinity. And that is it. We have a formula which tells us approximately how many primes there are up to any value, no counting needed. For example, let's say we need to know the number of primes less than 100 trillion. 

100 trillion divided by the natural log of 100 trillion equals 3.1 trillion. Compare this to the actual count, which is 3.2 trillion. This is over 99.99% accurate even at this relatively small scale. So to recap: Given a search size up to some integer x, the prime density is about 1 divided by lawn x And the number of primes is about x divided by lawn x. This is the prime number theorem.
