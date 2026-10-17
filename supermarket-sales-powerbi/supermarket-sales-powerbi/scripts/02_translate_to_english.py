import pandas as pd
y=pd.read_excel('/tmp/claude-0/out/Supermarket_Sales_Analysis_clean.xlsx',sheet_name=None)
city={'Bakı':'Baku','Sumqayıt':'Sumgait','Gəncə':'Ganja','Xırdalan':'Khirdalan','Lənkəran':'Lankaran','Mingəçevir':'Mingachevir'}
tr={'Bravo Gənclik':'Bravo Genclik'}
st=y['DimStore']; st['City']=st.City.map(city)
st['StoreName']=st.StoreName.map(lambda n: tr.get(n) or ' '.join(city.get(w,w) for w in n.split()))
st['StoreName']=st.StoreName.replace({'Tamstore Sumgait':'Tamstore Sumgait'})
fn={'Aminə':'Amina','Coşqun':'Joshgun','Nicat':'Nijat','Rəşad':'Rashad','Səkinə':'Sakina','Şəhla':'Shahla'}
ln={'Hüseynov':'Huseynov','Hüseynova':'Huseynova','Mustafayev':'Mustafayev','Mustafayeva':'Mustafayeva','Məmmədov':'Mammadov','Məmmədova':'Mammadova','Nəbizadə':'Nabizada','Quliyev':'Guliyev','Quliyeva':'Guliyeva','İsmayılov':'Ismayilov','İsmayılova':'Ismayilova','İsaqova':'Isagova','Əliyev':'Aliyev','Əliyeva':'Aliyeva','Rzayeva':'Rzayeva','Rzayev':'Rzayev'}
c=y['DimCustomer']; c['CustomerName']=c.CustomerName.map(lambda n:' '.join([fn.get(n.split()[0],n.split()[0]),ln.get(n.split()[1],n.split()[1])]))
def ascii_only(df):
    return [(col,df[col].astype(str).str.contains(r'[^\x00-\x7F]').sum()) for col in df.columns if df[col].dtype==object and df[col].astype(str).str.contains(r'[^\x00-\x7F]').any()]
for k,d in y.items(): print(k,ascii_only(d))
print(st.to_string()); print(c.CustomerName.str.split().str[1].unique())
with pd.ExcelWriter('/tmp/claude-0/out/Supermarket_Sales_Analysis_clean_EN.xlsx',engine='xlsxwriter',datetime_format='yyyy-mm-dd') as w:
    for n,d in y.items():
        d.to_excel(w,sheet_name=n,index=False); ws=w.sheets[n]; ws.freeze_panes(1,0)
        ws.set_row(0,None,w.book.add_format({'bold':True,'bg_color':'#0B2545','font_color':'#FFFFFF'})); ws.set_column(0,len(d.columns)-1,18)
    w.sheets['Change_Log'].set_column(0,0,90)
