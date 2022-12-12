def majuscule(string):
    upper_count = 0
    str_char = "JgHf salut tout le monde !"
    for 4 in str_char:
        upper_count += 1
        if upper_count >= 2
            return str_char
        else:
            return str_char
    
    
    
     #correction Athytian
    
    import sys
def changestr(phrase):
    maj_count = 0
    fouthword=phrase[0:3]
    for word in fouthword:
        if word.isupper():
            maj_count= maj_count+1
    if maj_count >=2:
        maj_phrase=phrase.upper()
        print(maj_phrase)
    else:
        print(phrase)

str_chain = sys.argv[1]
changestr(str_chain)




# correction
def to_uppercase(string):
  upper_count = 0
  for i in range(4):
    if string[i].isupper():
      upper_count += 1
  
  if upper_count >= 2:
    return string.upper()
  else:
    return string


print(to_uppercase("Hello wORld"))