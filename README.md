 Django CRUD Application

A simple Django application for performing CRUD (Create, Read, Update, Delete) operations on a User model. This project demonstrates basic usage of Django for building a web application that interacts with a database.

## Features

- Add new users with basic information such as name, email, and password.
- Display a list of all users.
- Update user information.
- Delete users from the list.
- Simple, clean UI using HTML and Bootstrap for styling.

## Technologies Used

- Python 3.12.4
- Django 5.0.6
- HTML/CSS for the frontend
- SQLite (default Django database)

## Installation

Follow these steps to set up and run the project locally.

### Clone the repository:


Follow these steps to set up the project locally:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/django-crud.git
cd django-crud
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations to set up the database:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Open your web browser and visit:

arduino
Copy code
http://127.0.0.1:8000/

## Usages
Home Page: The homepage displays a list of all users and provides options to add a new user or update/delete an existing user.
Add User: Use the form on the homepage to add a new user.
Update User: Click on the "Edit" button next to a user entry to update their information.
Delete User: Click on the "Delete" button to remove a user from the list

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or feedback, please contact:

Your Name - kabrahariom07@gmail.com
GitHub: https://github.com/Hariomkabra


