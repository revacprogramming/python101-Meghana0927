# Functions


def computepay(h, r):
    pass  # ...


hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)



def computepay(h, r):
    computepay=0
    pay=float(computepay)
    if h<40:
        pay=(h*r)
    if h>40:
        pay=((40*r)+(h-40)*1.5*r)
    return pay
    
hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter Rate:")
r=float(rate)

p = computepay(h, r)
print("Pay", p)