#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) As the size of n increases, the time complexity 
remains O(1) to complete each mathematical operation, but the time complexity scales at O(n**3). As the input grows, whether n is an integer or a matrix array (the instructions are unclear), it should take n-cubed time to run through all calculations in the loop. 


b) Exponential. I am having the hard time reading this 
pseudocode because n can be interpretted as an integer 
in my opinion the way it is written. Assuming that n
is an array, this would be exponential time, because for each item in the array, the function would run a while loop, doubling the value of j over and over until it exceeds what i assume is the length of the array. if you have millions of items in the array, j would always start at 1 and have to double until exceeding n for each item. 


c) bunnyEars is being called recursively, subtracting the value of bunnies in a loop until it reaches 0, so it would take O(bunnies) to reach 0, no matter how large the input, which I assume is an integer. The addition of 2 in the return statement doesn't impact the time complexity, which is reliant on bunnies reaching 0 before exiting the function.

## Exercise II

first_floor = 0
top_floor = len(num_floors)
middle_floor = 0
dropped_eggs = 0

while first_floor < top_floor:
    middle_floor = first_floor + top_floor // 2
    dropped_eggs += 1

    if num_floors[middle_floor] === survived_egg
        first_floor = middle_floor + 1
    
    elif num_floors[middle_floor] === broken_egg
        top_floor = middle_floor - 1

    else: 
         return middle_floor

This uses a modified binary search in n(log(n)), but I'm realizing now that this wont work to find the exact point at all. Instead I can do O(n) but just iterating up from the bottom floor.

for floor in num_floors:
    drop_egg
    if egg == survives:
        floor += 1
    else:
        return floor
