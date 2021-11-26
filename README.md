# Django-rest-framework CRUD API
To Do list app with User Registration, Login and full Create Read Update and DELETE functionality with Authentication.
## Django Project Setup
 pip install -r requirements.txt

1. django-admin startproject DRF_Todo
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py createsuperuser

### Just Run this command for server deployment:
  python manage.py runserver

### Database Configuartion with Django:
Install PostgreSQL Database using this link: https://tecadmin.net/how-to-install-postgresql-in-ubuntu-20-04/

## Create Django app:
### Run this command: 
   python manage.py startapp todo_app
   
## Check Code Coverage Report
 coverage run manage.py test && coverage report
   
## Clonning Project:
   git clone https://github.com/PakizaArhamsoft/DRF_Todo_API
   
<table>
  <td>
<h3>TASKS</h3>
  </td>
  <td>
<h3>EXPLANATION</h3>
    </td>
  <tr>
    <td>
User Creation API with Basic Authentication
    </td>
    <td>
Register new user with basic credentials first_name, last_name, username, email, password.
</td>
    <tr>
    <td>
Login API with Basic Authentication
      <td>
Login the user with valid username & password and generate refresh token and access token
      </td>
  </tr>
  <tr>
    <td>
Employee CRUD API with JWT Authentication
      </td>
        <td>
Create new Employee, Update the specific Employee data, Get all Employees data w.r.t User, Retrieve specific Employee data w.r.t to User, Delete the specific Employee data. 
    </td>
<tr>
    <td>
Forget Password with Basic Authentication
      </td>
  <td>
Reset the password with email, password and new generated token.
  </td>
  </tr>
 <tr>
    <td>
Refresh Token with Basic Authentication 
      </td>
   <td>
Generate new access token with refresh token
 </td>
  </tr>
      <tr>
    <td>
Pagination in Listing API 
      </td>
   <td>
Add the page numbers to get the list of data. Page size shows the no.of data in one page.
 </td>
  </tr>
      <tr>
    <td>
PostgreSQL Database
      </td>
   <td>
Store the Model collections in todo_app.
 </td>
  </tr>
      <tr>
    <td>
Filter in CRUD API
      </td>
   <td>
Add the Django-filter to filter the Employee data w.r.t User_id.
 </td>
  </tr>
      <tr>
    <td>
API Testing
      </td>
   <td>
Test Register, Login and CRUD APIs with valid and invalid credentials. 
 </td>
  </tr>
      <tr>
    <td>
Swagger Documentation
      </td>
   <td>
DRF Todo API Swagger UI.
     Run http://127.0.0.1:8000/swagger/
 </td>
  </tr>
      <tr>
    <td>
Soft-delete db data
      </td>
   <td>
Add SoftDeleteObject using soft-delete.models
 </td>
  </tr>
      <tr>
    <td>
Pylint 
      </td>
   <td>
Evaluate the API code using pylint. Run pylint todo_app to check the evaluation score of API code.
       </td>
  </tr>
</table>


