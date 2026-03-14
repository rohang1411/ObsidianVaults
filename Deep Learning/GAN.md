
Generates new data by learning from some data/distribution that follows the same distribution.

Discriminative models - Draw boundaries _between_ classes
Generative models - Learn the geometry/distribution of the data manifold itself

#### Architecture

![[Pasted image 20260307181831.png]]
Source - [[GAN#References#1. GAN Part 1 (Ahlad Kumar)|Ref 1 - GAN]]




#### Working

Goal of Generator - The goal is to learn $P_{model}(X) \approx P_{data}(X)$


When Discriminator return 0.5 as output, this signifies that Generator is trained, as the Discriminator is not able to clearly classify real vs fake images


##### Training

We train the Discriminator and Generator one at a time


#### Loss Function

###### Discriminator 

![[Pasted image 20260307192622.png]]
Source - [[GAN#References#2. GAN Part 2 (Ahlad Kumar)|Ref 2 - GAN]]
Use this diagram for terminologies

Think intuitively that, our goal is to optimize Discriminator and Generator separately. To optimize discriminator, we want to make sure that it predicts y = 1 for a real sample and y = 0 for a fake sample. 

Let's say we use Binary Cross Entropy to optimize the models.

y' is the predicted value by discriminator
y is the actual label

![[Pasted image 20260307193102.png]]
Source - [[GAN#References#2. GAN Part 2 (Ahlad Kumar)|Ref 2 - GAN]]

###### Samples coming from the real data

Let's consider the real samples first. Now to calculate the loss, we'll take the difference of  the actual value and the predicted value by the discriminator. So in binary cross entropy we'll put in the values D(x) 

y' = D(x) (Predicted value of Real data by the discriminator)
y = 1

Putting the values in Binary Cross Entropy equation gives us -

![[Pasted image 20260307193309.png]]
Source - [[GAN#References#2. GAN Part 2 (Ahlad Kumar)|Ref 2 - GAN]]

We want our discriminator to correctly classify the real samples by outputting y = 1 i.e. D(x) = 1. so D(x) = 1 is the correct scenario we want to acheive.

Let's look at the graph of the loss term -

![[Pasted image 20260307195304.png|637]]
Source - [[GAN#References#2. GAN Part 2 (Ahlad Kumar)|Ref 2 - GAN]]

We only need to look at the y values between 0 and 1, because D(x) is a probability  output from the Discriminator and will always be between 0 and 1. Hence we only look at the graph between 0 and 1. Forget the rest.

We can see that 1 is the maximum value that the loss function can achieve. And that's the scenario we want.

Since, our goal is to predict D(x) = 1 for real samples, we see that the loss function has the maximum value at D(x) = 1. Therefore we want to maximize the loss function to get D(x) = 1.

This is a bit counter intuitive, as we normally minimize the loss and loss function, But read the above paragraph again to gain clarity.

###### Samples coming from the Generator

Now let's look at the samples coming from generator. The discriminator should return y = 0 for the fake data. So when calculating loss, we should compare the actual value/label of fake data i.e. 0 and the predicted value of fake data by the discriminator.

Here y' = D(G(z)) (Predicted value of Fake data by the discriminator)
y = 0

Putting the values in Binary Cross Entropy equation gives us -

![[Pasted image 20260307193354.png]]
Source - [[GAN#References#2. GAN Part 2 (Ahlad Kumar)|Ref 2 - GAN]]

We want our discriminator to correctly classify the fake samples by outputting y = 0 i.e. D(G(z)) = 0. so D(G(z))) = 0 is the correct scenario we want to achieve.

Let's look at the graph of the loss term - 

![[Pasted image 20260307200144.png]]
Source - [[GAN#References#2. GAN Part 2 (Ahlad Kumar)|Ref 2 - GAN]]

We only need to look at the y values between 0 and 1, because D(G(z)) is a probability output from the Discriminator and will always be between 0 and 1. Hence we only look at the graph between 0 and 1. Forget the rest.

We can see that 0 is the maximum value that the loss function can achieve. And that's the scenario we want.

Since, our goal is to predict D(G(z))) = 0 for fake samples, we see that the loss function has the maximum value at D(G(z)) = 0. Therefore we want to maximize the loss function to get D(G(z)) = 0.

This is a bit counter intuitive, as we normally minimize the loss and loss function, But read the above paragraph again to gain clarity.


Final Loss Function for Discriminator -

Combining both the loss terms for real and fake samples, we get -

![[Pasted image 20260307200621.png]]
Source - [[GAN#References#2. GAN Part 2 (Ahlad Kumar)|Ref 2 - GAN]]


###### Generator Loss Function

Objective of Generator - To generate fake data to b so perfect that discriminator outputs 1 for fake data i.e. the generator wants D(G(z)) = 1.

![[Pasted image 20260307200621.png]]
Source - [[GAN#References#2. GAN Part 2 (Ahlad Kumar)|Ref 2 - GAN]]

In above loss term, the first term is independent of generator but the 2nd terms depends on it. The generator wants to make D(G(z)) = 1, so putting the value of D(G(z)) the 2nd term of loss would make it 0. So the generator wants to make the 2nd loss term 0.

Since D(G(z)) is a probability value from the discriminator model, it will always be between 0 and 1. Let's look again at the graph of the loss term. We'll only consider the graph for y value between 0 and 1. Hence the graph becomes -

![[Pasted image 20260307200144.png]]
Source - [[GAN#References#2. GAN Part 2 (Ahlad Kumar)|Ref 2 - GAN]]

Since the generator wants D(G(z)) = 1, the value of the 2nd loss term would be -infinity. Hence generator's goal is to minimize the 2nd term of the loss function. as it will force the D(G(z)) to be 1.

So the loss function equation for the generator comes out to be -

![[Pasted image 20260307210545.png]]



Final Loss -

![[Pasted image 20260307210716.png]]
Source - [[GAN#References#2. GAN Part 2 (Ahlad Kumar)|Ref 2 - GAN]]


Now, these loss values are for a single input x from the real data and single input z from the fake data. To calculate the total loss, we have to consider all the possible input values. Hence, we add [[Pre-requisites#Expectation |expectation]] of variables into the above equation.

The final loss function equation becomes -

![[Pasted image 20260307210938.png]]
Source - [[GAN#References#3. GAN Part 3 (Ahlad Kumar)|Ref 3 - GAN]]






### Conditional GAN






#### References

###### 1. GAN Part 1 (Ahlad Kumar)

```embed
title: "Deep Learning 27: (1) Generative Adversarial Network (GAN): Introduction and Back-Propagation"
image: "https://i.ytimg.com/vi/RRTuumxm3CE/hqdefault.jpg"
description: "In this lecture introduction to generative adversarial networks (GANs) is carried out in detail. The primary focus of this lecture is on  working and back-pr..."
url: "https://youtu.be/RRTuumxm3CE?list=PLdxQ7SoCLQAMGgQAIAcyRevM8VvygTpCu"
favicon: "https://www.youtube.com/s/desktop/ab5c3a01/img/favicon_32x32.png"
aspectRatio: "75"
```


###### 2. GAN Part 2 (Ahlad Kumar)
```embed
title: "Deep Learning 28: (2) Generative Adversarial Network (GAN) : Loss Derivation from Scratch"
image: "https://i.ytimg.com/vi/ZD7HtL1gook/hqdefault.jpg"
description: "This lecture derives the loss function of Generative Adversarial Network (GAN) from scratch#adversarial#generative#deeplearning"
url: "https://youtu.be/ZD7HtL1gook?list=PLdxQ7SoCLQAMGgQAIAcyRevM8VvygTpCu"
favicon: "https://www.youtube.com/s/desktop/ab5c3a01/img/favicon_32x32.png"
aspectRatio: "75"
```


###### 3. GAN Part 3 (Ahlad Kumar)
```embed
title: "Deep Learning 29: (3) Generative Adversarial Network (GAN) : Explanation of Loss Function"
image: "https://i.ytimg.com/vi/pPlnx9D8WZQ/maxresdefault.jpg"
description: "In this lecture we will gain more insights into the Loss function of Generative Adversarial Networks#adversarial#generative#deeplearning"
url: "https://youtu.be/pPlnx9D8WZQ?list=PLdxQ7SoCLQAMGgQAIAcyRevM8VvygTpCu"
favicon: "https://www.youtube.com/s/desktop/ab5c3a01/img/favicon_32x32.png"
aspectRatio: "56.25"
```


###### 4. GAN Part 4 (Ahlad Kumar)