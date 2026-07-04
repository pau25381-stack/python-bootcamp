#Pascal case - capital first letter of the word
class Employee:
    def __init__(self, name, id, company):
        self.name = name
        self.id = id
        self.company = company
        self.tasks = []
    def work(self, task):
        print(f"{self.name} is now working {task}")
        self.tasks.append(task)

        print(f"Employee {name} created with id {id} in {company} :")

employee1 = Employee("Richard", "1234", "IBM")
employee2 = Employee("Jelly", "5678", "Microsoft")

#variable approach
employee1.name = "Richard"
employee1.id = "1234"
employee1.company = "IBM"
print(f"Employee {employee1.name} created with id employee1.id in employee1.company:")

employee2.name = "Jelly"
employee2.id = "5678"
employee2.company = "Microsoft"

print(employee1.name)


#snake case
def work():
    pass
