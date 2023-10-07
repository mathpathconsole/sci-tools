import sympy
from sympy import *
from sympy.plotting import plot3d
import colorama
from colorama import Style, Fore, Back
a, b, c, d, e, f, g, h, i, j, k, l, m, n, p, r, s, t, u, v, x, y, z, nu, rho, phi= symbols("a b c d e f g h i j k l m n p r s t u v x y z nu rho phi")
init_printing(use_unicode=False)
colorama.init()

print(Fore.YELLOW,20*" ","Trigonometric Sum"," "*25)
print(Style.RESET_ALL)
print(""" You can define simply,
#definition: f(x)=trigonometric function -> Sum(f(x*i),(i,limit1,limit2)

Sample: >>:Sum(f(n),(n,0,5)) when typed, we display;

 _5_       
 \ `      
  )   f(n)   = f(0) + f(1) + f(2) + f(3) + f(4) + f(5)
 /_,      
n = 0
So, structure like this; f(n), (variable, limit1, limit2)
Triangle wave sample: >>:Sum(sin(n*x),(n,0,16))
Square wave sample: >>:Sum(sin((2*n+1)*x)/(2*n+1),(n,0,198))

                            Stars of the Sky|Reşat Berk
""")
print(Style.RESET_ALL)
print(Fore.CYAN)

while True:
    a=input(">>:")
    u=sympify(a)
    c=sympify(a).doit()
    pprint(u)
    #pprint(c)
    plot(c,show=False).show()
    print("")

#libraries:
#--colorama
#--sympy

    
    
    



