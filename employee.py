class Employee:
    company_name = 'lcs'
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("name:", self.name) 
        print("salary:", self.salary)
        print("Present company:",Employee.company_name)

    def update_salary(self,amount):
        self.salary +=amount
        print("updated salary:",self.salary)

    def apply_bonus(self, percentage):
        self.salary += self.salary * (percentage / 100)
        print("bonus amount",self.salary)

    @classmethod
    def change_company(cls, new_company):
        Employee.company_name = new_company
        print("New Company:",cls.company_name)
o


employee1 = Employee("John", 50000,)
employee2 = Employee("kishore", 30000)
employee3 = Employee("vimal", 20000)

employee1.display_info()
employee1.update_salary(20000)
employee1.apply_bonus(20)
Employee.change_company("rvl")



employee2.display_info()
employee2.update_salary(20000)
employee2.apply_bonus(15)

#employee3.display_info()
#employee3.update_salary(20000)
#employee3.apply_bonus(30)