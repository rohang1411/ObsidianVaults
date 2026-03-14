Need? Why?
Complex input like images, if fed directly i.e. if we send each pixel and connect it to a dense layer then the number of parameters (weights & biases) would scale exponentially with respect to input size. Hence we need to find a way to compress the input but at the same time not loose out on the important details/patterns in the input

CNN help reduce the number of inputs into the neural network.

CNNs have a filter which convolves (multiplies) over the input

All CNNs follow the structure -

1. Apply Convolution -> Creates Feature Map
2. Pass it through an Activation Function
3. Then pool it

Benefits of CNN -
1. **Reduce the number of inputs** 
2. **Preserves the spatial structure of Input** 
   Take correlations into account using filter (the filter looks at regions of the input and tries to match or correlate that part of input with the filter, it may correlate negatively but basically different parts of input would react differently with the filter, but similar parts/regions of the filter react similarly)
3. **Can tolerate shifts in input**
4. **Local Connectivity:** A neuron doesn't need to look at the whole image; it only needs to look at a small local patch (e.g., a $5 \times 5$ window) to find an edge.
5. **Parameter Sharing:** An edge detector useful in the top-left corner is equally useful in the bottom-right. Therefore, we use the _exact same_ local weights (a "filter") and slide it across the entire image.


Filter -
Stride - Stride dictates how many pixels the filter shifts per step.
A stride of 2 skips every other pixel, effectively halving the spatial dimensions.
Padding - 

**Intuition for Padding:** Zero-padding ensures the edge pixels contribute to the feature extraction equally. Without padding, center pixels are swept over many times by the sliding window, while corner pixels are only "seen" once.

Convolution Process-

**Edge Case:** 1x1 Convolutions. $1 \times 1$ convolutions manipulate depth without altering spatial size.

Slide 118 notes $F=1, S=1, P=0$ is a common setting. A $1 \times 1$ convolution does not look at spatial neighbors at all. It acts as a standard Fully Connected layer applied independently to every single pixel across the depth channels. It is used to cleanly shrink or expand the _depth_ ($C$) of the volume without touching spatial size.


##### Output size

Let $W_{in}$ be input width, $F$ be filter width, $P$ be padding, and $S$ be stride.

$$W_{out} = \frac{W_{in} - F + 2P}{S} + 1$$

(Note: The result must be an integer. If the arithmetic yields a fraction, the hyperparameters are structurally incompatible and the filter "doesn't fit").

In general, common to see CONV layers with stride 1, filters of size F x F, and zero-padding with (F-1)/2. (will preserve size spatially)


**Rule of thumb for "Same" padding:** To preserve spatial dimensions perfectly when Stride $S=1$, use padding $P = \frac{F-1}{2}$

(e.g., $F=3 \implies P=1$; $F=5 \implies P=2$).

This will produce an output of $W_2 \times H_2 \times K$ where:

$W_2 = (W_1 - F + 2P)/S + 1$
$H_2 = (H_1 - F + 2P)/S + 1$






### Pooling Layers

Pooling forces the network to retain only the most highly activated features in a local region, creating translation invariance while drastically reducing spatial dimensions and compute load for subsequent layers.

Benefits -
- Reduce input size - Make representations smaller
- Reduces Parameters - Helps in combatting overfitting
- No learnable params

Working -

Unlike convolutions, pooling layers do not perform dot products with learned weights. They slide a window (usually $2 \times 2$) over the spatial dimensions with a specified stride (usually $S=2$) and apply a fixed mathematical operation.

- **Max Pooling:** Takes the maximum value in the window. This is the most common. It mathematically says, "Did this feature (e.g., an edge) exist _anywhere_ in this $2 \times 2$ region? If yes, keep its strongest signal."
    
- **Average Pooling:** Takes the mean of the window.

Output Size -

This will produce an output of $W_2 \times H_2 \times K$ where:

$W_2 = (W_1 - F + 2P)/S + 1$
$H_2 = (H_1 - F + 2P)/S + 1$

With usually P = 0 

#### How does pooling layer backpropagation works?

Because pooling has 0 parameters, its backpropagation routing is fixed. A Max Pool gate acts like the "Router" we saw in Batch 7: during backprop, the upstream gradient is passed _entirely_ to the pixel that held the maximum value during the forward pass; the other pixels in the window receive a gradient of 0.

### Softmax layer 

Softmax is implemented through a neural network layer just before the output layer. The Softmax layer must have the same number of nodes as the output layer

The goal is to map the non-normalized output of a network to a probability distribution over predicted output classes.

The Softmax forces the raw logits $z$ into a valid probability distribution $\sigma(z)_i = \frac{e^{z_i}}{\sum e^{z_j}}$.



Batch Normalization -

Need?

As data flows through deep layers, small weight updates in early layers multiply, causing the distribution of inputs to later layers to shift wildly (Internal Covariate Shift). This forces us to use tiny learning rates.

BatchNorm fixes this by normalizing the activations $x$ of a batch to have mean $\mu = 0$ and variance $\sigma^2 = 1$.

$\hat{x} = \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}}$

- Stabilizes gradients
- Allowing higher learning rates
- Makes deep networks much easier to train!- Improves gradient flow
- Allows higher learning rates, faster convergence
- Networks become more robust to initialization
- Acts as regularization during training
- Zero overhead at test-time: can be fused with conv!
- Behaves differently during training and testing: this is a very common source of bugs!

_b) The Learnable Parameters ($\gamma$ and $\beta$)_

If we force every layer's activations to be $0$-mean and $1$-variance, we might destroy useful representations (e.g., if a feature _needs_ to be highly activated and positive to indicate a strong match).

To restore flexibility, BatchNorm applies a linear transformation _after_ normalization:

$y = \gamma \hat{x} + \beta$

Where $\gamma$ (scale) and $\beta$ (shift) are learned via backpropagation. If the network decides the optimal distribution _is_ the original unnormalized one, it can learn $\gamma = \sigma$ and $\beta = \mu$ to perfectly undo the normalization.

_c) Train-Time vs. Test-Time Behavior_

- **Training:** $\mu$ and $\sigma$ are calculated explicitly across the current mini-batch of size $N$.
    
- **Testing (Inference):** At test time, we might only evaluate a single image ($N=1$). We cannot calculate a batch mean of 1 item. Therefore, during training, BatchNorm keeps an exponentially decaying **running average** of the batch means and variances. At test time, these fixed running averages are used instead.


Questions -

1. Why $\gamma$ and $\beta$ exist?
   
   To preserve the network's representational capacity by allowing it to shift the normalized distribution).
   
   
1.  
2. 