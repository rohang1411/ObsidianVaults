
#### seq2seq problem

These are the problem where the all the inputs are of one particular type and the all outputs are of a same different type.

ex. Translate sentences from English to Spanish

In these type of problems the input and output lengths can differ.


We can use multiple layers of multiple LSTM cells for Encoder and Decoder.

![[Pasted image 20260306214444.png]]



Encoder - Encodes the input sentence into a context vector (collection of long and short term memories)

![[Pasted image 20260306214414.png]]



Decoder - Decodes the context vector 

![[Pasted image 20260306214558.png]]


Decoder stops after outputting the \<EOS\> token or after hitting max output length.

We provide the actual output tokens (spanish translation) to the decoder as inputs

![[Pasted image 20260306215300.png]]



##### Problems


With longer sequences, when the encoder compresses the encoded input into a single context vector, the model might loose out context on the earlier parts of the input. 

Why is this a problem? What can happen?

![[Pasted image 20260306215805.png]]

Hence it's essential to preserve context


Solution - [[Attention]]