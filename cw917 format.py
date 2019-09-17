x = 4.33
y = 2.33
z = x * y

#sep='' removes spaces from print funtions

print("The value of z is:",z,".")
#The value of z is: 10.0889 .

print("The value of z is:",z,".",sep='')
#The value of z is:10.0889.

print("The value of z is:" +str(z) +".")
#The value of z is:10.0889.

print("The value of z is:",format(z,',.2f'),'.')
#The value of z is: 10.09 .

print("The value of z is: ",format(z,',.2f'),".",sep='' )
#The value of z is: 10.09.

print("---------------------------------------------------------------")

print(x,y,z)
#4.33 2.33 10.0889

print(str(x) + str(y) + str(z))
#4.332.3310.0889

print(str(x).rjust(10) + str(y).rjust(10) + str(z).rjust(10))
#      4.33      2.33   10.0889

print(str(x).ljust(10) + str(y).ljust(10) + str(z).ljust(10))
#4.33      2.33      10.0889

print("Center".center(80))
#                                     Center                                     
