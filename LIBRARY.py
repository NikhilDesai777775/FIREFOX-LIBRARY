books=[]
members=[]
borrowed_books={}

def add_book():
    title=input("Enter book title: ")
    author=input("Enter book author: ")
    book_id=len(books)+1
    books.append({"id":book_id,"title":title,"author":author,"available":True})
    print(f"Book '{title}' added successfully!")

def view_books():
    if not books:
        print("No books available.")
    else:
        for book in books:
            status="Available" if book["available"] else "Borrowed"
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {status}")

def update_book():
    book_id=int(input("Enter book ID: "))
    for book in books:
        if book["id"]==book_id:
            book["title"]=input("Enter new title: ")
            book["author"]=input("Enter new author: ")
            print("Book updated successfully!")
            return
    print("Book not found!")

def delete_book():
    book_id=int(input("Enter book ID: "))
    global books
    books=[book for book in books if book["id"]!=book_id]
    borrowed_books.pop(book_id,None)
    print("Book deleted successfully!")

def add_member():
    name=input("Enter member name: ")
    member_id=len(members)+1
    members.append({"id":member_id,"name":name})
    print(f"Member '{name}' added successfully!")

def view_members():
    if not members:
        print("No members available.")
    else:
        for member in members:
            print(f"ID: {member['id']}, Name: {member['name']}")

def update_member():
    member_id=int(input("Enter member ID: "))
    for member in members:
        if member["id"]==member_id:
            member["name"]=input("Enter new name: ")
            print("Member updated successfully!")
            return
    print("Member not found!")

def delete_member():
    member_id=int(input("Enter member ID: "))
    global members
    members=[member for member in members if member["id"]!=member_id]
    borrowed_books.pop(member_id,None)
    print("Member deleted successfully!")

def borrow_book():
    member_id=int(input("Enter member ID: "))
    book_id=int(input("Enter book ID: "))
    for book in books:
        if book["id"]==book_id and book["available"]:
            book["available"]=False
            borrowed_books[book_id]=member_id
            print(f"Book '{book['title']}' borrowed successfully!")
            return
    print("Book not available or does not exist!")

def return_book():
    book_id=int(input("Enter book ID: "))
    if book_id in borrowed_books:
        for book in books:
            if book["id"]==book_id:
                book["available"]=True
                borrowed_books.pop(book_id)
                print(f"Book '{book['title']}' returned successfully!")
                return
    print("Invalid book ID or book was not borrowed!")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Add Member")
        print("6. View Members")
        print("7. Update Member")
        print("8. Delete Member")
        print("9. Borrow Book")
        print("10. Return Book")
        print("11. Exit")
        choice=input("Enter your choice: ")
        if choice=="1":
            add_book()
        elif choice=="2":
            view_books()
        elif choice=="3":
            update_book()
        elif choice=="4":
            delete_book()
        elif choice=="5":
            add_member()
        elif choice=="6":
            view_members()
        elif choice=="7":
            update_member()
        elif choice=="8":
            delete_member()
        elif choice=="9":
            borrow_book()
        elif choice=="10":
            return_book()
        elif choice=="11":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 11.")
main()