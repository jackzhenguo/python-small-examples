# class Book(object):
#     # 定义类的参数
#     def __init__(self, book_id, book_name, book_store_count):
#         self.book_id = book_id
#         self.book_name = book_name
#         self.book_store_count = book_store_count
#     # 定义加法操作

#     def __add__(self, book):
#         return self.book_store_count + book.book_store_count


# store_count = Book(1, 'python入门书', 100) + Book(2, '机器学习入门书', 200)
# print(store_count)


k = int(input())
print(f"I just input: {k}")
