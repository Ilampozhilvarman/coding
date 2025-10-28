code = "var name = str james"
vars = {}
def new_var(name, value):
  vars[name] = value
code = "n  = str hello"
lines = code.split("\n")
for line in lines:
  tokens = line.split()
  if tokens[0] == "var":
    #var declaration 
    if tokens[3] == "str":
      new_var(tokens[1], str(tokens[-1])

print(vars)
      
    
