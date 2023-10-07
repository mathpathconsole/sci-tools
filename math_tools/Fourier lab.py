import sympy
from sympy import *
from sympy.plotting import plot3d
import colorama
from colorama import Style, Fore, Back
a, b, c, d, e, f, g, h, i, j, k, l, m, n, p, r, s, t, u, v, x, y, z, nu, rho, phi= symbols("a b c d e f g h i j k l m n p r s t u v x y z nu rho phi")
init_printing(use_unicode=False)
colorama.init()

#sin(x)+sin(3*x)/3 + sin(5*x)/5... so , sin((2*n+1)*x)/(2*n+1)
#c=Sum(sin(A*x)/A,(n,0,198)).doit()

#                           *Reşat Berk tarafından oluşturulmuştur*
print(Fore.YELLOW,20*" ","Trigonometrik toplam(Fourier Lab.)"," "*25)
print(Style.RESET_ALL)
print(""" Tanımalama işlemi basittir.
#Tanım: f(x)=trigonometrik fonksiyon -> Sum(f(x*i),(i,sınır1,sınır2)
basit bir şekilde python ile oluşturulmuştur.
örnek: >>:Sum(f(n),(n,0,5)) yazdığımızda şöyle bir sonuç elde ederiz,

 _5_       
 \ `      
  )   f(n)   = f(0) + f(1) + f(2) + f(3) + f(4) + f(5)
 /_,      
n = 0
Dolayısıyla >>:Sum(f(i),(i,0,oo)) veya daha farklı işlemlerle işlemleri yaparız
sırasıyla, Sum:toplam sembolüdür. ilk terim:ifademiz, virgülden sonraki
(değişken,a,b) bizim değişkene göre sınırlarımızdır. ve buraya istediğimiz
terimleri tanımlayabiliriz.
üçgen dalga için örnek: >>:Sum(sin(n*x),(n,0,16))
kare dalga için örnek: >>:Sum(sin((2*n+1)*x)/(2*n+1),(n,0,198))

                            Stars of the Sky
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


    
    
    



