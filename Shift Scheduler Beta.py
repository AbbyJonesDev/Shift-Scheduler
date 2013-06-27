import random


                       # Helper Functions #
#==============================================================================#
                    
def getNumMachines():
    try:
        numMachines = input("How many machines will be in use for this shift?  ")
        return numMachines
    except:
        print "Please enter a number between 1 and 50."
        return getNumMachines()

def getNumDays():
    try:
        numDays = input("How many days would you like to create schedules for?  ")
        return numDays
    except:
        print "Please enter a number between 1 and 14."
        return getNumDays()

def getNames():
    fname = raw_input('''Enter the file name here.  Be sure to include the complete file path. \nExample:
C:/Users/Your Name/Desktop/file name.txt  \n''')
    try:
        f = open(fname, 'r')
    except IOError:
        print "File could not be found.  Please try again."
        return getNames()
    employees = []
    for line in f.readlines():
        employees.append(line[:-1])
        f.close()
    for employee in employees:
        if employee == '':
            employees.remove(employee)
    print "Employees Scheduled for this Shift:"
    for employee in employees:
        print employee
    ok = raw_input('Is this correct? y/n ')
    if ok.lower() == 'y' or ok.lower() == 'yes':
        return employees
    else:
        print
        print "Please modify your text file as needed or choose a different file. \nMake sure that each employee is listed on a separate line."
        return getNames()

def createSchedules(numMachines, employees):
    #Shuffle employees
    random.shuffle(employees)

    #Sort feeders only to the back of the list
    copy = employees[:]
    ordered = []
    for employee in copy:
        if employee[0] != '-':
            ordered.append(employee)
            employees.remove(employee)
    copy2 = employees[:]
    for employee in copy2:
        ordered.append(employee)

    #Initalize a list of machines and add employees

    machines = []
    index = 0

    for i in range(numMachines):
        machines.append([ordered[index]])
        index += 1
    while len(ordered) > index:
        for machine in machines:
            machine.append(ordered[index])
            index += 1
            if len(ordered) == index:
                break
    return machines

def closingOptions(shiftName, schedules, function):
    option = input("Enter 1 to save to a text file. \nEnter 2 to create a new schedule. \nEnter 3 to exit.")
    if option == 1:
        writeFile(shiftName, schedules)
        print "File saved successfully."
        return option
    elif option == 2:
        function()
    elif option == 3:
        print "Have a good day."
        return option
    else: return closingOptions()

def writeFile(shiftName, schedules):
    print 'File should be saved as a .txt file.  Example: MidnightShift.txt'
    print "File will be saved in your current directory unless you specify otherwise. \n"
    name = raw_input("Save as:  ")
    try:
        w = open(name, 'w')
        w.write(shiftName + '\n==========================\n')
        for day in schedules:
            w.write("Day: " + str(day) + '\n')
            i = 1
            for machine in schedules[day]:
                w.write("\nMachine:" + str(i) + '\n')
                i += 1
                for person in machine:
                    w.write(person + '    ')
                w.write('- - - - - - - - - -\n \n')
            w.write('\n============================\n')
        w.close()
    except:
        return writeFile(shiftName, schedules)

  
#========================================================================
                    # Main Function
#========================================================================

def kandidoShiftScheduler():
    """
    Takes a list of names and randomly assigns them to teams.
    List of names must be from a plain text file with specified format.
    Option to specify number of teams to create and number of schedules
    to create.
    Returns a list of teams with option to save list as a text file.
    """

    print "========================================================="
    print "          Welcome to Shift Scheduler.                    "
    print "========================================================="

    shiftName = raw_input('''What would you like to call this shift?\n(This name will be printed at the top of your schedule.)  ''')
    print
    numMachines = getNumMachines()
    print
    numDays = getNumDays()
    print
    
    print "Employees for this shift should be listed in a plain text file."
    print "Each employee name must be on a separate line.  Inclusion of ID numbers is optional."
    print "Employees who can be feeders only should have a - before their name.  Example:\n"
    print "Maria \n-Bill\nFred"
    print
    employees = getNames()
    print
    schedules = {}
    for day in range(1, numDays + 1):
        schedules[day] = createSchedules(numMachines, employees[:])

    print '=========================='    
    print shiftName
    print '=========================='
    for day in schedules:
        print "Day: ", day
        i = 1
        for machine in schedules[day]:
            print '------------------------'
            print "Machine: ", i
            i += 1
            for person in machine:
                print person
            
        print '============================\n'

    option = closingOptions(shiftName, schedules, kandidoShiftScheduler)
    if option == 1:
        closingOptions(shiftName, schedules, kandidoShiftScheduler)
    else:
        pass



kandidoShiftScheduler()
