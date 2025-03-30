# Shelf-Help Book Recommender
Like self-help, but with books. For your mental bookshelf.

This project is a command-line book recommendation system designed to **practice core data structures and algorithms using Python**. The main goal is not to build a real recommender engine, but to **apply fundamental concepts** like **linked lists**, **merge sort**, and **binary search** in a realistic scenario using book data.

## Main Learning Goals

- Understand, implement and use custom linked lists
- Practice merge sort on lists of dictionaries
- Implement binary search for strings
- Design a clean and modular object-oriented structure

## Class Documentation

### LinkedList (in models/linked_list.py)

Custom implementation of a linked list to store and manage book dictionaries.

**Features**:

- `append(book)`: Adds a new book node to the end of the list
- `display_all()`: Prints all books in the list
- `get_books_data(data)`: Returns a list of values from each book for a specific key (e.g. 'title')
- `get_all_books()`: Returns all stored book dictionaries in the linked list

### BookAlgorithms (in models/book_algorithms.py)

A class providing sorting and searching operations on a list of dictionaries (e.g., book data).

**Features**:

- `merge_sort_books()`: Sorts the list using merge sort by the selected key (e.g. score or title)
- `binary_search_inside_list(searching_element)`: Performs binary search on the sorted list by the given key. Works with strings and numbers.

## To-Do List

- Implement `binary_search_inside_linkedlist()` function inside BookAlgotithms class
- Handle case-insensitive string comparisons (e.g. lower())
- **Add CLI prompts to interact with user preferences (genre, mood)**
- Implement quick sort for comparison
- Add exception handling and input validation
- **Use Book class object instead of raw dictionaries**

## Manual Setup

If you prefer manually setting up the environment, follow these steps:

1. Clone the repository: `git clone https://github.com/AnzelaMachackova/shelf-help-book-recommender`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Run the main script: `python3 main.py` with the repositories.