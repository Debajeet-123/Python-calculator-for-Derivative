from sympy import *
symbol = int(input("Enter Number of Symbols in the equation"))
print(symbol)
symbol_list=[]
for i in range(0, symbol):
    print("Enter",i+1," symbol name" )
    item = (input())
    symbol_list.append(symbols(item))
print("symbol list is ", symbol_list)
def deriv(symbol_list):
  function=input("enter function")
  function
  der=Derivative(function,symbol_list)
  print(der)
  #you can take n derivative by taking the additional/ optional third argument 
  diff(function, symbol_list[0])
  variable=input("calculate the derivative on the basis of which variable?")
  df=diff(function,variable)
  print(df)
  #substitute values into expressions
  print("Now to substitute the values into symbolic equations, kindly enter the value")
  substitute=int(input())
  d=df.subs(variable, substitute)
  print(d)

deriv(symbol_list)
