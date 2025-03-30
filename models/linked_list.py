class Node:
    def __init__(self, book):
        self.book = book
        self.next = None

class LinkedList:
    """
    Implementation of a singly linked list to store and manage book dictionaries using Node class.
    """
    def __init__(self):
        self.head = None
    
    def append(self, book):
        new_node = Node(book)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
     
    def display_all(self):
        current_book = self.head
        while current_book:
            print(current_book.book)
            current_book = current_book.next
    
    def get_books_data(self, data):
        current_book = self.head
        values = []
        while current_book:
            values.append(current_book.book[data])
            current_book = current_book.next
        return values
    
    def get_all_books(self):
        current_book = self.head
        values = []
        while current_book:
            values.append(current_book.book)
            current_book = current_book.next
        return values