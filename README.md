This is a payroll program created over the course of my Spring 2022 semester at Bryant University.

To run the program, run through reportMenu.

The first half, reportWrite, takes inputs for employee name, pay rate, and weekly hours for four weeks, and determines the monthly billable pay to an employee, depending on their hours worked, their rate, and any overtime hours. Includes billing functions, an external write to a .txt file, and a loop to enter and write multiple employees.

The second half, reportAdHoc, reads data from the "billing.txt" file created by reportWrite and builds an ad-hoc report with all employees entered in the .txt file as a list. It shares functions with programWrite nested in the overtimeCalc() function. "Except" clause failsafes are also put in place to prevent code from breaking. 

Program functions are all written in the reportFunctions file, and the reportMenu contains all the main() calls.
