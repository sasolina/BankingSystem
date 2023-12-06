# make a banking system
# create a new card 
# enter a pin so give them a pin
# save it all in a system allowing them to put money in and take money out give them an options of the money 5, 10, 20, 30
# sort code
# long code
# put all of them in a system 
# transfer money to others
# overdraft
# admin
# change their pin
import random
from random import randint


def signup():
  global firstname, lastname, PIN1, num1, num2, num3, num4, signup, PIN_str, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15, num16, num17, num18, num19, num20, cardnum_str, num21, num22, num23, num24, num25, num26, sortcode, sortcode_str
  firstname = str(input(f'\n''please enter your name: '))
  lastname = str(input(f'please enter your last name: '))
  print (f'welcome {firstname } {lastname} you will now be given a pin,card number and sort code, please keep this safe')
  num1 = random.randint(1,9)
  num2 = random.randint(1,9)
  num3 = random.randint(1,9)
  num4 = random.randint(1,9)
  PIN1 = (f'{num1}{num2}{num3}{num4}')
  PIN_str = str(PIN1)
  print(f'\n'+PIN1)
  PIN_str = str(PIN1)
  PIN_str = input(f'\n''confirm PIN: ')
  num5 = random.randint(1,9)
  num6 = random.randint(1,9)
  num7 = random.randint(1,9)
  num8 = random.randint(1,9)
  num9 = random.randint(1,9)
  num10 = random.randint(1,9)
  num11 = random.randint(1,9)
  num12 = random.randint(1,9)
  num13 = random.randint(1,9)
  num14 = random.randint(1,9)
  num15 = random.randint(1,9)
  num16 = random.randint(1,9)
  num17 = random.randint(1,9)
  num18 = random.randint(1,9)
  num19 = random.randint(1,9)
  num20 = random.randint(1,9)
  cardnum =  (f'{num5}{num6}{num7}{num8} {num9}{num10}{num11}{num12} {num13}{num14}{num15}{num16} {num17}{num18}{num19}{num20}')
  cardnum_str = str(cardnum)
  
  num21 = random.randint(1,9)
  num22 = random.randint(1,9)
  num23 = random.randint(1,9)
  num24 = random.randint(1,9)
  num25 = random.randint(1,9)
  num26 = random.randint(1,9)
  sortcode = (f'{num21}{num22}-{num23}{num24}-{num25}{num26}')
  sortcode_str = str(sortcode)


  if PIN1 == PIN_str:
    print(f'\n''welcome to GOSPEL bank')
    f = open('Bankdetails.txt','a')
    f.write('\n'+ firstname)
    f.write(':'+ lastname)
    f.write(':'+PIN_str)
    f.write('\n'+ cardnum_str)
    f.write('\n'+ sortcode_str)
    f.close()
    login()
    
  elif PIN1 != PIN_str:
      print('Incorrect PIN')
  

def login(): 
  with open('Bankdetails.txt','r') as f:
    PIN_str = input(f'\n''please insert your PIN: ')
    for line in f:
     if PIN_str in line:
        print(f'\n''successful login')
        transaction()
    else:
        print('incorrect')
        login()

def PINchange():
  with open('Bankdetails.txt','r') as f:
    PIN_str = input('please insert your PIN: ')
    for line in f:
      line.strip() == line
      if PIN_str in line:
        print('successful login')
        with open('Bankdetails.txt','a') as f:
          PINchange = input('please insert your new PIN: ')
          firstname = str(input('please enter your name: '))
          lastname = str(input('please enter your last name: '))
          if firstname and lastname in line:
            f = open('Bankdetails.txt','r+')
            f.write('\n'+ firstname)
            f.write(':'+ lastname)
            f.write(':'+PINchange)
            f.close()
          elif firstname and lastname not in line:
            print('incorrect firstname or lastname, please try again')
            PINchange()
          else:
            print('error')
            PINchange()
          return
      else: 
        print('try again')
        return     
        

def transaction():
  global firstname, lastname, signup, login, transaction, cash, balance_str
  money = input(f'\n''welcome back would you like to insert money or take money out press (I) or (O)').upper()
  if money == 'I':
    cash = input(f'\n''how much do you want to do insert, please press one of the following (5) (10) (15) (20): ')
    if cash == '5':
      print('you have inserted £5')
      bal1 = (100 + 5)
      balance_str = str(bal1)
      balance()
    elif cash == '10':
      print('you have inserted £10')
      bal1 = (100 + 10)
      balance_str = str(bal1)
      balance()
    elif cash == '15':
      print('you have inserted £15')
      bal1 = (100 + 15)
      balance_str = str(bal1)
      balance()
    elif cash == '20':
      print('you have inserted £20')
      bal1 = (100 + 20)
      balance_str = str(bal1)
      balance()
  elif money == 'O' :
    cash = input(f'how much do you want to take out, please press one of the following (5) (10) (15) (20)')
    if cash == '5':
      print('you have taken out £5')
      bal1 = (100 - 5)
      balance_str = str(bal1)
      balance()
    elif cash == '10':
      print('you have taken out £10')
      bal1 =  (100 - 10)
      balance_str = str(bal1)
      balance()
    elif cash == '15':
      print('you have taken out £15')
      bal1 = (100 - 15)
      balance_str = str(bal1)
      balance()
    elif cash == '20':
      print('you have taken out £20')
      bal1 = (100 - 20)
      balance_str = str(bal1)
      balance()

def balance():
  global bal1, cash
  print(balance_str)
  with open('Bankdetails.txt','r') as f:
    cardnum_str = input('please enter your card number: ')
    PIN_str = input('please enter your PIN: ')
    for line in f:
      if cardnum_str and PIN_str in line:
        print(f'\n''thank you your process is being approved')
      with open('financemanage.txt','a') as f:
          f = open('financemanage.txt','a')
          f.write('\n'+cardnum_str)
          f.write(' : '+PIN_str)
          f.write(' : £'+balance_str)
          f.close()
          transfer()
    else:
        print(f'\n''incorrect bank details please try again')
        balance()
       

def transfer():
  print(f'\n''please enter the name of the individual you want to give money to')
  with open('Bankdetails.txt','r+') as f:
    firstname = input(f"please enter their first name: ")
    lastname = input(f"please enter their last name: ")
    cardnum_str = input('please enter their card number: ')
    sortcode_str = input('please enter their sortcode')
    for line in f:
      if firstname and lastname and cardnum_str and sortcode_str in line:
        cash = input(f'\n''how much do you want to do transfer, please press one of the following (5) (10) (15) (20): ')
    if cash == '5':
      print(f'you have tranfered £5 to {firstname}')
      wat = 100 - 5 
      wat = str(wat)
    elif cash == '10':
      print(f'you have tranfered £10 to {firstname}')
      wat = 100 - 10
      wat = str(wat)
    elif cash == '15':
      print(f'you have tranfered £15 to {firstname}')
      wat = 100 - 15
      wat = str(wat)
    elif cash == '20':
      print(f'you have tranfered £20 to {firstname}')
      wat = (balance_str - cash)
      wat = str(balance - cash)
      print(f'\n''thank you your process is being approved')
      with open('financemanage.txt','r+') as f:
          f = open('financemanage.txt','a')
          f.write('\n'+cardnum_str)
          f.write(' : '+sortcode)
          f.write(' : £'+wat)
          f.close()
          transfer()
print (f'\n' 'Welcome to the GOSPEL bank')
  
checking = input(f'\n''if you already have an account press (Y) to make a new one press (N) if you want to change your PIN press (C): ').upper()

if checking == 'Y':
  login()
elif checking == 'N':
  signup()
elif checking == 'C':
  PINchange()
