from dbconnection import connection


class employee:
    all_emp = []
    def __init__(self, id, fname, lname, age, department, salary):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age
        self.department = department
        self.salary = salary
        self.all_emp.append(self)
        print('employees added in list')
    
    @staticmethod
    def transfer(id, table_name, new_department):
        for emp in employee.all_emp:
            if emp.id == id:
                emp.department = new_department
            else:
                continue
        con = connection('postgres', 'psql', 'localhost', 'goegoegoe123', 5432)
        con.open_connection()
        con.update(table_name,f"depatment={new_department}, id={id}")
        con.close_connection()

    @staticmethod
    def fire(table_name, id):
        for emp in employee.all_emp:
            if emp.id == id:
                employee.all_emp.remove(emp)
            else:
                continue
        con = connection('postgres', 'psql', 'localhost', 'goegoegoe123', 5432)
        con.open_connection()
        con.delete(table_name, f'id={id}')
        con.close_connection()


    @staticmethod
    def show_emp(table_name, id):
        for emp in employee.all_emp:
            if emp.id == id:
                print(f'name:{emp.fname} {emp.laname}, his age:{emp.age}, works in {emp.department}, and his salary={emp.salary}')
            else:
                continue
        con = connection('postgres', 'psql', 'localhost', 'goegoegoe123', 5432)
        con.open_connection()
        con.select(table_name, f'id={id}')
        con.close_connection()


    @staticmethod
    def get_all_emp():
        for emp in employee.all_emp:
            print(emp)    
        