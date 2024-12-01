Role-Based Access Control (RBAC) System
Overview
This is a Django-based project implementing Authentication, Authorization, and Role-Based Access Control (RBAC). The system allows users to:

Register an account.
Log in to obtain a JWT token.
Access protected resources based on roles (e.g., Admin, User, Moderator).
This project demonstrates secure handling of user credentials, JWT-based session management, and role-specific access control.

Features
User Registration: New users can register with an email and password.
Login: Users log in to receive a JWT token.
Role-Based Access: Permissions are defined by user roles.
Secure Authentication: Passwords are securely hashed, and JWT tokens are used for sessions.
API Endpoints:
/api/users/register/: User registration.
/api/users/login/: User login.
/api/users/protected/: A protected route accessible based on roles.
Technologies Used
Backend: Django, Django Rest Framework (DRF)
Authentication: JWT (via djangorestframework-simplejwt)
Database: SQLite (default, can be changed)
Environment Management: Virtualenv
Setup and Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/swainKiran/rbac-project.git
cd rbac-project
2. Set Up a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
5. Start the Development Server
bash
Copy code
python manage.py runserver
API Usage
1. Register
Endpoint: POST /api/users/register/
Request Payload:

json
Copy code
{
    "email": "testuser@example.com",
    "password": "testpassword"
}
2. Login
Endpoint: POST /api/users/login/
Request Payload:

json
Copy code
{
    "email": "testuser@example.com",
    "password": "testpassword"
}
Response:

json
Copy code
{
    "refresh": "your-refresh-token",
    "access": "your-access-token"
}
3. Access Protected Route
Endpoint: GET /api/users/protected/
Headers:

bash
Copy code
Authorization: Bearer your-access-token
Response:

json
Copy code
{
    "message": "You have access to this resource."
}
Customization
Change Database
Open settings.py.
Update the DATABASES section to configure your preferred database (e.g., PostgreSQL, MySQL).
Add New Roles and Permissions
Modify the Role and Permission models in models.py.
Update the views.py to enforce new role-specific permissions.
Testing
You can test the API endpoints using:

Postman
cURL
Frontend Integration
Contributing
Contributions are welcome! If you have ideas for improvements or additional features, feel free to submit a pull request.

License
This project is licensed under the MIT License.

Contact
For questions or feedback, please contact:
Kiran
swainkiran181@gmail.com
