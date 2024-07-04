from booklover import booklover

obj = booklover.BookLover('Alex', 'zy7ts@virginia.edu', 'sci-fy')
obj.add_book(
    'New book',
    5
)
print(f' the number of books read is {obj.num_books_read()}')