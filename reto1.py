def solucion(b,n):
    #ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
    cantidad_intentos=0
    x='True'
    while x=="True":
        num_escojido=int(input("Ingrese un número: "))
    
        if num_escojido > n and num_escojido <=b:
            print("¡Ups! Te pasaste")
            cantidad_intentos= cantidad_intentos +1
    
        elif num_escojido < n and num_escojido >=0:
            print("¡Ups! Estás por debajo")
            cantidad_intentos= cantidad_intentos +1
    
        elif num_escojido==n:
            cantidad_intentos= cantidad_intentos +1
            (print(f"¡LO LOGRASTE! Usaste {cantidad_intentos} intentos"))
            break
    
        else:
    
            print("¡Te saliste del intervalo!")
                
    


        
                
    
    
    
    
    
    
    
    
    
    