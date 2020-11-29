import random
<<<<<<< HEAD
<<<<<<< HEAD
class EmployeeWage:

    def checkEmpAttendance(self):
        attendance = random.randint(0,1)
        if  attendance == 1:
            return "Employee is Present"
        else :
            return "Employee is absent"

if __name__ == "__main__":
    employee = EmployeeWage()
    print(employee.checkEmpAttendance())
=======


class EmployeeWage:
=======


class EmployeeWage:
    IS_FULL_TIME = 1
    IS_PART_TIME = 0
>>>>>>> UC3-AddPartTimeEmpWage
    EMP_WAGE_PER_HOUR = 20
    empHours = 0

    def checkEmpAttendance(self):
<<<<<<< HEAD
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
=======
        attendance = random.randint(0, 2)
        if attendance == EmployeeWage.IS_FULL_TIME:
            EmployeeWage.empHours = 8
            return "Employee is Present for Full Time"
        elif attendance == EmployeeWage.IS_PART_TIME:
            EmployeeWage.empHours = 4
            return "Employee is Present for Part Time"
        else:
            return "Employee is Absent"

    def calculateDailyEmpWage(self):
        dailyWage = EmployeeWage.EMP_WAGE_PER_HOUR * EmployeeWage.empHours
        return "Employee Daily Wage is : " + str(dailyWage)
>>>>>>> UC3-AddPartTimeEmpWage


if __name__ == "__main__":
    employee = EmployeeWage()
    print(employee.checkEmpAttendance())
    print(employee.calculateDailyEmpWage())
<<<<<<< HEAD

>>>>>>> UC2-CalculateDailyEmpWage
=======
>>>>>>> UC3-AddPartTimeEmpWage
