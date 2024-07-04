# Personal Data Management Project

## Project Overview

This project focuses on managing and securing personal data, particularly in the context of back-end systems. Key functionalities include logging, obfuscating sensitive data, encrypting passwords, and connecting securely to a database.

## Learning Objectives

By the end of this project, you will be able to:
- Identify examples of Personally Identifiable Information (PII).
- Implement a log filter to obfuscate PII fields.
- Encrypt and validate passwords.
- Authenticate to a database using environment variables.


## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project directory is mandatory.
- Code should follow the `pycodestyle` style (version 2.5).
- All files must be executable.
- Files' lengths will be tested using `wc`.
- All modules should have documentation.
- All classes and functions should have documentation.
- All functions should be type annotated.

## Tasks

### 0. Regex-ing

Write a function `filter_datum` that returns an obfuscated log message.

**Arguments:**
- `fields`: List of strings representing fields to obfuscate.
- `redaction`: String representing what to replace the field with.
- `message`: Log line string.
- `separator`: Character separating fields in the log line.

Use `re.sub` to perform the substitution in a single regex.

**Example:**
```python
#!/usr/bin/env python3

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = [
    "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
    "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

