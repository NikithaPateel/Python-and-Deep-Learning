from employee import Employee
from fulltimeemployee import FullTimeEmployee

e = Employee("Nikki", "pateel", 50000, 'HR')
f = FullTimeEmployee("Lekhu", 'kona', 60000, 'Finance')
print("Number of Employees %d" % Employee.empcount)
e.avg_salary()
e.displayEmployee()
