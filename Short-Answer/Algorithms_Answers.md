#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) As the size of n increases, the time complexity 
remains O(1) to complete each mathematical operation, but the time complexity scales at O(n**3). As the input grows, whether n is an integer or a matrix array (the instructions are unclear), it should take n-cubed time to run through all calculations in the loop. 


b) Exponential. I am having the hard time reading this 
pseudocode because n can be interpretted as an integer 
in my opinion the way it is written. Assuming that n
is an array, this would be exponential time, because for each item in the array, the function would run a while loop, doubling the value of j over and over until it exceeds what i assume is the length of the array. if you have millions of items in the array, j would always start at 1 and have to double until exceeding n for each item. 


c) bunnyEars is being called recursively, subtracting the value of bunnies in a loop until it reaches 0, so it would take O(bunnies) to reach 0, no matter how large the input, which I assume is an integer. The addition of 2 in the return statement doesn't impact the time complexity, which is reliant on bunnies reaching 0 before exiting the function

## Exercise II


