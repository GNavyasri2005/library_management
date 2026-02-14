class book:
    def __init__(self,bookid,title,author):
        self.bookid=bookid
        self.author=author
        self.title=title
        self.isavailable=True
        pass
    #get book details
    def book_details(self):
        return f"book name is {self.title} and author name is {self.author}"
        pass
    #convert book details to dictionary
    def to_dict(self):
        book={}
        book["self.bookid"]=self.bookid
        book["self.title"]=self.title
        book["self.author"]=self.author
        book["self.isvailable"]=True
        return book