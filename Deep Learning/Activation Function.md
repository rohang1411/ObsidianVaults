
### 1. Sigmoid

 Sigmoid outputs values between 0 and 1 for any input
 
$$
Sigmoid = \sigma(z) = \frac{1}{1 + e^{-z}}   
$$

- Squashes numbers to range [0,1]
- Historically popular since they have nice interpretation as a saturating “firing rate” of a neuron
#### Derivative
![[Pasted image 20260308131406.png]]


#### Problems
1. Vanishing Gradient (Saturation Problem)- tanh has the same problem
   Kills gradients and causes Vanishing gradients problem, as derivative is -
   
   $\nabla\sigma = (1-\sigma)\sigma$)
   
   So when then  $\sigma(x)$  approaches 0 or 1, the derivative ~ 0. And during backpropagation, it causes the gradients to become 0

2. Not zero centered -
   Because $\sigma(x)$ is always positive, the local gradient is always positive. By F8, the downstream gradient applied to the weights will all share the exact same sign as the upstream gradient. This forces weight updates to move in synchronized directions (all positive or all negative), leading to highly inefficient, zig-zagging optimization paths.
   
3. exp() is a bit compute expensive
   
   
#### Solution



### 2. ReLU

$\text{ReLU}(x) = \max(0, x)$

- Does not saturate (in positive region) - 
- Very computationally efficient
- Converges much faster than sigmoid/tanh in practice (e.g. 6x)

#### Problems
1. **Not zero-centered output**
2. **Dying ReLU** - If a particular neuron's output is negative(once or always) then, ReLU will return 0. The neuron will pass a gradient 0 and its weight will never update again. It is "dead."
3. **Hard zero cutoff** at negative values, which can disrupt gradient flow during training.

##### Why ReLU can still learn without negative response?
1. **Sparse Activation:** ReLU outputs zero for any negative input, leading to a portion of neurons in the network not activating. This sparsity in activation patterns improves computational efficiency and regularization.
2. **Non-saturation:** The ReLU function is linear for positive inputs, meaning it does not saturate (or flatline) as the input gets large, unlike the sigmoid or tanh functions.
3. **Enhancement of Positive Features:** Although ReLU does not directly process negative inputs (setting them to zero), it can emphasize positive features through the adjustment of weights learned by the network.
4. **Collaboration in Multilayer Networks:** even though individual ReLU units cannot process negative inputs, multiple layers of ReLU units can interact through their weights and structure to abstract useful information and features from complex inputs.

#### Solution

1. **Leaky ReLU** - Fixes the dead neuron problem by allowing a small gradient ($0.1$) to flow when $x < 0$.

   **Leaky ReLU =** $\max(0.1x, x)$
   
   ![[Pasted image 20260308133951.png]]
   - Does not saturate
   - Computationally efficient
   - Converges much faster than sigmoid/tanh in practice! (e.g. 6x)
   - Will not “die” like ReLU for negative input values


2. **Parametric Rectifier (PReLU)** - Introduces an alpha parameter
   
   **PReLU =** $\max(\alpha x, x)$
   
2. **Exponential Linear Units (ELU)** - Adds a smooth curve for negative values, making the mean output closer to zero.
   
   ![[Pasted image 20260308134449.png]]
   
   ![[Pasted image 20260308134512.png]]
   
   - All benefits of ReLU
   - Closer to zero mean outputs
   - Negative saturation regime compared with Leaky ReLU adds some robustness to noise
   
   Problem -
   Computation requires exp()

4. **GELU (Gaussian Error Linear Unit):** The standard for LLMs/Transformers. It provides a soft, probabilistic threshold rather than a hard cutoff at $0$, allowing neurons a chance to "recover" from negative regions, ensuring more stable gradient flow in very deep networks.
   
   ![[Pasted image 20260308134941.png]]
   
   $\phi(x)$ is the cumulative distribution function of a standard normal distribution.
   
   ![[Pasted image 20260308135804.png]]


   Key Issue with ReLU -
   - ReLU is not smooth; it has a hard zero cutoff at negative values, which can disrupt gradient flow during training.
   - If many activations fall into the negative range, ReLU sets them to zero permanently.
   - This creates "dead neurons", which never recover and are effectively useless.
   - This is a significant issue in deep models with large FFN layers, where some neurons may never activate after certain weight updates
   
   Why GELU is Preferred -
   - GELU is smoother and has a probabilistic activation mechanism, which helps gradients propagate more effectively.
   - GELU has a soft threshold instead of a hard cutoff.
   - Neurons have a chance of recovering instead of being permanently inactive.
   
   Why This Matters for Transformers -
   - Transformers, including LLMs, rely heavily on stable gradient flow.
   - In early experiments, GELU was found to improve training dynamics, leading to faster and more stable convergence.
   
   ![[Pasted image 20260308135841.png]]
   
   
   
6. vdasvdsa
   
#### Derivative




### 3. Argmax
 ArgMax = Largest value to 1, all other to 0
 
$$
\text{argmax}_{x \in S} \, f(x) := \{x \mid \forall y \in S : f(y) \leq f(x)\}
$$

#### Problems
Cannot be used with [[Backpropagation]], as the derivative would becomes 0 because there is no change in the output of lower classes wrt to input and the output stays 0 for multiple values of x or previous neuron values, when we'll calculate d(class2)/d(neuron of last layer) we get a 0. And when putting this value in Chain Rule, the gradients would become 0
But Argmax can be used for final classification

#### Solution



#### Derivative



### 4. Softmax

Softmax scales all values between 0 and 1
$$
Softmax = \sigma(\mathbf{x})i = \frac{e^{x_i}}{\sum{j=1}^{K} e^{x_j}}
$$


#### Problems



#### Solution


#### Derivative



### 5. Tanh

Sigmoid outputs values between -1 and 1 for any input


$$
\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}
$$   
#### Problems


#### Solution


#### Derivative



Cheat Sheet -


- **Sigmoid:** Kills gradients (saturates), not zero-centered.
- **ReLU:** Fast, fixes positive saturation, but suffers from Dying ReLU (hard 0 cutoff).
- **Leaky ReLU / GELU:** Prevents dying neurons by allowing small gradients for negative inputs.
- **Transformers:** Use GELU for smooth gradient flow.



Questions -

1. What is an activation function in neural networks and why are they used?
   
   An activation function in a neural network is a mathematical function applied to the output of a neuron or layer of neurons, transforming the input signal into an output signal. It's used for introducing non-linear properties to the network. Without non linearity, the neural network would essentially become a linear regression model, incapable of handling complex data patterns
   
2. Can you compare and contrast sigmoid, tanh, and ReLU activation functions?
   
   Sigmoid squashes the input values into a range between 0 and 1. It's often used in the output layer for binary classification. Tanh is similar but outputs values between -1 and 1, making it zero-centered and thus, in some cases, more efficient than sigmoid. ReLU is piece-wise linear, outputting the input directly if it is positive, otherwise zero. It's widely used in hidden layers due to its computational efficiency and ability to mitigate the vanishing gradient problem. However, ReLU can suffer from the "dying ReLU" problem, where neurons stop learning completely.
   
3. What is the 'dying ReLU' problem and how can it be addressed?
   
   The 'dying ReLU' problem occurs when ReLU neurons become inactive and only output zero for all inputs. This happens when negative inputs shift the neuron's weights in such a way that the neuron never activates on any data point again. To address this, variants of ReLU like Leaky ReLU or Parametric ReLU (PReLU) are used. These functions allow a small, positive gradient when the unit is not active, thereby keeping the neurons alive.