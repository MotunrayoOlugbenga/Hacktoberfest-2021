# printing students grades for a cgpa

n=input("number of student:")
n=int(n)
i=0
while(i<n):
    print("give me student gp")
    gp=input( )
    gp=float(gp)
    if gp>=4.5 and gp<=5.0:
        print("student gp:first class")
    elif gp>=3.5 and gp<=4.49:
        print("student gp: second class upper")
    elif gp>=2.5 and gp<=3.49:
        print("student gp:second class lower")
    elif gp>=1.5 and gp<=2.49:
        print("student gp:third class")
    elif gp>=1.0 and gp<=1.49:
        print("student gp:pass")
    else:
        print("invalid")
    i =i+1
 