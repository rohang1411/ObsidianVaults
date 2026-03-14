

What it Does? What's new? Problem it solves?
Introduces two different paths, one for long term memory (cell state) and keeps the short term memory paths (feedback loops) from [[Recurrent Neural Networks | RNNs]]. This approach allows LSTMs to solve the [[Recurrent Neural Networks#Vanishing / Exploding Gradients | Vanishing / Exploding Gradients]] problem.


![[Pasted image 20260306191820.png]]


---

Architecture of LSTM block -

![[Pasted image 20260306195545.png]]


**First Stage (Forget Gate) -**
Since sigmoid activation function returns any value between 0 and 1. Its output is multiplied by the long term memory. It determines what percentage of the long term memory would be remembered.

**Second Stage (Input Gate) -**
Updates short term memory. Determines is there any potential long term memory which should be saved and how much of it should be saved. 

**Third Stage (Output Gate) -**
Updates short term memory. Determines is there any potential short term memory which should be saved and how much of it should be saved. This is the output of the LSTM block.



Sigmoid - Used to determine what percent of memory does/should the LSTM remember
Tanh - Used to 

---

Other Points to Remember -

**We stack multiple of these LSTM blocks, all of them use same weights and biases. This is done so that the LSTM can handle inputs/data sequences of various lengths** . The idea is that each word is considered as a different input. So we want to treat all the inputs with the same model i.e. same weights and biases. And since the weights and biases are same, the input length can be anything from 10 - 100000.

LSTM can handle longer sequences of input than RNN as we can unroll them multiple times without facing the Exploding/Vanishing gradient problem



---

Questions -
1. How does LSTM prevent Exploding/Vanishing Gradient problem?
2. Why is the long term memory (cell state) is not affected by the Exploding / Vanishing gradients problem?
3. Why does LSTM blocks use same weight and biases