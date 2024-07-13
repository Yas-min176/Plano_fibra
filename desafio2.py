# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:

lista_equipamentos = []

# TODO: Crie um loop para solicita os itens ao usuário:
for i in range(3):
    # TODO: Solicite o item e armazena na variável "item":
    equipamento = input(f"Digite o nome do equipamento {i + 1}:")
    # TODO: Adicione o item à lista "itens":
    lista_equipamentos.append(equipamento)

# Exibe a lista de itens
print("Lista de Equipamentos:")  
# Loop que percorre cada item na lista "itens"
for equipamento in lista_equipamentos:
    print(f"- {equipamento}")