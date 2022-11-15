def formMyList():
    
    infile = open("billing.txt", "r")

    myList = infile.readlines()

    infile.close()
    
    index = 0
    while index < len(myList):
        myList[index] = myList[index].rstrip("\n")
        index += 1
    
    return myList

def overtimeCalc(rate, totalHours):
    OVERTIME_CUTOFF = 160.00
    if totalHours > OVERTIME_CUTOFF:
        totalPay = totalPayYesOT(rate, totalHours, OVERTIME_CUTOFF)
    else:
        totalPay = totalPayNoOT(rate, totalHours)

    return totalPay

def totalPayYesOT(rate, totalHours, cutoff):
    RATE_INCREASE = 1.05
    overtimeRate = round(rate * RATE_INCREASE, 2)
    overtime = totalHours - cutoff
    overtimeAmount = round(overtime * overtimeRate, 2)
    totalPay = (cutoff * rate) + overtimeAmount

    return totalPay

def totalPayNoOT(rate, totalHours):
    totalPay = totalHours * rate

    return totalPay

def writeBillingFile(employee, rate, week1, week2, week3, week4):
    outfile = open("billing.txt", "a")
    outfile.write(employee+"\n"+str(rate)+"\n"+
                  str(week1)+"\n"+str(week2)+"\n"+
                  str(week3)+"\n"+str(week4)+"\n")
    outfile.close

def resetBillingFile():
    outfile = open("billing.txt","w").close

def readWeeklyHours(prompt):
    again = True

    while again:
        try:
            weekHours = float(input(prompt))
            if weekHours <35 or weekHours >80:
                print("Invalid number of hours, must be between 35 and 80.\n")
            else:
                again = False
        except ValueError:
            print("Error: Value must be numeric.\n")
            
    return float(weekHours)
    
def readHourlyRate(prompt):
    again = True

    while again:
        try:
            rate = float(input(prompt))
            if rate < 20:
                print("Invalid hourly rate, must be at least $20/hour.\n")
            else:
                again = False
        except ValueError:
            print("Error: Value must be numeric.\n")

    return float(rate)

def readEmployeeName(prompt):
    employee = input("\n"+prompt)
    while not employee.isalpha():
        print("Employee name must be entered.")
        employee = input("\n"+prompt)
    return employee
