import jsonpath
import json

obj = json.load(open(file='store.json',mode='r',encoding='utf-8'))

# 获取书店所有书的作者
author_list = jsonpath.jsonpath(obj,'$.store.book[*].author')
print(author_list)

# 所有的作者
author_all = jsonpath.jsonpath(obj,'$..author')
print(author_all)

# store所有的元素，所有的books和bicycle
store = jsonpath.jsonpath(obj,'$.store.*')
print(store)

# store里面所有东西的price
price_list = jsonpath.jsonpath(obj,'$.store..price')
print(price_list)

# store书中第三本书
book = jsonpath.jsonpath(obj,'$.store.book[2]')
print(book)

# store中最后一本书
book_last = jsonpath.jsonpath(obj,'$.store.book[(@.length-1)')
print(book_last)

# 前面的两本书
booK_list = jsonpath.jsonpath(obj,'$.store.book[:2]')
print(booK_list)

# 过滤出所有的包含isbn的书
book_isbn = jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
print(book_isbn)

# 过滤出价格低于10的书
book_price = jsonpath.jsonpath(obj,'$..book[?(@.price<10)]')
print(book_price)
