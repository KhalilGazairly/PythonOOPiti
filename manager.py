from employee import employee
from dbconnection import connection

class manager(employee):
    def __init__(self, id, fname, lname, age, department, salary, managed_department):
        super().__init__(id, fname, lname, age, department, salary)
        self.managed_department = managed_department
        self.id = id
        print('Manager added successefully')

        con=connection('postgres','psql','localhost','goegoegoe123',5432)
        con.open_connection()
        con.insert('managers',self.id,self.fname,self.lname,self.age,self.department,self.salary,self.managed_department)
        con.close_connection()


    @staticmethod
    def show():
        for emn in employee.all_emp:
                print(f'name:{emn.fname} {emn.laname}, his age:{emn.age}, works in {emn.department}, and his salary= *****')
            