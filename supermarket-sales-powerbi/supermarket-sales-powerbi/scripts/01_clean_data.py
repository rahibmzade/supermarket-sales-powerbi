import pandas as pd,pickle
x=pickle.load(open('/tmp/claude-0/work/x.pkl','rb'))
log={}
s=x['FactSales']
n0=len(s); s=s.drop_duplicates(); log['dup_removed']=n0-len(s)
n1=len(s); s=s[s.Quantity<=7]; log['qty_outliers_removed']=n1-len(s)
c=x['DimCustomer'].copy()
first=(s.DateKey//10000).groupby(s.CustomerID).min()
c['fy']=c.CustomerID.map(first)
bad=(c.fy<c.RegistrationYear); log['reg_year_fixed']=int(bad.sum())
c.loc[bad,'RegistrationYear']=c.loc[bad,'fy'].astype(int); c=c.drop(columns='fy')
F={'Aminə','Aysel','Leyla','Mehriban','Nigar','Ofelya','Səkinə','Şəhla'}
fem={'Hüseynov':'Hüseynova','Məmmədov':'Məmmədova','Mustafayev':'Mustafayeva','Quliyev':'Quliyeva','İsmayılov':'İsmayılova','Əliyev':'Əliyeva'}
mal={'Hüseynova':'Hüseynov','Məmmədova':'Məmmədov','Rzayeva':'Rzayev','İsaqova':'İsaqov','Mustafayeva':'Mustafayev','Quliyeva':'Quliyev','İsmayılova':'İsmayılov','Əliyeva':'Əliyev'}
def fix(n):
    a,b=n.split(' ',1)
    b=fem.get(b,b) if a in F else mal.get(b,b)
    return f'{a} {b}'
new=c.CustomerName.map(fix); log['names_fixed']=int((new!=c.CustomerName).sum()); c['CustomerName']=new
x['DimCustomer']=c; x['FactSales']=s.reset_index(drop=True)
print(log)
with pd.ExcelWriter('/tmp/claude-0/out/Supermarket_Sales_Analysis_clean.xlsx',engine='xlsxwriter',datetime_format='yyyy-mm-dd') as w:
    for n,d in x.items():
        d.to_excel(w,sheet_name=n,index=False); ws=w.sheets[n]
        ws.freeze_panes(1,0); ws.set_row(0,None,w.book.add_format({'bold':True,'bg_color':'#DDEBF7'}))
        ws.set_column(0,len(d.columns)-1,16)
    pd.DataFrame([('FactSales exact duplicate rows removed',log['dup_removed']),('FactSales quantity outliers (>7, e.g. 8-45) removed',log['qty_outliers_removed']),('DimCustomer RegistrationYear later than first purchase -> set to first purchase year',log['reg_year_fixed']),('DimCustomer first/last name gender mismatch fixed',log['names_fixed'])],columns=['Fix','Rows']).to_excel(w,sheet_name='Change_Log',index=False)
    w.sheets['Change_Log'].set_column(0,0,90)
# verify
y=pd.read_excel('/tmp/claude-0/out/Supermarket_Sales_Analysis_clean.xlsx',sheet_name=None)
s=y['FactSales'];c=y['DimCustomer']
print({k:v.shape for k,v in y.items()}, s.duplicated().sum(), s.Quantity.max())
m=s.merge(c,on='CustomerID'); print('before reg',((m.DateKey//10000)<m.RegistrationYear).sum())
