import mysql.connector as m
con =  m.connect(host="localhost", user="root", password="root", database='sam')
print(con)
c=con.cursor()
create='create table if not exists password_manager(Username varchar(100) not null, Password varchar(100) not null, Website varchar(150) not null);'
c.execute(create)
print('')
print('Database successfully created.')

def insert():
    print('')
    print('Adding your details..')
    print('')
    ans='Y'
    while True:
            user=input(str("Enter username :"))
            if user=='':
                user=input(str('Error, Enter a valid username :'))
                if user=='':
                    print('Error, please try again.')
                    break
            if user!='':
                pas=input(str("Enter password :"))
                if pas=='':
                    pas=input(str('Error, Enter a valid password :'))
                    if pas=='':
                        print('Error, please try again.')
                        break
                if pas!='':
                    web=input(str('Enter website name :'))
                    if web=='':
                        web=input(str('Error, Enter a valid website :'))
                        if web=='':
                            print('Error, please try again.')
                            break
                    if web!='':   
                        a='insert into password_manager values'+ '('+ '"' + user + '"' +','+ '"' + pas + '"' +','+ '"' + web + '"'+ ');'
                        c.execute(a)
                        con.commit()
                        print('Entry successful.')
                        ans=input('Would you like to insert another username? Y/N? :')
                        if ans=='Y':
                            insert()
                        elif ans=='N':
                           input('Press Enter to continue.')
                           break
                        else:
                           print('Invalid choice.')
                           input('Press Enter to continue.')
                           break
    
def display():
        print('')
        print('Displaying all details..')
        print('')
        e='select * from password_manager;'
        s=c.execute(e)
        r=c.fetchall()
        if r==[]:
                   print('Empty database. Please enter values using Insert command.')
        else:       
                   print("Usernames, Passwords and Wesbites are :")
                   print('')
                   for i in r:
                       print(i)       
        input('''
Press Enter to continue.''')
        
def select():
    print('')
    print('Displaying preferred details..')
    print('')
    ans='Y'
    while True:
        a=input('Enter username :')
        if a=='':
            a=input('Invalid Username. Enter valid username :')
            if a=='':
                print('Invalid Username. Please try again.')
                break
        e='select * from password_manager where username='+'"'+a+'"'
        c.execute(e)
        r=c.fetchone()
        print("")
        print("Username and Password :")
        print("")
        if r==None:
            print('No details found. Try another username.')
        else:    
            print(r)
        print('')
        ans=input('Would you like to try another username? Y/N? :')
        if ans=='Y':
            select()
        elif ans=='N':
            input('Press Enter to continue.')
            break
        else:
            print('Invalid choice.')
            input('Press Enter to continue.')
            break
            
def delete():
    print('')
    print('Deleting details that are no longer needed..')
    print('')
    ans='Y'
    while True:
        a=input(str('Enter username present in table to be deleted :'))
        if a=='':
            a=input(str('Error, Please enter username to be deleted :'))
            if a=='':
                print('Error, please try again.')
                print('')
                input('Press Enter to continue')
                break
        d='delete from password_manager where username='+'"'+a+'"'+';'
        c.execute(d)
        con.commit()
        print('Details of Username', a, 'successfully deleted.')
        ans=input('Would you like to delete another username? Y/N? :')
        if ans=='Y':
            delete()
        elif ans=='N':
            input('Press Enter to continue.')
            break
        else:
            print('Invalid choice.')
            input('Press Enter to continue.')
            break

def clear():
    print('')
    print('Clearing all details..')
    print('')
    e='select * from password_manager'
    c.execute(e)
    r=c.fetchall()
    a='truncate table password_manager;'
    c.execute(a)
    if r==[]:
        print('Empty table. Cannot delete from empty table.')
    else:
        print('Details on table successfully deleted.')
    input('Press Enter to continue.')
    

print('')
input('Press Enter to begin')
while True:
    print('''
    Welcome to password manager :)
    
    Here you can:
    
    Press 1 to add your details
    Press 2 to display all your details
    Press 3 to view particular details
    Press 4 to delete particular details
    Press 5 to clear all details
    Press 6 to exit password manager
    ''')
    ch=input('Enter your choice :')
    if ch=='1':
        insert()
    elif ch=='2':
        display()
    elif ch=='3':
        select()
    elif ch=='4':
        delete()
    elif ch=='5':
        clear()
    elif ch=='6':
        con.close()
        print('Thank you for using password manager :)')
        input('Press Enter to Exit.')
        break
    else:
        print('Invalid choice.')
        input('Press Enter to continue.')
                
                
                
                
                

