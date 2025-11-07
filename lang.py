code = "emp n"
vars = {}
data_types = ["str", "num", "obj", "lst", "emp"]
def new_var(name, value):
  vars[name] = value
lines = code.split("\n")
for line in lines:
  if line[:3] in data_types:
    type = line[:3]
    comma_index = line.index(",")
    name = line[4:comma_index+1]
    value = line[comma_index+1:]
    if type == "num":
      new_var(name, int(values))
    elif type == "str":
      new_var(name, str(values))
    elif type == "obj":
      values = line[comma_index+2:]
      if not value:
        new_var(line[name], {})
        continue
      obj = {}
      for value in values.split():
        try:
          obj.update({str(value[0]): value[2]})
        except IndexError:
          obj.update({str(value[0]): None})
      new_var(name, obj)
    elif type == "lst":
      new_var(name, line[comma_index+2:].split())
    elif type == "emp"
      new_var(name, None)
  else:
    ValueError(f"{token[:3]} is not a valid type")
print(vars)
      
    
