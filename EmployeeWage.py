import random


class EmployeeWage:
    EMP_WAGE_PER_HOUR = 20
    empHours = 0

    def checkEmpAttendance(self):
        empcheck = random.randint(0, 1)
        if empcheck == 1:
            EmployeeWage.empHours = 8
            return "Employee is Present"
        else:
            EmployeeWage.empHours = 0
            return "Employee is absent"

    def calculateDailyEmpWage(self):
        dailyWage = EmployeeWage.EMP_WAGE_PER_HOUR * EmployeeWage.empHours
        return  "Employee Daily Wage is : "+str(dailyWage)


if __name__ == "__main__":
    employee = EmployeeWage()
    print(employee.checkEmpAttendance())
    print(employee.calculateDailyEmpWage())

