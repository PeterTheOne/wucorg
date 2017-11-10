---
layout: post
title: Video - Fermat Primality Test
description: Video - Fermat Primality Test
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>A quick outline of how & why it works. Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/xMj3jzFDZ38" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

Our goal is to define a series of instructions which can prove whether some input integer is composite -- or else identify it as prime -- with some very high degree of accuracy, which we can define. And it must be efficient to do so, meaning it should be fast to calculate on any machine, and even if the input size grows -- which is our input integer n -- it should still be fast. 

And so far, we've learned that, at the lowest level, this requires some known pattern that all primes follow and very few composites follow. However, in the previous video, we did a visual demonstration of Fermat's little theorem. And it provides us with a very interesting rule. Given some prime number, 'p,' and some other integer 'a,' which is just less than p, we know, now, that p divides a to the power of p minus a. 

We write this as a^p = a mod p. And that's the way you normally see it. Now because a and p share no common factors -- since p is a prime -- we can use the cancellation law -- and you'll sometimes see this written as a^(p -1) = 1 mod p. And remember, we can only do this because the greatest common divisor of a and p equals 1. And here, I've just set up a demo, so we can, at first, just see this equation in action, and get comfortable with it. 

Notice now, if I input prime for p, the output is always 1, no matter what a I choose. If we input a composite number for P, we see that it usually isn't 1. And any time this equation outputs something that isn't 1, we have a 'composite witness.' This is now proof that the p we chose cannot be prime. And that's the essence of this test. And before going any deeper, let's just step back and construct the framework for this test, using this pattern I just showed you. 

So our test [states] we are provided with some integer -- let's call it 'p' -- as input. Next, we generate a random integer, 'a,' which is less than p. And now we can ask, "Is the greatest common divisor of a and p 1?" If not -- if the greatest common divisor of a and p is greater than 1, then they share a common factor, and we've proven that p is composite -- because a factor exists. 

And we can halt and exit. And our algorithm will output 'composite.' However, if 'yes,' and we can ask the key question, "Does a to the power of p minus 1 mod p equal 1?" If not, we have a witness that p is composite. We can halt and say, "Yeah. We're done. p is composite." Otherwise, if 'yes' -- if our equation outputs 1 -- then it should be prime, right? I coded up this series of instructions and on the left-hand side we have Fermat's test, and on the right, I just have it in existing trial division test. 

And that's there because we know that that test is always correct. And, just at first glance, it seems like it's working. However, I found a problem. I hit the number 511, and now the Fermat's test is saying it's prime, and the trial division test is telling me that it's composite. 511 seems prime from the test's perspective. But it's not. Now let's just return back to our equation, and see what happened. 

Well, this is an example of what we call a 'pseudo-prime.' It's a composite number. But there are certain a's we can choose that <i>will</i> output a 1. That's incorrect again. So these a's which result in a composite number -- outputting a 1-- we can call 'fools.' Because they're fooling us into thinking the number is prime. But notice that if we choose different a's, we seem to find many composite witnesses instead of fools. So, we could maybe just step back. And let's apply the same logic we used in the divisibility test, where we simply repeat the experiment a few times, and generate a new random a each time. 

And hopefully, we won't pick a fool each time. Now it's been proven that the number of fools must divide the total size of the group we select from. Which means, at most, half of the choices or half of the elements in this pool, could be fools. So, since a is chosen randomly, the chance of finding a composite witness -- which is what we want -- is at least one half. After t iterations, the probability that no witness will be found with a composite number is at most 1/(2^t). 

So after 20 trials, the probability of mistakenly outputting a prime is just over one in a million. So that's the case we just keep getting really unlucky in generating random a's. And every time, we choose a fool. If you can let that sink in, that's really powerful to understand. And here now, we can see our test in action, with the increased number of trials, it seems to be working perfectly. 

And, notice that in the worst case -- which we know is when we provide our algorithm with a prime -- it's going to do the maximum amount of work. The Fermat test is much more efficient then trial division -- especially because the number of steps doesn't scale with the input. And that's a key distinction. 

We set the number of trials, and that's it. We never have to worry about our algorithm running millions and millions of iterations as we did before. So, I mean, this is quintessentially applied math. We are taking a pattern someone discovered, and we're saving an immense amount of computational cycles. However, there is one tiny flaw -- or error -- in this system. Can you find it?
