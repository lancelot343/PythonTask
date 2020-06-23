class Employee:
    def __init__(self):
        self.surname = ""
        self.year = 0
        self.salary = 0
        self.company = ""
        self.city = ""
        self.birth_year = 0

    def __init__(self, surname, year, salary, company, city, birth_year):
        if surname.isalpha():
            self.surname = surname
        else:
            print("Incorrect surname")
        if year.isdigit() and 0 < int(year) < 100:
            self.year = year
        else:
            print("Incorrect year")
        if salary.isdigit() and 0 < int(salary) < 10000:
            self.salary = salary
        else:
            print("Incorrect salary")
        if company.isalpha():
            self.company = company
        else:
            print("Incorrect company name")
        if city.isalpha():
            self.city = city
        else:
            print("Incorrect city name")
        if birth_year.isdigit() and 1930 < int(birth_year) < 2002:
            self.birth_year = birth_year
        else:
            print("Incorrect birth year")

    def __str__(self):
        return "{Surname:" + self.surname + ";year:" + str(self.year) + ";salary:" + str(self.salary) + ";company:" + self.company + ";city:" + self.city + ";birth year:" + str(self.birth_year) + "}"

    def upd_surname(self, surname):
        self.surname = surname

    def upd_year(self, year):
        self.year = year

    def upd_salary(self, salary):
        self.salary = salary

    def upd_company(self, company):
        self.company = company

    def upd_city(self, city):
        self.city = city

    def upd_birth_year(self, birth_year):
        self.birth_year = birth_year
