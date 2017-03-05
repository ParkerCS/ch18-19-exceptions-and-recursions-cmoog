'''
- Personal investment
Create a single recursive function (or more if you wish), which can answer the first three questions below.  For each question, make an appropriate call to the function. (5pts each)
'''

#1.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY, so MPR is APR/12).  Assuming you make no payments for 6 months, what is your new balance?  Solve recursively.

def g(balance, index):
    balance += balance * 0.016666666666666666666
    if index < 7:
        g(balance, index + 1)
    if index == 6:
        print("After 6 months, your balance would be:", balance)

g(10000, 1)


#2.  You have $5000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).  You make the minimum payment of $100 per month for 36 months.  What is your new balance?  Solve recursively.

def f(balance, index):
    balance += balance * 0.016666666666666666666
    balance -= 100
    if index < 37:
        f(balance, index + 1)
    if index == 36:
        print("After 36 months, paying 100 per month, your balance would be:", balance)

f(5000, 1)

#3.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).  If you make the minimum payment of $100 per month, how many months will it take to pay it off?  Solve recursively.

def h(balance, index, payed):
    balance += balance * 0.016666666666666666666
    balance -= 100
    if balance <= 0:
        payed = True
        print("It took", index, "months")
    if not payed and index < 1000:
        h(balance, index + 1, False)
h(10000, 1, False)


#4  Pyramid of Cubes - (10pts) If you stack boxes in a pyramid, the top row would have 1 box, the second row would have two, the third row would have 3 and so on.  Make a recursive function which calculates the TOTAL NUMBER OF BOXES for a pyramid of boxes n high.  For instance, a pyramid that is 3 high would have a total of 6 boxes.  A pyramid 4 high would have 10.