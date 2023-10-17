"""
empirically test if python
global and local settings of random seeds.
e.g.
at least in colab ipython notebooks,
global random seed setting do NOT apply within function
and resetting the random seed in function does NOT change the global setting
merely importing a global seed setting variable does not alter this
only manually resetting the random see to a global (or imported) ~global value
will make the random seed globally uniform (in all functions).

sample colab output:

irst print
first Random Number: 82
first Random Number: 82

function_no_reset Random Number before reset: 15
function_no_reset Random Number after: 4

function_no_reset Random Number before reset: 95
function_no_reset Random Number after: 36

function_reset Random Number before reset: 32
function_reset Random Number after: 29

function_reset Random Number before reset: 71
function_reset Random Number after: 10

function_global_seed Random Number before reset: 82
function_global_seed Random Number after: 15

function_global_seed Random Number before reset: 82
function_global_seed Random Number after: 15

last Random Number: 82
last Random Number: 82
"""

import random

print("first print")
# Set the global random seed
global_seed = 42
random.seed(global_seed)
# Generate a random number
random_number = random.randint(1, 100)
# Print the random number along with the function name
print(f"first Random Number: {random_number}")
print(f"first Random Number: {random_number}\n")

# Function to generate and print a random number
def function_no_reset():

    # Generate a random number
    random_number = random.randint(1, 100)
    # Print the random number along with the function name
    print(f"function_no_reset Random Number before reset: {random_number}")

    # Generate a random number
    random_number = random.randint(1, 100)
    # Reset the random seed for this function
    # random.seed(random_number)
    # Print the random number along with the function name
    print(f"function_no_reset Random Number after: {random_number}\n")


# Function to generate and print a random number
def function_reset():
    global global_seed

    # Generate a random number
    random_number = random.randint(1, 100)
    # Print the random number along with the function name
    print(f"function_reset Random Number before reset: {random_number}")

    # Generate a random number
    random_number = random.randint(1, 100)
    # Reset the random seed for this function

    random.seed(random_number)
    # Print the random number along with the function name
    print(f"function_reset Random Number after: {random_number}\n")

# Function to generate and print a random number
def function_global_seed():
    global global_seed
    random.seed(global_seed)

    # Generate a random number
    random_number = random.randint(1, 100)
    # Print the random number along with the function name
    print(f"function_global_seed Random Number before reset: {random_number}")

    # Generate a random number
    random_number = random.randint(1, 100)
    # Reset the random seed for this function

    random.seed(random_number)
    # Print the random number along with the function name
    print(f"function_global_seed Random Number after: {random_number}\n")

# Test the functions
function_no_reset()
function_no_reset()

function_reset()
function_reset()

function_global_seed()
function_global_seed()

# Print the random number along with the function name
print(f"last Random Number: {random_number}")
print(f"last Random Number: {random_number}\n")
