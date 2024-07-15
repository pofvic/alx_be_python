class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = 0
        self.is_checkout_out = False

    def check_out(self):
        self.is_checkout_out = True

    def return_book(self):
        self.is_checkout_out = False

    def is_available(self):
        return not self.is_checkout_out


class Library:
    def __init__(self):
        self.books = []
