import json
from abc import ABC, abstractmethod

class LibraryEntity(ABC):
    @abstractmethod
    def to_dict(self): pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        pass

class Book(LibraryEntity):
    def __init__(self, name_book, author):
        self._name_book = name_book 
        self._author = author
        self.is_available = True  
        self.borrowed_by = None 

    @property
    def name_book(self):
        return self._name_book
    
    @property
    def author(self):
        return self._author
    
    def to_dict(self):
        return {
            'name_book': self._name_book,  
            'author': self._author,
            'is_available': self.is_available,
            'borrowed_by': self.borrowed_by
        }
    
    @classmethod
    def from_dict(cls, data):  
        book = cls(data['name_book'], data['author'])
        book.is_available = data['is_available']
        book.borrowed_by = data['borrowed_by']
        return book

class User(LibraryEntity):
    def __init__(self, username):
        self._username = username
        self.borrowed_books = [] 
    
    @property
    def username(self):
        return self._username
    
    def to_dict(self):
        return {
            'username': self._username,
            'borrowed_books': self.borrowed_books
        }
    
    @classmethod
    def from_dict(cls, data):
        user = cls(data['username'])
        user.borrowed_books = data['borrowed_books']
        return user

class Library:
    def __init__(self):
        self._books = []
        self._users = []
        self._load_data()
    
    @property
    def books(self):
        return self._books
    
    @property
    def users(self):
        return self._users
    
    def _save_data(self):
        books_data = [book.to_dict() for book in self._books]
        with open('books.txt', 'w', encoding='utf-8') as f:
            json.dump(books_data, f, ensure_ascii=False, indent=2)
        
        users_data = [user.to_dict() for user in self._users]
        with open('users.txt', 'w', encoding='utf-8') as f:
            json.dump(users_data, f, ensure_ascii=False, indent=2)
    
    def _load_data(self):
        try:
            with open('books.txt', 'r', encoding='utf-8') as f:
                books_data = json.load(f)
                self._books = [Book.from_dict(data) for data in books_data]
        except FileNotFoundError:
            self._books = []
        try:
            with open('users.txt', 'r', encoding='utf-8') as f:
                users_data = json.load(f)
                self._users = [User.from_dict(data) for data in users_data]
        except FileNotFoundError:
            self._users = []
    
    def find_book(self, title): 
        for book in self._books:
            if book.name_book == title: 
                return book
        return None
    
    def find_user(self, username):
        for user in self._users:
            if user.username == username:
                return user
        return None
    
    def get_book(self, title, username):  
        book = self.find_book(title)
        user = self.find_user(username)
        
        if not book:
            print(f"Книга '{title}' не найдена")
            return False
        
        if not user:
            print(f"Пользователь '{username}' не найден")
            return False
        
        if not book.is_available:
            print(f"Книга '{title}' уже занята")
            return False
        
        book.is_available = False
        book.borrowed_by = username
        user.borrowed_books.append(title) 
        self._save_data()
        print(f"Книга '{title}' выдана пользователю {username}")
        return True
    
    def return_book(self, title, username):  
        book = self.find_book(title)
        user = self.find_user(username)
        
        if not book:
            print(f"Книга '{title}' не найдена")
            return False
        
        if not user:
            print(f"Пользователь '{username}' не найден")
            return False
        
        if title not in user.borrowed_books:  
            print(f"Пользователь {username} не брал эту книгу")
            return False
        
        book.is_available = True
        book.borrowed_by = None
        user.borrowed_books.remove(title)  
        self._save_data()
        print(f"Книга '{title}' возвращена")
        return True
    
    def add_book(self, name_book, author): 
        book = Book(name_book, author)
        self._books.append(book)
        self._save_data()
        print(f"Книга '{name_book}' добавлена")
        return True
    
    def delete_book(self, name_book): 
        for book in self._books:
            if book.name_book == name_book: 
                if book.is_available:  
                    self._books.remove(book)
                    self._save_data()
                    print(f"Книга '{name_book}' удалена")
                    return True
                else:
                    print(f"Книга '{name_book}' занята, нельзя удалить")
                    return False
        
        print(f"Книга '{name_book}' не найдена") 
        return False
    
    def reg_user(self, username): 
        if not any(user.username == username for user in self._users):
            user = User(username)
            self._users.append(user)
            self._save_data()
            print(f"Пользователь '{username}' зарегистрирован")
            return True
        else:
            print("Пользователь уже зарегистрирован")
            return False
    
    def list_users(self):  
        if not self._users:
            print("Нет зарегистрированных пользователей")
            return
        
        print("Список пользователей библиотеки:")
        for i, user in enumerate(self._users, 1):
            print(f"- {user.username}")
    
    def view_all_books(self):  
        if not self._books:
            print("В библиотеке пока нет книг")
            return
        
        print("\nСписок всех книг:")
        for i, book in enumerate(self._books, 1):
            status = "доступна" if book.is_available else f"занята ({book.borrowed_by})"
            print(f"{i:3}. '{book.name_book}' - {book.author} ({status})")

class Librarian():
    def __init__(self, name, library):  
        self.name = name
        self.library = library  
def librarian_menu(library):
    librarian = Librarian("Библиотекарь", library)  
    
    while True:
        print(f"\nМеню библиотекаря)")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Зарегистрировать пользователя")
        print("4. Просмотреть всех пользователей")
        print("5. Просмотреть все книги")
        print("6. Выйти")
            
        choice = input("Выберите действие: ")
            
        if choice == '1':
            title = input("Название книги: ")
            author = input("Автор: ")
            library.add_book(title, author) 
            
        elif choice == '2':
            title = input("Название книги для удаления: ")
            library.delete_book(title)  
            
        elif choice == '3':
            username = input("Имя пользователя: ")
            library.reg_user(username)  
        elif choice == '4':
            library.list_users()  
        elif choice == '5':
            library.view_all_books()  
            
        elif choice == '6':
            break

def user_menu(library):
    username = input("Ваше имя: ")
    user = library.find_user(username)
    
    if not user:
        print("Пользователь не найден. Обратитесь к библиотекарю.")
        return
    
    while True:
        print(f"\nМеню пользователя)")
        print("1. Просмотреть доступные книги")
        print("2. Взять книгу")
        print("3. Вернуть книгу")
        print("4. Просмотреть мои книги")
        print("5. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            print("\nДоступные книги:")
            available_books = [book for book in library.books if book.is_available]
            if available_books:
                for i, book in enumerate(available_books, 1):
                    print(f"{i}. '{book.name_book}' - {book.author}")
            else:
                print("Нет доступных книг")
        
        elif choice == '2':
            title = input("Название книги: ")
            library.get_book(title, username)
        
        elif choice == '3':
            if not user.borrowed_books:
                print("У вас нет взятых книг")
                continue
            
            print("Ваши книги:")
            for i, title in enumerate(user.borrowed_books, 1):
                print(f"{i}. {title}")
            
            try:
                idx = int(input("Номер книги для возврата: ")) - 1
                if 0 <= idx < len(user.borrowed_books):
                    title = user.borrowed_books[idx]
                    library.return_book(title, username)
                else:
                    print("Неверный номер")
            except ValueError:
                print("Ошибка ввода")
        
        elif choice == '4':
            if user.borrowed_books:
                print("\nВаши книги:")
                for i, title in enumerate(user.borrowed_books, 1):
                    print(f"{i}. {title}")
            else:
                print("У вас нет взятых книг")
        
        elif choice == '5':
            break



library = Library() 
while (True):
    print("Библиотека")
    print("1. Библиотекарь")
    print("2. Пользователь")
    print("3. Выйти")
    
    role = input("Выберите роль (1-2): ")
    
    if role == '1':
        librarian_menu(library)
    elif role == '2':
        user_menu(library)
    else: 
        print("\nДо свидания!") 
        break