l1 = int(input('Length of Rectangle 1: '))
w1 = int(input('width of Rectangle 1: '))
l2 = int(input('Length of Rectangle 2: '))
w2 = int(input('width of Rectangle 2: '))

a1 = l1 * l2
a2 = l2 * w2

if a1 > a2:
    print('Rectangle 1 is bigger than Rectangle 2')
    print('Area of Rectangle 1: ',a1 )
    print('Area of Rectangle 2: ',a2 )
else:
    if a2 > a1:
        print('Rectangle 2 is bigger than Rectangle 1')
        print('Area of Rectangle 1: ',a1 )
        print('Area of Rectangle 2: ',a2 ) 
    else:
        print('Both Rectangles have equal areas')
        print('Area of Rectangle 1: ',a1 )
        print('Area of Rectangle 2: ',a2 )
hold = int(input(' '))

