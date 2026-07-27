import sys
print("Welcome to the calculator program!")
print("Programmed by Mithum")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")
print("5. Denary to Binary Converter")
print("6.Unit conversions (Eg. km to miles, Celsius to Fahrenheit, etc.)")
choice=int(input("Choose: "))
if choice != 5 and choice != 6:
    n1=input("Enter number 1: ")
    n2=input("Enter number 2: ")
    if n1=="" or n1=="":
        print("NUMBER 1 IS EMPTY, DEFAULTING TO 0")
        n1=0
    if n2=="" or n2=="":
        print("NUMBER 2 IS EMPTY, DEFAULTING TO 0")
        n2=0
    n1=float(n1)
    n2=float(n2)
    if n1>1.7e+308:
        print("NUMBER 1 IS TOO LARGE, DEFAULTING TO 1.7e+308 (or it will be considered as infinity)")
        n1=1.7e+308
    if n2>1.7e+308:
        print("NUMBER 2 IS TOO LARGE, DEFAULTING TO 1.7e+308 (or it will be considered as infinity)")
        n2=1.7e+308
elif choice == 5:
    num=int(input("Enter a number: "))
else:
    print("Choose the option for unit conversion:")
notmyfile=open("logs.txt","w")
notmyfile.close()
Answers=[]
n1log=[]
n2log=[]
convlog=[]
binoppo=[]
statementconv=[]
binar=""
keepLoop=True
filler=""
contchoice=True
statementconv=[]
invalidconv=False
while contchoice:
    statementconv=[]
    Answers=[]
    n1log=[]
    n2log=[]
    binar=""
    invalidconv=False
    while keepLoop:
        binar=""
        if choice==1:
            ans=n1+n2
            Answers.append(ans)
            n1log.append(n1)
            n2log.append(n2)
            print("Addition Completed")
            print("Would you like to perform another addition calculation? (Y/n)")
            cont=input()
            if cont=="Y":
                keepLoop=True
                n1=float(input("Enter number 1: "))
                n2=float(input("Enter number 2: "))
            else:
                ask=input("Would you like to switch modes to another calculation type? (y/n)")
                if ask=="Y" or ask=="y":
                    contchoice=True
                else:
                    contchoice=False
                keepLoop=False
        
        elif choice==2:
            ans=n1-n2
            Answers.append(ans)
            n1log.append(n1)
            n2log.append(n2)
            print("Substraction completed")
            print("Would you like to perform another substraction calculation?(Y/n) ")
            cont=input()
            if cont=="Y":
                keepLoop=True
                n1=float(input("Enter number 1: "))
                n2=float(input("Enter number 2: "))
            else:
                ask=input("Would you like to switch modes to another calculation type (Y/n)")
                if ask=="Y" or ask=="y":
                    contchoice=True
                else:
                    contchoice=False
                keepLoop=False
        elif choice==3:
            ans=n1*n2
            Answers.append(ans)
            n1log.append(n1)
            n2log.append(n2)
            print("Multiplication completed")
            print("Would you like to perform another multiplication calculation? (Y/n)")
            cont=input()
            if cont=="Y":
                keepLoop=True
                n1=float(input("Enter number 1: "))
                n2=float(input("Enter number 2: "))
            else:
                ask=input("Would you like to switch modes to another calculation type (Y/n)")
                if ask=="Y" or ask=="y":
                    contchoice=True
                else:
                    contchoice=False
                keepLoop=False
        elif choice==4:
            if n2==0 or n2==0.0:
                print("\n")
                print("\n")
                print("CANNOT HAVE DENOMINATOR AS 0!!")
                print("Defaulting number 2 as '1' and proceeding...")
                print("\n")
                n2=1
            ans=n1/n2
            Answers.append(str(ans))
            n1log.append(n1)
            n2log.append(n2)
            print("Division completed")
            print("Would you like to perform another division calculation? (Y/n)")
            cont=input()
            if cont=="Y" or cont=="y":
                keepLoop=True
                n1=float(input("Enter number 1: "))
                n2=float(input("Enter number 2: "))
            else:
                ask=input("Would you like to switch modes to another calculation type (Y/n)")
                if ask=="Y" or ask=="y":
                    contchoice=True
                else:
                    contchoice=False
                keepLoop=False
        elif choice==5:
            if num<0:
                print("Negative numbers cannot be converted to binary, defaulting to 0")
                num=0
            n1log.append(num)
            binar=""
            binoppo=[]   #I cant bro i spent 1 hour debugging without realising this was the issue, i was not resetting the list for each new number, so it kept appending to the previous number's binary conversion and giving wrong results
            while num>0:
                rem=num%2
                num=num//2
                binoppo.append(rem)
            for i in range(len(binoppo)-1,-1,-1):
                binar=binar+str(binoppo[i])
            zerolen=8-len(binar)
            for i in range(0,zerolen):
                binar="0"+binar
            # Add code here pls-done!
            Answers.append(binar)
            print("Binary conversion completed")
            print("Would you like to perform another denary to binary conversion? (Y/n)")
            cont=input()
            if cont=="Y" or cont=="y":
                keepLoop=True
                num=int(input("Enter a number: "))
            else:
                ask=input("Would you like to switch modes to another calculation type (Y/n)")
                if ask=="Y" or ask=="y":
                    contchoice=True
                else:
                    contchoice=False
                print("Thank you for using the calculator (logs can be found in the 'logs.txt' file)")
                keepLoop=False
        elif choice==6:
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            print("3. Kilometers to Miles")
            print("4. Miles to Kilometers")
            conv=input("Choose the conversion type: ")
            if conv=="1":                                                           #Starting logic for unit conversions
                celsius=float(input("Enter temperature in Celsius: "))
                fahrenheit=(celsius*9/5)+32
                tempans=fahrenheit
                filler="Celsius in Fahrenheit is"
                namepart1=celsius
            elif conv=="2":
                fahrenheit=float(input("Enter temperature in Fahrenheit: "))
                celsius=(fahrenheit-32)*5/9
                tempans=celsius
                filler="Fahrenheit in Celsius is"
                namepart1=fahrenheit
            elif conv=="3":
                kilometers=float(input("Enter distance in Kilometers: "))
                miles=kilometers*0.621371
                tempans=miles
                filler="Kilometers in Miles is"
                namepart1=kilometers
            elif conv=="4":
                miles=float(input("Enter distance in Miles: "))
                kilometers=miles/0.621371
                tempans="Miles is " + str(kilometers) + " Kilometers"
                namepart1=miles
                filler="Miles in Kilometers is"
            else:
                print("Invalid conversion choice, defaulting to Celsius to Fahrenheit")
                print("The logs will show the conversion as error")
                conv="1"
                tempans="INPUT ERROR"
                invalidconv=True
            if tempans=="INPUT ERROR":
                line="INPUT ERROR - WRONG CONVERSION CHOICE"
                statementconv.append(line)
            else:
                line=str(namepart1)+" "+str(filler)+" "+str(tempans)
                statementconv.append(line)
            
            convlog.append(conv)
            Answers.append(tempans)
            print("Conversion completed")
            print("Would you like to perform another conversion? (Y/n)")
            cont=input()
            if cont=="Y" or cont=="y":
                keepLoop=True
            else:
                ask=input("Would you like to switch modes to another calculation type (Y/n)")
                if ask=="Y" or ask=="y":
                    contchoice=True
                else:
                    contchoice=False
                print("Thank you for using the calculator (logs can be found in the 'logs.txt' file)")
                keepLoop=False    
        else:
            print("Invalid mathematical operation choice, defaulting to addition")
            choice=1
    notmyfile=open("logs.txt","a")
    if choice==1:
        filler=" + "
    elif choice==2:
        filler=" - "
    elif choice==3:
        filler=" * "
    elif choice==4:
        filler=" / "
    else:
        filler=filler
    print("Preview of logs:")
    print("\n")
    if choice==5:
        for r in range(len(Answers)):
            line="Denary "+str(n1log[r])+" to binary as: "+str(Answers[r])   # HEHEEEEEEEEEEEE
            notmyfile.write(line)
            notmyfile.write("\n")
            print(line)
    elif choice == 6:
        for r in range(0,len(Answers)):
            #str(namepart1)+" "+str(filler)+" "+str(tempans)
            line=str(line)
            notmyfile.write(statementconv[r])
            notmyfile.write("\n")
            print(statementconv[r])
    else:
        for i in range(0,len(Answers)):
            line=str(n1log[i])+filler+str(n2log[i])+" = "+str(Answers[i])
            line=str(line)
            notmyfile.write(line)
            notmyfile.write("\n")
            print(line)
    print("\n")
    notmyfile.write("\n")
    notmyfile.write("Mode Changed Here.")
    notmyfile.write("\n")
    notmyfile.write("\n")
    notmyfile.close()
    if contchoice==False:
        sys.exit()
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Denary to Binary Converter")
    print("6.Unit conversions (Eg. km to miles, Celsius to Fahrenheit, etc.)1")
    choice=int(input("Choose: "))
    if choice !=5 and choice != 6:
        n1=input("Enter number 1: ")
        n2=input("Enter number 2: ")
        if n1=="" or n1=="":
            print("NUMBER 1 IS EMPTY, DEFAULTING TO 0")
            n1=0
        if n2=="" or n2=="":
            print("NUMBER 2 IS EMPTY, DEFAULTING TO 0")
            n2=0
        n1=float(n1)
        n2=float(n2)
    elif choice == 5:
        num=int(input("Enter a number: "))
    elif choice == 6:
        print("Choose the option for unit conversion:")
    if contchoice:
        keepLoop=True
    else:
        keepLoop=False
