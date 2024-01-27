#Argument: There is set like N = [a1, a2, a3, ... an] can you sort this set should be as a1 != a2 != a3 != a4 != an
#example = Numbers: 55221 -> 5,4,3,2,1

#here is result. | Reşat Berk

import random

new_list=[]

def lined():
    latest_list=[]
    for h in new_list:
        hh = int(h)
        latest_list.append(hh)

    latest_list.sort(reverse=True) #sort
    return latest_list
                     
def check():
    
    chc = [-1, 1] #add or minus
    t = 0
    for p in new_list:
        t += 1
        for s in new_list[t:]:
            if p==s: 
                inx = new_list.index(s)
                if int(p) or int(s) >len(new_list):
                    new_list[inx] = str(int(p) - 1)
                elif int(p) or int(s) <= 0:
                    new_list[inx] = str(int(p) + 1)
                else:
                    new_list[inx] = str(int(p) + random.choice(chc))
                return check() #re-check
         
    if '0' in new_list: 
        sum_list=[]
        for m in new_list:
            sum_list.append(int(m))
            
        sum_ = sum(sum_list) #method: Example: Sum(5,4,3,2,1) - Sum(5,4,3,0,1) , so '0' must be '2'
        real_sum = sum(range(len(new_list)+1))
        put = real_sum - sum_
        inxx=new_list.index('0')
        new_list[inxx] = str(put)
        
    return lined()

def min_(arr:str) -> int:
    
    for i in arr:
        for j in str(i):
            new_list.append(j)
                
    
    return check()

if __name__ == '__main__':
    line = input('numbers: ') #like 55221
    k = [int(i) for i in line.strip().split()]
    print(min_(k))
