---
layout: post
title: Video - Conditional Probability Explained Visually
description: Video - Conditional Probability Explained Visually
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>This is an explanation of conditional probability. Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/KqCKZwh5WY8" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

Consider the following story. Bob is in a room and he has two coins. One fair coin and one double sided coin. He picks one at random, flips it, and shouts the result. - [Bob] Heads. - [Instructor] Now what is the probability that he flipped the fair coin? 

To answer this question, we need only rewind and grow a tree. The first event, he picks one of two coins, so our tree grows two branches, leading to equally likely outcomes, fair or unfair. The next event, he flips the coin. We grow again, if he had the fair coin, we know this flip can result in two equally likely outcomes, heads and tails, while the unfair coin results in two outcomes, both heads. 

Our tree is finished, and we see it has four leaves, representing four equally likely outcomes. The final step, new evidence, he says. - [Bob] Heads. - [Instructor] Whenever we gain evidence, we must trim our tree. We cut any branch leading to tails because we know tails did not occur, and that is it, so the probability that he chose the fair coin is the one fair outcome leading to heads divided by the three possible outcomes leading to heads, or one third. 

What happens if he flips again and reports? - [Bob] Heads. - [Instructor] Remember, after each event, our tree grows. The fair coin leaves result in two equally likely outcomes, heads and tails, the unfair coin leaves result in two equally likely outcomes, heads and heads. After we hear the second. - [Bob] Heads. - [Instructor] We cut any branches leading to tails. 

Therefore the probability the coin is fair after two heads in a row, is the one fair outcome leading to heads divided by all possible outcome leading to heads, or one fifth. Notice our confidence in the fair coin is dropping as more heads occur, though realize that we'll never reach zero. No matter how many flips occur, we can never be 100% certain the coin is unfair. 

In fact, all conditional probability questions can be solved by growing trees. Let's do one more to be sure. Bob has three coins, two are fair, one is biased, which is weighted to land heads two thirds of the time and tails one third. He chooses a coin at random and flips it. - [Bob] Heads. - [Instructor] Now what is the probability he chose the biased coin? Let's rewind and build a tree. 

The first event, choosing the coin, can lead to three equally likely outcomes, fair coin, fair coin, and unfair coin. The next event, the coin is flipped. Each fair coin leads to two equally likely leaves, heads and tails. The biased coin leads to three equally likely leaves, two representing heads, and one representing tails. Now the trick is to always make sure our tree is balanced, meaning an equal amount of leaves growing out of each branch. 

To do this, we simply scale up the number of branches to the least common multiple. For two and three, this is six. And finally, we label our leaves. The fair coin now splits into six equally likely leaves, three heads and three tails. For the biased coin, we now have two tail leaves and four head leaves, and that is it. 

When Bob shouts the result. - [Bob] Heads. - [Instructor] This new evidence allows us to trim all branches leading to tails since tails did not occur, so the probability that he chose the biased coin given heads occurred, well four leaves can come from the biased coin divided by all possible leaves. 

Four divided by 10, or 40%. When it doubt, it's always possible to answer conditional probability questions by Bayes Theorem, it tells us the probability of event A given some new evidence B, though if you forgot it, no worries. You need only how to grow stories with trimmed trees.
