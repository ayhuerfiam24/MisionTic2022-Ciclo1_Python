def es_semestre_valido(p, s):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    return s in range(1, len(p) + 1)
    
def es_semestre_vacio(p, s):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    return len(p[s - 1])==0
    
def es_materia_valida(p, s, m):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    return m in p[s -1]
    
def modificar_materia(pensum, semestre, materia, nombre, creditos):
    # ACÁ INICIA LA FUNCIÓN
        if es_semestre_valido(pensum, semestre) and not es_semestre_vacio(pensum, semestre) and es_materia_valida(pensum,semestre,materia):
            pensum[semestre-1][materia]["nombre"]=nombre
            pensum[semestre-1][materia]["creditos"]=creditos
    
    # ACÁ TERMINA LA FUNCIÓN
    # ESTA VEZ TU DEFINES TUS RETORNOS

def eliminar_materia(pensum, semestre, materia):
    # ACÁ INICIA LA FUNCIÓN
        if es_semestre_valido(pensum, semestre) and not es_semestre_vacio(pensum, semestre) and es_materia_valida(pensum,semestre,materia):
            del pensum[semestre-1][materia]