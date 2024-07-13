def main():
    lista_equipamentos = []

    for i in range(3):
        equipamento = input(f"Digite o nome do equipamento {i + 1}: ")
        lista_equipamentos.append(equipamento)
    
    print("\nLista de Equipamentos:")
    for equipamento in lista_equipamentos:
        print(f"- {equipamento}")

if __name__ == "__main__":
    main()