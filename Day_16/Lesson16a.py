import sqlite3

class myDatabase:
    def __init__(self,dbname):
        self.conn= sqlite3.connect(dbname)
        self.cur=self.conn.cursor()
        self.cur.execute("Create Table if not exists Employee (Id integer primary key, Name varchar (50), Email Varchar (50), DOB Datetime)")
        self.conn.commit()

    def AddData(self,Id,Name,Email,DOB):
        self.cur.execute("Insert into Employee (Name,Email,DOB) values(?,?,?,?)",(Name,Email,DOB))
        self.conn.commit()

    def Insert(self):
        print('Add new Data')
        id=input('Enter id Number          :')
        name=input('Enter Employee name    :')
        email=input('Enter Email address   :')
        dob=input('Enter Date Of Birth     :')

        self.AddData(id,name,email,dob)

    def showData(self):
        print('List all employee information')
        self.cur.execute("select * from Employee ")
        self.conn.commit()

        print("%-5s %-30s %-20s %-15s" %('Id','Employee Name','Email Address','Date Of Birth'))
        print(70 *'=')

        employee= self.cur.fetchall()
        for Data in employee:
            print("%-5s %-30s %-20s %-15s" %(Data[0],Data[1],Data[2],Data[3]))

            print("Total Record   : %s" %len(employee))

    def searchData(self,idn):
        found=False
        self.cur.execute("select * from Employee where Id=?",(idn,))
        mydata=self.cur.fetchall()
        if len(mydata)>0:

            for Data in mydata:
                print('Id Number     :%s' % (Data[0]))
                print('Employee Name :%s' % (Data[1]))
                print('Email Address :%s' % (Data[2]))
                print('Date of Birth :%s' % (Data[3]))
                print(60*"=")

            found= True
        
        else:
            print('Sorry record not found !!!')
        return found

    def Find(self):
        print('search by id')
        print(50*"=")
        idn=input('Enter Employee id number: ')
        found = self.searchData(idn,)


obj=myDatabase('Emp.db')
obj.Insert()
obj.showData()
#obj.Find()        