import pandas as pd
import matplotlib.pyplot as plt

def menu():
    print()
    print("*******************************************************")
    print("       MEDICAL STORE MANAGEMENT SYSTEM      ")
    print("*******************************************************")
    print("0. Know about the project")
    print("1. Reading file stock")
    print("2. Reading file stock without index")
    print("3. Make an entry of new medicine in stock")
    print("4. Arrange medicines in stock alphabetically")
    print("5. Delete medicine details if it is out of stock")
    print("6. Update details of medicine in stock")
    print("7. Show list of medicines in stock")
    print("8. Read few records from the stock")
    print("9. Read some medicines' details from top and bottom arranged according to code")
    print("10. Show price list of medicines")
    print("11. Show records of staff in the store")
    print("12. Add new employee record in staff")
    print("13. Find maximum salary of staff")
    print("14. Find minimum salary of staff")
    print("15. Record of sold medicines in detail")
    print("16. Customer's order for medicine")
    print("17. Search medicine by name")
    print("18. Line1 plot of medicines' names and prices")
    print("19. Bar Plot of names of medicines and their date of expiry")
    print("20. Bar Plot of employees' names and their salaries")
    print("21. Bar Plot of medicines' names and their quantity in stock")
    print("22. Bar Plot of medicines' names and their prices")
    print()
    print("**********************************************************")

menu()

def about():
    print("In MEDICAL STORE MANAGEMENT SYSTEM project there are 3 CSV files named as- stock,staff and bill. There are 22 options including six plots")
    cnt()
        
def stockcsv():
    print("Reading file stock...\n\n")
    df=pd.read_csv("Stock.csv")
    print(df)
    cnt()
    
def no_index():
    df=pd.read_csv("Stock.csv",index_col=0)
    print("File without index:")
    print(df)
    print()
    cnt()
    

def newmed():
    df=pd.read_csv("Stock.csv",index_col=0)
    print("Current Stock: ")
    print(df)
    print()
    print("Enter details of new medicine")
    a=int(input("Enter medicine code: "))
    b=input("Enter medicine name: ")
    c=input("Enter date of expiry: ")
    d=int(input("Enter quantity: "))
    e=int(input("Enter price: "))
    df.loc[a]=[b,c,d,e]
    print()
    print("New medicine added in stock\n")
    print(df)
    cnt()

def sortmed():
    print("Displaying names of medicines in ascending order...")
    print()
    df=pd.read_csv("Stock.csv",index_col=0)
    df=df.sort_values('mname')
    print(df)
    cnt()

def removemed():
    df=pd.read_csv("Stock.csv",index_col='mcode')
    print(df)
    print()
    mcode=int(input("Enter code of the medicine to be deleted: "))
    print("\nDeleting medicine from file stock\n")
    df.drop(mcode,axis=0,inplace=True)
    print("Record of Medicine temporarily deleted")
    print(df)
    cnt()
    

def updatemed():
    df=pd.read_csv("Stock.csv",index_col='mcode')
    print(df)
    a=int(input("\nEnter medicine code that has to be updated: "))
    b=input("Enter medicine name: ")
    c=input("Enter date of expiry: ")
    d=int(input("Enter quantity: "))
    e=int(input("Enter price: "))
    df.loc[a]=[b,c,d,e]
    print("\nData successfuly updated")
    print(df)
    cnt()

def medstock():
    print("Displaying only Account no. , name and balance...")
    df=pd.read_csv("Stock.csv",usecols=['mname','quan'])
    print(df)
    cnt()

def read_rows():
    n=int(input("Enter number of recors to show: "))
    print("Showing ",n," records")
    df=pd.read_csv("Stock.csv",nrows=n)
    print(df)
    cnt()

def top_bottom():
    r=int(input("Enter number of records to be shown from top and botttom: "))
    print("\nShowing ",r," records from top and botttom")
    df=pd.read_csv("Stock.csv")
    print("Top ",r," records")
    print(df.head(r))
    print()
    print()
    print("Last ",r," records")
    print(df.tail(r))
    cnt()

def pricelist():
    print("Medicine price list sorted in ascending order")
    df=pd.read_csv("Stock.csv",index_col=0,usecols=['mname','price'])
    df=df.sort_values('mname')
    print(df)
    cnt()
    
def readstaff():
    print("Reading file staff..")
    print()
    print()
    df=pd.read_csv("Staff.csv",index_col=0)
    print(df)
    cnt()
    
def new_staff():
    print("\nOld employees record in file staff")
    print()
    df=pd.read_csv("Staff.csv")
    print(df)
    print()
    print()
    e=int(input("Enter number of employees to be added: "))
    for i in range(1,e+1):
        print("Enter details of employee ",i)
        id=int(input("Enter the id "))
        name=input("Enter name: ")
        age=int(input("Enter age: "))
        profile=input("Enter profile: ")
        mobile=int(input("Enter mobile no. "))
        salary=int(input("Enter salary: "))
        x=5+i
        df.at[x,:]=[id,name,age,profile,mobile,salary]
    print("\nEmployee/s added\n")
    print(df)
    cnt()

def maxsal():
    df=pd.read_csv("Staff.csv")
    print(df)
    print("\nHighest salary of staff: ")
    print(df.salary.max())
    cnt()

def minsal():
    df=pd.read_csv("Staff.csv")
    print(df)
    print("\nLowest salary of staff: ")
    print(df.salary.min())
    cnt()

def billrec():
    print("Reading sales records")
    print()
    print()
    df=pd.read_csv("Bill.csv",index_col=0)
    print(df)
    cnt()

def order():
    df=pd.read_csv("Bill.csv",index_col=0)
    print(df)
    m=int(input("Enter mobile number"))
    n=input("Enter medicine name: ")
    q=int(input("Enter quantity: "))
    p=int(input("Enter price: "))
    bill=q*p
    print(m,"  Your bill is ",bill,"  You have bought ",n,q,'pieces')
    p=int(input("Enter payment you are giving: "))
    balance=p-bill
    print("You will get back Rs. ",balance)
    cnt()
    
def searchmed():
    df=pd.read_csv("Stock.csv")
    print(df)
    print()
    nm=input("Enter the name of the medicine to be searched: ")
    print(df.loc[df['mname']==nm])
    cnt()

def line_plot():
    print("Line plot")
    df=pd.read_csv("Stock.csv")
    print(df)
    x=df['mname']
    y=df['price']
    plt.title("Medicines Names and Prices")
    plt.xlabel("Medicine")
    plt.ylabel("Price")
    plt.xticks(rotation=30)
    plt.plot(x,y,marker='X',ls="dashed",linewidth=4,color="y")
    plt.show()
    cnt()

def bar_plot():
    print('Bar Plot')
    df=pd.read_csv("Stock.csv")
    print(df)
    x=df['mname']
    y=df['dateofexp']
    plt.title("Medicines Names and their date of expiry")
    plt.xlabel("Medicine")
    plt.ylabel("Date of expiry")
    plt.xticks(rotation=30)
    plt.legend()
    plt.bar(x,y,color=['red','green'])
    plt.show()
    cnt()

def bar1_plot():
    print('Bar Plot')
    df=pd.read_csv("Staff.csv")
    print(df)
    x=df['name']
    y=df['salary']
    plt.title('Employees Names and their salary')
    plt.xlabel('Names')
    plt.ylabel('Salary')
    plt.xticks(rotation=30)
    plt.bar(x,y,color=['red','green'])
    plt.show()
    cnt()

def barh_plot():
    print('Horizontal Bar Plot')
    df=pd.read_csv("Stock.csv")
    print(df)
    x=df['mname']
    y=df['quan']
    plt.title('Medicines Names and their quantity in stock')
    plt.xlabel('Quantity')
    plt.ylabel('Medicines')
    plt.barh(x,y,color='blue',edgecolor="pink")
    plt.show()
    cnt()

def barh1_plot():
    print('Horizontal Bar Plot')
    df=pd.read_csv("Stock.csv")
    print(df)
    x=df['mname']
    y=df['price']
    plt.title('Medicines Names and their')
    plt.xlabel('Price')
    plt.ylabel('Medicines')
    plt.barh(x,y,color='orange',edgecolor="black")
    plt.show()
    cnt()

def cnt():
    global x
    print("\n\n")
    x=input("Want to continue?\nEnter 'y' or 'Y' to continue and\nEnter 'n' or 'N' to terminate:\n")
    if x=='y' or x=='Y':
        choice()
    else:
        print("Terminated!\nThank you")
    

def choice():
    print()
    opt=int(input("Enter your choice: "))
    print()
    if opt==0:
        about()
    elif opt==1:
        stockcsv()
    elif opt==2:
        no_index()
    elif opt==3:
        newmed()
    elif opt==4:
        sortmed()
    elif opt==5:
        removemed()
    elif opt==6:
        updatemed()
    elif opt==7:
        medstock()
    elif opt==8:
        read_rows()
    elif opt==9:
        top_bottom()
    elif opt==10:
        pricelist()
    elif opt==11:
        readstaff()
    elif opt==12:
        new_staff()
    elif opt==13:
        maxsal()
    elif opt==14:
        minsal()
    elif opt==15:
        billrec()
    elif opt==16:
        order()
    elif opt==17:
        searchmed()
    elif opt==18:
        line_plot()
    elif opt==19:
        bar_plot()
    elif opt==20:
        bar1_plot()
    elif opt==21:
        barh_plot()
    elif opt==22:
        barh1_plot()
    else:
        print("Invalid Choice!")
        print("Please choose from the above options")
        print("\a")
choice()

