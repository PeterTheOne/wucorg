---
layout: post
title: Video - Algorithmic Efficiency
description: Video - Algorithmic Efficiency
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>How can we improve the speed of a (deterministic) primality test? Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/oYUzKAfrx0w" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

I have a report now that they are sending a new rover to Mars. We are responsible for doing one thing which is programing the algorithm inside the rover which checks if numbers are prime. Let's say our rover is communicating using RSA. It needs an algorithm inside that can do a primality test. 

When you design a rover or anything to go in to space you have to be very efficient in every way. The components used have to be very light. The amount of power every subsystem uses has to be minimal. You have to be saving energy and mass at every point in the design process. We have our work cut out for us. We have to be able to deal with numbers up to this size. It has to do it very fast. 

If we give it a very small input, let's say just 90, it should be able to calculate that almost as fast as this entire number. As the input grows, we don't want to see any of this noticeable slow down. I want to analyze the user questions or the ideas users have which were really good from a mathematical standpoint. We are checking if N is prime or composite. Given some number N, think of this space of all possible Ns. 

If N is 100, this space is two to 100. What our algorithm is doing is searching this space. Think of algorithm searching a space. At each point it is asking- Think of it as a step, a primitive step. It is asking a question and it's actually a composite test, the question. 

Say this is a number A, we would say in the trial division method "is N divided by A?" We just try this, we drop A here and we try N divides A and we see if the remainder is zero, which means A is a divisor of N, we say "Ah, we know 100 percent-" We raise the flag and know 100 percent sure it's composite. Otherwise, at each step, we aren't quite sure. It might be prime but we're not sure. 

We continue searching until we hit the end. Remember our wall in this case was at the square root of N. Worst case situation occurs when N is prime, we search all the way to the square root of N and then we can say "Ah, it is prime "and we are 100 percent sure." In the case where N is even the multiple of two primes, seven times seven equals 49 if we throw 49 into our algorithm, the worst case occurs. 

We go all the way to the square root of N. The first set of questions, for example TheFourthDimension asks "Once we rule out two "as not divisible, then all multiples of two could be "ruled out, the same for three, four, five, et cetera." That's a really great point. Our old algorithm was stepping along one at a time. We could be using patterns we know about composite numbers, such as we know for sure that if a number is divisible by two then it's composite. 

If it is greater than two, so two is a prime. Then we can say four is composite. I missed five here, sorry about that. Four, six, eight, 10, and instead we can step like this. Three, five, seven, nine. One category of questions all try to reduce this space. If we eliminate all the even numbers, now the check space, instead of being up to the square root of N is the square root of N divided by two. 

We can find other patterns in composite numbers to try to make this even smaller. The other type of question concerns the case where we find a composite witness. That is, we find an A that allows us to say "Oh, we know N is composite." Lola said "Wouldn't leaving the loop "as soon as primeCheck equals false cut down "on some of the time?" Yes, that is totally correct and is something we want to do. 

As soon as we are searching along using some step defined by whatever pattern we are using, we find a composite witness. That means it passes our test and we say 100 percent confidence we should halt early. We stop and say "Oh, we're done. We won't continue searching." This halting early is great except it doesn't help us in the worst case, which is if N is prime then the early halting wont help us. 

Now, we can visualize how these improvements allow us to reduce the space thus preventing as many checks happening inside the computer which, depending on our computer, will reduce the amount of time it takes. Now I can show you the visualization I set up below which allows us to compare two algorithms based on how many steps occur during their execution. 

On the left is algorithm A, which is trial division which checks from two to the square root on N. On the right is algorithm B, which is let's say our improved algorithm. In this case, I have applied the check if it's divisible by two so we only do half as many steps. I also terminate early in this algorithm B. It's not perfect, I just applied a few user modifications so we can see what happens. 

Now, I am going to play with this to show you it. Here we can see as I scroll, we see algorithm A. We have the output, whether it is composite or prime. At the bottom you'll see the number of steps. The first thing to notice is on the right hand side every other number takes only one step. We know why that is. If it is an even number such as this, it will quit. Our old algorithm took 314 steps. 

Our new algorithm only took one step because it checks if it is divisible by two. That seems like a really nice optimization. However, as we build our input, you'll notice the steps increase and the bar grows and turns red once we approach the region where we are going to crash. This red line up here is step limit. If your bar hits there, we fail, which means our rover would break. 

In this case, the browser will actually crash. I'll try to get close to it. I am close to it now and it's running very slow. I can feel that my browser is just about to crash and give me the circle of death. Notice the improved algorithm took only two steps in that case, but remember the worst case. I am going to- I have a few large prime numbers saved here for example. We have to be able to handle any case. 

We don't know what we are throwing at our algorithm. If I throw a large prime at it, look what happens. Algorithm B, as we know, is taking half as many steps in the worst case but it is still taking many steps here because it is the worst case, right. We are getting close to crashing here, and this is not a very long prime. We are still way under 15 digits. When I put this 12 digit prime into our algorithm let's see what happens. 

It's lagging, it's going to crash. Look what happened, both algorithms went way overboard. It didn't work. Our improvement algorithm is not good enough yet. But, now we have an understanding of what we are trying to improve which is number of steps in the worst case. 

We also have this cool tool which allows us to visualize how fast it is growing, how fast the number of steps grows as our input grows. Below, I'll explain how I set this up so you can set up your algorithm and compare it with the base case and see how much better you can do.
