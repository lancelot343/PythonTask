from Employee import Employee


def sort_by_salary(employee_list):
    get_salary = lambda employee: employee.salary
    employee_list.sort(key=get_salary)


def sort_by_company(employee_list):
    get_company = lambda employee: employee.company
    employee_list.sort(key=get_company)


def sort_by_city(employee_list):
    get_city = lambda employee: employee.city
    employee_list.sort(key=get_city)


def sort_by_year(employee_list):
    get_year = lambda employee: employee.year
    employee_list.sort(key=get_year)


def sort_by_surname(employee_list):
    get_surname = lambda employee: employee.surname
    employee_list.sort(key=get_surname)


def sort_by_birth_year(employee_list):
    get_birthYear = lambda employee: employee.birth_year
    employee_list.sort(key=get_birthYear)


def search_by_surname(employee_list, search_surname):
    for employee in employee_list:
        if employee.surname == search_surname:
            return employee


def search_by_year(employee_list, search_year):
    for employee in employee_list:
        if employee.year == search_year:
            return employee


def search_by_salary(employee_list, search_salary):
    for employee in employee_list:
        if employee.salary == search_salary:
            return employee


def search_by_company(employee_list, search_company):
    for employee in employee_list:
        if employee.company == search_company:
            return employee


def search_by_city(employee_list, search_city):
    for employee in employee_list:
        if employee.city == search_city:
            return employee


def search_by_birth_year(employee_list, search_birth_year):
    for employee in employee_list:
        if employee.birth_year == search_birth_year:
            return employee


def delete_by_surname(employee_list, surname):
    to_delete = search_by_surname(employee_list, surname)
    index = employee_list.index(to_delete)
    employee_list.pop(index)
    return employee_list


def delete_by_year(employee_list, year):
    to_delete = search_by_year(employee_list, year)
    index = employee_list.index(to_delete)
    employee_list.pop(index)
    return employee_list


def delete_by_salary(employee_list, salary):
    to_delete = search_by_surname(employee_list, salary)
    index = employee_list.index(to_delete)
    employee_list.pop(index)
    return employee_list


def delete_by_company(employee_list, company):
    to_delete = search_by_surname(employee_list, company)
    index = employee_list.index(to_delete)
    employee_list.pop(index)
    return employee_list


def delete_by_birth_year(employee_list, birth_year):
    to_delete = search_by_birth_year(employee_list, birth_year)
    index = employee_list.index(to_delete)
    employee_list.pop(index)
    return employee_list


def write_list(FILENAME, employee_list):
    with open(FILENAME, 'w') as file:
        for emp in employee_list:
            file.writelines(str(emp) + "\n")


def read_file(FILENAME):
    employee_list = list()
    with open(FILENAME, "r") as file:
        for row in file:
            employee_list.append(Employee(*row.split()))
    return employee_list


if __name__ == "__main__":
    #emp = Employee("Zxcc", "20", "2000", "Epam", "Uzhhorod", "1959")
    #emp2 = Employee("Lisabon", "33", "1400", "SoftServe", "Kiev", "1993")
    #employee_list = [emp, emp2]

    #delete_by_surname(employee_list, "Zxcc")

    #for employee in employee_list:
        #print(str(employee))
    #emp3 = Employee("MBmbm", "30", "1000", "Epam", "Kiev", "1988")
    #employee_list.append(emp3)
    #write_list("mm.txt", employee_list)
    #emp3.upd_year(50)
    #write_list("mm.txt", employee_list)
    #emp2.upd_company("Loool")
    #write_list("mm.txt", employee_list)
    employee_list = read_file("mm.txt")
    for employee in employee_list:
        print(str(employee))