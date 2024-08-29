#1
tuplex= (2,4,5,6,2,3,4,4,7)
count4 = tuplex.count(4)
print(f"The number 4 appears :{count4}: times in the tuple.")

"""output is
The number 4 appears :3: times in the tuple."""

#2
listx = [5,10,7,4,15,3]
tuplex =  tuple(listx)
print(listx)

""" output is
[5, 10, 7, 4, 15, 3]"""

#3
tuples_list = [(1, 2), (3, 4), (5, 6)]
total_sum = sum(sum(tup) for tup in tuples_list)
print(f"sum of value in the tuple: {total_sum}")

"""output is
sum of value in the tuple: 21"""

#4
employee1 = ("john doe","101","Human Resources","60000")
employee2 = ("Alice Smith","102","Marketing","55000")
employee3 = ("Bob johnson","103","Engineering","75000")

employees = [employee1, employee2, employee3]
print("employee record:")

for employee in employees:
    name, emp_id, department, salary = employee
    
    print(f"Employee Name: {name}")
    print(f"Employee ID: {emp_id}")
    print(f"Department: {department}")
    print(f"Salary: ${salary}")
    print()

"""output is
employee record:
Employee Name: john doe
Employee ID: 101
Department: Human Resources
Salary: $60000

Employee Name: Alice Smith
Employee ID: 102
Department: Marketing
Salary: $55000

Employee Name: Bob johnson
Employee ID: 103
Department: Engineering
Salary: $75000"""
   
