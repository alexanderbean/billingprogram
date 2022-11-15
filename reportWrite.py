# ------------------------------------------------------------------
# Author: Alexander Bean &  Raj Khanderia
# Program: Program4
#
# Description:
# This is a payroll program used to determine the monthly billable
# pay to an employee, depending on their hours worked and their rate,
# including any overtime hours. Includes billing functions, an external
# write to a .txt file, and a loop to enter and write multiple employees
# ------------------------------------------------------------------

#input

import reportFunctions as rf

def main():
    rf.resetBillingFile()
    again = 'y'
    TOTAL_WEEKS = 4.00
    OVERTIME_CUTOFF = 160.00
    RATE_INCREASE = 1.05
    while again == 'y':
        employee = rf.readEmployeeName("Employee Name: ")
        rate = rf.readHourlyRate("Hourly Rate: ")
        week1 = rf.readWeeklyHours("Enter hours worked for week 1: ")
        week2 = rf.readWeeklyHours("Enter hours worked for week 2: ")
        week3 = rf.readWeeklyHours("Enter hours worked for week 3: ")
        week4 = rf.readWeeklyHours("Enter hours worked for week 4: ")
        totalHours = week1 + week2 + week3 + week4
        averageHours = totalHours/TOTAL_WEEKS
#processing
        rf.writeBillingFile(employee, rate, week1, week2, week3, week4)
        if totalHours > OVERTIME_CUTOFF:
            overtimeRate = round(rate * RATE_INCREASE, 2)
            overtime = totalHours - OVERTIME_CUTOFF
            overtimeAmount = round(overtime * overtimeRate, 2)
            totalPay = rf.totalPayYesOT(rate, totalHours, OVERTIME_CUTOFF)
            invoiceAmount = totalPay - overtimeAmount
            workStatement = '\n'+employee+' worked '+ format(overtime, ',.2f')+ \
                            ' hours of overtime.\n'
            billableHours = 'Overtime Hours: '+\
                    format(overtime, ',.2f')+ ' @ $' +\
                    format(overtimeRate,',.2f')+ ' = $' +\
                    format(overtimeAmount, ',.2f')+\
                '\nRegular Hours: '+\
                    format(totalHours - overtime, ',.2f')+ ' @ $' +\
                    format(rate, ',.2f')+ ' = $' +\
                    format(invoiceAmount, ',.2f')
        else:
            overtime = 0.00
            overtimeAmount = 0.00
            totalPay = rf.totalPayNoOT(rate, totalHours)
            workStatement = '\n'+employee+' worked no overtime.\n'
            billableHours = 'Regular Hours: '+\
                    format(totalHours - overtime, ',.2f')+ ' @ $' +\
                    format(rate, ',.2f')+ ' = $' +\
                    format(totalPay, ',.2f')
#output
        print(workStatement, '\nInvoice')
        print('Resource: ',employee,'\tAverage weekly hours: ',\
                format(averageHours, ',.2f'))
        print('\nTotal billable hours: ',\
                format(totalHours, ',.2f'), '\tRate: $',\
                format(rate, ',.2f'), sep='')
        print(billableHours, '\nAmount Due: $',\
                format(totalPay, ',.2f'), sep='')
 
        again = input('\nEnter another employee? ("y" = yes): ')
    
