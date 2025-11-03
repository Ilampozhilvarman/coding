code = "num n,9"
vars = {}
data_types = ["str", "num", "obj", "lst"]
def new_var(name, value):
  vars[name] = value
lines = code.split("\n")
for line in lines:
  if line[:3] in data_types:
    type = line[:3]
    if type == "num":
      new_var(line[4:line.index(",")+1], int(line[line.index(",")+1:]))
    elif type == "str":
      new_var(line[4:line.index(",")+1], str(line[line.index(",")+1:]))
    elif type == "obj":
      pass
    elif type == "lst":
      pass
    else:
      ValueError(f"{token[:3]} is not a valid type")
print(vars)
      
    
