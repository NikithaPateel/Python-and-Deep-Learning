class Employee(object):

   empcount = 0
   totalSalary = 0

   def __init__(self, name, family, salary, department):
       self.name = name
       self.family = family
       self.salary = salary
       self.department = department
       Employee.empcount += 1
       Employee.totalSalary += salary

   def avg_salary(self):
       Employee.avgsalary = Employee.totalSalary / Employee.empcount
       print("Average salary of employees is  ", Employee.avgsalary)

   def displayEmployee(self):
        print("Name : ", self.name, "family: ", self.family, "salary:", self.salary, "department", self.department)






