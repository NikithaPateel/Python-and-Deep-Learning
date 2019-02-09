from employee import Employee

class FullTimeEmployee(Employee):
    def fulltimesalary(self):
        print("This is full time employee", self.name)