from models.linked_list import LinkedList
import json

book_data_json_path = 'data/books_data.json'

with open(book_data_json_path, 'r', encoding='utf-8') as book_data_json:
    book_data = json.load(book_data_json)

my_books = LinkedList()
for book in book_data:
    my_books.append(book)

#my_books.display_all()

print(my_books.head.book)

fiction_list = LinkedList()

for book in book_data:
    if book['genre'] == 'Fiction':
        fiction_list.append(book)

print(fiction_list.get_books_data('title'))
print(fiction_list.get_all_books()[1])
