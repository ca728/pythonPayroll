# here I am importing my package
from tabulate import tabulate

# print my application name
Print = ('WELCOME TO PAYCAL')

# I will be printing 2 lists
Emplopyee_list = []
New_list = []

# enter the number of employees you will be calculating for
try:
    Employee_number = int(input("Enter how much employees for payroll:"))
    i = 1

    # here I will collecting the employees name, pay rate, and hours.

    while i <= Employee_number:
        Employee_name = input('Enter the employee name:')
        Employee_pay_rate = float(input('Enter the pay rate:'))
        Employee_hours = float(input('Enter hours worked:'))
        Overtime_hours = 0
        if Employee_hours <= 40:
            Rate_of_pay = Employee_pay_rate * Employee_hours
        else:
            Regular_hours = Employee_hours - 40
            Rate_of_pay = Employee_pay_rate * 40
            Overtime_hours = Employee_pay_rate * (Regular_hours * 1.5)
        Gross_pay = Rate_of_pay + Overtime_hours

        #here I am calculating tax deductions

        #Federal Tax
        Federal_Tax = (Gross_pay * .2)

        #State_Tax
        State_tax = (Gross_pay * .06)

        #FICA
        FICA_TAX = (Gross_pay * .07)

        Net_pay = Gross_pay - (FICA_TAX + State_tax + FICA_TAX)
        Emplopyee_list = [Employee_name, Employee_hours, Employee_pay_rate, Rate_of_pay,
                          Overtime_hours, Gross_pay, Federal_Tax, State_tax, FICA_TAX,
                          Net_pay]
        New_list.append(Emplopyee_list)
        i = i + 1
#If the input is an error it will automatically print a table
#print data in table using tabulate package
except:
    print('An Error occured. Please enter valid input')
finally:
    print(tabulate(New_list, headers=['Employee Name', 'Hours Worked', 'Pay Rate',
                                      'Regular Pay', 'OT Pay', 'Gross Pay', 'Fed Tax',
                                      'State Tax', 'FICA', 'Net Pay']))








