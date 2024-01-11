from flask import jsonify, request
from bson import ObjectId
from app import app, mongo
from app.services.employee_service import EmployeeService

employee_service = EmployeeService(mongo)

@app.route('/api/employees', methods=['GET'])
def get_employees():
    employees = employee_service.get_employees()
    return jsonify(employees)

@app.route('/api/employees/<string:emp_id>', methods=['GET'])
def get_employee(emp_id):
    emp = employee_service.get_employee(emp_id)
    if emp:
        return jsonify(emp)
    else:
        return jsonify({'error': 'Employee not found'}), 404

@app.route('/api/employees', methods=['POST'])
def add_employee():
    new_employee = request.get_json()
    result = employee_service.add_employee(new_employee)
    return jsonify(result), 201

@app.route('/api/employees/<string:emp_id>', methods=['PUT'])
def update_employee(emp_id):
    emp = employee_service.get_employee(emp_id)
    if emp:
        updated_employee = request.get_json()
        result = employee_service.update_employee(emp_id, updated_employee)
        return jsonify(result)
    else:
        return jsonify({'error': 'Employee not found'}), 404

@app.route('/api/employees/<string:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    result = employee_service.delete_employee(emp_id)
    if result:
        return jsonify({'message': 'Employee deleted successfully'})
    else:
        return jsonify({'error': 'Employee not found'}), 404
