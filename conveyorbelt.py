# goal: write a python script that prompts the user to input n numbers, and create a indexed set of those numbers. Following this, move all the elements of the indexed set one place to the left, with the first element moving to the last place.

# input: n numbers

n = 4

# define the loop function

def loop(inputs):
    tmp = inputs[0]
    for i in range(n-1):
        inputs[i] = inputs[i+1]
    inputs[n-1] = tmp
    return inputs

# take user input

u_input = {}
for i in range(n):
    u_input[i] = int(input("Enter number: "))

print("The input is ")
print(u_input)

# apply loop function

u_input = loop(u_input)

print("The output is ")
print(u_input)