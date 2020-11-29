import random
<<<<<<< HEAD
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
=======


class EmployeeWage:
    FULL_TIME_HOUR = 8
    PART_TIME_HOUR = 4
    IS_ABSENT = 0
    EMP_WAGE_PER_HOUR = 20

    randcheck = random.randint(0, 2)

    def checkEmpAttendance(self):
        if EmployeeWage.randcheck == 1:
            return "Employee is Present for Full Time"
        elif EmployeeWage.randcheck == 2:
>>>>>>> UC4-UsingCaseStatement
            return "Employee is Present for Part Time"
        else:
            return "Employee is Absent"

<<<<<<< HEAD
    def calculateDailyEmpWage(self):
        dailyWage = EmployeeWage.EMP_WAGE_PER_HOUR * EmployeeWage.empHours
        return "Employee Daily Wage is : " + str(dailyWage)
>>>>>>> UC3-AddPartTimeEmpWage
=======
    def empPerDayHours(self):
        switch = {
            0:EmployeeWage.IS_ABSENT,
            1:EmployeeWage.FULL_TIME_HOUR,
            2:EmployeeWage.PART_TIME_HOUR
        }
        return switch.get(EmployeeWage.randcheck)

    def calculateDailyEmpWage(self,empHours):
        dailyWage = EmployeeWage.EMP_WAGE_PER_HOUR * empHours
        return "Employee Daily Wage is : " + str(dailyWage)
>>>>>>> UC4-UsingCaseStatement


if __name__ == "__main__":
    employee = EmployeeWage()
    print(employee.checkEmpAttendance())
<<<<<<< HEAD
    print(employee.calculateDailyEmpWage())
<<<<<<< HEAD

>>>>>>> UC2-CalculateDailyEmpWage
=======
>>>>>>> UC3-AddPartTimeEmpWage
=======
    print(employee.calculateDailyEmpWage(employee.empPerDayHours()))
>>>>>>> UC4-UsingCaseStatement
