
#### Probability Basics

p(x) - probability of a random variable x
p(x | y) - probability of random variable x provided y has happened. Also called Conditional Probability

p(x) and p(x | y) can be very different because of y's occurrence

##### Bayes' Theorem -

p(y | x) = p(x | y) p(y) / p(x)        (1)

Here,
p(y | x) -> Posterior Probability
p(y) -> Prior Probability
p(x | y) / p(x) -> Likelihood Ratio

p(x | y) p(y) can  be written as p(x, y) ---> This is called **Joint Distribution**

###### What does joint distribution signify?
**Joint distribution** signifies the probability distribution of two or more random variables considered simultaneously.  It quantifies the likelihood of specific combinations of outcomes occurring together, capturing the relationship and dependencies between the variables. For example, it can describe the probability of rolling a 3 on one die and a 5 on another, or the joint likelihood of a person having a certain height and IQ score.

###### Difference between Joint Distribution and Conditional Distribution
The **joint distribution** gives the probability that two or more random variables take specific values _together_—for example, $ P(X = x, Y = y) $.  It describes the likelihood of simultaneous events.

In contrast, the **conditional distribution** gives the probability of one event occurring _given_ that another has already occurred—expressed as $ P(X = x \mid Y = y) $.  It reflects how knowledge of one variable updates the probability of the other.

Putting this in above Formula

p(y|x) = p(x, y) / p(x) = Joint Distribution / p(x)



![[Pasted image 20260307121041.png]]
Source - [[Pre-requisites#References -#1. Variational Auto Encoder | Ref 1 - Variational Auto Encoder]]

##### Theorem of Total Probability

Let y1, y2 .... yn be a set of mutually exclusive events (i.e. yi Intersection yj = 0) & event X iss the union of N mutually exclusive events, then 

P(x) = Sigma(1 - n) P(X | yi) P(yi)                             (2)

If we substitute 2 in 1, we get 

p(y|x) = p(x|y) p(y) /  Sigma(1 - n) P(X | yi) P(yi)


##### Expectation

E(x) - Expectation of random variable x is a weighted average of the possible values that x can take. Each value is weighted according to the probability of it.

E(x) = sigma(1-k) xi P(x = xi)

E<sub>p</sub>(x) ~ x has probability density function given as p



##### K-L Divergence

Measure of how a probability distribution is different from another one 

![[Pasted image 20260307131807.png]]
Source - [[Pre-requisites#References -#2. Variational Auto Encoder Part 2 (Ahlad Kumar) | Ref 2 - Variational Auto Encoder]]

D<sub>KL</sub> = (P || Q)  ---> Sigma(x) P(X = x) * log(p(X = x) / Q(X = x)

![[Pasted image 20260307134803.png]]
Source - [[Pre-requisites#References -#2. Variational Auto Encoder Part 2 (Ahlad Kumar) | Ref 2 - Variational Auto Encoder]]

Where, 
P(X=x) = Summation of all the values the variable will take


###### Properties of KL Divergence

![[Pasted image 20260307135035.png]]
Source - [[Pre-requisites#References -#2. Variational Auto Encoder Part 2 (Ahlad Kumar) | Ref 2 - Variational Auto Encoder]]






#### References -

###### 1. Variational Auto Encoder Part 1 (Ahlad Kumar)
```embed
title: "Deep Learning 19: (1) Variational AutoEncoder : Introduction and Probability Refresher"
image: "https://i.ytimg.com/vi/w8F7_rQZxXk/maxresdefault.jpg"
description: "Today we will start a mini-lecture series on Variational Auto-Encoders. It is divided into six lectures. This is the first lecture that discusses the archite..."
url: "https://youtu.be/w8F7_rQZxXk?list=PLdxQ7SoCLQANizknbIiHzL_hYjEaI-wUe"
favicon: "https://www.youtube.com/s/desktop/ab5c3a01/img/favicon_32x32.png"
aspectRatio: "56.25"
```

###### 2. Variational Auto Encoder Part 2 (Ahlad Kumar)
```embed
title: "Deep Learning 20: (2) Variational AutoEncoder : Explaining KL (Kullback-Leibler) Divergence"
image: "https://i.ytimg.com/vi/wdKYveLIxgU/maxresdefault.jpg"
description: "Its a part of mini lecture series on Variational Auto-Encoders which is divided into six lectures. This is the second lecture  that discuss the detail deriva..."
url: "https://youtu.be/wdKYveLIxgU?list=PLdxQ7SoCLQANizknbIiHzL_hYjEaI-wUe"
favicon: "https://www.youtube.com/s/desktop/ab5c3a01/img/favicon_32x32.png"
aspectRatio: "56.25"
```

2. sdbsb
3. sdbs