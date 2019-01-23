def is_isogram(word):
    if type(word) == str:
      for i in word:
        if word.count(i) >1 or word == "":
          return print("No")
        else:
          return print("Yes")
    else:
      raise TypeError ("'{}' should be a string" .format(word))
s=input()
is_isogram(s)
