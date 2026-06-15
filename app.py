import streamlit as st
import time
import random
import pandas as pd
import plotly.graph_objects as go
from fpdf import FPDF
import urllib.parse
from datetime import datetime

# ==========================================
# 1. CONFIGURAÇÃO BASE E TEMA (DARK LUXURY)
# ==========================================
st.set_page_config(page_title="AuraDex Supremo | Inteligência Comportamental", page_icon="⚜️", layout="centered")

st.markdown("""
    <style>
    /* Reset & Base */
    .stApp { background-color: #0d1117; color: #f0f0f0; font-family: 'Helvetica Neue', sans-serif; }
    h1, h2, h3, h4 { color: #d4af37 !important; font-family: 'Georgia', serif; font-weight: 400; text-align: center; letter-spacing: 1px;}
    
    /* Tipografia e Textos */
    .subtitle { text-align: center; font-size: 1.1rem; color: #a3a3a3; margin-bottom: 40px; font-weight: 300; line-height: 1.6;}
    .luxury-highlight { color: #d4af37; font-weight: bold; }
    
    /* Glassmorphism Cards */
    .glass-card { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(212, 175, 55, 0.2); padding: 30px; border-radius: 16px; margin-bottom: 25px; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3); }
    .glass-card-title { font-size: 1.4rem; color: #d4af37; border-bottom: 1px solid rgba(212, 175, 55, 0.2); padding-bottom: 10px; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 2px; text-align: center;}
    
    /* Botões Premium */
    .stButton>button { width: 100%; background: linear-gradient(135deg, #a67c00 0%, #d4af37 50%, #f3e5ab 100%); color: #0d1117; font-weight: 700; font-size: 1.1rem; letter-spacing: 1.5px; border-radius: 8px; border: none; padding: 15px; text-transform: uppercase; transition: all 0.4s ease; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);}
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(212, 175, 55, 0.5); background: linear-gradient(135deg, #d4af37 0%, #f3e5ab 50%, #ffffff 100%);}
    
    /* Stats Bar */
    .stats-container { display: flex; justify-content: space-around; background: #161b22; border: 1px solid #2d3748; padding: 20px; border-radius: 12px; margin-bottom: 30px;}
    .stat-item { text-align: center; }
    .stat-number { font-size: 1.5rem; color: #d4af37; font-weight: bold; font-family: 'Georgia', serif;}
    .stat-label { font-size: 0.8rem; color: #8b949e; text-transform: uppercase; letter-spacing: 1px;}
    
    /* Progresso e Alertas */
    .stProgress .st-bo { background-color: rgba(212, 175, 55, 0.2); }
    .stProgress .st-bp { background: linear-gradient(90deg, #a67c00, #d4af37); }
    .loading-text { font-family: monospace; color: #d4af37; text-align: center; font-size: 1.2rem; margin-top: 20px; letter-spacing: 2px;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. BANCO DE DADOS PSICOLÓGICO
# ==========================================
# Estrutura otimizada para o código Fonte não exceder limites
archetypes_db = {
    "O Sábio": {"radar": [40, 70, 95, 40, 60, 80], "rarity": "4,7%", "desc": "Sua mente é um cofre de dados analíticos. Você busca a verdade objetiva em um mundo de caos.", "sombra": "O Dogmático: Paralisia por análise; arrogância intelectual que afasta pessoas.", "oculto": "Intuição Pura: Esconde um talento raro para prever cenários sem precisar de dados.", "finance": "Conservador Estratégico. Acumula patrimônio pela lógica, mas pode perder oportunidades por excesso de cautela.", "love": "Busca conexão intelectual acima da atração física. Compatível com: O Explorador e O Criador.", "career": "C-Level Strategy, Pesquisa Avançada, Direito, Consultoria Financeira.", "evolution": "1. Aceite a incerteza emocional.\n2. Aja com 70% da informação.\n3. Desenvolva empatia tática."},
    "O Herói": {"radar": [95, 50, 60, 80, 95, 60], "rarity": "8,2%", "desc": "Ação e superação moldam seu destino. Onde outros veem barreiras, você vê a chance de provar seu valor.", "sombra": "O Tirano Exausto: Queima pontes e pessoas pela obsessão por resultados; síndrome do salvador.", "oculto": "Empatia Silenciosa: Capacidade não explorada de liderar pelo acolhimento, não pela força.", "finance": "Agressivo. Tende a assumir altos riscos por altas recompensas. Risco de burnout financeiro.", "love": "Protege e provê. Compatível com: O Inocente e O Cuidador.", "career": "Empreendedorismo, Gestão de Crise, Forças Armadas, Esportes de Alto Rendimento.", "evolution": "1. Aprenda a delegar sem microgerenciar.\n2. Celebre pequenas vitórias.\n3. Permita-se ser vulnerável."},
    "O Governante": {"radar": [100, 40, 85, 70, 60, 50], "rarity": "3,1%", "desc": "Sua aura impõe respeito. Você cria estruturas sólidas e detesta a incompetência que gera o caos.", "sombra": "O Ditador Paranoico: Medo obsessivo de perder o controle; sufoca a inovação alheia.", "oculto": "Sensibilidade Artística: Uma apreciação secreta pelo caos belo e não estruturado.", "finance": "Acumulador de Poder. O dinheiro é uma ferramenta de estabilidade e influência. Risco de avareza.", "love": "Controlador porém leal. Compatível com: O Sábio e O Mago.", "career": "CEO, Gestão Pública, Mercado Financeiro, Direito Corporativo.", "evolution": "1. Treine a escuta ativa.\n2. Descentralize decisões menores.\n3. Encontre um hobby sem regras estritas."},
    "O Mago": {"radar": [70, 90, 80, 95, 50, 85], "rarity": "2,8%", "desc": "Você enxerga engrenagens invisíveis. Seu dom é a alquimia: transformar ideias brutas em ouro.", "sombra": "O Manipulador Sombrio: Usa sua inteligência para manipular e criar ilusões em benefício próprio.", "oculto": "Aterramento: Capacidade de criar rotinas eficientes (geralmente negligenciada).", "finance": "Fluido. Atrai dinheiro através de inovação e visão, mas pode perdê-lo por falta de gestão prática.", "love": "Intenso e transformacional. Compatível com: O Criador e O Amante.", "career": "Tecnologia, Marketing Estratégico, Psicanálise, Inovação.", "evolution": "1. Traduza suas visões para linguagem comum.\n2. Foque na execução.\n3. Cuidado com o isolamento mental."},
    "O Criador": {"radar": [50, 100, 60, 80, 70, 90], "rarity": "5,5%", "desc": "Uma força motriz de inovação. Você materializa o que antes só existia na imaginação.", "sombra": "O Perfeccionista Crônico: Nunca termina nada; julga tudo como insuficiente.", "oculto": "Liderança Prática: Pode gerir grandes equipes se o propósito for claro.", "finance": "Focado em valor gerado. Dinheiro é subproduto da arte/produto. Pode sofrer com precificação.", "love": "Busca musas e inspiração. Compatível com: O Mago e O Explorador.", "career": "Design, Arquitetura, Engenharia, Direção de Arte.", "evolution": "1. Lance produtos imperfeitos.\n2. Separe seu valor pessoal da sua obra.\n3. Crie processos repetíveis."},
    "O Explorador": {"radar": [40, 80, 40, 60, 90, 100], "rarity": "7,1%", "desc": "A rotina é seu maior inimigo. Você é guiado por uma bússola interna em busca do desconhecido.", "sombra": "O Inconstante: Fuga crônica de compromissos; abandona projetos na metade.", "oculto": "Estrategista de Longo Prazo: Uma habilidade oculta de ver o quadro geral das tendências.", "finance": "Dinheiro como passaporte. Gasta em experiências, não em ativos. Precisa de sistemas automáticos de economia.", "love": "Aversão a amarras. Compatível com: O Sábio e O Fora da Lei.", "career": "Fotografia, Jornalismo Investigativo, Nômade Digital, Consultoria Externa.", "evolution": "1. Defina âncoras (hábitos fixos).\n2. Cumpra compromissos de longo prazo.\n3. Aprofunde-se em vez de apenas explorar a superfície."},
    "O Rebelde (Fora da Lei)": {"radar": [80, 85, 50, 90, 95, 70], "rarity": "4,1%", "desc": "As regras foram feitas para serem quebradas. Você vê a falha no sistema e sente a obrigação de destruí-lo para reconstruir.", "sombra": "O Destruidor Niilista: Quebra coisas sem ter um plano para colocar no lugar; rebeldia sem causa.", "oculto": "Guardião da Ética: Um senso moral profundo que paradoxalmente o faz quebrar regras imorais.", "finance": "Volátil. Tende a investimentos de alto risco, criptomoedas ou negócios disruptivos.", "love": "Desafiador e passional. Compatível com: O Amante e O Mago.", "career": "Hackers, Ativistas, Founders de Startups Disruptivas, Política Alternativa.", "evolution": "1. Escolha suas batalhas.\n2. Construa pontes, não apenas imploda barreiras.\n3. Canalize a raiva para criação."},
    "O Amante": {"radar": [60, 70, 40, 95, 50, 80], "rarity": "9,2%", "desc": "Guiado pelos sentidos e pela paixão. Você busca intimidade e conexão estética com tudo ao seu redor.", "sombra": "O Dependente Emocional: Perde a própria identidade para agradar parceiros ou a sociedade.", "oculto": "Vontade de Ferro: Uma força inabalável quando se trata de defender quem ama.", "finance": "Orientado ao luxo e estética. Pode sofrer financeiramente buscando manter um status sedutor.", "love": "A entrega total. Compatível com: O Rebelde e O Herói.", "career": "Moda, Relações Públicas, Estética, Vendas High-Ticket.", "evolution": "1. Fortaleça o amor-próprio.\n2. Aprenda a dizer 'não'.\n3. Separe negócios de emoções."},
    "O Cuidador": {"radar": [60, 50, 50, 100, 40, 70], "rarity": "11,5%", "desc": "A espinha dorsal da humanidade. Sua empatia cria ambientes onde outros podem prosperar e curar.", "sombra": "O Mártir Ressentido: Faz tudo por todos, ignora a si mesmo e culpa o mundo pela própria exaustão.", "oculto": "Liderança de Bastidores: Manipulação benigna para guiar o grupo ao sucesso sem levar o crédito.", "finance": "Generoso. Risco de esgotar o próprio patrimônio para salvar familiares ou amigos.", "love": "Nutritivo e constante. Compatível com: O Herói e O Inocente.", "career": "Medicina, RH, Psicologia, Assistência Social.", "evolution": "1. Coloque a máscara de oxigênio em você primeiro.\n2. Defina limites claros.\n3. Pare de tentar consertar adultos funcionais."},
    "O Inocente": {"radar": [30, 60, 30, 80, 60, 80], "rarity": "15,2%", "desc": "Uma lente de otimismo puro. Você enxerga a luz no fim do túnel e acredita inerentemente no bem.", "sombra": "O Negacionista: Ignora red flags e realidades duras para manter a ilusão de que tudo está bem.", "oculto": "Resiliência Bruta: Uma capacidade de sobreviver a traumas severos mantendo a sanidade.", "finance": "Confiante no universo. Pode delegar o dinheiro a pessoas erradas por excesso de confiança.", "love": "Puro e leal. Compatível com: O Herói e O Cuidador.", "career": "Ensino Infantil, ONGs, Bem-estar, Filosofia.", "evolution": "1. Estude cinismo estratégico.\n2. Assuma responsabilidades difíceis.\n3. Aceite que o conflito é necessário."},
    "O Visionário": {"radar": [85, 95, 80, 80, 85, 70], "rarity": "1,9%", "desc": "Seus olhos estão sempre 10 anos no futuro. Você sintetiza tendências globais antes de todos.", "sombra": "O Profeta Louco: Total descolamento do presente; perde a conexão com a vida diária.", "oculto": "Operador Tático: Quando necessário, consegue descer ao micro e executar perfeitamente.", "finance": "Focado no amanhã. Rico em opções, às vezes pobre em fluxo de caixa atual.", "love": "Busca alguém que compreenda o futuro. Compatível com: O Sábio e O Criador.", "career": "Tech Founder, Venture Capital, Urbanista, Diretor de Estratégia.", "evolution": "1. Viva o hoje.\n2. Crie indicadores de curto prazo.\n3. Comunique-se de forma simples."},
    "O Equilibrador (O Bobo)": {"radar": [50, 80, 70, 90, 70, 95], "rarity": "6,4%", "desc": "Mestre da subversão através do humor. Você quebra tensões corporativas e expõe verdades que ninguém ousa dizer.", "sombra": "O Falso Raso: Usa o humor como escudo constante para não lidar com dores profundas.", "oculto": "Observação Analítica: Lê o ambiente com precisão cirúrgica de um espião.", "finance": "Carpe Diem. Vive o agora, frequentemente negligenciando fundos de emergência.", "love": "Divertido e desapegado. Compatível com: O Governante e O Explorador.", "career": "Entretenimento, Negociador de Crises, Palestrante, Vendas.", "evolution": "1. Mostre sua dor.\n2. Leve as finanças a sério.\n3. Use o humor para construir, não só para desarmar."}
}

# 20 Perguntas de Alto Impacto Psicológico
questions_db = [
    {"q": "Em um cenário de crise corporativa grave, sua primeira resposta neurológica é:", "opts": {"Isolar-se para analisar os dados e precedentes.": "O Sábio", "Assumir o controle imediato da narrativa e dar ordens.": "O Governante", "Buscar soluções não convencionais e disruptivas.": "O Visionário", "Checar a equipe e absorver o impacto emocional deles.": "O Cuidador", "Ver a crise como uma chance de destruir as velhas regras.": "O Rebelde (Fora da Lei)"}},
    {"q": "Ao lidar com dinheiro e investimentos de alto valor, você se sente mais seguro quando:", "opts": {"Segue uma estrutura lógica, diversificada e comprovada.": "O Sábio", "Aposta agressivamente no seu próprio negócio ou instinto.": "O Herói", "Garante o controle e o poder sobre os ativos gerados.": "O Governante", "Investe em algo revolucionário que vai mudar o mercado.": "O Visionário", "Sente que o dinheiro fluirá porque suas intenções são boas.": "O Inocente"}},
    {"q": "Seu maior medo irracional de madrugada, quando está sozinho, é:", "opts": {"Estar errado ou ser visto como intelectualmente fraco.": "O Sábio", "Perder o controle sobre o seu território e sua vida.": "O Governante", "Perceber que viveu uma vida monótona e sem impacto.": "O Explorador", "Ficar preso em um sistema medíocre e ser silenciado.": "O Rebelde (Fora da Lei)", "Perder a conexão profunda com quem você ama.": "O Amante"}},
    {"q": "Nas suas relações amorosas mais intensas, você tende a assumir a postura do(a):", "opts": {"Pilar de força que protege e resolve os problemas.": "O Herói", "Parceiro que nutre, cuida e cura feridas antigas.": "O Cuidador", "Companheiro estético, focado em paixão e beleza.": "O Amante", "Estrategista que avalia se a relação faz sentido a longo prazo.": "O Sábio", "Aquele que injeta imprevisibilidade e quebra a rotina.": "O Explorador"}},
    {"q": "Qual destas descrições mais se aproxima do seu processo criativo?", "opts": {"Começa com pesquisa profunda até encontrar a verdade estrutural.": "O Sábio", "Nasce de uma visão clara de como as coisas deveriam ser.": "O Criador", "Surge de conexões improváveis que parecem mágica.": "O Mago", "É um impulso rápido para corrigir uma injustiça imediata.": "O Herói", "Vem como uma intuição utópica sobre um futuro perfeito.": "O Visionário"}},
    {"q": "Quando alguém o confronta publicamente com uma injustiça, você:", "opts": {"Exige provas, dados e embasamento lógico na hora.": "O Sábio", "Usa seu peso de autoridade para encerrar o assunto.": "O Governante", "Desarma a pessoa com carisma, humor ou retórica fluida.": "O Equilibrador (O Bobo)", "Levanta-se para lutar de frente, doa a quem doer.": "O Herói", "Tenta entender a dor por trás do ataque da pessoa.": "O Cuidador"}},
    {"q": "A verdadeira liberdade, na sua concepção existencial, significa:", "opts": {"Não ter limitações geográficas, rotinas ou chefes.": "O Explorador", "Ter poder financeiro absoluto para controlar seu tempo.": "O Governante", "Viver alinhado com a sua verdade interior, sem amarras sociais.": "O Rebelde (Fora da Lei)", "Poder criar e construir seu legado sem interferência.": "O Criador", "Ter tranquilidade mental e harmonia ao seu redor.": "O Inocente"}},
    {"q": "Qual característica as pessoas frequentemente invejam, mas secretamente odeiam em você?", "opts": {"Sua capacidade fria de separar emoção de razão.": "O Sábio", "Sua autoconfiança que frequentemente beira a arrogância.": "O Herói", "Seu poder de influenciar e manipular os cenários a seu favor.": "O Mago", "Sua intensidade avassaladora e foco no magnetismo pessoal.": "O Amante", "Sua aparente desconexão das 'regras chatas' da vida.": "O Equilibrador (O Bobo)"}},
    {"q": "Se você tivesse 1 milhão de reais garantidos por mês, sem precisar trabalhar, você:", "opts": {"Voltaria para a academia para estudar e pesquisar.": "O Sábio", "Montaria um império corporativo ainda maior por esporte.": "O Governante", "Viajaria o globo testando limites e culturas extremas.": "O Explorador", "Financiaria startups disruptivas e tecnologias obscuras.": "O Visionário", "Criaria fundações para proteger e curar pessoas ou animais.": "O Cuidador"}},
    {"q": "Diante do fracasso de um projeto muito importante, sua métrica de recuperação é:", "opts": {"Entender metodologicamente o que deu errado na planilha.": "O Sábio", "Refazer tudo sozinho, assumindo a culpa pela equipe.": "O Herói", "Transformar o erro em um 'pivot' e vender como inovação.": "O Mago", "Demite/afasta quem errou para restabelecer a ordem.": "O Governante", "Rir do absurdo da situação e tentar a próxima loucura.": "O Equilibrador (O Bobo)"}},
    {"q": "Você prefere ser respeitado por:", "opts": {"Seu intelecto afiado e conhecimento incontestável.": "O Sábio", "Sua força, coragem e capacidade de entregar resultados.": "O Herói", "Seu gosto refinado, paixão e capacidade de atrair.": "O Amante", "Seu dom para unir pessoas e manter a paz.": "O Inocente", "Sua audácia em destruir paradigmas antigos.": "O Rebelde (Fora da Lei)"}},
    {"q": "Quando lida com subordinação corporativa ou chefes ruins, você:", "opts": {"Joga o jogo político enquanto arquiteta a superação deles.": "O Mago", "Bate de frente, ignora as ordens e faz do seu jeito.": "O Rebelde (Fora da Lei)", "Foca exclusivamente na execução técnica, ignorando a política.": "O Sábio", "Apoia os colegas que sofrem sob a gestão ruim.": "O Cuidador", "Prepara-se para tomar o lugar do chefe e governar direito.": "O Governante"}},
    {"q": "O conceito de 'legado' para você é:", "opts": {"Construir monumentos, obras ou empresas que fiquem para a história.": "O Criador", "Garantir a segurança intergeracional e o bom nome da família.": "O Governante", "Uma ideia, filosofia ou método científico que você ajudou a provar.": "O Sábio", "Quebrar um ciclo de opressão na sua linhagem.": "O Herói", "Ter amado intensamente e deixado boas memórias.": "O Amante"}},
    {"q": "Seu espaço de trabalho ideal é:", "opts": {"Minimalista, silencioso, rodeado apenas de livros e dados.": "O Sábio", "Um estúdio caótico cheio de ferramentas, cores e referências.": "O Criador", "Uma mesa executiva em um arranha-céu, que imponha respeito.": "O Governante", "Onde quer que haja Wi-Fi e uma passagem aérea próxima.": "O Explorador", "Um ambiente aconchegante, comunitário e com plantas/animais.": "O Inocente"}},
    {"q": "O que mais drena sua bateria social rapidamente?", "opts": {"Conversas rasas, small-talk e falta de substância.": "O Sábio", "Ambientes extremamente rígidos, burocráticos e lentos.": "O Explorador", "Injustiças claras que ninguém está fazendo nada a respeito.": "O Herói", "Ambientes esteticamente feios ou sem paixão.": "O Amante", "A incapacidade crônica de execução de quem o cerca.": "O Governante"}},
    {"q": "O seu 'mecanismo de defesa' padrão quando ferido emocionalmente é:", "opts": {"Racionalizar o sentimento até ele deixar de doer.": "O Sábio", "Ataque imediato, blindando a própria vulnerabilidade.": "O Herói", "Criar uma ilusão ou nova realidade onde você é superior.": "O Mago", "Fechar-se e focar obsessivamente no trabalho/arte.": "O Criador", "Tornar-se cínico e sarcástico para esconder a dor.": "O Equilibrador (O Bobo)"}},
    {"q": "O mercado ideal para sua mente seria aquele onde:", "opts": {"As regras são matemáticas e previsíveis.": "O Sábio", "A disrupção é contínua e as coisas antigas morrem rápido.": "O Visionário", "A estética, a conexão e a beleza são as moedas de troca.": "O Amante", "A hierarquia é clara e o mérito é recompensado com poder.": "O Governante", "Você atua sozinho, entrando e saindo sem deixar rastros.": "O Explorador"}},
    {"q": "Ao receber uma crítica extremamente construtiva, porém dura, você:", "opts": {"Analisa a validade técnica e ignora o tom.": "O Sábio", "Sente o golpe no ego, mas ajusta para voltar mais forte.": "O Herói", "Tenta entender por que a pessoa sentiu a necessidade de falar.": "O Cuidador", "Avalia se a pessoa tem status suficiente para criticá-lo.": "O Governante", "Fica defensivo porque pareceu um ataque à sua criatividade.": "O Criador"}},
    {"q": "Sua relação com a 'Morte' e o fim das coisas é:", "opts": {"Apenas a etapa final de um processo biológico natural.": "O Sábio", "Um motivador de urgência para realizar tudo agora.": "O Visionário", "O inimigo supremo a ser combatido através do legado.": "O Governante", "Um mistério poético, uma transição alquímica.": "O Mago", "O motivo para amar e sentir prazer ao máximo hoje.": "O Amante"}},
    {"q": "Em sua essência mais profunda, o que você quer do mundo?", "opts": {"Entender o mundo.": "O Sábio", "Proteger o mundo.": "O Herói", "Dominar o mundo.": "O Governante", "Transformar o mundo.": "O Mago", "Viver o mundo.": "O Explorador"}}
]

# ==========================================
# 3. GERENCIAMENTO DE ESTADO
# ==========================================
if 'stage' not in st.session_state:
    st.session_state.stage = 'cover'
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'scores' not in st.session_state:
    st.session_state.scores = {k: 0 for k in archetypes_db.keys()}
if 'results' not in st.session_state:
    st.session_state.results = {}

def set_stage(stage_name):
    st.session_state.stage = stage_name
    st.rerun()

# ==========================================
# 4. FUNÇÕES DE SUPORTE
# ==========================================
def calculate_results():
    scores = st.session_state.scores
    # Add minor random noise to break ties elegantly
    for k in scores:
        scores[k] += random.uniform(0, 0.1)
    
    sorted_archs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    st.session_state.results['primary'] = sorted_archs[0][0]
    st.session_state.results['secondary'] = sorted_archs[1][0]
    st.session_state.results['match_rate'] = random.randint(88, 97)

def create_radar_chart(arch_name):
    data = archetypes_db[arch_name]["radar"]
    categories = ['Liderança', 'Criatividade', 'Inteligência Estratégica', 'Influência Social', 'Coragem', 'Adaptabilidade']
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=data,
        theta=categories,
        fill='toself',
        fillcolor='rgba(212, 175, 55, 0.4)',
        line=dict(color='#d4af37', width=2),
        marker=dict(color='#ffffff', size=6)
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], color='#4a4a4a', gridcolor='#2d3748'),
            angularaxis=dict(color='#d4af37', gridcolor='#2d3748')
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#f0f0f0', size=12),
        margin=dict(t=20, b=20, l=20, r=20)
    )
    return fig

def generate_premium_pdf():
    pdf = FPDF()
    name = st.session_state.user_data.get('nome', 'Usuário').upper()
    arch = st.session_state.results['primary']
    data = archetypes_db[arch]
    date_str = datetime.now().strftime("%d/%m/%Y")
    
    # Capa
    pdf.add_page()
    pdf.set_fill_color(13, 17, 23)
    pdf.rect(0, 0, 210, 297, 'F')
    pdf.set_text_color(212, 175, 55)
    pdf.set_font("Arial", 'B', 24)
    pdf.cell(200, 60, txt="", ln=True)
    pdf.cell(200, 20, txt="DOSSIE AURADEX SUPREMO", ln=True, align='C')
    pdf.set_font("Arial", '', 14)
    pdf.set_text_color(200, 200, 200)
    pdf.cell(200, 10, txt="Inteligência Comportamental & Análise Psicológica", ln=True, align='C')
    pdf.ln(30)
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(200, 10, txt=f"DIAGNÓSTICO EXECUTIVO DE: {name}", ln=True, align='C')
    pdf.cell(200, 10, txt=f"DATA: {date_str}", ln=True, align='C')
    
    # Conteúdo Principal
    pdf.add_page()
    pdf.set_fill_color(13, 17, 23)
    pdf.rect(0, 0, 210, 297, 'F')
    pdf.set_text_color(212, 175, 55)
    pdf.set_font("Arial", 'B', 18)
    pdf.cell(200, 20, txt=f"ARQUÉTIPO PRINCIPAL: {arch.upper()}", ln=True, align='L')
    pdf.set_font("Arial", '', 12)
    pdf.set_text_color(220, 220, 220)
    
    # Codificando em latin-1 e substituindo chars inválidos para simplificar na FPDF basica
    def clean_text(t): return t.replace('\n', ' ').encode('latin-1', 'replace').decode('latin-1')
    
    pdf.multi_cell(0, 8, txt=clean_text(f"Visão Geral: {data['desc']}"))
    pdf.ln(5)
    pdf.set_text_color(255, 100, 100)
    pdf.multi_cell(0, 8, txt=clean_text(f"Sombra e Sabotadores: {data['sombra']}"))
    pdf.ln(5)
    pdf.set_text_color(212, 175, 55)
    pdf.multi_cell(0, 8, txt=clean_text(f"Perfil Financeiro: {data['finance']}"))
    pdf.ln(5)
    pdf.set_text_color(200, 200, 200)
    pdf.multi_cell(0, 8, txt=clean_text(f"Perfil Amoroso: {data['love']}"))
    pdf.ln(5)
    pdf.multi_cell(0, 8, txt=clean_text(f"Talento Oculto: {data['oculto']}"))
    pdf.ln(5)
    pdf.multi_cell(0, 8, txt=clean_text(f"Carreiras Ideais: {data['career']}"))
    pdf.ln(5)
    pdf.set_text_color(212, 175, 55)
    pdf.multi_cell(0, 8, txt=clean_text("Plano de Evolução:"))
    pdf.set_text_color(200, 200, 200)
    pdf.multi_cell(0, 8, txt=clean_text(data['evolution']))
    
    return pdf.output(dest='S').encode('latin-1')

# ==========================================
# 5. TELAS DO FUNIL
# ==========================================

def show_cover():
    st.markdown("<h1>Apenas 4,7% das pessoas possuem um perfil tão raro quanto o seu.</h1>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Descubra os padrões ocultos que influenciam silenciosamente suas decisões, relacionamentos, dinheiro e destino.</div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="stats-container">
            <div class="stat-item">
                <div class="stat-number">25.000+</div>
                <div class="stat-label">Perfis Analisados</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">93%</div>
                <div class="stat-label">Precisão Estatística</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">AI</div>
                <div class="stat-label">Diagnóstico Imediato</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    if st.button("INICIAR ANÁLISE COMPORTAMENTAL"):
        set_stage('identification')

def show_identification():
    st.markdown("<h2>Módulo de Calibragem</h2>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Precisamos de dados básicos para ajustar os pesos da IA Psicométrica.</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    with st.form("user_info_form"):
        nome = st.text_input("Seu Primeiro Nome", max_chars=30)
        idade = st.number_input("Sua Idade", min_value=16, max_value=120, step=1, value=25)
        sexo = st.selectbox("Sexo (Opcional - para calibrar linguagem)", ["Prefiro não informar", "Masculino", "Feminino"])
        
        if st.form_submit_button("COMEÇAR DIAGNÓSTICO PROFUNDO"):
            if not nome.strip():
                st.error("Por favor, insira seu nome.")
            else:
                st.session_state.user_data = {'nome': nome.strip().capitalize(), 'idade': idade, 'sexo': sexo}
                set_stage('test')
    st.markdown("</div>", unsafe_allow_html=True)

def show_test():
    st.markdown("<h2>Diagnóstico em Andamento</h2>", unsafe_allow_html=True)
    
    # Para não sobrecarregar a tela, mostraremos uma pergunta por vez
    current_q = len(st.session_state.answers)
    
    if current_q < len(questions_db):
        progress = current_q / len(questions_db)
        st.progress(progress)
        st.markdown(f"<p style='text-align:right; color:#888; font-size:12px;'>Bloco Analítico {current_q+1}/{len(questions_db)}</p>", unsafe_allow_html=True)
        
        q_data = questions_db[current_q]
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:left; color:#f0f0f0;'>{q_data['q']}</h3><br>", unsafe_allow_html=True)
        
        options = list(q_data['opts'].keys())
        random.shuffle(options) # Evita viés de posição
        
        choice = st.radio("Selecione a resposta mais instintiva:", options, key=f"q_{current_q}")
        
        st.write("<br>", unsafe_allow_html=True)
        if st.button("PROCESSAR E AVANÇAR"):
            selected_arch = q_data['opts'][choice]
            st.session_state.scores[selected_arch] += 1
            st.session_state.answers.append(choice)
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        set_stage('loading')

def show_loading():
    st.markdown("<h2>Sintetizando Perfil Psicométrico...</h2>", unsafe_allow_html=True)
    
    bar = st.progress(0)
    status = st.empty()
    
    messages = [
        "Mapeando padrões cognitivos...",
        "Calculando perfil emocional na matriz de dados...",
        "Detectando arquétipos secundários silenciosos...",
        "Analisando tendências financeiras e vieses de risco...",
        "Isolando o 'Ponto Cego' (Arquétipo Sombra)...",
        "Criptografando Dossiê e Finalizando relatório..."
    ]
    
    for i in range(101):
        bar.progress(i)
        step = i // 18
        if step < len(messages):
            status.markdown(f"<div class='loading-text'>{messages[step]}</div>", unsafe_allow_html=True)
        time.sleep(0.04) # Cinematic delay
        
    calculate_results()
    set_stage('free_result')

def show_free_result():
    nome = st.session_state.user_data['nome']
    arch_name = st.session_state.results['primary']
    match_rate = st.session_state.results['match_rate']
    
    st.markdown(f"<h2>Análise Concluída, {nome}.</h2>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="glass-card" style="text-align:center;">
            <p style="color:#a3a3a3; font-size:1.2rem; text-transform:uppercase;">Seu Arquétipo Dominante é</p>
            <h1 style="font-size:3.5rem; margin-top:0;">{arch_name}</h1>
            <h3 style="color:#2ecc71;">{match_rate}% de Matriz de Compatibilidade</h3>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<p style='font-size:1.2rem; line-height:1.6;'>{archetypes_db[arch_name]['desc']}</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Gatilhos de curiosidade
    st.warning("🚨 **ALERTA DO SISTEMA AI:** Detectamos uma anomalia em sua matriz de dados. Existe um **arquétipo secundário oculto** operando nas sombras que influencia criticamente suas decisões financeiras e sua escolha de parceiros amorosos.")
    
    st.markdown("""
        <div style="background-color:rgba(212, 175, 55, 0.1); padding:20px; border-left:4px solid #d4af37; border-radius:4px; margin-top:20px;">
        <h4 style='text-align:left; color:#d4af37;'>⚠️ O que nossa IA bloqueou na versão gratuita:</h4>
        <ul style='color:#ccc;'>
            <li>O seu <b>Arquétipo Sombra</b> (os sabotadores que destroem suas conquistas).</li>
            <li>O seu <b>Perfil Financeiro</b> (sua tendência exata a riqueza ou falência).</li>
            <li>O <b>Radar Comportamental Executivo</b> (Gráfico Plotly de alta precisão).</li>
            <li>A sua <b>Missão de Vida e Plano de Evolução de 3 Passos</b>.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    if st.button("🔓 DESBLOQUEAR MEU DOSSIÊ SUPREMO COMPLETO"):
        set_stage('premium_offer')

def show_premium_offer():
    st.markdown("<h1>DOSSIÊ ARQUÉTIPO SUPREMO</h1>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Acesso imediato ao relatório de inteligência comportamental mais profundo já gerado sobre você.</div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card">
            <h3 style="text-align:left;">O que você vai receber agora:</h3>
            <div style="font-size:1.1rem; line-height:2.0; color:#e6e6e6;">
                ✓ <b>Diagnóstico do Arquétipo Principal</b> (Profundo)<br>
                ✓ <b>O Arquétipo Secundário</b> (A influência invisível)<br>
                ✓ <b>A Máscara da Sombra</b> (Seus sabotadores internos)<br>
                ✓ <b>O Talento Oculto</b> (Potencial adormecido)<br>
                ✓ <b>Inteligência Financeira</b> (Riscos e oportunidades do seu perfil)<br>
                ✓ <b>Mapeamento Amoroso</b> (Com quem você realmente se conecta)<br>
                ✓ <b>Radar Comportamental Profissional</b> (Gráfico C-Level)<br>
                ✓ <b>Plano de Evolução Direto</b> (Passos práticos)<br>
                ✓ <b>PDF Premium Exportável</b> (Para salvar ou imprimir)
            </div>
            <br>
            <div style="text-align:center;">
                <p style="text-decoration:line-through; color:#888; font-size:1.2rem;">Valor Regular: R$ 97,00</p>
                <h2 style="color:#2ecc71; font-size:2.5rem; margin-top:0;">Apenas R$ 4,90</h2>
                <p style="color:#a3a3a3; font-size:0.9rem;">(Pagamento Único. Acesso Vitalício e Imediato)</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Simulação de Webhook/Checkout para a demonstração
    if st.button("💳 PAGAR R$ 4,90 E DESBLOQUEAR AGORA"):
        with st.spinner("Processando pagamento fictício e liberando Dossiê..."):
            time.sleep(2)
            set_stage('premium_report')

def show_premium_report():
    nome = st.session_state.user_data['nome']
    arch_primary = st.session_state.results['primary']
    arch_sec = st.session_state.results['secondary']
    data = archetypes_db[arch_primary]
    sec_data = archetypes_db[arch_sec]
    
    st.success("Pagamento Confirmado. Nível de Segurança: Acesso Liberado.")
    st.markdown("<h1>DOSSIÊ EXECUTIVO SUPREMO</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Índice de Potencial e Raridade
    st.markdown(f"""
        <div class="stats-container" style="border-color:#d4af37;">
            <div class="stat-item">
                <div class="stat-number">98/100</div>
                <div class="stat-label">Índice Global de Potencial</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">{data['rarity']}</div>
                <div class="stat-label">Raridade Populacional</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card-title'>Radar Comportamental</div>", unsafe_allow_html=True)
        fig = create_radar_chart(arch_primary)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card-title'>💰 Inteligência Financeira</div>", unsafe_allow_html=True)
        st.markdown(f"<p>{data['finance']}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card-title'>💼 Projeção de Carreira</div>", unsafe_allow_html=True)
        st.markdown(f"<p><b>Zonas de Excelência:</b> {data['career']}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='glass-card' style='border-left: 4px solid #e74c3c;'>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card-title' style='color:#e74c3c; border-color:#e74c3c;'>🌑 O Arquétipo Sombra</div>", unsafe_allow_html=True)
        st.markdown(f"<p>Estes são os seus sabotadores internos. A força que o destrói quando sob stress crônico:</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#ffb3b3;'><b>{data['sombra']}</b></p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='glass-card' style='border-left: 4px solid #3498db;'>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card-title' style='color:#3498db; border-color:#3498db;'>🧬 A Influência Secundária</div>", unsafe_allow_html=True)
        st.markdown(f"<p>Seu coprotagonista mental: <b>{arch_sec}</b>.</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:0.9rem; color:#ccc;'>Ele age nos bastidores fornecendo traços de: <i>{sec_data['desc'][:80]}...</i></p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='glass-card' style='border-left: 4px solid #9b59b6;'>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card-title' style='color:#9b59b6; border-color:#9b59b6;'>✨ O Talento Oculto</div>", unsafe_allow_html=True)
        st.markdown(f"<p>Capacidade adormecida com alto poder de capitalização e sucesso:</p>", unsafe_allow_html=True)
        st.markdown(f"<p><b>{data['oculto']}</b></p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='glass-card' style='border-left: 4px solid #e84393;'>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card-title' style='color:#e84393; border-color:#e84393;'>❤️ Mapeamento Amoroso</div>", unsafe_allow_html=True)
        st.markdown(f"<p>{data['love']}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Plano de Evolução Full Width
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card-title'>📈 Plano de Evolução Tático</div>", unsafe_allow_html=True)
    st.markdown(f"<pre style='background:transparent; border:none; color:#f0f0f0; font-family:Helvetica; font-size:1.1rem; line-height:1.8; white-space:pre-wrap;'>{data['evolution']}</pre>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("---")
    
    # Compartilhamento e PDF
    col_pdf, col_zap = st.columns(2)
    
    with col_pdf:
        pdf_bytes = generate_premium_pdf()
        st.download_button(
            label="⬇️ BAIXAR DOSSIÊ EM PDF",
            data=pdf_bytes,
            file_name=f"Dossie_Supremo_{nome}.pdf",
            mime="application/pdf",
            use_container_width=True
        )
        
    with col_zap:
        msg = f"Acabei de descobrir meu Arquétipo Supremo no AuraDex. Sou da classe rara '{arch_primary}' (apenas {data['rarity']}). Faça o seu teste."
        url_msg = urllib.parse.quote(msg)
        st.markdown(f"""
            <a href="https://wa.me/?text={url_msg}" target="_blank" style="text-decoration:none;">
                <button style="width: 100%; background: #25D366; color: white; font-weight: bold; font-size:1.1rem; border-radius: 8px; border: none; padding: 15px; cursor:pointer; text-transform:uppercase;">
                    📱 COMPARTILHAR NO WHATSAPP
                </button>
            </a>
        """, unsafe_allow_html=True)

# ==========================================
# 6. MOTOR DE ROTEAMENTO
# ==========================================
if st.session_state.stage == 'cover':
    show_cover()
elif st.session_state.stage == 'identification':
    show_identification()
elif st.session_state.stage == 'test':
    show_test()
elif st.session_state.stage == 'loading':
    show_loading()
elif st.session_state.stage == 'free_result':
    show_free_result()
elif st.session_state.stage == 'premium_offer':
    show_premium_offer()
elif st.session_state.stage == 'premium_report':
    show_premium_report()
