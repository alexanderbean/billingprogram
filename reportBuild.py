# ------------------------------------------------------------------
# Author: Alexander Bean & Raj Khanderia
# Program: Program5
#
# Description:
# This is a program that reads data from the "billing.txt" file
# created by Program4 and builds an ad-hoc report with all employees
# entered in the .txt file as a list. It shares functions with
# program4 nested in the overtimeCalc() function. "Except" clause
# failsafes are also put in place to prevent code from breaking.
# ------------------------------------------------------------------

import reportFunctions as rf

def main():
#input
    NAME_LINE = 0
    RATE_LINE = 1
    FIRST_WEEK = 2
    FULL_ROW = 6
    finalHours = 0
    finalPay = 0
    rowSkip = 0
    dataPrint = '\nEmployee\tRate\tWeek 1\tWeek 2\tWeek 3'+\
                '\tWeek 4\tHours\tTotal\n'
#processing
    try:
        myList = rf.formMyList()
        while rowSkip < len(myList):
            totalHours = 0
            empName = myList[NAME_LINE + rowSkip] + '\t'
            empRate = format(float(myList[RATE_LINE + rowSkip]), ',.2f')
            empList = empName+'\t$'+str(empRate)
            for count in range(FIRST_WEEK, FULL_ROW):
                elem = format(float(myList[count + rowSkip]), ',.2f')
                totalHours += float(elem)
                empList += '\t' + str(elem)
            totalPay = rf.overtimeCalc(float(empRate), totalHours)
            dataPrint += empList+'\t'+\
                  str(format(totalHours, ',.2f'))+'\t$'+\
                  str(format(totalPay, ',.2f')) + '\n'
            finalHours += totalHours
            finalPay += totalPay
            rowSkip += FULL_ROW

        dataPrint += '\n'\
        'Total Billable Due:\t$'+str(format(finalPay, ',.2f'))+'\n'\
        'Total Billable Hours:\t'+str(format(finalHours, ',.2f'))+'\n'\
        'Average Billable Hours:\t'+ \
            str(format(finalHours/(rowSkip/FULL_ROW), ',.2f'))
        
    except FileNotFoundError:
        dataPrint += 'No employees on file'
#output
    print(dataPrint)
