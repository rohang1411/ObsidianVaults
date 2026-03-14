
Cross Entropy vs Sum of Squared Residuals
If we calculate the value of both CE and SSR the difference between the values of loss for a bad prediction and a good prediction is much more in CE as compared to SSR. And since when calculating the step size in [Gradient Descent], the derivate/slop of CE loss would be much more than SSR. Hence, it will allow us to take a large step if our prediction is bad as compared to a much smaller step of derivative of SSR. Hence, the loss can be minimized faster.

![[Pasted image 20260306145237.png]]