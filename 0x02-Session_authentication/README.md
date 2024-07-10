# 0x02. Session Authentication

## Background Context
In this project, you will implement a Session Authentication system from scratch for learning purposes. In real-world applications, it is recommended to use existing modules or frameworks (e.g., Flask-HTTPAuth for Python-Flask). This project aims to help you understand the underlying mechanisms of session authentication by building it yourself.

## Learning Objectives
By the end of this project, you should be able to explain the following without external help:
- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies

## Requirements
### Python Scripts
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All files must be executable
- The length of your files will be tested using `wc`
- All modules should have documentation (e.g., `python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (e.g., `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (e.g., `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

## Tasks

### 0. Et moi et moi et moi!
Copy all your work from the 0x06. Basic authentication project into this new folder. You will add a new endpoint: `GET /users/me` to retrieve the authenticated User object.

#### Instructions:
- Copy folders `models` and `api` from the previous project 0x06. Basic authentication
- Update `@app.before_request` in `api/v1/app.py`:
  - Assign the result of `auth.current_user(request)` to `request.current_user`
- Update the method for the route `GET /api/v1/users/<user_id>` in `api/v1/views/users.py`:
  - If `<user_id>` is equal to `me` and `request.current_user` is `None`: abort(404)
  - If `<user_id>` is equal to `me` and `request.current_user` is not `None`: return the authenticated User in a JSON response
  - Otherwise, keep the same behavior

### 1. Empty session
Create a class `SessionAuth` that inherits from `Auth`. This class will be empty for now. Ensure that it inherits correctly without any overloading. Update `api/v1/app.py` to use `SessionAuth` based on the environment variable `AUTH_TYPE`.

### 2. Create a session
Update `SessionAuth` class:
- Create a class attribute `user_id_by_session_id` initialized by an empty dictionary
- Create an instance method `create_session(self, user_id: str = None) -> str` to create a Session ID for a `user_id` and store it in `user_id_by_session_id`

### 3. User ID for Session ID
Update `SessionAuth` class:
- Create an instance method `user_id_for_session_id(self, session_id: str = None) -> str` that returns a User ID based on a Session ID

### 4. Session cookie
Update `api/v1/auth/auth.py` by adding the method `session_cookie(self, request=None)` to return a cookie value from a request.

### 5. Before request
Update the `@app.before_request` method in `api/v1/app.py`:
- Add the URL path `/api/v1/auth_session/login/` in the list of excluded paths of the method `require_auth`
- If `auth.authorization_header(request)` and `auth.session_cookie(request)` return `None`, abort(401)

### 6. Use Session ID for identifying a User
Update `SessionAuth` class:
- Create an instance method `current_user(self, request=None)` that returns a User instance based on a cookie value

### 7. New view for Session Authentication
Create a new view for Session Authentication.

## Usage
Run the project with the appropriate environment variables to switch between different authentication mechanisms.

```bash
# Example commands to run the application
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
v
