class Text:
  def __init__(self, text, iterateBy="chars"):
    self.text = text
    self.index = 0
    self.iterateBy = "words"
    self.changes = 0
  
  def change(self):
    self.change += 1

  def find_amount(self, key):
    return self.text.count(key)
    self.change()
    
  def find_index(self, key):
    return self.text.find(key)
    self.change()
  
  def remove(self, key):
    if not key in self.text:
      raise Exception("Key not in text")
    self.change()
    
    self.text = self.text.replace(key, "")

  def delete(self):
    self.text = ""
    self.change()

  def reverse(self):
    self.text = self.text[::-1]
    self.change()
  
  def __str__(self):
    return f"{self.text}"


  
    
