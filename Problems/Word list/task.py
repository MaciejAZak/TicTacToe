len_dist = int(input())

text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

list = [word for sentence in text for word in sentence if len(word) <= len_dist]


#for sentence in text:
#        for word in sentence:
#                if len(word) <= len_dist:
#                        list.append(word)

print(list)