
n = input("Give a value for variable n: ")
text  = input("What's your text input?: ")

textsplit = text.split()

checkvid = [0,0]

finaltext = "none"
sectext = "none"

for word in textsplit:
    if len(word) >= int(n):
        if finaltext == "none":
            finaltext = word
        else:
            finaltext = finaltext + "\n" + word
        checkvid[0] = 1
    else:
        if sectext == "none":
            sectext = word
        else:
            sectext = sectext + "\n" + word
        checkvid[1] = 1

finaltext = finaltext + "\n" + sectext
if checkvid[1] == 1 and checkvid[0] == 1:
    print(finaltext)
else:
    print("nu exista")