# 0x01. Basic Authentication

## Back-end
**Authentication**

## Background Context
In this project, you will learn what the authentication process means and implement Basic Authentication on a simple API.

In the industry, you should not implement your own Basic authentication system and use a module or framework that does it for you (like in Python-Flask: Flask-HTTPAuth). Here, for learning purposes, we will walk through each step of this mechanism to understand it by doing.

## Learning Objectives
By the end of this project, you should be able to explain to anyone, without the help of Google:
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## Requirements

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (use `python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (use `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (use `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)

## Tasks

### 0. Simple-basic-API
- Download and start your project from this [archive.zip](https://example.com/archive.zip)
- In this archive, you will find a simple API with one model: User. Storage of these users is done via serialization/deserialization in files.

**Setup and start server:**
```bash
bob@dylan:~$ pip3 install -r requirements.txt
...
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Serving Flask app "app" (lazy loading)
...
bob@dylan:~$

