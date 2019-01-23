def is_isogram(word):
    if type(word) == str:
      for i in word:
        if word.count(i) >1 or word == "":
          return print("NO")
        else:
          return print("YES")
    else:
      raise TypeError ("'{}' should be a string" .format(word))
s=input()
is_isogram(s)
