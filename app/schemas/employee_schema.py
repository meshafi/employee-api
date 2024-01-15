from marshmallow import Schema, fields, validate

class EmployeeSchema(Schema):
    _id = fields.String(attribute='_id', dump_only=True)  
    name = fields.String(required=True)
    position = fields.String(required=True)
    department = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.Integer(validate=validate.Range(min=0, max=9999999999), required=True)
    address = fields.String(required=True)
    hireDate = fields.String(required=True) 
    salary = fields.Float(validate=validate.Range(min=0), required=True)
