from sympy import solve, Eq
import sympy as sp
print("""Hello!, welcome to the equation solver
please enter the equation you want solve""")
equation = input("Enter the equation: ")
for i in range(len(equation)):
    if equation[i] == '=':
        result = equation[i+1:]
        break
for i in range(len(equation)):
    if equation[i] == '=':
        equation = equation[:i]
        break
s = sp.parsing.sympy_parser.parse_expr(equation)
s1 = sp.parsing.sympy_parser.parse_expr(result)
eq = Eq(s, s1)
sol = solve(eq)
print(sol)