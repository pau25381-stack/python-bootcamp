class Employee:
    """Class representation for employee data"""

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with ID {self.id}")

    def add_work(self, task):
        print(f"Added work {task} to {self.name}")
        return self.tasks.append(task)

    def show_tasks(self):
        print(f"{self.name}'s tasks: {', '.join(self.tasks) if self.tasks else 'No tasks yet'}")

class Recruiter(Employee):
    def recruit(self):
        self.tasks.append("Recruiting...")

class Developer(Employee):
    def code(self):
        self.tasks.append("Coding...")

class Manager(Employee):
    def manage(self):
        self.tasks.append("Managing...")

employee1 = Employee("Jho", 1)

employee1 = Recruiter("Paulo", "1010")
employee2 = Developer("Huge", "2020")
employee3 = Manager("Jun", "3030")

employee1.recruit()
employee2.code()
employee3.manage()

print(f"{employee1.name}'s tasks: {', '.join(employee1.tasks)})