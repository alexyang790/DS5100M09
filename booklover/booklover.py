import pandas as pd
class BookLover():
    def __init__(self, name, email, fav_genere):
        self.name = name
        self.email = email
        self.fav_genere = fav_genere
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def add_book(self, book_name, rating):
        if not book_name in self.book_list['book_name'].values: #checking if book already exists
            #frame new book & rating and concat to book list
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1

    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
    
    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]