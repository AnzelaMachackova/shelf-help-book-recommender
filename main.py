from models.linked_list import LinkedList
import json
from models.book_algorithms import BookAlgorithms
import data.inputs
from data.helpers import genre_letter_dict, mood_letter_dict

book_data_json_path = 'data/books_data.json'

with open(book_data_json_path, 'r', encoding='utf-8') as book_data_json:
    book_data = json.load(book_data_json)

my_books = LinkedList()
for book in book_data:
    my_books.append(book)

def main():
    print(data.inputs.book_img)
    print(data.inputs.welcome_message)
    play_again = True
    while play_again:
        genre_letter = input(data.inputs.select_genre)
        if genre_letter.lower().strip() in genre_letter_dict.keys():
            genre = genre_letter_dict[genre_letter.lower().strip()]
        else:
            print("Incorrect input. Please, start again...")
            continue
        print("Your selected genre is: " + genre)

        book_class_for_binary_search_genre = BookAlgorithms(book_data, "genre")
        selected_genre_list = book_class_for_binary_search_genre.binary_search_inside_list(genre)
        mood_letter = input(data.inputs.select_mood)
        
        if mood_letter.lower().strip() in mood_letter_dict.keys():
            mood = mood_letter_dict[mood_letter.lower().strip()]
        else:
            print("Incorrect input. Please, start again...")
            continue

        print("Your selected mood is: " + mood)
        print(data.inputs.approval_message)
        book_class_for_binary_search_mood = BookAlgorithms(selected_genre_list, "mood")
        selected_mood_list = book_class_for_binary_search_mood.binary_search_inside_list(mood)
        
        if selected_mood_list:
            print(f"First suggested book is: {selected_mood_list[0]}")
        else:
            print("There is no book for the specified criteria, we are sorry.")
        
        continue_game = input("Would you like to search for another book recommendation? (y/n)\n")
        if continue_game.lower().strip() != "y":
            print(data.inputs.goodbye_message)
            play_again = False

if __name__ == "__main__":
    main()