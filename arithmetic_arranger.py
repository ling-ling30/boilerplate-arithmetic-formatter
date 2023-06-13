def arithmetic_arranger(problems, a=False):
  import sys
  import math
  import re

  spacing = []
  opp1 = []
  opp2 = []
  oper = []
  sum = []

  for problem in problems:

    problem = problem.split()
    operator = problem[1]
    operand1 = problem[0]
    operand2 = problem[2]

    #check what is the operator
    if operator not in ["+", "-"]:
      return ("Error: Operator must be '+' or '-'.")

    #check if the operand max = 4
    if len(operand1) > 4:
      return ("Error: Numbers cannot be more than four digits.")
    if len(operand2) > 4:
      return ("Error: Numbers cannot be more than four digits.")

    #find the longest operand
    if len(operand1) > len(operand2):
      spacing.append(len(operand1))
    else:
      spacing.append(len(operand2))

    #result
    #check if it is a digit
    try:
      if operator == "-":
        sum.append(int(operand1) - int(operand2))
      elif operator == '+':
        sum.append(int(operand1) + int(operand2))
    except:
      return ("Error: Numbers must only contain digits.")

    #add operand to the list
    opp1.append(operand1)
    opp2.append(operand2)
    oper.append(operator)

  if len(sum) > 5:
    return ("Error: Too many problems.")

  statement1 = ""
  statement2 = ""
  dash_space = ""
  sum_space = ""
  arranged_problem = ""
  for i in range(len(sum) - 1):

    q1 = (f"{opp1[i]:>{spacing[i]+2}}")
    q2 = f"{oper[i]} {opp2[i]:>{spacing[i]}}"
    dash = "-" * (spacing[i] + 2)
    res = (f"{sum[i]:>{spacing[i]+2}}")

    statement1 += (q1 + "    ")
    statement2 += (q2 + "    ")
    dash_space += (dash + "    ")
    sum_space += (res + "    ")

  statement1 += ((f"{opp1[-1]:>{spacing[-1]+2}}"))
  statement2 += (f"{oper[-1]} {opp2[-1]:>{spacing[-1]}}")
  dash_space += "-" * (spacing[-1] + 2)
  sum_space += (f"{sum[-1]:>{spacing[-1]+2}}")

  if a == False:
    arranged_problem = f"{statement1}\n{statement2}\n{dash_space}"
  if a == True:
    arranged_problem = f"{statement1}\n{statement2}\n{dash_space}\n{sum_space}"

  return arranged_problem
