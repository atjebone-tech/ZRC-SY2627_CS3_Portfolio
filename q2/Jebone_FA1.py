
class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = 1
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if isinstance(number_of_pages, int) and not isinstance(number_of_pages, bool) and number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print("Number of Pages:", self.__number_of_pages)


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 1
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if isinstance(issue_number, int) and not isinstance(issue_number, bool) and issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")

    def display_info(self):
        super().display_info()
        print("Issue Number:", self.__issue_number)


publication1 = Publication("Introduction to Science", "John Smith")
publication2 = Publication("Computer Fundamentals", "Mary Santos")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 350)

magazine1 = Magazine("National Geographic", "Various Authors", 202)
magazine2 = Magazine("Science Today", "Science Editors", 15)


print("=== PUBLICATION 1 ===")
publication1.display_info()

print("\n=== PUBLICATION 2 ===")
publication2.display_info()


print("\n=== BOOK 1 ===")
book1.display_info()

print("\n=== BOOK 2 ===")
book2.display_info()


print("\n=== MAGAZINE 1 ===")
magazine1.display_info()

print("\n=== MAGAZINE 2 ===")
magazine2.display_info()


print("\n=== GETTER METHODS ===")
print("Book Title:", book1.get_title())
print("Number of Pages:", book1.get_number_of_pages())
print("Magazine Issue:", magazine1.get_issue_number())


print("\n=== SETTER METHODS ===")
book1.set_number_of_pages(320)
magazine1.set_issue_number(203)

print("Updated Book Pages:", book1.get_number_of_pages())
print("Updated Magazine Issue:", magazine1.get_issue_number())


print("\n=== DATA VALIDATION ===")
book1.set_number_of_pages(-10)
magazine1.set_issue_number(0)
