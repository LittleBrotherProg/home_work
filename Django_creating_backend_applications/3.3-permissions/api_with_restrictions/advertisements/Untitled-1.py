from turtle import *; from math import acos, pi, sqrt
k = 20; home(); begin_poly(); right(60)
for i in range(2):fd(10*k); right(120); fd(5*k); right(240)
right(120); fd(3*k); right(90); fd(20*sqrt(3)*k); right(90); fd(8*k); right(120)
for i in range(2):fd(10*k); left(120); fd(5*k); left(240)
end_poly(); t = [(round(i[0],2),round(i[1],2)) for i in get_poly()[:-1]]
ln = lambda x1,y1,x2,y2,X,X1,X2,Y,Y1,Y2: x1*y2-x2*y1==0 and (X1>=X>=X2 or X2>=X>=X1) and (Y1>=Y>=Y2 or Y2>=Y>=Y1)
def f(x1,y1,x2,y2): 
    a = acos((x1*x2+y1*y2)/(sqrt(x1*x1+y1*y1)*sqrt(x2*x2+y2*y2)))
    return a*180/pi if (y1*x2-x1*y2)>0 else -(a*180/pi) 
otv = ['line' if 1 in [ln((m[0]-n[0]),(m[1]-n[1]),(x*k-n[0]),(y*k-n[1]),x*k,n[0],m[0],y*k,n[1],m[1]) for n, m in zip(t,t[1:])] 
       else 361>sum([f((n[0]-x*k),(n[1]-y*k),(m[0]-x*k),(m[1]-y*k)) for n, m in zip(t,t[1:])])>359
       for x in range(-100,100) for y in range(-100,100)] 
print(otv.count('line'), otv.count(1)) # 36 - линия; 174 - в контуре
# Расставим точки для наглядности 
pu()
for x in range(-7,7):
    for y in range(-20,20):
        setpos(x*k,y*k)
        if 1 in [ln((m[0]-n[0]),(m[1]-n[1]),(x*k-n[0]),(y*k-n[1]),x*k,n[0],m[0],y*k,n[1],m[1]) for n, m in zip(t,t[1:])]:
            dot(3, 'red')
        elif 361>sum([f((n[0]-x*k),(n[1]-y*k),(m[0]-x*k),(m[1]-y*k)) for n, m in zip(t,t[1:])])>359:
            dot(3,'green')