class Text:
  def __init__(self, text, iterateBy="chars"):
    self.text = text
    self.index = 0
    self.iterateBy = "words"
    self.changes = {
      "find_amount": 0
      "find_index": 0
      "remove": 0
      "delete_all": 0
      "reverse": 0
    }
  
  def change(self, change):
    if change in self.changes:
      self.changes[change] += 1
    else:
      raise Exception("Something went wrong")

  def find_amount(self, key):
    return self.text.count(key)
    self.change("find_amount")
    
  def find_index(self, key):
    return self.text.find(key)
    self.change("find_index")
  
  def remove(self, key):
    if not key in self.text:
      raise Exception("Key not in text")
    self.change("remove")
    
    self.text = self.text.replace(key, "")

  def delete_all(self):
    self.text = ""
    self.change("delete_all")

  def reverse(self):
    self.text = self.text[::-1]
    self.change("reverse")
  
  def __str__(self):
    return f"{self.text}"
  
  def __repr__(self):
    if len(self.text) > 20:
      return f"{self.text[:10]}...{self.text[-10:]}\nchanges: {self.changes}"

  def delete_key(self, key, amount=1):
    for i in range(amount):
      self.text = self.text.replace(key, "")



  
    
