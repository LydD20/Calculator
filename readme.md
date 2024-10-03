# Calculator Project

##HW 3 Description

Homework 3 required creating a calculator that does the following:

1. Add, Subtract, and Divide
2. Throw exception for divide by zero and test that the exception is thrown
3. Use at least one class, at least one static method, at least one class method.
4. Stores a history of calculations
5. Have 100% test coverage, pass pylint, and does not repeat any lines of code
6. Use type hints for input parameter types and return types
7. Implement a pytest fixture to test the calculator

##HW 4 Description

Homework 4 required generating test data with faker and adding package to command line

1. add faker library and save to requirements.txt
2. add new command to pytest to generate N number of records so can reun the command: pytest--num_records=100
3. add main.py file to serve as entry point to program and add the code from professor's main.py so can have som exception handling program.

##Additional Note:
My pytests were successful until I added the main.py which failed to recognize main as a module. From there, I tried to fixing the code by exporting a PATH specific to the location of the main.py/main function but still would not work. I checked location, casing, and syntax and still can't figure out the issue. I plan to go back in and try to fix the code but not sure what the next step would be.

