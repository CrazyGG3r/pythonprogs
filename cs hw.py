flaguse = 0
def menu():
    global flaguse
    choice = 0
    print("Enter 0 to Add a record in file from scratch")
    print("Enter 1 to APPEND record to the file")
    print("Enter 2 to READ record from the file")
    print("Enter 3 to ADD a record in sequence")
    print("Enter 4 to DELETE a record from the file")
    print("Enter 5 to EDIT a record in the file")
    print("Enter 6 to SEARCH a record from the file")
    print("7 to exit")
    choice = input("Enter choice :")
    choice = int(choice)

    while choice > 7 or choice < 0:
        choice = input("Stop messing around, Enter again:")

    if choice == 0:

        flaguse = 1
        command_0()
    if choice == 1:

        flaguse = 1
        command_1()
    if choice == 2:

        flaguse = 1
        command_2()
    if choice == 3:

        flaguse = 1
        command_3()
    if choice == 4:

        flaguse = 1
        command_4()
    if choice == 5:

        flaguse = 1
        command_5()
    if choice == 6:

        flaguse = 1
        command_6()
    if choice == 7:
        if flaguse == 1:
            print('See Ya :3')
        if flaguse == 0:
            print('Why did u even bother opening me :(')

def command_0():
    rollno = 0
    sname = ""
    rollnumberss = 0
    i = 0
    recordline = ""
    record = ""
    a = ""
    f = open('stufile.txt','w')

    rollnumberss = int(input('how many rollnos are there?:'))

    while i < rollnumberss:
        rollno = str(input('rollno:'))
        sname = input('name:')
        record = '*' + rollno + ',' + sname + ':'
        recordline = recordline + record
        i = i + 1

    f.write(recordline)
    f.close()
    menu()
def command_1():
    rollno = 0
    sname = ""
    b = ''
    f = open('stufile.txt','rt')
    wholedoc = f.read()
    f.close()

    f = open('stufile.txt','w')
    rollno = input("Enter roll no. :")
    sname = input('Enter name :')
    record =  '*' + rollno + ',' + sname + ':'
    wholedoc = wholedoc + record
    f.write(wholedoc)
    f.close()
    menu()
    f = open('stufile.txt','rt')
    b = f.read()
    f.close()
    print(b)

def command_2():
    f = open('stufile.txt','rt')
    wholedoc = f.read()
    f.close()
    c = len(wholedoc)
    x = 0
    rollflag = 0
    nameflag = 1
    sterrick = '*'
    commaa = ','
    rollnostr =''
    namestr = ''
    rolllist = []
    namelist = []
    dispRoll = ''
    dispName = ''

    while x <= c:
        w = x - 1
        y = x + 1
        charA = wholedoc[w:x]
        if charA == '*':
            rollflag = 1
            nameflag = 0

        if charA == ',':
            rollflag = 0
            nameflag = 1

        if charA == ':':
            rolllist.append(rollnostr)
            namelist.append(namestr)
            rollnostr = ''
            namestr =''

        if rollflag == 1 and charA != '*' and charA != ':':
            rollnostr = rollnostr + charA

        if nameflag == 1 and charA != ','and charA != ':':
            namestr = namestr + charA

        x = x + 1

    a = len(rolllist)
    for x in range(a):
       print('Rollno:',rolllist[x] )
       print('Name:', namelist[x])
    menu()
def command_3():
    f = open('stufile.txt','rt')
    wholedoc = f.read()
    f.close()
    c = len(wholedoc)
    x = 0
    l = ''
    rollflag = 0
    nameflag = 1
    sterrick = '*'
    commaa = ','
    rollnostr =''
    namestr = ''
    rolllist = []
    namelist = []
    roll2list = []
    name2list = []
    rollnoAdd = ''
    nameadd = ''
    foundspace = 0
    namewrite = ''
    rollwrite = ''
    record = ''
    recordline = ''


    while x <= c:
        w = x - 1
        y = x + 1
        charA = wholedoc[w:x]
        if charA == '*':
            rollflag = 1
            nameflag = 0

        if charA == ',':
            rollflag = 0
            nameflag = 1

        if charA == ':':
            rolllist.append(rollnostr)
            namelist.append(namestr)
            rollnostr = ''
            namestr =''

        if rollflag == 1 and charA != '*' and charA != ':':
            rollnostr = rollnostr + charA

        if nameflag == 1 and charA != ','and charA != ':':
            namestr = namestr + charA

        x = x + 1
    rollnoAdd = input('Enter roll number :')
    nameadd = input('Enter name:')
    c = len(rolllist)
    try :
        indexx = rolllist.index(rollnoAdd)
    except ValueError:
        for i in range(c):
            charA = rolllist[i]
            if rollnoAdd > charA:
                charC = rolllist[i]
                roll2list.append(charC)
                nameD = namelist[i]
                name2list.append(nameD)
            if rollnoAdd < charA and foundspace == 0:
                name2list.append(nameadd)
                roll2list.append(rollnoAdd)
                foundspace = 1
            if foundspace ==1:
                charC = rolllist[i]
                roll2list.append(charC)
                nameD = namelist[i]
                name2list.append(nameD)

        d = len(roll2list)
        for i in range(d):
            namewrite = name2list[i]
            rollwrite = roll2list[i]
            record = '*' + rollwrite + ',' + namewrite + ':'
            recordline = recordline + record
        f = open('stufile.txt','w')
        f.write(recordline)
        f.close()
        f = open('stufile.txt','rt')
        l = f.read()
        f.close()
        print(l)
        menu()
    else:
        print('Record already exists :(')
        menu()

def command_4():
    f = open('stufile.txt','rt')
    wholedoc = f.read()
    f.close()
    c = len(wholedoc)
    x = 0
    rollflag = 0
    nameflag = 1
    sterrick = '*'
    commaa = ','
    rollnostr =''
    namestr = ''
    rolllist = []
    namelist = []
    delrol = ''
    delname = ''


    while x <= c:
        w = x - 1
        y = x + 1
        charA = wholedoc[w:x]
        if charA == '*':
            rollflag = 1
            nameflag = 0

        if charA == ',':
            rollflag = 0
            nameflag = 1

        if charA == ':':
            rolllist.append(rollnostr)
            namelist.append(namestr)
            rollnostr = ''
            namestr =''

        if rollflag == 1 and charA != '*' and charA != ':':
            rollnostr = rollnostr + charA

        if nameflag == 1 and charA != ','and charA != ':':
            namestr = namestr + charA

        x = x + 1
    a = len(rolllist)
    delted = 0
    roll2list = []
    name2list = []
    charC = ''
    nameD = ''
    delrol = input('Enter rollno. to delete')
    record = ''
    recordline = ''


    try:
        indexdsdsds = rolllist.index(delrol)
    except ValueError:
        print('Roll no doesnot exist')
        menu()
    else:
        for i in range(a):
            charA = rolllist[i]
            if charA != delrol:
                charC = rolllist[i]
                roll2list.append(charC)
                nameD = namelist[i]
                name2list.append(nameD)
        d = len(roll2list)
        for i in range(d):
            namewrite = name2list[i]
            rollwrite = roll2list[i]
            record = '*' + rollwrite + ',' + namewrite + ':'
            recordline = recordline + record
        f = open('stufile.txt','w')
        f.write(recordline)
        f.close()
        f = open('stufile.txt','rt')
        l = f.read()
        f.close()
        print(l)
        menu()
def command_5():
    f = open('stufile.txt','rt')
    wholedoc = f.read()
    f.close()
    c = len(wholedoc)
    x = 0
    rollflag = 0
    nameflag = 1
    sterrick = '*'
    commaa = ','
    rollnostr =''
    namestr = ''
    rolllist = []
    namelist = []

    while x <= c:
        w = x - 1
        y = x + 1
        charA = wholedoc[w:x]
        if charA == '*':
            rollflag = 1
            nameflag = 0

        if charA == ',':
            rollflag = 0
            nameflag = 1

        if charA == ':':
            rolllist.append(rollnostr)
            namelist.append(namestr)
            rollnostr = ''
            namestr =''

        if rollflag == 1 and charA != '*' and charA != ':':
            rollnostr = rollnostr + charA

        if nameflag == 1 and charA != ','and charA != ':':
            namestr = namestr + charA

        x = x + 1

    editrol = input('Enter roll no. to edit :')
    try :
        indexa = rolllist.index(editrol)
    except ValueError:
        print('Rollno. doesnot exist :(')
        menu()
    else:
        rolansweer = input('Enter new roll no:')
        nameansweer = input('Enter new name:')
        minusindexa = indexa - 1
        plusindexa = indexa + 1
        if rolansweer == '' and nameansweer == '':
            print('why must you hurt me this way :(')
        if rolansweer != '' and nameansweer != '':
            if indexa > 0 and indexa < len(rolllist) :
                rolllist.insert(indexa, rolansweer)
                rolllist.pop(plusindexa)
                namelist.insert(indexa, nameansweer)
                namelist.pop(plusindexa)
            elif indexa == 0 or indexa == len(rolllist):
                rolllist.insert(indexa, rolansweer)
                rolllist.pop(plusindexa)
                namelist.insert(indexa, nameansweer)
                namelist.pop(plusindexa)
        d = len(rolllist)
        record = ''
        recordline = ''
        for i in range(d):
            namewrite = namelist[i]
            rollwrite = rolllist[i]
            record = '*' + rollwrite + ',' + namewrite + ':'
            recordline = recordline + record
        f = open('stufile.txt','w')
        f.write(recordline)
        f.close()
        f = open('stufile.txt','rt')
        l = f.read()
        f.close()
        print(l)
        menu()
def command_6():
    f = open('stufile.txt','rt')
    wholedoc = f.read()
    f.close()
    c = len(wholedoc)
    x = 0
    rollflag = 0
    nameflag = 1
    sterrick = '*'
    commaa = ','
    rollnostr =''
    namestr = ''
    rolllist = []
    namelist = []

    while x <= c:
        w = x - 1
        y = x + 1
        charA = wholedoc[w:x]
        if charA == '*':
            rollflag = 1
            nameflag = 0

        if charA == ',':
            rollflag = 0
            nameflag = 1

        if charA == ':':
            rolllist.append(rollnostr)
            namelist.append(namestr)
            rollnostr = ''
            namestr =''

        if rollflag == 1 and charA != '*' and charA != ':':
            rollnostr = rollnostr + charA

        if nameflag == 1 and charA != ','and charA != ':':
            namestr = namestr + charA

        x = x + 1

    printrol = ''
    printname = ''
    editrol = input('Enter roll no. to search for :')
    try :
        indexa = rolllist.index(editrol)
    except ValueError:
        print('Doesnot exist :(')
        menu()
    else:
        printrol = rolllist[indexa]
        printname = namelist[indexa]
        print('found;')
        print('Roll no: ',printrol)
        print('Namee:', printname)
        menu()
menu()