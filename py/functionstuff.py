# ask user what they want to do (derivative, antiderivative, calculate values, etc.) and do it.

# import modules
import sympy as sp

# define variable
x = sp.Symbol('x')

# take user input
function = input("What is your function?\n Please only enter functions in terms of x. No other variables will be accepted.\n Please enter in Python-compatible format.\n Example: x**2 + 3*x + 5\n\t")

# degub # function = "4*x**2 + 3*x + 5"

function = sp.sympify(function)

# ask the user for a series of numbers denoting the values of x at which to evaluate the function, then evaluate the same.
values = []
numberofvalues = int(input("How many values of x would you like to evaluate?"))
# debug # numberofvalues = 2
for i in range(numberofvalues):
    values.append(float(input("What is the value of x?")))
evaluations = []
for i in values:
    evaluations.append(function.subs(x, i))

# ask the user for a series of numbers denoting the orders of derivatives to take, then take the derivatives.
derivativeorders = []
numberofderivatives = int(input("How many derivatives would you like to take?"))
for i in range(numberofderivatives):
    derivativeorders.append(int(input("What is the order of the derivative?")))
derivatives = []
for i in derivativeorders:
    derivatives.append(function.diff(x, i))

# ask the user for a series of numbers denoting the orders of antiderivatives to take, then take the antiderivatives.
antiderivativeorders = []

numberofantiderivatives = int(input("How many antiderivatives would you like to take?"))

for i in range(numberofantiderivatives):
    print("What is the order of antiderivative no. ", i+1,"?")
    antiderivativeorders.append(int(input("")))



antiderivatives = []

for i in antiderivativeorders:
    antiderivatives.append(sp.integrate(function, x))


# ask the user whether to calculate a bounded integral
boundedintegral = input("Would you like to calculate a bounded integral? (y/n)")
if boundedintegral == "y":
    lowerbound = float(input("What is the lower bound?"))
    upperbound = float(input("What is the upper bound?"))
    boundedintegral = function.integrate((x, (lowerbound, upperbound)))
    isboundedintegral = True
else:
    isboundedintegral = False

# ask the user whether they want the resultant expressions in LaTeX format, Python format, or both.
format = []
format.append(input("Would you like the resultant expressions in LaTeX format? (y/n)"))
format.append(input("Would you like the resultant expressions in Python format? (y/n)"))

# print the results
printed = False


if format[0] == 'y':
    for i in range(len(derivatives)):
        print(f"{derivativeorders[i]}th order derivative is: {sp.latex(derivatives[i])}")
    for i in range(len(antiderivatives)):
        print(f"{antiderivativeorders[i]}th order antiderivative is: {sp.latex(antiderivatives[i])}")
    if isboundedintegral:
        print(f"bounded integral is {sp.latex(boundedintegral)} with bounds {lowerbound} and {upperbound}")
    printed = True

if format[1] == 'y':
    for i in range(len(derivatives)):
        print(f"{derivativeorders[i]}th order derivative is: {derivatives[i]}")
    for i in range(len(antiderivatives)):
        print(f"{antiderivativeorders[i]}th order antiderivative is: {antiderivatives[i]}")
    if isboundedintegral: 
        print(f"bounded integral is {sp.latex(boundedintegral)} with bounds {lowerbound} and {upperbound}")
    printed = True


if printed == False:
    print("No results printed. Please enter y for at least one of the format options.")

# say bye bye
print("Thank you for using the Derivative Calculator!")