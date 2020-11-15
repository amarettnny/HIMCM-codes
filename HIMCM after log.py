import math
#define the record data type of Companies
class Comp():
    def __init__ (self):
        self.name = ""
        self.address = 0
        self.payment = 0
        self.type = 0
        self.workTime = 0
        
#define the record data type of Users
class User():
    def __init__ (self):
        self.name = ""
        self.purpose = 0
        self.prefType = 0
        self.location = 0
        self.trans = 0
        self.time = 0.0
        self.risk = 0
        
#define the function of dealing with the premeter in the utility function
def View(user,comp):
    #factors is a varible to represent how many factors we have, in this example factor is 5
    factors = 3
    #list imp is a 2D list store the factors' names
    result = {'Transportation Money Cost': None,'Transportation Time Cost': None,'Preparation Money Cost':None,'Preparation Time Cost':None,'Expectation Matchness':None}
  
    #caculate the cost of preparation
    ## revise here, the preparation money cost should be devided by 60
    if user.prefType == 0 and comp.type == 0:
        result['Preparation Money Cost'] = 0.5
        result['Preparation Time Cost'] = 0.2
    elif user.prefType == 0 and comp.type == 1:
        result['Preparation Money Cost'] = 25
        result['Preparation Time Cost'] = 1.0
    elif user.prefType == 1 and comp.type == 0:
        result['Preparation Money Cost'] = 0.5
        result['Preparation Time Cost'] = 0.2
    elif user.prefType == 1 and comp.type == 1:
        result['Preparation Money Cost'] = 5
        result['Preparation Time Cost'] = 0.5

    #caculate the cost to go to work
    ##revise the price of transportation
    index = user.location + comp.address
    if index == 2 and user.trans == 0:
        result['Transportation Money Cost'] = 0
        result['Transportation Time Cost'] = 0.5
    elif index == 2 and user.trans == 1:
        result['Transportation Money Cost'] = 6
        result['Transportation Time Cost'] = 0.5
    elif index == 2 and user.trans == 2:
        result['Transportation Money Cost'] = 15
        result['Transportation Time Cost'] = 0.2
    elif index == 1 and user.trans == 0:
        result['Transportation Money Cost'] = 0
        result['Transportation Time Cost'] = 0
    elif index == 1 and user.trans == 1:
        result['Transportation Money Cost'] = 10
        result['Transportation Time Cost'] = 1.0
    elif index == 1 and user.trans == 2:
        result['Transportation Money Cost'] = 35
        result['Transportation Time Cost'] = 0.5
    elif index == 0 and user.trans == 0:
        result['Transportation Money Cost'] = 0
        result['Transportation Time Cost'] = 0.5
    elif index == 0 and user.trans == 1:
        result['Transportation Money Cost'] = 6
        result['Transportation Time Cost'] = 0.2
    elif index == 0 and user.trans == 2:
        result['Transportation Money Cost'] = 15
        result['Transportation Time Cost'] = 0.2
        
    return result

#define a function FindP to return the p1 p2 for the utility function
def FindP(user):
    user.risk = int(user.risk)
    user.purpose = int(user.purpose)
    if user.risk == 0 and user.purpose == 1:
        p1,p2 = 0.5,1.5
    elif user.risk == 0 and user.purpose == 2:
        p1,p2 = 1.5,0.5
    elif user.risk == 1 and user.purpose == 1:
        p1,p2 = 1.5,0.5
    elif user.risk == 1 and user.purpose == 2:
        p1,p2 = 0.5,1.5
    else:
        p1,p2 = 1,1 
    return p1,p2
    
#set up all the testing companies data
example_num = 44
companies = [Comp() for i in range(example_num)]
File = open("CompaniesInput.txt","r")
Line = File.readline()
counter = 0
while True:
    Line = File.readline()
    if Line == '':
        break
    companies[counter].name = Line.replace("\n","")
    Line = File.readline()
    if Line == '':
        break
    companies[counter].workTime = int(Line)
    Line = File.readline()
    if Line == '':
        break
    companies[counter].payment = float(Line)
    Line = File.readline()
    if Line == '':
        break
    if Line == 'R':
        companies[counter].address = 0
    else:
        companies[counter].address = 1
    Line = File.readline()
    if Line == '':
        break
    if Line == 'M':
        companies[counter].type = 0
    else:
        companies[counter].type = 1
    counter += 1




#prompt user to input all the required information
hi = User()
hi.name = input("What is your name:\n")
hi.purpose = int(input("What is your purpose:(“1” for earn money,“2” for gaining experience,“3” for both value,'4' for neither value)\n"))
hi.prefType = int(input("What do you want for your job:(Write “0”for manual, “1”for intellectual)\n"))
hi.location = int(input("Where do you live:(Write “0” for rural and“1” for urban)\n"))
hi.trans = int(input("How do you want to go to work:(Write “0” for walk,“1” for public transportation and “2” for private transportation)\n"))
hi.time = float(input("How much percent in a day do you want consider for work:(input by 1 decimals)\n"))
hi.risk = int(input("Are you a risk seeking person:(“0” for no,“1” for yes,’2‘ for neutral)\n"))



#utility function u = (I(x)**p1)*(E(x)**p2)*T(x)
#test all the data with the companies
Utility = [0 for i in range(example_num)]
Names = ["" for i in range(example_num)]


for i in range(example_num - 1):
    # print(companies[i].name,": ",end="")
    data = View(hi,companies[i])
    I = companies[i].payment*companies[i].workTime - data['Transportation Money Cost'] - data['Preparation Money Cost']
    A = math.log10(I)
    if companies[i].type == 1 and data['Expectation Matchness']:
        E = 3
    elif companies[i].type == 1 and not(data['Expectation Matchness']):
        E = 0.5
    elif companies[i].type == 0 and data['Expectation Matchness']:
        E = 2.1
    elif companies[i].type == 0 and not(data['Expectation Matchness']):
        E = 0.3

    p1,p2 = FindP(hi)
    
    T = 24*hi.time - companies[i].workTime - data['Transportation Time Cost'] - data['Preparation Time Cost']
    # print((I**p1)*(E**p2)*T)
    Utility[i] = (A**p1)*(E**p2)*T
    Names[i] = (A**p1)*(E**p2)*T


Utility.sort(reverse = True)
x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x10 = 0
for  i in range(example_num):
    if Utility[0] == Names[i]:
        x1 = i
    if Utility[1] == Names[i]:
        x2 = i
    if Utility[2] == Names[i]:
        x3 = i
    if Utility[3] == Names[i]:
        x4 = i
    if Utility[4] == Names[i]:
        x5 = i
    if Utility[5] == Names[i]:
        x6 = i
    if Utility[6] == Names[i]:
        x7 = i
    if Utility[7] == Names[i]:
        x8 = i
    if Utility[8] == Names[i]:
        x9 = i
    if Utility[9] == Names[i]:
        x10 = i

print("Hi",hi.name,", the 10 jobs that are most suitble for you is: ",
      companies[x1].name,", ",companies[x2].name,", ",companies[x3].name,", ",
      companies[x4].name,", ",companies[x5].name,", ",companies[x6].name,", ",
      companies[x7].name,", ",companies[x8].name,", ",companies[x9].name,
      ", ",companies[x10].name,
      "!")


