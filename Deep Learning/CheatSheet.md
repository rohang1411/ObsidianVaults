## General 

Step Size = Slope x Learning Rate


## Activation Functions

Formulas of Activation functions and their derivatives



- **Sigmoid:** Kills gradients (saturates), not zero-centered.
- **ReLU:** Fast, fixes positive saturation, but suffers from Dying ReLU (hard 0 cutoff).
- **Leaky ReLU / GELU:** Prevents dying neurons by allowing small gradients for negative inputs.
- **Transformers:** Use GELU for smooth gradient flow.


## CNN -


#### CNN Output Formula
W = Input width
H = Input height
F = Filter width (hyperparameter)
P = Padding (hyperparameter)
S = Stride (hyperparameter)

$$W_2 = \frac{W_1 - F + 2P}{S} + 1$$
$$H_2 = \frac{H_1 - F + 2P}{S} + 1$$

**This will produce an output of $W_2 \times H_2 \times K$. If output is not an integer, then filter is incompatible.**

#### Total number of parameters formula

$$F^2CK + K$$ 

F<sup>2</sup>CK - weights
K - biases


Pooling layers have **0 learnable parameters**

If asked to calculate the parameter count of a `Conv -> ReLU -> Pool` block, only the Conv layer contributes to the count.