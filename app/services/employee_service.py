from bson import ObjectId

class EmployeeService:
    def __init__(self, mongo):
        self.mongo = mongo

    def get_employees(self):
        employees = list(self.mongo.db.employees.find())
        return [self.parse_employee(emp) for emp in employees]

    def get_employee(self, emp_id):
        emp = self.mongo.db.employees.find_one({'_id': ObjectId(emp_id)})
        return self.parse_employee(emp) if emp else None

    def add_employee(self, new_employee):
        result = self.mongo.db.employees.insert_one(new_employee)
        new_employee['_id'] = str(result.inserted_id)
        return new_employee

    def update_employee(self, emp_id, updated_employee):
        self.mongo.db.employees.update_one({'_id': ObjectId(emp_id)}, {'$set': updated_employee})
        return updated_employee

    def delete_employee(self, emp_id):
        result = self.mongo.db.employees.delete_one({'_id': ObjectId(emp_id)})
        return result.deleted_count > 0

    def parse_employee(self, employee):
        employee['_id'] = str(employee['_id'])
        return employee


# from bson import ObjectId

# class EmployeeService:
#     def __init__(self, mongo):
#         self.mongo = mongo

   
#     def get_employees(self, page=1, page_size=5):
#          print('Fetching employees for page:', page)

#          start_index = (page - 1) * page_size
#          employees = list(self.mongo.db.employees.find().skip(start_index).limit(page_size))
          
#          response_data = [self.parse_employee(emp) for emp in employees]
#          print('Response data:', response_data)

#          return response_data


#     def get_employee(self, emp_id):
#         emp = self.mongo.db.employees.find_one({'_id': ObjectId(emp_id)})
#         return self.parse_employee(emp) if emp else None

#     def add_employee(self, new_employee):
#         result = self.mongo.db.employees.insert_one(new_employee)
#         new_employee['_id'] = str(result.inserted_id)
#         return new_employee

#     def update_employee(self, emp_id, updated_employee):
#         self.mongo.db.employees.update_one({'_id': ObjectId(emp_id)}, {'$set': updated_employee})
#         return updated_employee

#     def delete_employee(self, emp_id):
#         result = self.mongo.db.employees.delete_one({'_id': ObjectId(emp_id)})
#         return result.deleted_count > 0

#     def parse_employee(self, employee):
#         employee['_id'] = str(employee['_id'])
#         return employee
