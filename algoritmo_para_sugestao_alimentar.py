import random

cardapio = {
    "cafe_da_manha": [
        {"nome": "Pão francês com manteiga", "lactose": True, "alergenos": ["gluten"]},
        {"nome": "Tapioca com ovo", "lactose": False, "alergenos": []},
        {"nome": "Frutas variadas (banana, maçã, mamão)", "lactose": False, "alergenos": []},
        {"nome": "Iogurte natural com granola", "lactose": True, "alergenos": ["gluten"]},
        {"nome": "Ovo mexido com tomate", "lactose": False, "alergenos": []},
        {"nome": "Vitamina de frutas com leite", "lactose": True, "alergenos": []},
        {"nome": "Café preto com pão de queijo", "lactose": True, "alergenos": ["gluten"]},
        {"nome": "Tapioca com queijo e orégano", "lactose": True, "alergenos": []},
        {"nome": "Crepioca com banana e canela", "lactose": False, "alergenos": []},
        {"nome": "Pão integral com abacate", "lactose": False, "alergenos": ["gluten"]},
        {"nome": "Cuscuz nordestino com ovo", "lactose": False, "alergenos": []},
        {"nome": "Panqueca de aveia com mel e banana", "lactose": False, "alergenos": ["gluten"]},
        {"nome": "Bolo de cenoura caseiro", "lactose": True, "alergenos": ["gluten"]},
    ],
    "almoco": [
        {"nome": "Arroz, feijão, frango grelhado e salada verde", "lactose": False, "alergenos": []},
        {"nome": "Arroz integral, feijão, carne moída e abobrinha refogada", "lactose": False, "alergenos": []},
        {"nome": "Macarrão alho e óleo com salada de cenoura", "lactose": False, "alergenos": ["gluten"]},
        {"nome": "Escondidinho de carne com purê de mandioca", "lactose": False, "alergenos": []},
        {"nome": "Omelete de legumes com arroz e feijão", "lactose": False, "alergenos": []},
        {"nome": "Filé de peixe assado com arroz e vinagrete", "lactose": False, "alergenos": []},
        {"nome": "Arroz, feijão, frango desfiado e quiabo refogado", "lactose": False, "alergenos": []},
        {"nome": "Estrogonofe de frango com arroz e batata palha", "lactose": True, "alergenos": []},
        {"nome": "Feijoada leve (feijão preto, carnes magras) com arroz e couve", "lactose": False, "alergenos": []},
        {"nome": "Abóbora assada com arroz integral, feijão e frango grelhado", "lactose": False, "alergenos": []},
        {"nome": "Salada de grão-de-bico, tomate, pepino, cenoura e ovo cozido", "lactose": False, "alergenos": []},
        {"nome": "Berinjela à parmegiana (sem fritura) com arroz e feijão", "lactose": True, "alergenos": []},
    ],
    "lanche_da_tarde": [
        {"nome": "Frutas picadas com aveia", "lactose": False, "alergenos": ["gluten"]},
        {"nome": "Pão integral com queijo", "lactose": True, "alergenos": ["gluten"]},
        {"nome": "Bolo de banana caseiro", "lactose": False, "alergenos": ["gluten"]},
        {"nome": "Tapioca com banana e canela", "lactose": False, "alergenos": []},
        {"nome": "Castanhas e frutas secas", "lactose": False, "alergenos": ["oleaginosas"]},
        {"nome": "Suco natural de laranja com biscoito de polvilho", "lactose": False, "alergenos": []},
        {"nome": "Crepioca com queijo", "lactose": True, "alergenos": []},
        {"nome": "Iogurte com frutas e chia", "lactose": True, "alergenos": []},
        {"nome": "Pão de queijo com café", "lactose": True, "alergenos": []},
        {"nome": "Mix de nozes, amêndoas e damasco", "lactose": False, "alergenos": ["oleaginosas"]},
        {"nome": "Smoothie de morango com leite vegetal", "lactose": False, "alergenos": []},
    ],
    "jantar": [
        {"nome": "Sopa de legumes com frango", "lactose": False, "alergenos": []},
        {"nome": "Arroz, feijão, ovo cozido e couve refogada", "lactose": False, "alergenos": []},
        {"nome": "Panqueca de carne com salada", "lactose": False, "alergenos": ["gluten"]},
        {"nome": "Tapioca com frango desfiado e tomate", "lactose": False, "alergenos": []},
        {"nome": "Purê de batata com carne moída e salada de alface", "lactose": True, "alergenos": []},
        {"nome": "Filé de frango grelhado com arroz e salada", "lactose": False, "alergenos": []},
        {"nome": "Sopa de feijão com cenoura, batata e cheiro verde", "lactose": False, "alergenos": []},
        {"nome": "Cuscuz com ovos mexidos e tomate", "lactose": False, "alergenos": []},
        {"nome": "Sopa de mandioquinha com frango", "lactose": False, "alergenos": []},
        {"nome": "Omelete de queijo com tomate e salada verde", "lactose": True, "alergenos": []},
    ],
}

def filtrar_opcoes(opcoes, intolerancia_lactose, alergias):
    filtrados = []
    for item in opcoes:
        if intolerancia_lactose and item["lactose"]:
            continue
        if any(alergia.lower() in [a.lower() for a in item["alergenos"]] for alergia in alergias):
            continue
        filtrados.append(item["nome"])
    return filtrados


print("Bem-vindo(a) ao Gerador de Cardápio Saudável")
intolerancia_lactose = input("Você possui intolerância à lactose? (sim/não): ").strip().lower() == "sim"

tem_alergia = input("Você possui alguma alergia alimentar? (sim/não): ").strip().lower()

alergias = []
if tem_alergia == "sim":
    alergias = input(
        "Digite os alimentos ou grupos aos quais você é alérgico, separados por vírgula (ex.: glúten, amendoim, castanhas, etc.): "
    ).lower().replace(" ", "").split(",")

print("\n----- Seu Cardápio Saudável -----\n")

for refeicao, opcoes in cardapio.items():
    opcoes_filtradas = filtrar_opcoes(opcoes, intolerancia_lactose, alergias)

    if not opcoes_filtradas:
        sugestao = "Nenhuma opção disponível para esta refeição considerando suas restrições."
    else:
        sugestao = random.choice(opcoes_filtradas)

    print(f"{refeicao.replace('_', ' ').title()}: {sugestao}")

print("\nLembre-se de beber bastante água e fazer suas refeições em ambientes tranquilos.")