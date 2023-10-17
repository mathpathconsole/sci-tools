#Numerical approach to integral -- Reşat Berk --look 'numerical integral' on 'src4methods' file.

from sympy import * #this is symbolic computing. need some piece for using symbols
x,y,z=symbols('x y z') #here are symbols in SymPy lib.
area_data=[]

def find_area(f='your function as x',a='low-limit',b='up-limit',
              n='rectangles amount'):
    
    delta_x=(float(b)-float(a))/float(n)
    alim=a
    blim=b #use these real integral at below.
    
    while a>=0: #start for low limit
        
        a +=delta_x #-->a increasing by every delta_x amount. so if how many reactangle put that amount 
        i=sympify(f).subs('x',float(a)) #put a in f function instead of x.
        
        print('f({})= '.format(a),i) #print the f increasing of a.
        
        area=delta_x*i #every small area (please look approach image.)
        area_data.append(area) #append the area_data then collect all of them in below.
        
        if a>=float(b): #end limit-b
            
            if round(a,6)>round(b,6): #round(numb,limitted) --for edited some over the original number like x**2,0,2,//300<100
                exact_area=sum(area_data) #sum each of small area data element.
                print("----approximate area *NotClear ~= ",exact_area)
                print("----exactly area = ",integrate(f,(x,alim,blim)).evalf()) #real answer of function. (you can change x-symbol)
                area_data.clear() #del data for new using.
                break
            else:
                exact_area=sum(area_data) #sum each of small area data element.
                print("----approximate area ~= ",exact_area)
                print("----exactly area = ",integrate(f,(x,alim,blim)).evalf()) #real answer of function. (you can change x-symbol)
                area_data.clear() #del data for new using.
                break
find_area(f=x+2, a=0, b=2, n=20)


        
##INFO##
#-sympy is a symbolic computing. we need for use symbols our code (y=f(x); x is a symbol) then we used find for exactly value.
  #--sympy piceses are in this code; x,y,z=symbols('x y z'), sympify(), .subs(), integrate() --Also you can look sympy on web.
        
#operator means: +: add, -: minus, /:divide  *:multiply, **:power

        

    
    
    
