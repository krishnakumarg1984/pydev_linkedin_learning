# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if booktype not in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid book type")
        self.booktype = booktype


# TODO: access the class attribute
print("Book types: ", Book.getbooktypes())


# TODO: Create some book instances
b1 = Book("Title 1", "HARDCOVER")
# b2 = Book("Title 2", "COMIC")
b2 = Book("Title 2", "PAPERBACK")

# TODO: Use the static method to access a singleton object (singleton design pattern)
thebooks = Book.getbooklist()  # is a static function
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)

# you want to make a class callable and not have its state modified

# static methods don't modify the state of the class or a specific object instance
# not many great uses
# scenario:
# And I should point out here that there aren't really that many great use cases for static methods. They are useful, however, for scenarios where you don't need to access any properties of a particular object or the class itself but where it makes sense for the method to belong to the class. In other words it's a good way of name spacing certain kinds of methods. Whereas you might in another way create a global function, this is a way of taking a global function and just putting it in the classes namespace. So one good example of static methods is to implement a singleton design pattern. And remember, the singleton design pattern let's us make sure that only one instance of a particular variable or object is ever created. So let's imagine that we wanted to have book class to be responsible for keeping track of a list of books. Now we could create a global variable to hold all the books but it might be a better approach to encapsulate that behavior within the book class. So what I'm going to do here is create a double underscore attribute named booklist. And remember, the double underscore essentially makes this a private variable. And we saw this previously in the chapter. And then I'll define a static method that exposes this property to the consumers of the book class. So I'll initialize this to none and then I'll create a static method to access it. So to create a static method I need to use the static method decorator. And then I'll define my method. I'll call it getbooklist. So then I can check to see if the booklist attribute is null and create a new list. So if book.__booklist is none then I'll just create a new one. And if it's already been created, then we'll just return the existing one. So now let's use this feature to add our books to a list. So I'm going to scroll down to the bottom here and I'll write some code. So I'll create a books variable and I'll assign it to the result of getbooklist. Now remember, this is a static function. It's on the book class, but it doesn't actually modify the class's state. So then I'll write thebooks and I'll append book one and then I'll append book two and then we'll print out thebooks. All right, so let's go ahead and run this. And here in the output we can see that our books are being added to the list. And remember, we've ensured in our logic that only one of these will ever be created. Right, so if it's none, then we create it. Otherwise we just return the existing one. So we've namespaced what would otherwise be a global function to our booklist and this is one of the good uses of a static method. There are some other ones, but more the most part they're really useful for namespacing what would otherwise be a global function into the namespace of a class.
