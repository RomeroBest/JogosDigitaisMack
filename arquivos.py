import random
import csv
from faker import Faker
from datetime import datetime, timedelta
from unidecode import unidecode  # Para remover acentos e caracteres especiais

# Inicializando o Faker
fake = Faker('pt_BR')  # Para gerar dados em português

# Função para gerar uma data e hora aleatória entre 18 e 24 de setembro de 2024
def gerar_data_hora():
    inicio = datetime(2024, 9, 18, 0, 0)
    fim = datetime(2024, 9, 24, 23, 59)
    data_aleatoria = inicio + (fim - inicio) * random.random()
    return data_aleatoria.strftime("%d de set. de 2024 %H:%M")

# Função para gerar um telefone no formato (11) 9 XXXX - XXXX
def gerar_telefone():
    parte1 = random.randint(1000, 9999)
    parte2 = random.randint(1000, 9999)
    return f"(11) 9 {parte1} - {parte2}"

# Função para remover acentos e caracteres especiais
def remover_acentos(texto):
    return unidecode(texto)

# Lista de 77 mensagens exclusivas
mensagens = [
    "Estou interessada nos uniformes personalizados, como faço o pedido?",
    "Qual o prazo de entrega para a linha de acessórios de moda?",
    "Vocês aceitam trocas de tamanhos?",
    "Estou procurando roupas para uniforme escolar, quais as opções disponíveis?",
    "Gostaria de mais informações sobre o material das roupas esportivas.",
    "Vocês fazem uniformes corporativos sob medida?",
    "As roupas são laváveis à máquina ou precisam de lavagem especial?",
    "Existe algum desconto para compras em grandes quantidades?",
    "Qual é a tabela de medidas das peças femininas?",
    "Gostaria de saber se vocês oferecem personalização de acessórios.",
    "Estou buscando por uniformes para academias, quais modelos têm disponível?",
    "Os acessórios de moda são feitos com materiais sustentáveis?",
    "Vocês têm uma loja física para eu experimentar as roupas?",
    "Como funciona o processo de devolução?",
    "A coleção de inverno já está disponível para venda?",
    "Gostaria de encomendar uniformes para minha empresa, como proceder?",
    "As peças possuem proteção UV? Busco roupas para esportes ao ar livre.",
    "Vocês trabalham com roupas para times de futebol amador?",
    "Existe a possibilidade de bordar o logotipo da empresa nos uniformes?",
    "Vocês fazem uniformes para escolas? Estou interessada em personalização.",
    "Preciso de uma linha de acessórios para uma sessão de fotos. Como encomendar?",
    "As roupas esportivas são à prova d'água?",
    "Quais formas de pagamento vocês aceitam no site?",
    "Aguardo o lançamento da nova coleção de verão! Quando estará disponível?",
    "Qual a gramatura do tecido utilizado nas camisas sociais?",
    "Vocês têm roupas infantis para ocasiões formais?",
    "Posso combinar acessórios com as roupas do catálogo?",
    "É possível pedir uniformes com tamanhos personalizados?",
    "As roupas vêm acompanhadas de instruções de lavagem?",
    "Gostaria de saber mais sobre as condições de frete gratuito.",
    "Como posso acompanhar o status do meu pedido?",
    "Os produtos possuem garantia de fábrica?",
    "Vocês oferecem serviços de reparo em uniformes adquiridos?",
    "Há algum catálogo disponível para download no site?",
    "Gostaria de comprar acessórios para um evento corporativo, quais as opções?",
    "As peças de roupa são confeccionadas no Brasil?",
    "Vocês têm uma linha específica de moda sustentável?",
    "As jaquetas possuem forro térmico?",
    "Qual é a política de descontos em compras acima de 10 peças?",
    "Existe a possibilidade de customizar as cores dos uniformes?",
    "Vocês fazem entregas internacionais?",
    "Gostaria de mais informações sobre as camisetas de algodão orgânico.",
    "Qual é o tempo médio de produção de uniformes personalizados?",
    "Os tecidos são antialérgicos? Preciso para uma pele sensível.",
    "Gostei das roupas de inverno, há mais cores disponíveis além das listadas?",
    "É possível estampar o nome da empresa nas camisetas de uniforme?",
    "Vocês oferecem consultoria de estilo para empresas?",
    "Gostaria de saber se as roupas são adequadas para ambientes formais.",
    "Os uniformes têm opções unissex ou tamanhos variados para homens e mulheres?",
    "Preciso de acessórios minimalistas para um evento. Vocês recomendam algo?",
    "As bolsas disponíveis são feitas de couro sintético?",
    "Vocês aceitam pedidos personalizados para times de esportes?",
    "Gostaria de ver mais opções de estampas nas camisetas de uniforme.",
    "As calças sociais possuem ajuste na cintura?",
    "Quais as cores disponíveis para as jaquetas impermeáveis?",
    "As roupas de inverno são adequadas para temperaturas muito baixas?",
    "Vocês têm opções de uniformes com manga curta para o verão?",
    "Gostaria de fazer um pedido com entrega expressa, é possível?",
    "Existe a possibilidade de gravar nomes nos bonés?",
    "Vocês vendem acessórios para festas temáticas?",
    "Preciso de roupas para uniformes escolares de qualidade, como faço o orçamento?",
    "Gostaria de saber se as mochilas têm compartimentos para laptop.",
    "As peças esportivas são feitas de tecidos respiráveis?",
    "Vocês têm moda plus size no catálogo?",
    "É possível adicionar logotipos em cores diferentes nos uniformes?",
    "Quais os principais tecidos usados nas peças de alfaiataria?",
    "Vocês têm opções de uniformes para setores da saúde?",
    "Gostaria de um orçamento para um grande evento corporativo.",
    "As saias são ajustáveis na cintura?",
    "Posso solicitar amostras de tecido antes de encomendar?",
    "Os chapéus e bonés são feitos de materiais recicláveis?",
    "Quais são as opções de customização para os uniformes de empresa?",
    "Vocês têm promoções frequentes no site? Gostaria de ser notificada.",
    "As calças jeans são ajustáveis ou seguem uma numeração padrão?",
    "Estou interessada em acessórios de luxo para um evento. Vocês têm opções?",
    "Vocês têm estoque disponível para entregas rápidas?",
    "Gostaria de conhecer mais sobre as políticas de sustentabilidade da empresa."
]

# Função para gerar e salvar os dados no arquivo CSV
def gerar_csv(quantidade, nome_arquivo):
    random.shuffle(mensagens)  # Embaralha as mensagens para garantir que não haja repetição
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Data e Hora de Envio", "Nome", "Sobrenome", "E-mail", "Telefone", "Deixe-nos uma mensagem"])
        for i in range(quantidade):
            data_hora = gerar_data_hora()
            nome = remover_acentos(fake.first_name())
            sobrenome = remover_acentos(fake.last_name())
            email = remover_acentos(f"{nome.lower()}.{sobrenome.lower()}@{random.choice(['gmail.com', 'hotmail.com', 'outlook.com', 'uol.com.br', 'bol.com.br', 'ig.com.br', 'yahoo.com'])}")
            telefone = gerar_telefone()
            mensagem = remover_acentos(mensagens[i])  # Cada registro recebe uma mensagem única
            writer.writerow([data_hora, nome, sobrenome, email, telefone, mensagem])

# Defina o local de armazenamento aqui
local_arquivo = r"C:\Users\jorja\Downloads\dados_aleatorios.csv"

# Gerar CSV com 77 registros
gerar_csv(77, local_arquivo)

print(f'Arquivo salvo em: {local_arquivo}')
