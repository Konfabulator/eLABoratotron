import sympy as sp
import ast
import numpy as np
import os, sys

################################################################################

## set directory to the current file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

################################################################################

# x**2*a+b*c**3
# E = R * (a*n+b)/(a*x+b)

################################################################################

## Input the function to analyze
expression = input("Enter the expression with multiple variables: ")
expression = expression.replace("^", "**").strip()
print('-'*50)

################################################################################

## Parse the expression to get the variables
variables = set()
for node in ast.walk(ast.parse(expression)):
    if isinstance(node, ast.Name):
        variables.add(node.id)
variables = list(variables)

# Define the variables as symbols
variables_symbolic = [sp.symbols(v) for v in variables]

################################################################################

## Get the derivatives of the expression by each variable
derivatives = [sp.diff(sp.sympify(expression), symbol) for symbol in variables_symbolic]
for variable, derivative in zip(variables, derivatives):
    print(f"The derivative of the expression with respect to {variable} is: {derivative}")
print('-'*50)
print('-'*50)

################################################################################

## create symbols for the variables errors
variables_err = []
for variable in variables:
    variables_err.append((f"U_{variable}"))
variable_err_symbolic = [sp.symbols(v_e) for v_e in variables_err]

################################################################################

## calculate the ERROR expression
expression_error = []
expression_error_to_read = [] 
for variable, derivative, error_symbol in zip(variables, derivatives, variable_err_symbolic):
    expression_error.append((derivative*error_symbol)**2)
    expression_error_to_read.append(f"\\left({sp.latex(sp.simplify((derivative)))}\\cdot {error_symbol}\\right)^2")
expression_error_to_read = '\\sqrt{' + f"{' + '.join(expression_error_to_read)}" + "}"
expression_error = str(sp.simplify(sum(expression_error)**0.5))

print("The error of the expression in LATEX: ")
print(expression_error_to_read)
print('-'*50)
print("The error of the expression in PYTHON: ")
print(expression_error)
print('-'*50)
print('-'*50)

################################################################################

## INPUT whole tables of VALUES and ERRORS for each variable
values = {}
values_errors = {}
input_type = 'human'

if input_type == 'human':
    # HUMAN input
    for v, ve in zip(variables, variables_err):
        vals =      input(f"Enter VALUES for {v} (separated with SPACE): ")
        vals_err =  input(f"Enter ERRORS for {v} (separated with SPACE): ")
        # decimal separator = dot
        vals = vals.replace(',', '.').split(' ')
        vals_err = vals_err.replace(',', '.').split(' ')
        # values to floats
        values[v] = [float(i.strip()) for i in vals]
        values_errors[ve] = [float(i) for i in vals_err]
    print('-'*50)
    print('-'*50)
    # Make all the lists the same length by filling the shorter with zeros
    max_len = max([len(v) for v in values.values()])
    for v, ve in zip(values, values_errors):
        values[v] += [0.0]*(max_len - len(values[v]))
        values_errors[ve] += [0.0]*(max_len - len(values_errors[ve]))
else:
    # RANDOM input
    for v,ve in zip(variables, variables_err):
        values[v] = np.random.uniform(0, 10, 10)
        # the error can be only 10% of the value
        values_errors[ve] = np.random.uniform(0, 1, 10)*values[v]/10

################################################################################

## Calculate the EXPRESSION and IT'S ERROR for each set of values
results = []
errors = []
for i in range(len(values[variables[0]])):
    values_i = {}
    values_errors_i = {}
    for v, ve in zip(variables, variables_err):
        values_i[v] = values[v][i]
        values_errors_i[ve] = values_errors[ve][i]
    results.append(eval(expression, values_i))
    errors.append(eval(expression_error, {**values_i, **values_errors_i}))

################################################################################,

## DISPLAY the results
print(f"Results for each set of values: ")
for r,e in zip(results, errors):
    print(f"{r} +/- {e}")

################################################################################

## SAVE the results to a file
with open("results.txt", "w+") as f:
    f.write("Results: \n")
    for r,e in zip(results, errors):
        f.write(f"{r} {e}\n")