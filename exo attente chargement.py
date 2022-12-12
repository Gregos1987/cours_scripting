#remplacer dans un fichier les 'hello world' par 'bonjour'

with open("fichier.txt", "a") as f:
    f.write("hello world\nhello world\nhello world\nhello world\nhello world\n")
    
with open("fichier.txt", "a") as f1:
    if "hello world":
        str.replace('hello world','bonjour')