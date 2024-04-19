def choose_level(n_pregunta, p_level):
  level = ""
  
  if p_level == 1:
    if n_pregunta == 1:
      level = "basicas"
    elif n_pregunta == 2:
      level = "intermedias"
    elif n_pregunta == 3:
      level = "avanzadas"

  elif p_level == 2:
    if n_pregunta == 1 or n_pregunta == 2:
      level = "basicas"
    elif n_pregunta == 3 or n_pregunta == 4:
      level = "intermedias"
    elif n_pregunta == 5 or n_pregunta ==6:
      level = "avanzadas"

  elif p_level == 3:
    if n_pregunta == 1 or n_pregunta == 2 or n_pregunta == 3:
      level = "basicas"
    elif n_pregunta == 4 or n_pregunta == 5 or n_pregunta == 6:
      level = "intermedias"
    elif n_pregunta == 7 or n_pregunta == 8 or n_pregunta == 9:
      level = "avanzadas"
  
  return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias