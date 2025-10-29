class Text:
  def __init__(self, text, iterateBy="chars"):
    self.text = text
    self.index = 0
    self.iterateBy = "words"

def find_amount(self, key):
  return self.text.count(key)
  
def find_index(self, key):
  return self.text.find(key)

def __iter__(self):
  return self

def __next__(self):
  if self.iterateBy == "chars":
    if self.index < len(self.text):
      item = self.text[self.index]
      self.index += 1
      return item
    else:
      raise StopIteration
  if self.iterateBy == "words":
    if self.index < len(self.text.split()):
      self.words = self.text.split()
      self.index2 = self.text.index(self.words[self.index])
      item = self.text[self.index2]
      return item
    else:
      raise StopIteration
  
    
