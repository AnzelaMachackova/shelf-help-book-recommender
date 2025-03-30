from models.linked_list import LinkedList
import json
from models.book_algorithms import BookAlgorithms

book_data_json_path = 'data/books_data.json'

with open(book_data_json_path, 'r', encoding='utf-8') as book_data_json:
    book_data = json.load(book_data_json)

my_books = LinkedList()
for book in book_data:
    my_books.append(book)

#my_books.display_all()

#print(my_books.head.book)

fiction_list = LinkedList()

for book in book_data:
    if book['genre'] == 'Fiction':
        fiction_list.append(book)

#print(fiction_list.get_books_data('title'))
#print(fiction_list.get_all_books()[1])

# test for merge sort 
my_list = [{"key": 1, "value": "hello"}, {"key": 3, "value": "hello"}, {"key": 2, "value": "hello"}]
my_sorting_element = "key"
book_class_for_score_search = BookAlgorithms(my_list, my_sorting_element)

# print(book_class_for_score_search.merge_sort_books())

# test for binary search 
my_sorting_element_for_title = "title"
book_class_for_binary_search = BookAlgorithms(book_data, my_sorting_element_for_title)

searching_value = "Lessons in Chemistry"
searching_value_index = book_class_for_binary_search.binary_search_inside_list(searching_value)
print(searching_value_index)