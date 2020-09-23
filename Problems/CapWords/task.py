text = input()
text = text.split("_")
i= 0
while i < len(text):
    text[i] = text[i].capitalize()
    i +=1
text = "".join(text)
print(text)