class Library:
    shop_name="zayied ettante library kada"

    def __init__(self):
        self.books=[]

    def add_book(self):
        book_id=int(input("enter the Book ID:"))
        for book in self.books:
            if book['book_id']==self.books:
                print("book already exist with this id! try another id")
                return

        else:    
            book_title=input("enter the Book title:")
            author=input("enter author name:")
            book_price=int(input("enter the book price:"))
            if book_price>0:
                book={
                    "book_id":book_id,
                    "book_title":book_title,
                    "book_author":author,
                    "book_price":book_price,
                    "Available":True
                }
                self.books.append(book)
                print("book added successfully")
            else:
             print("book price must be greater than 0")


    def display_book(self):
        if self.books:
            for book in self.books:
                print(f"Book ID          : {book['book_id']}")
                print(f"Book title       : {book['book_title']}")
                print(f"author           :  {book['book_author']}                    ")
                print(f"Book price       : {book['book_price']}")
                print(f"Availibile       : {book['Available']}")
                print("        *------------*       ")
        else:
            print("No books found!")

    def search_book(self):
        book_id=int(input("enter book id :"))
        for book in self.books:
            if book.get('book_id')==book_id:
                 print(f"Book ID         : {book['book_id']}")
                 print(f"Book title      : {book['book_title']}")
                 print(f"Author          : {book['book_author']}")
                 print(f"Book price      : {book['book_price']}")
                 print(f"Availibile      : {book['Available']}")
                 print("        *------------*       ")
                 break
            
        else:
            print("Book does not exist")

    def update_book(self):
        book_id=int(input("enter the book id:"))
        for book in self.books:
            if book.get('book_id')==book_id:
                choice=int(input("1.update Book Name\n2.Update Author\n 3. Update price\nEnter your choice:"))
                if choice==1:
                    new_book_name=input("enter new book name:")
                    book['book_title']=new_book_name
                    print(f"book name updated to{new_book_name}")
                elif choice==2:
                    new_author=input("enter new author name:")
                    book['book_author']=new_author
                    print(f"book author name updated to{new_author}")
                elif choice==3:
                    new_price=int(input("enter the new price:"))
                    book['book_price']=new_price
                    print(f"book price updated to {new_price}")
                else:
                    print("Invalid updation choice")
                break
        else:
            print("book does not exissst")
    def issue_book(self):
        book_id=int(input("enter the Book id :"))
        for book in self.books:
            if book['Available']:
                book['Available']=False
                print("book issued succesfully")
            else:
                print("book is already issued")
            break
        else:
            print("book does not exist")

    def return_book(self):
        book_id=int(input("enter the book id:"))
        for book in self.books:
            if book['Available']:
                print("book is already available")
            else:
                book['Available']=True
                print("book returned successfully")
            break
        else:
            print("Book does not exist")

    def Delete_book(self):
        book_id=int(input("enter you book id:"))
        for book in self.books:
            if book['Available']:
                self.books.remove(book)
                print("book has been removed")
            else:
                print("book cannot be deleted ")
            return
        else:
            print('book not exist')



l1=Library()
print("===============LIBRARY MANAGEMENT SYSTEM================")
while True:
    choice=int(input("1.Add Book\n2.Display Books\n3.Search Book\n4.Update Book\n5.Issue Book\n6.Return Book\n7.Delete Book\n8.Exit\n Enter Your choice:"))
    if choice==1:
        l1.add_book()
        print("------------------------------")
    elif choice==2:
        l1.display_book()
        print("------------------------------")
    elif choice==3:
        l1.search_book()
        print("------------------------------")
    elif choice==4:
        l1.update_book()
        print("------------------------------")
    elif choice==5:
        l1.issue_book()
        print("------------------------------")
    elif choice==6:
        l1.return_book()
        print("------------------------------")
    elif choice==7:
        l1.Delete_book()
        print("------------------------------")
    elif choice==8:
        break
    else:
        print("enter a valid choice")

