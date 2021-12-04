
def details():
    print('--WELCOME TO 3HACKERS PAGE--')
    global a
    a=input('Select and enter your user id:')
    global b
    b=int(input('Enter your phone number:'))
    if len(str(b))==10:
        password()
    else:
        print('invalid mobile number\n--TRY AGAIN--')
        details()
    
def password():
    global c
    c=input('Please enter a password:')
    import re
    flag = 0
    while True:  
     if (len(c)<8):
        flag = -1
        break
     elif not re.search("[a-z]",c):
        flag = -1
        break
     elif not re.search("[A-Z]",c):
        flag = -1
        break
     elif not re.search("[0-9]",c):
        flag = -1
        break
     elif not re.search("[_@$]",c):
        flag = -1
        break
     elif re.search("\s",c):
        flag = -1
        break
     else:
        flag = 0
        print("Valid Password")
        global d
        d=input('confirm password:')
        if c==d:
          login()
          break
        else:
          print('two passwords are not matching \n --TRY AGAIN--')
          password()
          break
    if flag ==-1:
      print("Not a Valid Password\n--TRY AGAIN--")
      password()
      
def login():
    print('--WELCOME TO LOGIN PAGE--')
    e=input('Enter your user id:')
    if e==a:
       f=input('Enter password:')
       if f==c:
          print('-CONGRATS YOU HAVE LOGGED IN SUCCESSFULLY-')
       else:
          print('incorrect password\n--TRY AGAIN--')
          login()
    else:
       print('--you have entered wrong user id try again--')
       login()
details()
