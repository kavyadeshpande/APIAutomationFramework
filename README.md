## APIAutomationFramework
###Python API Automation Framework
Integration Test cases for the Restful Booker
URL - https://restful-booker.herokuapp.com/apidoc/index.html

##Verify GET, POST, PACTH, DELETE, PUT
1.Response Body, Headers, Status Code.
2.Auth - Basic Auth, Cookie Based Auth.
3.JSON Schema Validation.
###Tech Stack (Python Packages used)
Python, Request Module
PyTest, PyTest-html
Allure Report
Faker, CSV, JSON, YAML.
Run via Commandline - Jenkins
P.S - DB Connection(in future)
###Install pip packkes
 'pip install requests pytest pytest-html faker allure-pytest jsonschema
pip install requirements.txt '
##How to run Locally and see the Report?
pytest tests/* -s -v --alluredir=./reports --html=report.html

How to Run via Jenkins?
