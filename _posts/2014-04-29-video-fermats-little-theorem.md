---
layout: post
title: Video - Fermats Little Theorem
description: Video - Fermats Little Theorem
author: Brit Cruise
authorurl: /brit-cruise/
published: true
---

<p>Introduction to a key result in elementary number theory using a visualization with beads. Created by Brit Cruise.</p>

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/OoQ16YCYksw" frameborder="0" allowfullscreen></iframe></center>

<h2>TRANSCRIPT</h2>

Voiceover: Bob discovered something very interesting while making multicolored earrings out of beads for his store. Now, his customers like variety, so he decides to make every possible style for each size. Starting with size three, he begins by figuring out all possible styles. Each earring begins as a string of beads, and then the ends are attached to form a ring. 

So first, how many possible strings are there? With two colors and three beads, there are three choices, each from two colors. So two times two times two equals eight possible unique strings. And then he subtracts the strings which have only one color, or monocolored strings, since he's only building multicolored earrings. Then he glues them all together to form rings. 

He was assuming he would end up with six different earrings, but something happened. He could no longer tell the difference between most of them. It turns out he only has two styles, because each style is now part of a group with two identical partners. Notice you can always match them up based on rotations. So the size of these groups must be based on how many rotations it takes to return to the original. 

Or how many rotations to complete a cycle. So this means that the original set of all multicolored strings divides evenly into groups of size three. Now, would this be true for other sizes? That would be convenient, since he always wants the same amount of each style. So he tries this with four beads. 

First he builds all possible strings. With four beads he can choose from two colors for each bead, so two times two times two times two equals sixteen. Then he removes the two monocolored necklaces and attaches all of the others to form rings. 

Now, will they form equal sized groups? Apparently not. What happened? Notice how the initial set of strings divides into styles. If strings are of the same style, it means you can form one into the other simply by grabbing beads from one end and sticking them onto the other end. And there is one style which only has two members, and this is because it's built out of a repeating unit of length two. So only two rotations are required to complete a cycle. 

Therefore this group only contains two. He cannot split them into an equal number of styles. What about size five? Will they break into equal number of each style? Wait, suddenly he realizes he doesn't even need to build them in order to find out. It must work, since five cannot be made up of a repeating pattern, because five cannot be broken up into equal parts. It's a prime number. 

So no matter what kind of multicolored string you start with, it will always take five rotations, or bead swaps, to return to itself. The cycle length of every string must be five. Well let's check. First we'll build all possible strings and remove the two monocolored strings. Then we separate the strings into groups which belong to the same style, and build a single earring for each style. 

Notice that each earring rotates exactly five times to complete a cycle. Therefore, if we glued all the strings into rings, they must split into equal sized groups of five. But then he goes one step further. Currently he is only using two colors, but he realizes this must hold with any number of colors. 

Because any multicolored earring with a prime number of beads, P, must have a cycle length of P, since primes cannot be broken into equal sized units. But if a composite number of beads are used, such as six, we will always have certain strings with shorter cycle lengths, since it's actually built out of a repeating unit, and therefore will form smaller groups. 

And amazingly he just stumbled onto Fermat's Little Theorem. Given A colors and strings of length P, which are prime, the number of possible strings is A times A times A, P times, or A to the power of P. And when he removed the monocolored strings, he subtracts exactly A strings, since there are one for each color. This leaves him with A to the power of P minus A strings. 

And when he glues these strings together, they will fall into groups of size P, since each earring must have a cycle length of P. Therefore, P divides A to the power of P minus A. And that's it. We can express this statement in modular arithmetic too. Think of it, if you divide A to the power of P by P, you will be left with a remainder of A. 

So we can write this as A to the power of P is congruent to A mod P. And here we have stumbled onto one of the fundamentals results in number theory merely by playing with beads.
