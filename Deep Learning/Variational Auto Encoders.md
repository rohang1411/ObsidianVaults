
Comes under unsupervised Deep Learning. The goal is to model the true data distribution $P_{data}(X)$ (Probability Distribution Function) rather than a conditional label boundary (class) $P(Y|X)$.


Discriminative models - Draw boundaries _between_ classes
Generative models - Learn the geometry/distribution of the data manifold itself


#### Auto Encoders

##### Use?
It is used to create a low dimensional representation of a higher dimensional input

Ex. Get a low res image of a higher res one
##### Autoencoder Architecture

![[Pasted image 20260307113751.png]]
Source - Source - [[Variational Auto Encoders#References#1. Variational Auto Encoder Part 1 (Ahlad Kumar)| Ref 1 - Variational Auto Encoder]]


Autoencoder generate the same thing from input sample space. Basically generate a copy of input.

##### Working -

The higher dimensional input is converted into a lower dimensional vector/variable. That low dimensional variable is called "Latent Variable". We call them latent variables because they are hidden variables. Then That latent variable is used by the Decoder to create a copy of the original input.

Autoencoder compresses data into a bottleneck to force the learning of high-yield semantic features (latent variable)


![[Pasted image 20260307141900.png]]
Source - [[Variational Auto Encoders#References#3. Variational Auto Encoder Part 3 (Ahlad Kumar) | Ref 3 - Variational Auto Encoder]]


##### Latent Variables

Also called Latent Attributes/ Hidden Attributes / Hidden Layer

![[Pasted image 20260307145957.png]]
Source - [[Variational Auto Encoders#References#3. Variational Auto Encoder Part 3 (Ahlad Kumar) | Ref 3 - Variational Auto Encoder]]



##### Problems?
Autoencoder assumes that the encoding given to the decoder are coming from the input space (source dataset / training data). And if we provide any other input from outside of the training dataset, then the decoder will generate a random output. 

Autoencoders have no idea if the vector we are passing to decoder is coming from the input dataset or outside?

Standard AEs are deterministic. The latent space $Z$ is highly discontinuous and unregularized. If you sample a random point in $Z$ that the encoder has never mapped training data to, the decoder will output complete garbage. To generate new data smoothly, we need the latent space to follow a continuous probability distribution.


##### Intuition -

**Intuition:** An Autoencoder is like a compression algorithm (like ZIP) built specifically for your dataset. The Encoder creates the ZIP file ($z$), and the Decoder extracts it ($\hat{x}$). However, if you write random binary code into a ZIP file and try to extract it, it corrupts. This is why AEs can't generate _new_ data.


##### Solution 
[[Variational Auto Encoders#Variational Auto Encoders | VAE]] tries to solve this problem. It attempts to make sure that these unknown encodings can be decoded to some reasonable output

Probability basics are required for the next section. Review [[Pre-requisites#Probability Basics | Probability Basics]]

#### Variational Auto Encoders

##### Goal? Why? Use?
These are used to generate some new sample from the given input. The output is not part of the original dataset. 

![[Pasted image 20260307141142.png]]
Source - [[Variational Auto Encoders#References#3. Variational Auto Encoder Part 3 (Ahlad Kumar) | Ref 3 - Variational Auto Encoder]]

##### How it solves the problem of Auto Encoders?
In Auto Encoders the encoder generates a single encoding value/vector for a particular input.
![[Pasted image 20260307143216.png]]

VAE has something called as probabilistic encoders and probabilistic decoders. It forces the encoder (probabilistic encoder) to create a probability distribution function over the input encodings instead of single vector.

![[Pasted image 20260307143229.png]]



##### Architecture

![[Pasted image 20260307140716.png]]
Source - [[Variational Auto Encoders#References#3. Variational Auto Encoder Part 3 (Ahlad Kumar) | Ref 3 - Variational Auto Encoder]]

##### Working -

###### Overall working

We calculate latent/hidden variables/features z from x (input) and then generate x' (new data) from z

![[Pasted image 20260307145221.png]]
Source - [[Variational Auto Encoders#References#3. Variational Auto Encoder Part 3 (Ahlad Kumar) | Ref 3 - Variational Auto Encoder]]

The goal is to learn/find a distribution $Q_\phi(Z|X)$ of some latent variables (z). Then we'll sample the values of z from the learnt distribution. Once done, we'll generate new samples of x' (new data, not from the input space), using $P_\theta(X|Z)$

The $Q_\phi(Z|X)$ distribution would be learnt by [[Backpropagation |backpropagation]].
Here $\phi$ and $\theta$ are the learnable parameters (weights & biases), learnt through [[Backpropagation |backpropagation]].

![[Pasted image 20260307152644.png]]
Source - [[Variational Auto Encoders#References#3. Variational Auto Encoder Part 3 (Ahlad Kumar) | Ref 3 - Variational Auto Encoder]]

The end goal is to create x', which is new data that belongs to the same family of x (input), or has similar probability distribution as x.

###### Creating the latent variables -

AE will create a fix value for the latent/hidden features while VAE will create a probability distribution

![[Pasted image 20260307150320.png]]
Source - [[Variational Auto Encoders#References#3. Variational Auto Encoder Part 3 (Ahlad Kumar) | Ref 3 - Variational Auto Encoder]]

Then we randomly sample from the generated probability distributions (basically, randomly send a part of the distribution) of latent variables and feed it to the decoder.

![[Pasted image 20260307151037.png]]
Source - [[Variational Auto Encoders#References#3. Variational Auto Encoder Part 3 (Ahlad Kumar) | Ref 3 - Variational Auto Encoder]]

In the below image we are giving different samples to thee decoder. The Green and Orange sample are closer to each other and hence generate de the pink sample to the decoder, would generate a very different image.

![[Pasted image 20260307151318.png]]
Source - [[Variational Auto Encoders#References#3. Variational Auto Encoder Part 3 (Ahlad Kumar) | Ref 3 - Variational Auto Encoder]]

###### Encoding Part -
x ---> z (Creating z from x) is done using p(z | x)

p(z | x) = Probability of z when x is given 

Instead of the encoder outputting a single vector $z$, the **Probabilistic Encoder** $Q_\phi(Z|X)$ outputs the _parameters_ of a distribution (a mean vector $\mu$ and variance vector $\sigma^2$).
Where $\phi$ are learnable parameters (weights & biases).

###### Decoding Part -
z ---> x (Creating x or x' from z) is done using p(x | z)

p(x | z) = Probability of x when z is given 

We then _sample_ $z \sim \mathcal{N}(\mu, \sigma^2)$ and pass it to the **Probabilistic Decoder** $P_\theta(X|Z)$ to reconstruct the image. Where $\theta$ are learnable parameters (weights & biases).



Encoders are also called - Recognition Models
Decoders are also called - Generative Models


##### Loss Function 

To find a loss function, we should know our end goal. And then take the decision on that whether to maximise or minimise.

End Goal - To make sure x' mimics the probability distribtuion of x.
In other words, we want to make sure that each point in x' is as close to each point in x. 

In terms of probability we can say that, we want to train our machine (adjust its internal weights) so that the probability of it generating our real, training data is as high as possible. This concept is called **Maximum Likelihood Estimation (MLE)**.

Since we have many images in out dataset, we have to multiply their individual probabilities together:

$$P(\text{total}) = P(x_1) \times P(x_2) \times P(x_3) \dots$$

Probabilities are fractions (like $0.01$). If you multiply thousands of fractions together ($0.01 \times 0.01 \times 0.01 \dots$), the number gets so microscopically small that a computer literally cannot comprehend it and rounds it to $0$. This is called "underflow."

To fix this, we take the **logarithm** of the probability. A magical property of logarithms is that they turn multiplication into addition:

$$\log(A \times B) = \log(A) + \log(B)$$

Now, our encoder wants to find the probability distribution of x. We represent it by $Q_\phi(Z|X)$.


We are given -
x -> a set of observed variables (input)

Let -
z -> set of latent variables having joint distribution p(z, x)

The goal is to find a conditional distribution p(z | x) given the observations x. This is what we want $Q_\phi(Z|X)$ (This is the PDF returned by our encoder neural network) to be.

Using Bayes' rule we can write $P(Z|X)$ (this is the actual PDF of input x that we want to find) as  as -

![[Pasted image 20260307160216.png]]
Source - [[Variational Auto Encoders#References#4. Variational Auto Encoder Part 4 (Ahlad Kumar)|Ref 4 - Variational Auto Encoder]]

Now we want to solve p(x) i.e. maximise p(x) for all the inputs in x. The integral of p(x) cannot be solved. Because p(x) can be written as below formulae

And integral of p(x | z) dz cannot be calculated in exponential time as we don't know the size of z (latent variable)

![[Pasted image 20260307160350.png]]
Source - [[Variational Auto Encoders#References#4. Variational Auto Encoder Part 4 (Ahlad Kumar)|Ref 4 - Variational Auto Encoder]]

Now since we can't compute the true distribution $P(z|x)$, we use our Encoder, $Q(z|x)$, to approximate it.

In below line don't confuse the p with the Decoder function variable (The decoder function p is p(x | z))

The approximation is done using Variational Inference.
![[Pasted image 20260307160832.png]]
Source - [[Variational Auto Encoders#References#4. Variational Auto Encoder Part 4 (Ahlad Kumar)|Ref 4 - Variational Auto Encoder]]

We'll calculate the KL Divergence between p(z | x) and q(z | x) to check if they are similar. If the difference between these 2 probabilities is nearly zero, we can say q(z | x) is an approximation of p(z | x)

**Step 1: The definition of KL Divergence**

$$D_{KL}(Q(z|x) || P(z|x)) = \mathbb{E}_{Q} [\log Q(z|x) - \log P(z|x)]$$

_Intuition:_ How much does our estimated distribution ($Q$) differ from the true distribution ($P$)? We want this difference to be as small as possible.

**Step 2: Apply Bayes' Theorem**

We can rewrite the true posterior $P(z|x)$ using Bayes' rule:

$$P(z|x) = \frac{P(x|z)P(z)}{P(x)}$$

**Step 3: Substitute and expand**

Plug Bayes' rule into our KL Divergence equation:

$$D_{KL}(Q(z|x) || P(z|x)) = \mathbb{E}_{Q} \left[\log Q(z|x) - \log \left(\frac{P(x|z)P(z)}{P(x)}\right)\right]$$

Using the logarithm rule $\log(a/b) = \log(a) - \log(b)$, we break it apart:

$$D_{KL} = \mathbb{E}_{Q} [\log Q(z|x) - \log P(x|z) - \log P(z) + \log P(x)]$$

**Step 4: Isolate our main goal, $\log P(x)$**

The term $\log P(x)$ does not depend on $z$. Because the expectation $\mathbb{E}_{Q}$ is taken over $z$, the expectation of a constant is just the constant itself. We can pull $\log P(x)$ out and rearrange the equation to solve for it:

$$\log P(x) - D_{KL}(Q(z|x) || P(z|x)) = \mathbb{E}_{Q} [\log P(x|z)] - \mathbb{E}_{Q} [\log Q(z|x) - \log P(z)]$$

**Step 5: Form the ELBO**

Look at the second part of the right side: $\mathbb{E}_{Q} [\log Q(z|x) - \log P(z)]$. This is exactly the definition of KL Divergence between $Q(z|x)$ and the prior $P(z)$. Let's substitute that back in:

$$\log P(x) - D_{KL}(Q(z|x) || P(z|x)) = \mathbb{E}_{Q} [\log P(x|z)] - D_{KL}(Q(z|x) || P(z))$$


Let's look at the full, un-shortened equation one more time, and group it very carefully with brackets.

$$ \log P(x) = \underbrace{\Big( \mathbb{E}_{Q} [\log P(x|z)] - D_{KL}(Q(z|x) || P(z)) \Big)}_{\text{The Table (ELBO)}} + \underbrace{D_{KL}(Q(z|x) || P(z|x))}_{\text{The Empty Space (Gap)}}$$

# IMP
**Now the goal is to maximise the ELBO term, as we know that the 2nd term is already positive. Hence the maximising the ELBO term is our loss function.**


Here is how all the pieces fit together without interfering with each other:

### 1. The "Empty Space" (The term that guarantees the limit)

Look at the very last term on the right: **$D_{KL}(Q(z|x) || P(z|x))$**.

Notice what it is measuring: the difference between our Encoder's guess $Q(z|x)$ and the _true, impossible-to-know_ blueprint distribution $P(z|x)$.

This term is the "empty space" between the table and the ceiling. Because it is a KL Divergence, it is a mathematical guarantee that **this specific term is always $\ge 0$**. It is the _only_ reason the rest of the equation acts as a lower limit.

Because KL Divergence is a measure of distance, it is _always_ greater than or equal to zero. Therefore, the right side of the equation acts as a lower limit for $\log P(x)$. This right side is called the **Evidence Lower Bound (ELBO)**.

Since we can't compute $P(z|x)$ directly, we instead focus on maximizing the ELBO. If we push the lower bound up, we inevitably push $\log P(x)$ up too.



###### Final Loss Function -


$$Loss = - \mathbb{E}_{Q} [\log P(x|z)] + D_{KL}(Q(z|x) || P(z))$$

**Intuition of loss function -**
By minimising loss, we are maximising the lower bound of the probability of generating real data samples

###### There are 2 parts of the loss function -

Log likelihood and Regularizer

- **$- \mathbb{E}_{Q} [\log P(x|z)]$ (Reconstruction Loss):** This term measures how well the Decoder reconstructs the original data $x$ from the latent variable $z$. Intuition: "Did the output image look like the input image?"
    
- **$+ D_{KL}(Q(z|x) || P(z))$ (Regularization Term):** This term forces the Encoder's generated distribution $Q(z|x)$ to be as close as possible to a standard Normal distribution $P(z)$ (mean of 0, variance of 1). Intuition: "Keep the latent space smooth and organized so we can easily sample from it later."


KL Divergence prevents the PDF of latent variables from collapsing with zero variance, but penalizes it if it deviates from N(0,1) = $P_\theta(Z)$

![[Pasted image 20260307154454.png]]
Source - [[Variational Auto Encoders#References#4. Variational Auto Encoder Part 4 (Ahlad Kumar)|Ref 4 - Variational Auto Encoder]]


Optimization -

We perform Alternate Optimization Principle

![[Pasted image 20260308202349.png]]
Source - Ref 5

When we find derivative with respect to $\phi$, there's a problem. We cannot, take derivative of random variables, we need something deterministic to take the derivative of off. Hence we write a linear equation in terms od mu and sigma and add randomness as a variable epsilon. Hence now there is a particular deterministic equation where randomness is just a variable. Now the derivative can be taken. 

So during backpropagation, the gradiencts can be calculated and phi parametrs (weights and biases of encoder can be updated.).

This problem is not there, when optimizing the decoder, as when we update theta (weights and biases of decoder) the gradients come from the end of netwrok and they don't have any randomeness.

### Optimization and the Reparameterization Trick

**The Problem: The Sampling Bottleneck**

To train this neural network, we use backpropagation. Backpropagation requires calculating gradients (derivatives) through every step of the network to update the weights.

However, the Encoder does not output a single vector $z$. It outputs the parameters of a distribution: a mean ($\mu$) and a variance ($\sigma^2$). To pass information to the Decoder, we have to randomly sample $z$ from this distribution:

$$z \sim \mathcal{N}(\mu, \sigma^2)$$

_Here is the fatal flaw:_ **Sampling is a stochastic (random) process.** You cannot calculate the derivative of a random dice roll. When backpropagation reaches this sampling step, the gradients are blocked. The network cannot update the Encoder's weights, meaning the model cannot learn.

**The Solution: The Reparameterization Trick**

We need a way to sample $z$ that still allows gradients to flow backwards into $\mu$ and $\sigma$. We do this by rewriting the sampling process so that the randomness is injected as an _independent, external input_.

Instead of sampling $z$ directly from $\mathcal{N}(\mu, \sigma^2)$, we define $z$ as a deterministic equation:

$$z = \mu + \sigma \odot \epsilon$$

- **$\mu$:** The mean vector (output by the Encoder).
    
- **$\sigma$:** The standard deviation vector (output by the Encoder).
    
- **$\epsilon$:** A random noise vector sampled from a standard Normal distribution, $\mathcal{N}(0, 1)$.
    

**The Intuition:**

By isolating the randomness into the $\epsilon$ variable, the path from $z$ back to $\mu$ and $\sigma$ becomes a simple addition and multiplication. Backpropagation treats $\epsilon$ as just a constant input. The gradients can now flow smoothly through the deterministic nodes ($\mu$ and $\sigma$) all the way back through the Encoder, allowing the entire VAE to be trained end-to-end.

#### How to Study
##### Quick Review

Read this doc

##### Some Time

Watch - [[Variational Auto Encoders#References#1. Variational Auto Encoder Part 1 (Ahlad Kumar)| Ref 1 - Variational Auto Encoder]]
Watch - [[Variational Auto Encoders#References#2. Variational Auto Encoder Part 2 (Ahlad Kumar) | Ref 2 - Variational Auto Encoder]] (Skip the derivations)
Watch - [[Variational Auto Encoders#References#3. Variational Auto Encoder Part 3 (Ahlad Kumar) | Ref 3 - Variational Auto Encoder]]

##### Plenty Time

Watch the entire playlist - 

```embed
title: "Variational_AutoEncoder"
image: "https://i.ytimg.com/vi/w8F7_rQZxXk/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD-yur_HnXsn3-ZCBjLvTnvkfVn9w&days_since_epoch=20519"
description: ""
url: "https://youtube.com/playlist?list=PLdxQ7SoCLQANizknbIiHzL_hYjEaI-wUe&si=AaGp6FnerYKZSlWN"
favicon: "https://www.youtube.com/s/desktop/ab5c3a01/img/favicon_32x32.png"
aspectRatio: "56.25"
```



#### References

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

###### 3. Variational Auto Encoder Part 3 (Ahlad Kumar)

```embed
title: "Deep Learning 21: (3) Variational AutoEncoder : Working details of Variational AutoEncoder"
image: "https://i.ytimg.com/vi/YHldNC1SZVk/maxresdefault.jpg"
description: "In this Lecture, we will gain insight into the working of Variational autoencoders (VAE). Its difference from simple autoencoders will also be explained.#aut..."
url: "https://youtu.be/YHldNC1SZVk?list=PLdxQ7SoCLQANizknbIiHzL_hYjEaI-wUe"
favicon: "https://www.youtube.com/s/desktop/ab5c3a01/img/favicon_32x32.png"
aspectRatio: "56.25"
```


###### 4. Variational Auto Encoder Part 4 (Ahlad Kumar)

```embed
title: "Deep Learning 22: (4) Variational AutoEncoder : Derivation of the Loss Function"
image: "https://i.ytimg.com/vi/Hlr3CYfRMf0/maxresdefault.jpg"
description: "In this lecture derivation of the loss function is derived for the Variational Autoencoder in detail.#autoencoder#variational#generativeImplementation by And..."
url: "https://youtu.be/Hlr3CYfRMf0?list=PLdxQ7SoCLQANizknbIiHzL_hYjEaI-wUe"
favicon: "https://www.youtube.com/s/desktop/ab5c3a01/img/favicon_32x32.png"
aspectRatio: "56.25"
```


###### 5. Variational Auto Encoder Part 5 (Ahlad Kumar)

```embed
title: "Deep Learning 23: (5) Variational AutoEncoder : Optimization and  Reparametrization Trick"
image: "https://i.ytimg.com/vi/7MVJ7FgrsYc/maxresdefault.jpg"
description: "In this lecture optimization of the loss function of Variational Autoencoder is discussed. Also, a discussion on re-parametrization technique is carried out ..."
url: "https://youtu.be/7MVJ7FgrsYc?list=PLdxQ7SoCLQANizknbIiHzL_hYjEaI-wUe"
favicon: "https://www.youtube.com/s/desktop/ab5c3a01/img/favicon_32x32.png"
aspectRatio: "56.25"
```
