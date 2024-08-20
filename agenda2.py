import re
plantilla="""
\\begin{multicols}{3}
{$DAY$\\ \\ \\ \\ \\ --------------------------------}
\\begin{flushright}\\begin{small}\\texttt{:) :| :(}\\end{small}\\end{flushright}
\\vfill
{$DAY$\\ \\ \\ \\ \\ --------------------------------}
\\begin{flushright}\\begin{small}\\texttt{:) :| :(}\\end{small}\\end{flushright}\\par
\\vfill
{$DAY$\\ \\ \\ \\ \\ --------------------------------}
\\begin{flushright}\\begin{small}\\texttt{:) :| :(}\\end{small}\\end{flushright}\\par
\\vfill
\\end{multicols}
\\vspace{1.05cm}
"""
dayRegex="\\$DAY\\$"
iter=42
def genDays()->list:
    meses=["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic","ene"]
    mesesDias=[31,29,31,30,31,30,31,31,30,31,30,31,31] #si es viciesto [1]=29 si no [1]=28
    semana=["lun","mar","mie","jue","vie","sáb","dom"]
    semanadia=0 #cambiar al dia en el que inicia el año 0,1,2,3,4,5,6
    año="2024"

    calendar=[]
    for mes in meses:
        for i in range(1,mesesDias[meses.index(mes)]+1):
            #print(i, semana[semanadia])
            day=str(i) if(len(str(i))==2) else "0"+str(i)
            #print(semana[semanadia]+" "+meses[mes-1]+" "+day+", "+año)
            #print(semana[semanadia]+" "+day+", "+mes)
            calendar.append(semana[semanadia]+" "+day+", "+mes)
            semanadia+=1
            if(semanadia==7):
                semanadia=0
    return calendar

def genAgenda():
    end="""\\documentclass[letterpaper,10pt]{article}
\\usepackage[utf8]{inputenc}
\\usepackage[spanish]{babel}
\\usepackage[margin=0.5cm]{geometry}
\\usepackage{multicol}
\\begin{document}"""
    end+=plantilla*iter*3
    end+="""\\end{document}"""
    return end

def generateIndex():
    frente=[
            [0,6,12],
            [1,7,13],
            [2,8,14]
        ]
    atras=[
            [15,9,3],
            [16,10,4],
            [17,11,5]
        ]
    final=[frente]
    x=18
    sw=True
    c=1
    aa=True
    hh=1
    while(hh<=iter):
        hh+=1
        if(sw):
            frente=[[i[0]+x,i[1]+x,i[2]+x] for i in frente]
            final.append(frente)
        else:
            if(aa):
                final.append(atras)
                aa= False
            else:
                atras=[[i[0]+x,i[1]+x,i[2]+x] for i in atras]
                final.append(atras)
        c+=1
        if c==3:
            c=0
            sw= not sw
    return final


def setdays():
    end=genAgenda()
    days=genDays()
    index= generateIndex()
    c=0
    for i in index:
        for j in i:
            for k in j:
                #if(k<=365):
                try:
                    c+=1
                    print(k,days[k])
                    
                    end=re.sub(dayRegex, days[k], end,1)
                    days[k]="NULL"
                except:
                    print("error")

                
    print(c)
    return end;

f = open("agenda2.tex","w")
f.write(setdays())
f.close()


