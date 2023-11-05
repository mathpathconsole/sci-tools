import pandas as pd
import yfinance as yf
from datetime import date  

print('Connecting...')

today=date.today() #today date
first=str(today)
firstday=first[:8]+'01' #first month of current date
print("current day:",today,end=2*'\n')
pull_data=pd.read_html('https://finance.yahoo.com/currencies')[0] #pull data

use1=pull_data['Symbol'].str.replace('=X','') #for delete =X symbol.

pull_data.to_csv('_backsource.csv')
data = pd.read_csv('_backsource.csv')
data.drop('52 Week Range', inplace=True, axis=1) #delete some columns that don't need
data.drop('Day Chart', inplace=True, axis=1)
data.drop('Unnamed: 0', inplace=True, axis=1)
data['Symbol']=use1 #write new symbols without =X

data.to_excel('Currencies.xlsx') #turn excel

writer = pd.ExcelWriter('Currencies.xlsx') 
data.to_excel(writer, sheet_name=str(today), index=False)


writer.sheets[str(today)].set_column(0, 4, 10) #set column width
writer.close()

reach=pd.read_excel('Currencies.xlsx')
see_change=reach.sort_values('% Change', ascending=False)

minus_data=[] #if no or not enough top (+) data use top minus datas. 
sign_data=[]
ticker_data=[]
ticker=[]
def access_change_values():
    print('-----Loading...-----')

    for i in see_change['% Change']: #add top 5 big values
        if "+" in i and len(sign_data)<5:  
            sign_data.append(i)
            
        elif "-" in i or '0.00%' in i:
            minus_data.append(i)

    if len(sign_data) <5: #not enough (+) top datas

        while len(sign_data)<5:
            if "0.00%" not in minus_data:
                sign_data.append(minus_data[-1])
                minus_data.remove(minus_data[-1])  #this field for top (-) datas uses for not enough (+) datas

            elif "0.00%" in minus_data:
                L=minus_data.count('0.00%')
                for z in range(L):
                    sign_data.append(minus_data[0])
                    minus_data.remove(minus_data[0])
                    
                sign_data.append(minus_data[-1])
                minus_data.remove(minus_data[-1])
                
            elif len(sign_data)==5:
                break
                           
    print(sign_data) #here show data
    return write()

def write():
    for j in range(0,24):
        if see_change['% Change'][j] in sign_data:
            ticker_data.append(int(j))
            sign_data.remove(see_change['% Change'][j])
    return find()

def find():
    for r in ticker_data:
        r1=see_change['Symbol'][r]+'=X' #add tickers in symbols
        ticker.append(r1)
    print(ticker) #here show data               
    return get()


def get():
    for g in ticker:
        datax=yf.download(g, start=firstday, end=today, interval='1d')
        datax.to_csv('{}.csv'.format(g)) #download top 5 big currencies

    print('Completed. Please look your current file')
    import time
    time.sleep(5) #close console after 5 second
    print('')

access_change_values()



    
    
    
