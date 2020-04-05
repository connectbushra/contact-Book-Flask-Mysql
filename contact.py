def validate(name):
    if name in contact:
        return 1
    else:
        return 0
    
def print_contact(name):
    print("Name - ",name,end="")
    for val in contact[name]:
        print(" ",val,end="")
    print()
    
    
def add_to_existing(name):
    global contact
    if(validate(name)):
        temp_list=list(contact[name])
        print_contact(name)
        temp_list.append(int(input("Enter number to store : ")))        
        contact[name]=temp_list
    else:
        print("Name does not exists.")
        
    
def view(name):
    if validate(name):
        print_contact(name)
    else:
        print("No Match Found !")

def addcontact():
    global contact
    token=False
    name=''
    while True:
        name=input("Enter a Name : ")
        if(validate(name)):
            op=int(input(name," Found.\n1. add phone number for this name or\n2. try again "))
            if op==1:
                add_to_existing(name)
                token=False
                break
        else:
            token=True
            break
    if token:
        put=True
        while True:
            #phone_no1=int(input("enter phone number:"))
            phone_no1=int(input("Phone Number:"))
            print("Do you want to add more information??its optional,press['Y/N']")
            opt=input()
            if opt.lower()=='y':
                company=input("entercompany  name:")
                phone_no2=int(input("enter another phone number:"))
                email=input("enter your email:")
                contact[name]=[phone_no1,company,phone_no2,email]
                print("your contact is saved.  \n")
                break
                
            else:
                contact[name]={phone_no1}
                break
            
    
def edit():
    global contact
    name=input("enter name: ")
    if(validate(name)):
        print("1. Primary Phone Number\n2. company Name\n3. Other Phone Number\n4. email\n99. Return")
        while True:
            choice=int(input("Enter Option to change : "))
            if choice !=99:
                print("Current Entry : ",contact[name][choice - 1])
                contact[name][choice-1]=input(("Enter new entry"))
            else:
                break
        
    else:    
        print("contact not exist !")

def delete():
    name=input("enter name:")
    if(validate(name)):
        del contact[name]
        print("succesfully deletd")
    else: 
        print("contact not found")
def search():
    global contact 
    token=0
    srch=input("enter name to search:")
    for name in contact.keys():
        if srch in name:
            view(name)#print(contact[name])
            token=1
    if token==0:
        print("not match")
               
def groups():
    global contact
    global group
    op=int(input("1. family \n2. friend \n 3.colleague \n4. create group"))
    if op==1:
        if group.family in group:
            for name in group:
                print(name," , ",end="")
        else:
           
            print("No contact found on this group")
        inp=int(input("Do want to add contact, Press 1"))
        if inp==1:
            while True:
                name=input("Enter name to Add ")
                if validate(name):
                    string=list(group[family])
                    string.append(name)
                    group[family]=string
                    print("Added successfully")
                    break
                else:
                    choice=input(name," does not exist. Try again or return (1 or 99)")
                    if choice ==1:
                        continue
                    else:
                        break
    
    
          
       
group=dict()

contact=dict()
while True:
    print(" 1.Add new contact: \n 2.edit contact: \n 3.delete contact: \n 4.search contact: \n 5.view contact: \n 6. Add to existing\n 7. Manage Groups 99:exit")
    
    op=int(input())
    if op==1:
        addcontact()
    elif op==2:
        edit()
    elif  op==3:
        delete()
    elif op==4:
        search()
    elif op==5:
        view(input("Enter name : "))
        
    elif op==6:
        add_to_existing(input("Enter name of recipient"))
        
    elif op==7:
        groups()
    elif op==99:
        break
    else:
        print("innvalid option")
    

        #phone_no1=int(input("enter phone number"))
               #name=input("enter name")
               #company=input("entercompany  name:")
               #phone_no2=int(input("enter another phone number:"))
               #email=input("enter your email:")
               #contact[name]=[phone_no1,name,company,title,phone_2,email] 
               #print("")