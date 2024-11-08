from graphviz import Digraph

# Criar o diagrama de atividades para o processo de controle de sinistro
diagrama = Digraph(comment='Processo de Controle de Sinistro', format='pdf')
diagrama.attr(rankdir='TB', size='10')

# Início do processo
diagrama.node('Inicio', 'Início', shape='ellipse')

# Ação do Segurado: Envia a requisição de conserto
diagrama.node('ReqConserto', 'Segurado envia requisição de conserto', shape='box')

# Ação da Seguradora: Verifica completude da requisição
diagrama.node('VerificaReq', 'Seguradora verifica completude da requisição', shape='diamond')

# Decisão: Requisição completa ou incompleta
diagrama.node('ReqIncompleta', 'Requisição incompleta\nDevolve para Segurado', shape='box')
diagrama.node('EncaminhaOficina', 'Encaminha requisição e carro para Oficina', shape='box')

# Oficina verifica tipo de sinistro
diagrama.node('TipoSinistro', 'Oficina verifica tipo de sinistro', shape='diamond')

# Decisão: Perda total ou conserto
diagrama.node('PerdaTotal', 'Caso de perda total', shape='box')
diagrama.node('Conserto', 'Caso de conserto', shape='box')

# Perda total - ações
diagrama.node('TermoPerdaTotal', 'Oficina gera termo de perda total e envia para Seguradora', shape='box')
diagrama.node('Deposito', 'Seguradora deposita valor para Segurado', shape='box')
diagrama.node('FimPerdaTotal', 'Fim do processo', shape='ellipse')

# Conserto - ações e bifurcação
diagrama.node('Orcamento', 'Oficina gera orçamento e envia para Seguradora', shape='box')
diagrama.node('AprovaOrcamento', 'Seguradora aprova orçamento e devolve para Oficina', shape='box')

# Bifurcação para conserto e cobrança de franquia
diagrama.node('Bifurcacao', '', shape='point')  # Ponto de bifurcação
diagrama.node('ConsertaCarro', 'Oficina realiza conserto do carro', shape='box')
diagrama.node('CobraFranquia', 'Seguradora cobra franquia do Segurado', shape='box')
diagrama.node('PagamentoFranquia', 'Segurado paga franquia', shape='box')

# Junção após o conserto e pagamento da franquia
diagrama.node('Juncao', '', shape='point')  # Ponto de junção
diagrama.node('BaixaReq', 'Seguradora dá baixa na requisição', shape='box')
diagrama.node('FimConserto', 'Fim do processo', shape='ellipse')

# Conexões
diagrama.edge('Inicio', 'ReqConserto')
diagrama.edge('ReqConserto', 'VerificaReq')
diagrama.edge('VerificaReq', 'ReqIncompleta', label='Incompleta')
diagrama.edge('VerificaReq', 'EncaminhaOficina', label='Completa')
diagrama.edge('EncaminhaOficina', 'TipoSinistro')
diagrama.edge('TipoSinistro', 'PerdaTotal', label='Perda Total')
diagrama.edge('TipoSinistro', 'Conserto', label='Conserto')

# Conexões para perda total
diagrama.edge('PerdaTotal', 'TermoPerdaTotal')
diagrama.edge('TermoPerdaTotal', 'Deposito')
diagrama.edge('Deposito', 'FimPerdaTotal')

# Conexões para conserto
diagrama.edge('Conserto', 'Orcamento')
diagrama.edge('Orcamento', 'AprovaOrcamento')
diagrama.edge('AprovaOrcamento', 'Bifurcacao')
diagrama.edge('Bifurcacao', 'ConsertaCarro')
diagrama.edge('Bifurcacao', 'CobraFranquia')
diagrama.edge('CobraFranquia', 'PagamentoFranquia')
diagrama.edge('ConsertaCarro', 'Juncao')
diagrama.edge('PagamentoFranquia', 'Juncao')
diagrama.edge('Juncao', 'BaixaReq')
diagrama.edge('BaixaReq', 'FimConserto')

# Salvar e visualizar o PDF gerado
output_path = r"C:\Users\jorja\OneDrive\Programacao\ADS\2SEM\MODELAGEM DE NEGOCIOS\Diagrama_Processo_Controle_Sinistro.pdf"
diagrama.render(filename=output_path, cleanup=True)
output_path
