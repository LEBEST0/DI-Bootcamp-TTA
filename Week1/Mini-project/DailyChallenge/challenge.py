# Défi 1

"""

saisie=input("Enter your senquence of word separate by comma: ")

sep=saisie.split(",")
sep.sort()
print(sep)

ordseq=",".join(sep)

print(ordseq)


"""

# Défi 2

def longest_word(word):
    separated=word.split(" ")
    a=0
    for e in separated:
        if len(e)>a:
            a=len(e)
            word_f=e
    print(word_f)

longest_word("Forgetfulness is by all means powerless!")
