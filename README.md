#Employee Api

This is a simple Flask application for managing employee information, including CRUD operations.

## Getting Started

Follow these instructions to set up and run the application on your local machine.

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Virtualenv (optional)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/meshafi/employee-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd employee-app
    ```

3. Create a virtual environment (optional):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

    - Windows:

        ```bash
        venv\Scripts\activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Ensure your virtual environment is activated (If you are using virtual environment).

2. Make sure to make changes according to mongoDB database name 
```
/app/__init__.py
```
'mongodb://localhost:27017/EmployeeDB'. Replace 'EmployeeDB' with your database name

3. Run the Flask application:

    ```bash
    python3 run.py
    ```

4. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

## API Endpoints

- **GET /api/employees:** Get a list of all employees.
- **GET /api/employees/<employee_id>:** Get details of a specific employee by ID.
- **POST /api/employees:** Add a new employee.
- **PUT /api/employees/<employee_id>:** Update details of a specific employee by ID.
- **DELETE /api/employees/<employee_id>:** Delete a specific employee by ID.

## Schema Validation

Employee data is validated using the Marshmallow library. Ensure that the request payload adheres to the specified schema.

## Troubleshooting

If you encounter issues, check the following:

- Virtual environment is activated.
- Dependencies are installed (`pip install -r requirements.txt`).
- API requests are correctly formatted.

