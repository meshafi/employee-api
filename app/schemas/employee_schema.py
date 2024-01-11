from marshmallow import Schema, fields, validate

class EmployeeSchema(Schema):
    name = fields.String(required=True)
    position = fields.String(required=True)
    department = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(validate=validate.Regexp(r'^\d{10}$'), required=True)
    address = fields.String(required=True)
    hire_date = fields.Date(format='%Y-%m-%d', required=True)
    salary = fields.Float(validate=validate.Range(min=0), required=True)
