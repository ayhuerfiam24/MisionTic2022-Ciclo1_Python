nombres=["Martín","Milú","Anastasia","Lupita","Tomasa","Genoveva"]
tipos=["canino", "canino", "felino", "felino", "felino", "bovino"]
edades=[12, 9, 9, 7, 9, 11]
pesos=[33, 27, 5, 6, 6, 120]
diccionario,beneficiarios_can_fel,beneficiarios_equ_bov,promedio_can_fel,promedio_equ_bov =({},{},{},None,None)
sumaedadesCF,sumaedadesEB=(0,0)
    
for i in range(len(nombres)):
        listaXanimal=[]
        listaXanimal.extend([nombres[i],tipos[i],edades[i],pesos[i]])
        diccionario[str(i+1)]=listaXanimal
i=i+1

    
k=0
for j in range(len(tipos)):
      if edades[j]>8:
         if tipos[j]=="canino" or tipos[j]=="felino":
            sumaedadesCF=sumaedadesCF+edades[j]
            listaXCF=[]
            listaXCF.extend([nombres[j],tipos[j],pesos[j]])
            k=k+1
            beneficiarios_can_fel[str(k)]=listaXCF
      j=j+1
    
    
L=0
for P in range(len(tipos)):
        if edades[P]>15:
            if tipos[P]=="equino" or tipos[P]=="bovino":
                sumaedadesEB=sumaedadesEB+edades[P]
                listaXEB=[]
                listaXEB.extend([nombres[P],tipos[P],pesos[P]])
                L=L+1
                beneficiarios_equ_bov[str(L)]=listaXEB
        P=P+1
    
if k!=0:
        promedio_can_fel=sumaedadesCF/k
    
    
    
if L!=0:
        promedio_equ_bov=sumaedadesEB/L