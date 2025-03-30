class BookAlgorithms:
    """
    The BookAlgorithms class provides algorithmic utilities for working with a list of book-like dictionaries. 
    Its primary purpose is to support sorting and searching operations to enhance book recommendation systems.
    """
    def __init__(self, data, sorting_element):
        self.data = data
        self.sorting_element = sorting_element
    
    def merge_sort_books(self, data_list=None):
        if not data_list:
            data_list = self.data
        if len(data_list) <= 1:
            return data_list
        middle = len(data_list) // 2
        left = data_list[:middle]
        right = data_list[middle:]
        sleft = self.merge_sort_books(left)
        sright = self.merge_sort_books(right)
        return self.merge_books(sleft, sright)

    def merge_books(self, left, right):
        sorted_books_lst = []
        while (left and right):
            if left[0][self.sorting_element] < right[0][self.sorting_element]:
                sorted_books_lst.append(left[0])
                left.pop(0)
            else:
                sorted_books_lst.append(right[0])
                right.pop(0)
        if left:
            sorted_books_lst += left
        if right:
            sorted_books_lst += right
        
        return sorted_books_lst
    
    # TODO: implement lower(), function binary_search_inside_linkedlist()
    def binary_search_inside_list(self, searching_element):
        sorted_data = self.merge_sort_books()
        left_pointer = 0
        right_pointer = len(sorted_data) - 1
        
        while left_pointer < right_pointer:
            middle_index = (left_pointer + right_pointer) // 2
            middle_value = sorted_data[middle_index][self.sorting_element]
            if middle_value == searching_element:
                return sorted_data[middle_index]
            if searching_element < middle_value:
                right_pointer = middle_index
            if searching_element > middle_value:
                left_pointer = middle_index + 1
        return None
    