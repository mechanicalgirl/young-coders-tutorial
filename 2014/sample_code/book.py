class Book:
    title = ""
    authors = []
    pages = 0

    def print_book(self):
        print self.title
        print "Authors"
        print "="*15
        for author in self.authors:
            print author
        print "Pages: ", self.pages
