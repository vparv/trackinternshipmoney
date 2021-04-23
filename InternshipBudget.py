budget = open("budget.txt", "r+")
def write():
    budget.truncate()
    
    hourly = float(input("How much are you being paid per hour this summer? "))
    stipend = float(input("How much is your relocation bonus (total)? "))
    weeks = float(input("How many weeks are you working? "))
    salary = (hourly * weeks * 8 * 5) + stipend
    print("You are making" , salary)
    ogSalary = salary

    names = []
    prices = []
    i = 0
    while (input("Any items to report? (Y/N) ") == "Y"):
        
        name1 = input("What are you buying? ")
        names.append(name1)
        name1 = "How much is " + name1 + "? "
        price1 = float(input(name1))
        prices.append(price1)
        salary -= price1
        str1 = str(i) + ", " + names[i] + ", " + str(prices[i]) + ", " + str(salary) + "\n"
        budget.write(str1)
        i += 1
        print("You have " , str(salary), " left!\n")
    
    perc = salary / ogSalary
    percentage = "{:.2%}".format(perc)
    percentage = str(percentage)

    finalStr = "You will be making " + str(ogSalary) + " and will be retaining " + percentage + "percent of it\n"
    budget.write(finalStr)
    if (salary > (ogSalary/2)):
        budget.write("Let's go! You still have over half of your money. Be smart and invest that :)")
    elif (salary > (ogSalary/4)):
        budget.write("Sorry! ALl your remaining money has to be to invest! Don't make the rules around here boss :/")
    elif (salary > 0):
        budget.write("Congrats! You still have money! Good for you bud :) But you should've invested\n")
    elif (salary <= 0):
        budget.write("Oopsies! You are gonna be a broke boy :( Try planning it out again!\n")

    budget.write("Thanks for trying Vineet's Internship Money Budgetter! Would love to connect sometime if you are 1. my friend 2. a recruiter 3. random stranger on the internet :)")
    return(0)

def read():
    readItems = budget.readlines()
    items = []
    for d in range(0, len(readItems)-2):
        
        split = readItems[d].split(", ")
        items.append(split)
        balance = items[d][3].split("\n")
        items[d][3] = balance[0]
        #print(items[d])

    saveItems = items
    
    for d in range(0, len(saveItems)):
        print(saveItems[d])

def clear():
   
    budget.truncate()

def main():

    cmd = input("WRITE(w)/READ(r)/CLEAR(c)/EXIT(x)")
    while(cmd != "x"):
        if (cmd == "w"):
            print("Are you sure? Writing will clear the current txt! (Y/N)? ")
            if (input("") == "Y"):
                write()
                print("Browse your internship money assignment here on the file: budget.txt")
                break
        elif (cmd == "r"):
            read()
        elif (cmd == "c"):
            clear()
        else:
            break

        cmd = input("WRITE(w)/READ(r)/CLEAR(c)/EXIT(x)")
        
        
    budget.close()
        

main()
