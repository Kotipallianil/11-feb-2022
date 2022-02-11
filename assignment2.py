sno=int(input('student no:'))
sname=input('student name:')
s1=int(input('enter JAVA marks:'))
s2=int(input('enter TELUGU marks:'))
s3=int(input('enter AFM marks:'))
s4=int(input('enter OS marks:'))
s5=int(input('enter EE marks:'))
s6=int(input('enter OB marks:'))
total=s1+s2+s3+s4+s5+s6
avg=total/6
print('total marks:',total)
print('average marks:',avg)

if avg>=91:
    print('O Grade')
elif avg>=81:
    print('A Grade')
elif avg>=71:
    print('B Grade')
elif avg>=61:
    print('C Grade')
elif avg>=51:
    print('D Grade')
elif avg>=41:
    print('PASS')
else:
    print('FALI')
