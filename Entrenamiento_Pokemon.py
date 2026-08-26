def mostrar_menu():
    print("\n===== CENTRO DE ENTRENAMIENTO =====")
    print ("\n1. Entrenar \n2. Curar \n3. Combatir \n4. ver estadísticas \n5. Salir")

def entrenar_pokemon(energia, nivel):
    if energia > 0 and energia <= 100:
        energia -= 5
        nivel += 1
        print("Tu Pokemon ha sido entrenado")
    else: print("\nError")
    return energia, nivel

def curar(energia):
    if energia > 100:
        energia = 100
        print(f"¡Nivel de energía máximo alcanzado!: {energia} puntos de energía.")
    elif energia <= 0: 
        print(f"\n¡Derrotado! Energía: {energia} Agotada")
    else: energia = 100
    return energia
        
def participar_en_combate (energia, combates_ganados):
    if energia >= 5:
        energia -= 5
        combates_ganados += 1
        print("\n¡Combate ganado!")
    else: print(f"¡Combate Perdido! {energia} puntos de energia")
    return energia, combates_ganados

def ver_estadisticas(nombre_entrenador, energia, nivel, combates_ganados):
     print("===== ESTADÍSTICAS =====")
     print(f"\nEntrenador: {nombre_entrenador} \nEnergía: {energia} \nNivel: {nivel} \nVictorias: {combates_ganados}")

def salir():
    print("Fin del entrenamiento.\n")

def resumen_final(nombre_entrenador, energia, nivel, combates_ganados):
        print("\n===== RESUMEN FINAL =====")
        print(f"\nEntrenador: {nombre_entrenador} \nEnergía: {energia} \nNivel: {nivel} \nVictorias: {combates_ganados}")

def main():
    nombre_entrenador = input("\nIngrese el nombre del entrenador: ")
    energia = 100
    nivel = 1
    combates_ganados = 0
    
    while True:
            mostrar_menu()
            opcion = int(input("\nSeleccione la opción deseada: "))
            match opcion:
                case 1:
                  energia, nivel = entrenar_pokemon(energia, nivel)
                case 2:
                  energia = curar(energia)
                case 3:
                  energia, combates_ganados = participar_en_combate(energia, combates_ganados)
                case 4:
                  ver_estadisticas(nombre_entrenador, energia, nivel, combates_ganados)
                case 5:
                  salir()
                  resumen_final(nombre_entrenador, energia, nivel, combates_ganados)
                  break
                case _:
                    print("Opción Inválida. Intente de nuevo.")
                    
main()