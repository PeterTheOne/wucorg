---
layout: post
title: Video - Perfect Secrecy
description: Video - Perfect Secrecy
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>Claude Shannon's idea of perfect secrecy: no amount of computational power can help improve your ability to break the one-time pad. Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/vKRMWewGE9A" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

Consider the following game. Eve instructs Bob to go into a room. (door creaks shut) Bob finds the room empty, except for some locks, an empty box, and a single deck of cards. Eve tells Bob to select a card from the deck and hide it as best he can. 

The rules are simple. Bob cannot leave the room with anything, cards and keys all stay in the room, and he can put, at most, one card in the box. Eve agrees that she has never seen the locks. He wins the game if Eve is unable to determine his card. 

So what is his best strategy? Well, Bob selected a card, six of diamonds, and threw it in the box. (box clicks shut) First he considered the different types of locks. Maybe he should lock the card in the box with the key. Though, she could pick locks, so he considers the combination lock. 

The key is on the back, so if he locks it and scratches it off, it seems like the best choice. But suddenly he realizes the problem. The remaining cards on the table leak information about his choice, since it's now missing from the deck. The locks are a decoy. (metal jangles) 

He shouldn't separate his card from the deck. He returns his card to the deck but can't remember the position of his card. So he shuffles the deck to randomize it. Shuffling is the best lock, because it leaves no information about his choice. His card is now equally likely to be any card in the deck. 

He can now leave the cards openly, in confidence. Bob wins the game, because the best Eve can do is simply guess, as he has left no information about his choice. Most importantly, even if we give Eve unlimited computational power, she can't do any better than a guess. 

This defines what we call "perfect secrecy." On September first, 1945, 29-year-old Claude Shannon published a classified paper on this idea. Shannon gave the first mathematical proof for how and why the one time pad is perfectly secret. Shannon thinks about encryption schemes in the following way. 

Imagine Alice writes a message to Bob, 20 letters long. (paper ruffling) This is equivalent to picking one specific page from the message space. The message space can be thought of as a complete collection of all possible 20 letter messages. (paper ruffling) Anything you can think of that's 20 letters long is a page in this stack. 

Next, Alice applies a shared key, which is a list of 20 randomly generated shifts between one and 26. The key space is the complete collection of all possible outcomes, so generating a key is equivalent to selecting a page from this stack at random. 

When she applies the shift to encrypt the message, she ends up with a cipher text. The cipher text space represents all possible results of an encryption. When she applies the key, it maps to a unique page in this stack. Notice that the size of the message space equals the size of the key space equals the size of the cipher text space. 

This defines what we call "perfect secrecy," for if someone has access to a page of cipher text only, the only thing that they know is that every message is equally likely. So no amount of computational power could ever help improve a blind guess. 

Now the big problem, you're wondering, with the time pad, is we have to share these long keys in advance. To solve this problem, we need to relax our definition of secrecy by developing a definition of pseudo-randomness.
