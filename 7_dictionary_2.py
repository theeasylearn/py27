# concept of dictionary,list,tuples as nested structure (empty)
book = {}
print(book)
book['name'] = "Secret"
book['price'] = 500
book['author'] = "unknown"
print(book)
book['chapters'] = (1,2,3,4,5) #tuple inside dictionary
book['topics'] = ['intorudction to thinking','logical thinking','creative thinking','summery']
print(book)

#is it possible
# del book['chapters']
# del book['chapters'][0]
print(book)
# book['chapters'][0] ='introduction' #read only
book['topics'][0] ='introduction' #read only
print(book)