from xlrd import open_workbook
import xlrd
import matplotlib.pyplot as plt 

# 读取文件
wb = open_workbook('dataset.xlsx')
sheet = wb.sheet_by_name('Data')

#***********************fig1*************************
usa=0
china=0
india=0
russia=0
num1=0
num2=0
num3=0
num4=0
for i in range(1,sheet.nrows):
    name=sheet.row(i)[0].value
    # if sheet.row(i)[7].value=='':
    #     mushyC=1
    # if sheet.row(i)[8].value=='':
    #     mushyR=1
    if sheet.row(i)[5].value=='':
        value=0
    else:
        value=sheet.row(i)[5].value
        
    if sheet.row(i)[4].value=='':
        flag=1
    else:
        flag=int(sheet.row(i)[4].value)
    sw_f=sheet.row(i)[2].value
    # sw_f=1
    # if sheet.row(i)[5].value==-1.30848956108093:
    #     continue
    if name=='USA':
        if value!=0:
            num1+=sw_f
            usa=usa+value*sw_f
    elif name=="China" :
        if value!=0:
            num2+=sw_f
            china=china+value*sw_f
    elif name=="India":
        if value!=0:
            num3+=sw_f
            india=india+value*sw_f
    else:
        if value!=0:
            num4+=sw_f
            russia=russia+value*sw_f
ave_U=round(usa/num1,3)
ave_C=round(china/num2,3)
ave_I=round(india/num3,3)
ave_R=round(russia/num4,3)
data=[ave_C,ave_I,ave_R,ave_U]
lable=['China','India','Russia','USA']

fig, ax=plt.subplots()
plt.bar(lable,data,width=0.5)
for a,b in zip(lable,data):
    if b>0:
        plt.text(a, b+0.05, b, ha='center', va= 'top',fontsize=8)
    else:
        plt.text(a, b-0.05, b, ha='center', va= 'bottom',fontsize=8)
    
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()
print(ave_U,ave_C,ave_I,ave_R)


#****************************fig2******************************
usa=0
usa_ne=0
china=0
china_ne=0
india=0
india_ne=0
russia=0
russia_ne=0
num1=0
num11=0
num2=0
num22=0
num3=0
num33=0
num4=0
num44=0
for i in range(1,sheet.nrows):
    name=sheet.row(i)[0].value
    # if sheet.row(i)[7].value=='':
    #     mushyC=1
    # if sheet.row(i)[8].value=='':
    #     mushyR=1
    if sheet.row(i)[5].value=='':
        value=0
    else:
        value=sheet.row(i)[5].value
    if sheet.row(i)[1].value=='':
        elite=2
    else:
        elite=sheet.row(i)[1].value
    # if sheet.row(i)[4].value=='':
    #     flag=1
    # else:
    #     flag=int(sheet.row(i)[4].value)
    sw_f=sheet.row(i)[2].value
    # sw_f=1
    if name=='USA':
        if value!=0:
            if elite==1:

                num1+=sw_f
                usa=usa+value*sw_f
            elif elite==0:
                num11+=sw_f
                usa_ne=usa_ne+value*sw_f
    elif name=="China" :
        if value!=0:
            if elite==1:

                num2+=sw_f
                china=china+value*sw_f
            elif elite==0:
                num22+=sw_f
                china_ne=china_ne+value*sw_f
    elif name=="India":
        if value!=0:
            if elite==1:
                num3+=sw_f
                india=india+value*sw_f
            elif elite==0:
                num33+=sw_f
                india_ne=india_ne+value*sw_f
    else:
        if value!=0:
            if elite==1:

                num4+=sw_f
                russia=russia+value*sw_f
            elif elite==0:
                num44+=sw_f
                russia_ne=russia_ne+value*sw_f
ave_U=round(usa/num1,3)
ave_Une=round(usa_ne/num11,3)
ave_C=round(china/num2,3)
ave_Cne=round(china_ne/num22,3)
ave_I=round(india/num3,3)
ave_Ine=round(india_ne/num33,3)
ave_R=round(russia/num4,3)
ave_Rne=round(russia_ne/num44,3)
data1=[ave_C,ave_I,ave_R,ave_U]
data2=[ave_Cne,ave_Ine,ave_Rne,ave_Une]
lable1=['China','India','Russia','USA']


ax1=plt.subplot(121)
plt.bar(lable,data1,width=0.5)
for a,b in zip(lable,data1):
    if b>0:
        plt.text(a, b+0.05, b, ha='center', va= 'top',fontsize=8)
    else:
        plt.text(a, b-0.05, b, ha='center', va= 'bottom',fontsize=8)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
plt.ylim(-1,1)
plt.title('Elite Institutions')

ax2=plt.subplot(122)
plt.bar(lable,data2,width=0.5)
for a,b in zip(lable,data2):
    if b>0:
        plt.text(a, b+0.05, b, ha='center', va= 'top',fontsize=8)
    else:
        plt.text(a, b-0.05, b, ha='center', va= 'bottom',fontsize=8)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
plt.ylim(-1,1)
plt.title('No-elite Institutions')
plt.show()
print(ave_U,ave_C,ave_I,ave_R)
print(ave_Une,ave_Cne,ave_Ine,ave_Rne)

#******************************fig3********************************
usa_A=0
usa_EB=0
usa_E=0
china=0
india=0
russia=0
num1=0
num11=0
num111=0
num2=0
num3=0
num4=0
for i in range(1,sheet.nrows):
    name=sheet.row(i)[0].value
    # if sheet.row(i)[7].value=='':
    #     mushyC=1
    # if sheet.row(i)[8].value=='':
    #     mushyR=1
    if sheet.row(i)[5].value=='':
        value=0
    else:
        value=sheet.row(i)[5].value
    # if sheet.row(i)[4].value=='':
    #     flag=1
    # else:
    #     flag=int(sheet.row(i)[4].value)
    sw_f=sheet.row(i)[2].value
    # sw_f=1


    if name=='USA':
        england=sheet.row(i)[3].value

        if value!=0:
            if england=='01':
                num1+=sw_f
                usa_A=usa_A+value*sw_f
            if (england=='01') | (england=='03'):
                num11+=sw_f
                usa_EB=usa_EB+value*sw_f
            
            num111+=sw_f
            usa_E=usa_E+value*sw_f
    elif name=="China" :
        if value!=0:
            num2+=sw_f
            china=china+value*sw_f
    elif name=="India":
        if value!=0:
            num3+=sw_f
            india=india+value*sw_f
    else:
        if value!=0:
            num4+=sw_f
            russia=russia+value*sw_f
ave_E=round(usa_A/num1,3)
ave_EB=round(usa_EB/num11,3)
ave_A=round(usa_E/num111,3)
ave_C=round(china/num2,3)
ave_I=round(india/num3,3)
ave_R=round(russia/num4,3)

data=[ave_C,ave_I,ave_R,ave_A,ave_EB,ave_E]
lable=['China','India','Russia','USA(All student)','USA(English/Bilingual','USA(English only']

fig, ax=plt.subplots()
plt.bar(lable,data,width=0.5)
plt.xticks(rotation=15,size=8)
for a,b in zip(lable,data):
    if b>0:
        plt.text(a, b+0.05, b, ha='center', va= 'top',fontsize=8)
    else:
        plt.text(a, b-0.05, b, ha='center', va= 'bottom',fontsize=8)
    
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()
print(ave_C,ave_I,ave_R,ave_A,ave_EB,ave_A,ave_EB,ave_E)


#*********************************fig4************************************
usa_m=0
usa_f=0
china_m=0
china_f=0
india_m=0
india_f=0
russia_m=0
russia_f=0
num1=0
num11=0
num2=0
num22=0
num3=0
num33=0
num4=0
num44=0
for i in range(1,sheet.nrows):
    name=sheet.row(i)[0].value
    # if sheet.row(i)[7].value=='':
    #     mushyC=1
    # if sheet.row(i)[8].value=='':
    #     mushyR=1
    if sheet.row(i)[5].value=='':
        value=0
    else:
        value=sheet.row(i)[5].value
    if sheet.row(i)[6].value=='':
        female=2
    else:
        female=sheet.row(i)[6].value
    # if sheet.row(i)[4].value=='':
    #     flag=1
    # else:
    #     flag=int(sheet.row(i)[4].value)
    sw_f=sheet.row(i)[2].value
    sw_f=1
    if name=='USA':
        if value!=0:
            if female==0:
                num1+=sw_f
                usa_m=usa_m+value*sw_f
            elif female==1:
                num11+=sw_f
                usa_f=usa_f+value*sw_f
    elif name=="China" :
        if value!=0:
            if female==0:
                num2+=sw_f
                china_m=china_m+value*sw_f
            elif female==1:
                num22+=sw_f
                china_f=china_f+value*sw_f
    elif name=="India":
        if value!=0:
            if female==0:
                num3+=sw_f
                india_m=india_m+value*sw_f
            elif female==1:
                num33+=sw_f
                india_f=india_f+value*sw_f

    else:
        if value!=0:
            if female==0:
                num4+=sw_f
                russia_m=russia_m+value*sw_f
            elif female==1:
                num44+=sw_f
                russia_f=russia_f+value*sw_f
ave_Um=round(usa_m/num1,3)
ave_Uf=round(usa_f/num11,3)
ave_Cm=round(china_m/num2,3)
ave_Cf=round(china_f/num22,3)
ave_Im=round(india_m/num3,3)
ave_If=round(india_f/num33,3)
ave_Rm=round(russia_m/num4,3)
ave_Rf=round(russia_f/num44,3)

data=[ave_Cm,ave_Cf,ave_Im,ave_If,ave_Rm,ave_Rf,ave_Um,ave_Uf]
lable=['China-male','China-female','India-male','India-female','Russia-male','Russia-female','USA-male','USA-female']

fig, ax=plt.subplots()
plt.bar(lable,data)
plt.xticks(rotation=15,size=8)
for a,b in zip(lable,data):
    if b>0:
        plt.text(a, b+0.05, b, ha='center', va= 'top',fontsize=8)
    else:
        plt.text(a, b-0.05, b, ha='center', va= 'bottom',fontsize=8)
    
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()
print(ave_Um,ave_Uf,ave_Cm,ave_Cf,ave_Im,ave_If,ave_Rm,ave_Rf)
