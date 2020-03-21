#dictionary of dictionaries
itemDictionary = {'Mr.A': {'apples': 5, 'pretzels': 12, 'Candies': 25},
         'Mr.B': {'cups': 3, 'apples': 2} ,
         'Mr.C':{'cups': 3, 'pretzels': 1}}

# this method returns all the unique items in the sub dictionary
def getUniqueItems(items):
    newCounter = set()
    for v in items.items():
        for itemDic in v[1]:
            newCounter.add(itemDic)
    return(newCounter)

# returns the count of each item
def countParticularItem(bigDictionary, itemKey):
    itemCounter = 0
    for key, value in bigDictionary.items():
        itemCounter = itemCounter + value.get(itemKey,0)
    return itemCounter

uniqueItems = getUniqueItems(itemDictionary)
for uniqueItem in uniqueItems:
    print("Count for "+ uniqueItem+" is "+str(countParticularItem(itemDictionary,uniqueItem)) )
