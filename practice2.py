#Taking data from students and store them in file(studentdetal.txt)
f=open("studentdetail.txt","a+")#creating and opening new file studentdetail.txt
class student:
    def __init__(self,name,address,DOB,Father_name):
        self.name=name
        self.address=address
        self.DOB=DOB
        self.Father_name=Father_name
    def printname(self):
        print(self.name)   
        print(self.address)
        print(self.DOB)
        print(self.Father_name)        
j=int(input("Enter the number of student :"))
i=0
a=""
while(i<j):
    a="s"+str(i)
    name=input("Enter Name")
    add=input("Enter Address")
    dob=input("Enter DOB")
    father=input("Enter Father name")    
    a=student(name,add,dob,father)
    b=("Name="+a.name+"\t"+"Address="+a.address+"\t"+"DOB="+a.DOB+"\t"+"Father name="+a.Father_name+"\n")
    f.write(b)
    print("\n")
    i+=1
f.close()
