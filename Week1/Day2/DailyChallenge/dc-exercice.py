# Challenge 1


dic={}
user_m=input("Enter a word: ")

for index,v in enumerate(user_m):
    if v in dic:
        dic[v].append(index)
    else:
        dic[v]=[index]
print(dic)


# Challenge 2: Affordable Items
cleaned_items={}
basket=[]
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

wallet_c=int(wallet.replace("$","").replace(",",""))

for cle, price in items_purchase.items():
    price=int(price.replace("$","").replace(",",""))
    cleaned_items[cle]=price

for cle, val in cleaned_items.items():
    if wallet_c>=val:
        basket.append(cle)
        wallet_c=wallet_c-val
    else:
        continue
if not basket :
    print("Nothing")
else:
    print(sorted(basket))
