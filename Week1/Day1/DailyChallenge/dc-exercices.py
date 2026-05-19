# Challenge 1

"""
numb=int(input("Enter your number: "))
length=int(input("Enter a length: "))
e=[i*numb for i in range(1,length+1)]
print(f" number: {numb} - length {length} ➞ {e}")
"""

# Challenge 2
result=""  # storage of letter
word=input("Enter your word: ")
for i in range(len(word)):
    if i==0:
        # supprimer le doublon
        result+=word[i]
    elif  word[i]!=word[i-1] :
        result+=word[i]

print(f"user's word : {word}  ➞  {result}")
 
