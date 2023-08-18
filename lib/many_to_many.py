from datetime import datetime

class Author:
    members = []

    def __init__(self, name):
        self.name = name
        self.__class__.members.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        total = sum(contract.royalties for contract in self.contracts())
        return total


class Book:
    members = []

    def __init__(self, title):
        self.title = title
        self.__class__.members.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        total = sum(contract.royalties for contract in self.contracts())
        return total
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author) or not isinstance(book, Book):
            raise Exception("Invalid author or book")
        
        if not isinstance(date, str):
            raise Exception("Date must be of type str")
        
        if not isinstance(royalties, int):
            raise Exception("Royalties must be of type int")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all.append(self)

    @classmethod
    def contracts_by_date(date, cls):
        return [contract for contract in cls.all if contract.date == date]
    
