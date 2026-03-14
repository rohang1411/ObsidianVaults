
Slope = dy/dx (rate of change of y with respect to x)
Step Size = Slope x Learning Rate
New Intercept = Old Intercept - Step Size
Two or more derivatives of the same function are called Gradient
Gradient descent is very sensitive to learning rate (Basically it determines the step size)

In GD, to get the predicted values by running the neural network. So during the forward pass, we get the predicted values

Gradient Descent is the algorithm used to quickly minimize the loss by updating gradients. Gradients are updated based on step size. 

Ex.  if initial input is x 

![[Pasted image 20260305225550.png]]

![[Pasted image 20260305225650.png]]


Intuition of GD -
When we minimize the Loss using GD, essentially what we are doing is - calculating how much the output/loss changes wrt on of the neuron in last layer, and how much that neuron changes wrt the neuron of previous layer and so on until the first layer and input. In the first layer we are calculating how much the first neuron is changing with respect to the input x.

So when minimizing the loss in the backward step we basically calculate the gradients(derivatives) of a particular neuron wrt to the previous neuron and so on. And multiplying those gradients gives us how much the output/loss would change wrt input/x. And that is essentially our slope. Slope -> change of y wrt x -> change in y/change in x

This is [[Backpropagation]] step -
Multiplying the derivatives/gradients at each step gives us, how much the output/loss is changing wrt that particular neuron. For ex. change in weight of neuron in 5th layer is affecting the output by 0.2. And change in bias of a neuron in 7th layer change the output/loss by 0.1. All these values, i.e. how much the output changes with respect to each parameter in the network can be calculated & updated in parallel simultaneously.

And based on this we calculate the step size, multiply it by learning rate and then update the weights accordingly.


SGD -> Randomly takes a batch of data to perform gradient Descent instead of the entire dataset as Gradient Descent is time consuming