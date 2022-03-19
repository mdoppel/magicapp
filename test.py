import json

#-------------------------------------
#Import Files
with open('AllPrintings.json', encoding = 'utf-8') as json_file:
    allprintresults = json.load(json_file)

with open('AllPrices.json') as json_file:
    allpriceresults = json.load(json_file)    

#-------------------------------------

#-------------------------------------
#Data holders
cards = {}
ownerlist=[]
setlist=[]
cardnumber=[]
cardnumber1=[]
id=0
rare = []
pricedollar=[]
blpricedollar=[]
tcgpricedollar=[]
foil = "f"
token = "t"
date = ""
set = 'NEO'
number1 = '507'
#-------------------------------------
if "f" in number1:
        number1 = number1.replace('f','')
        foil = "Foil"
else:
    number1 = number1
    foil = "Not Foil"

# setsize = allprintresults['data'][set]['baseSetSize']
# print(setsize)
count = 0
# while count <= setsize:
for i in allprintresults['data'][set]['cards']:
    if number1 == allprintresults['data'][set]['cards'][count]['number']:
        card_name = allprintresults['data'][set]['cards'][count]['name']
        card_uuid = allprintresults['data'][set]['cards'][count]['uuid']
        card_rarity= allprintresults['data'][set]['cards'][count]['rarity']
        if foil == "Foil":
            try: 
                CKfoil_buylistprice = allpriceresults['data'][card_uuid]['paper']['cardkingdom']['buylist']['foil']
                ckbuylistkey = list(CKfoil_buylistprice.keys())[-1]
                ckbuylistprice = CKfoil_buylistprice[ckbuylistkey]
            except:
                ckbuylistprice = "0"
            try:
                CKfoil_retailprice = allpriceresults['data'][card_uuid]['paper']['cardkingdom']['retail']['foil']
                ckretailkey = list(CKfoil_retailprice.keys())[-1]
                ckretailprice = CKfoil_retailprice[ckretailkey]
            except:
                ckretailprice = "0"
        elif foil=="Not Foil":
            try:
                CKfoil_buylistprice = allpriceresults['data'][card_uuid]['paper']['cardkingdom']['buylist']['normal']
                ckbuylistkey = list(CKfoil_buylistprice.keys())[-1]
                ckbuylistprice = CKfoil_buylistprice[ckbuylistkey]
            except:
                ckbuylistprice = "0"
            try:    
                CKfoil_retailprice = allpriceresults['data'][card_uuid]['paper']['cardkingdom']['retail']['normal']
                ckretailkey = list(CKfoil_retailprice.keys())[-1]
                ckretailprice = CKfoil_retailprice[ckretailkey]
            except:
                ckretailprice = "0"
        else:
            ckbuylistprice = "0"
            ckretailprice = "0"     
        break
    else:
        count=count+1

print(card_name)
print(card_rarity)
print(card_uuid)
print(foil)
print(ckretailprice)
print(ckbuylistprice)

# #-------------------------------------
# #User input stuff
# print("---------------------")
# print("Name of Owner")
# owner = input()
# print("---------------------")

# print("Enter Set Code")
# set = input()
# print("---------------------")
# print("List cards by number")
# print("---------------------")
# print("Hit enter after each card [f to denote foil; t for token; q to quit; r to remove last; p to print list]")
# #-------------------------------------

# #-------------------------------------
# #Add new data
# while True:
#     data = input()
#     if foil in data:
#         nfdata = data.replace('f','')
#         if k == allprintresults[]
#         for k, v in allprintresults.items():
#             for k1, v1 in v.items():
#                 if k1 == set:
#                     for k2, v2 in v1.items():
#                         if k2 == nfdata:
#                             for k3, v3 in v2.items():
#                                 idNumber = k
#                                 name = k3
#                                 rarity = v3
#                                 for k4, v4 in allpriceresults['data'].items():
#                                     if k4==idNumber:
#                                         for k5, v5 in v4.items():
#                                             for k6,v6 in v5.items():
#                                                 if k6 == "cardkingdom":
#                                                     cardkingdom = k6
#                                                     for k7,v7 in v6.items():
#                                                         markettype = k7
#                                                         if k7 == "retail":
#                                                             for k8,v8 in v7.items():
#                                                                 if k8=="foil":
#                                                                     for k9,v9 in v8.items():
#                                                                         if k9 == date:
#                                                                             cardtype="Foil"
#                                                                             pricedate = k9
#                                                                             cardkingdomprice = v9
#                                                                             id= id+1
#                                                                             print(k9, name, " - ", rarity, cardtype," - Cardkingdom - Retail ",cardkingdomprice)
#                                                         # else:
#                                                         #     print("No Retail Price")  
#                                                         #     cardkingdomprice = 0                                                      
#                                                         if k7 == "buylist":
#                                                             for k8,v8 in v7.items():
#                                                                 if k8=="foil":
#                                                                     for k9,v9 in v8.items():
#                                                                         if k9 == date:
#                                                                             cardtype="Foil"
#                                                                             pricedate = k9
#                                                                             ckblprice = v9
#                                                                             id= id+1
#                                                                             print(k9, name, " - ", rarity, cardtype," - Cardkingdom - Buylist ",ckblprice)                    
#                                                         # else:
#                                                         #     print("No Buylist Price")
#                                                         #     ckblprice = 0
#                                                 if k6 == "tcgpplayer":
#                                                     source = k6
#                                                     for k7,v7 in v6.items():
#                                                         markettype = k7
#                                                         if k7 == "retail":
#                                                             for k8,v8 in v7.items():
#                                                                 if k8=="foil":
#                                                                     for k9,v9 in v8.items():
#                                                                         if k9 == date:
#                                                                             cardtype="Foil"
#                                                                             pricedate = k9
#                                                                             tcgprice = v9
#                                                                             id= id+1
#                                                                             print(k9, name, " - ", rarity, cardtype," - TCGPlayer - ",tcgprice)                                                                            
#                                                 # else:
#                                                 #     print("No TCG Price")
#                                                 #     tcgprice=0   
#     elif token in data:
#         nfdata = data.replace('t','')
#         for k, v in alltokenresults.items():
#             for k1, v1 in v.items():
#                 if k1 == set:
#                     for k2, v2 in v1.items():
#                         if k2 == nfdata:
#                             idNumber = k
#                             name = v2
#                             for k4, v4 in allpriceresults['data'].items():
#                                 if k4==idNumber:
#                                     for k5, v5 in v4.items():
#                                         for k6,v6 in v5.items():
#                                             if k6 == "cardkingdom" or k6=="tcgplayer":
#                                                 source = k6
#                                                 for k7,v7 in v6.items():
#                                                     markettype = k7
#                                                     if k7 == "retail":
#                                                         for k8,v8 in v7.items():
#                                                             if k8=="normal":
#                                                                 for k9,v9 in v8.items():
#                                                                     if k9 == date:
#                                                                         cardtype="Token"
#                                                                         pricedate = k9
#                                                                         price = v9
#                                                                         id= id+1                                                                        
#                                                                         print(k9, name, " - ", price, cardtype) 
#     else:
#         for k, v in allprintresults.items():
#             for k1, v1 in v.items():
#                 if k1 == set:
#                     for k2, v2 in v1.items():
#                         if k2 == data:
#                             for k3, v3 in v2.items():
#                                 idNumber = k
#                                 name = k3
#                                 rarity = v3
#                                 for k4, v4 in allpriceresults['data'].items():
#                                     if k4 == idNumber:
#                                         for k5, v5 in v4.items():
#                                             for k6,v6 in v5.items():
#                                                 if k6 == "cardkingdom":
#                                                     source = k6
#                                                     for k7,v7 in v6.items():
#                                                         markettype = k7
#                                                         if k7 == "retail":
#                                                             for k8,v8 in v7.items():
#                                                                 if k8=="normal":
#                                                                     for k9,v9 in v8.items():
#                                                                         if k9 == date:
#                                                                             cardtype="Normal"
#                                                                             pricedate = k9
#                                                                             cardkingdomprice = v9
#                                                                             id= id+1
#                                                                             print(k9, name, " - ", rarity, cardtype," - Cardkingdom - Retail ",cardkingdomprice)
#                                                         # else:
#                                                         #     print("No Retail Price")      
#                                                         #     cardkingdomprice = 0                                                  
#                                                         if k7 == "buylist":
#                                                             for k8,v8 in v7.items():
#                                                                 if k8=="normal":
#                                                                     for k9,v9 in v8.items():
#                                                                         if k9 == date:
#                                                                             cardtype="Normal"
#                                                                             pricedate = k9
#                                                                             ckblprice = v9
#                                                                             id= id+1
#                                                                             print(k9, name, " - ", rarity, cardtype," - Cardkingdom - Buylist ",ckblprice)                                                    
#                                                         # else:
#                                                         #     print("No Buylist Price")    
#                                                         #     ckblprice = 0                                            
#                                                 if k6 == "tcgplayer":
#                                                     source = k6
#                                                     for k7,v7 in v6.items():
#                                                         markettype = k7
#                                                         if k7 == "retail":
#                                                             for k8,v8 in v7.items():
#                                                                 if k8=="normal":
#                                                                     for k9,v9 in v8.items():
#                                                                         if k9 == date:
#                                                                             cardtype="Normal"
#                                                                             pricedate = k9
#                                                                             tcgprice = v9
#                                                                             id= id+1
#                                                                             print(k9, name, " - ", rarity, cardtype," - TCGPlayer - ",tcgprice)      
#                                                 # else:
#                                                 #     print("No TCG Price")
#                                                 #     tcgprice=0
#     data1 = data
#     if data == '0' or data == "":
#         print("Not acceptable number")
#     elif str.lower(data) == "q":
#         break
#     elif str.lower(data) == "r":
#         last = cardnumber[-1]
#         print(cardnumber[-1], pricedollar[-1])
#         del cardnumber[-1]
#         del pricedollar[-1]
#     elif str.lower(data) == "p":
#         print (cardnumber) 
#     else:
#         cardnumber.append(data)
#         pricedollar.append(cardkingdomprice)
#         blpricedollar.append(ckblprice)
#         tcgpricedollar.append(tcgprice)
#         print("CardKingdom Retail ", len(pricedollar)," - ", sum(pricedollar), " - ", round(sum(pricedollar)/len(pricedollar),2))
#         print("CardKingdom Buylist ", len(blpricedollar)," - ", sum(blpricedollar), " - ", round(sum(blpricedollar)/len(blpricedollar),2))
#         print("TCG Price ", len(tcgpricedollar)," - ", sum(tcgpricedollar), " - ", round(sum(tcgpricedollar)/len(tcgpricedollar),2))
#         cardnumber1.append({"id": id, "owner": owner, "set": set, "uuid": idNumber, "cardname": name, "rarity": rarity})
# #-------------------------------------


# #-------------------------------------
# #Put data into Dict
# if owner in results and set in results[owner]:
#     for number in cardnumber:
#         results[owner][set].append(number) 
# elif owner in results:
#     results[owner][set] = cardnumber
# else:
#     results[owner] = {set:cardnumber}
# #-------------------------------------


# #-------------------------------------
# #Drop into json
# with open('cardportfolio.json', 'w') as fp:
#     json.dump(results, fp)
#-------------------------------------
