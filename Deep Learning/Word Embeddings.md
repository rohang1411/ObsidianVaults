
Neural Networks work with numbers
The goal is to represent words as numbers

1. Sequential Series
One way is to use a different number for each word sequentially.

I like NYC. NYC is on my bucket list
0 1      2       2   3   4    5      6       7

But as soon as the vocabulary grows

I would love to go there
0     8      9   10 11   12

We want similar words to be closer, so that the network knows that they are similar. But in this case the embeddings for similar words like "like" and "love" are 1 and 9, which are very far. And hence these don't make good features.

2. Bag of words
3. Skip Gram

If we use a neural network to create embeddings, then the total number of parameters increase exponentially, as for each word in the vocab we connect it with dense layers.

![[Pasted image 20260306212642.png]]


Optimization
We only update the parameters of words which we want to predict and which we don't want to predict.