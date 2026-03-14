

##### What it Does? What's new? Problem it solves?
Introduces feedback loop

![[Pasted image 20260306191023.png]]


---

#### Vanishing / Exploding Gradients

 Since the previous output is part of the the next input, as the number of inputs grows, the previous output again and again gets diminished/amplified 
 
![[Pasted image 20260306190959.png]]

When training the network, during [[Backpropagation]] the huge number will make its way into the derivatives and changes step size which make it very small/large

![[Pasted image 20260306191159.png]]



Activation functions that cause the problem of Vanishing / Exploding Gradients -

1. Sigmoid - 
2. 

Solution - [[Long Short Term Memory Networks (LSTM)]]