u=float(input("initial velocity="))
a=float(input("acceleration="))
t=float(input("Time="))
if t >= 0:
    v=u+(a*t)
    s=(u*t)+((a*t**2)/2)
    print("final velocity=",v)
    print("distance travelled=",s)
else:
    print("enter valid time")





