# Library management app
This project is an interactive library system, implemented using the Flask framework. This application demonstrates full-stack development, database management, secure user management and intuitive user interface.

## Key Features

- User management : secure login with password hashing, role-based access control (Admin/Normal), personalised user dashboard
- Book management: comprehensive book catalog, availability status
- Loan system: date-logged loans, concurrency control


### Technical implementation

- **Database design**
  - SQLAlchemy for database management
  - one-to-one (Book to Loan) and one-to-many (User to Loan) relationships
  - cascade delete for data integrity, back-popuoate for bidirectional access
- **Form management and validation**: WTForms, CRSF protection, flash messages
- **Error-handling**: Custom error pages for 403, 404, 413, and 500 errors
- **Responsive interface**: Bootstrap powered interface, remember-me functonality, user dashboard for personlised information





## How to run 
In the terminal:
1. Clone repository: `git clone https://github.com/MaddieMiyazaki/Library-management-app.git`
2. Change directoy:  `cd Library-management-app`
3. Install dependencies: `pip install -r requirements.txt`
4. Application context: `flask shell`
5. Populate database: `reset_db()`
6. Exit context: `exit()`
7. Start the app: `flask run`

Then open `http://localhost:5000` in your browser

Example login:
- Username: `amy`
- Password: `amy.pw`

## Technologies used
- **Framework**: Flask (Python backend)
- **Frontend**: HTML, Bootstrap
- **Templating**: Jinja2
- **Database management**: SQLAlchemy


