"""
AURADEX ARQUÉTIPOS SUPREMO
Premium Archetype Intelligence Platform
"""

import streamlit as st
import plotly.graph_objects as go
import json
import time
import io
import base64
from datetime import datetime
import random

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AuraDex · Arquétipos Supremo",
    page_icon="◈",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  GLOBAL CSS — DARK LUXURY THEME
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

:root {
  --black:    #0a0c0f;
  --black2:   #0d1117;
  --graphite: #161b22;
  --surface:  #1a1f2e;
  --border:   #21262d;
  --gold:     #d4af37;
  --gold2:    #e8c95d;
  --gold3:    #b8960c;
  --white:    #f0f1f3;
  --white2:   #c9ced8;
  --dim:      #7d8590;
  --accent:   #7c5cbf;
}

html, body, [data-testid="stAppViewContainer"] {
  background: var(--black2) !important;
  color: var(--white) !important;
}

[data-testid="stAppViewContainer"] > .main {
  background: var(--black2) !important;
}

section[data-testid="stSidebar"] { display: none; }
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stToolbar"] { display: none; }
footer { display: none !important; }
#MainMenu { display: none; }

* { font-family: 'Inter', sans-serif; box-sizing: border-box; }

h1, h2, h3 { font-family: 'Cormorant Garamond', serif !important; }

/* ─── BUTTONS ─── */
.stButton > button {
  width: 100%;
  background: linear-gradient(135deg, #d4af37 0%, #b8960c 50%, #d4af37 100%) !important;
  background-size: 200% 200% !important;
  color: #0a0c0f !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-weight: 700 !important;
  font-size: 0.9rem !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  border: none !important;
  border-radius: 4px !important;
  padding: 0.85rem 2rem !important;
  cursor: pointer !important;
  transition: all 0.3s ease !important;
  box-shadow: 0 0 24px rgba(212,175,55,0.25), inset 0 1px 0 rgba(255,255,255,0.15) !important;
}
.stButton > button:hover {
  box-shadow: 0 0 40px rgba(212,175,55,0.45), inset 0 1px 0 rgba(255,255,255,0.2) !important;
  transform: translateY(-1px) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ─── INPUTS ─── */
.stTextInput > div > div > input,
.stSelectbox > div > div > div,
.stNumberInput > div > div > input {
  background: var(--graphite) !important;
  border: 1px solid var(--border) !important;
  border-radius: 4px !important;
  color: var(--white) !important;
  font-family: 'Space Grotesk', sans-serif !important;
  padding: 0.65rem 1rem !important;
}
.stTextInput > div > div > input:focus,
.stSelectbox > div > div > div:focus {
  border-color: var(--gold) !important;
  box-shadow: 0 0 0 2px rgba(212,175,55,0.12) !important;
}

.stSelectbox > div > div { background: var(--graphite) !important; }
.stSelectbox [data-baseweb="select"] > div { background: var(--graphite) !important; border-color: var(--border) !important; }

label, .stTextInput label, .stSelectbox label, .stNumberInput label {
  color: var(--white2) !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-size: 0.75rem !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
}

/* ─── RADIO ─── */
.stRadio > label { color: var(--white2) !important; font-size: 0.75rem !important; letter-spacing: 0.1em !important; text-transform: uppercase !important; }
.stRadio > div { gap: 0.5rem !important; }
.stRadio > div > label {
  background: var(--graphite) !important;
  border: 1px solid var(--border) !important;
  border-radius: 4px !important;
  padding: 0.65rem 1rem !important;
  color: var(--white2) !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-size: 0.85rem !important;
  cursor: pointer !important;
  transition: all 0.2s !important;
  width: 100% !important;
}
.stRadio > div > label:hover { border-color: var(--gold3) !important; color: var(--white) !important; }
div[data-baseweb="radio"] input:checked + div + div { color: var(--gold) !important; }

/* ─── PROGRESS ─── */
.stProgress > div > div { background: var(--border) !important; border-radius: 2px !important; }
.stProgress > div > div > div { background: linear-gradient(90deg, var(--gold3), var(--gold)) !important; border-radius: 2px !important; }

/* ─── DIVIDER ─── */
hr { border-color: var(--border) !important; }

/* ─── COMPONENTS ─── */
.gold-divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
  margin: 2rem 0;
}

.glass-card {
  background: rgba(22,27,34,0.7);
  border: 1px solid rgba(212,175,55,0.15);
  border-radius: 8px;
  padding: 1.75rem 2rem;
  backdrop-filter: blur(12px);
  margin-bottom: 1.25rem;
}

.metric-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  background: rgba(212,175,55,0.08);
  border: 1px solid rgba(212,175,55,0.2);
  border-radius: 100px;
  padding: 0.35rem 0.85rem;
  font-family: 'Space Grotesk', sans-serif;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  color: var(--gold2);
  text-transform: uppercase;
}

.archetype-title {
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 2.8rem;
  font-weight: 700;
  color: var(--gold);
  line-height: 1.1;
  letter-spacing: -0.01em;
}

.section-eyebrow {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--gold3);
  margin-bottom: 0.5rem;
}

.lock-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.65rem 0;
  border-bottom: 1px solid var(--border);
  color: var(--dim);
  font-family: 'Space Grotesk', sans-serif;
  font-size: 0.85rem;
}
.lock-item.unlocked { color: var(--white2); }
.lock-icon { font-size: 0.9rem; min-width: 1.2rem; }

.price-tag {
  font-family: 'Cormorant Garamond', serif;
  font-size: 3.5rem;
  font-weight: 700;
  color: var(--gold);
  line-height: 1;
}

.rarity-bar {
  height: 6px;
  background: var(--border);
  border-radius: 3px;
  overflow: hidden;
  margin: 0.5rem 0;
}
.rarity-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--gold3), var(--gold2));
  border-radius: 3px;
}

.stat-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.6rem 0;
  border-bottom: 1px solid var(--border);
  font-family: 'Space Grotesk', sans-serif;
  font-size: 0.85rem;
}
.stat-label { color: var(--dim); }
.stat-value { color: var(--gold2); font-weight: 600; }

.warning-box {
  background: rgba(212,175,55,0.06);
  border: 1px solid rgba(212,175,55,0.3);
  border-left: 3px solid var(--gold);
  border-radius: 4px;
  padding: 1rem 1.25rem;
  font-family: 'Space Grotesk', sans-serif;
  font-size: 0.85rem;
  color: var(--gold2);
  line-height: 1.6;
}

.cta-headline {
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 2.1rem;
  font-weight: 700;
  color: var(--white);
  line-height: 1.25;
}

.benefit-item {
  display: flex;
  align-items: flex-start;
  gap: 0.65rem;
  padding: 0.45rem 0;
  font-family: 'Space Grotesk', sans-serif;
  font-size: 0.85rem;
  color: var(--white2);
}
.benefit-check { color: var(--gold); font-size: 0.9rem; margin-top: 0.05rem; }

.hero-number {
  font-family: 'Cormorant Garamond', serif;
  font-size: 4.5rem;
  font-weight: 700;
  color: var(--gold);
  line-height: 1;
}

.tag-pill {
  display: inline-block;
  background: rgba(212,175,55,0.1);
  border: 1px solid rgba(212,175,55,0.25);
  border-radius: 3px;
  padding: 0.2rem 0.6rem;
  font-family: 'Space Grotesk', sans-serif;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--gold2);
  margin: 0.15rem;
}

.blurred-text {
  filter: blur(5px);
  user-select: none;
  color: var(--white2);
  font-family: 'Space Grotesk', sans-serif;
  font-size: 0.85rem;
  line-height: 1.7;
}

.premium-section-header {
  background: linear-gradient(135deg, rgba(212,175,55,0.1), rgba(124,92,191,0.05));
  border: 1px solid rgba(212,175,55,0.2);
  border-radius: 6px;
  padding: 1rem 1.25rem;
  margin: 1.5rem 0 1rem 0;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.score-ring {
  text-align: center;
  padding: 1rem;
}

/* ─── QUESTION CARD ─── */
.question-card {
  background: var(--graphite);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 1.5rem 1.75rem;
  margin-bottom: 1.5rem;
}

.q-number {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--gold3);
  margin-bottom: 0.65rem;
}

.q-text {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.35rem;
  font-weight: 500;
  color: var(--white);
  line-height: 1.4;
  margin-bottom: 1.25rem;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  ARCHETYPE DATA
# ─────────────────────────────────────────────
ARCHETYPES = {
    "O Sábio": {
        "symbol": "◎",
        "rarity": 7.2,
        "tagline": "A mente que ilumina o que os outros não enxergam",
        "description": "Você possui uma capacidade rara de síntese intelectual. Seu cérebro opera como um processador de padrões — enxerga conexões invisíveis, questiona premissas que outros aceitam cegamente e constrói sistemas de compreensão que transcendem o óbvio. Há em você uma fome insaciável por profundidade.",
        "shadow": "A paralisia analítica e o distanciamento emocional são seus sabotadores. Você pode se tornar tão apegado à perfeição do pensamento que adia decisões importantes. O medo de estar errado às vezes congela a ação.",
        "financial": "Perfil conservador-estratégico. Você analisa antes de investir, o que te protege de perdas impulsivas. Risco: excesso de análise pode fazer você perder janelas de oportunidade. Potencial para acumulação sólida via ativos de longo prazo.",
        "love": "Você precisa de um parceiro que estimule sua mente. Compatível com O Amante (complemento emocional) e O Explorador (expansão intelectual). Pode ter dificuldade em expressar vulnerabilidade.",
        "career": ["Cientista / Pesquisador", "Filósofo / Consultor Estratégico", "Analista de Dados", "Escritor", "Estrategista Corporativo"],
        "talent": "Síntese de sistemas complexos — você pode ver o todo quando todos os outros estão presos nas partes.",
        "evolution": ["Pratique decisões rápidas com informação incompleta", "Cultive relações emocionais sem agenda intelectual", "Publique seu pensamento — ele tem valor imenso", "Aceite que ação imperfeita supera análise perfeita"],
        "compatible": ["O Herói", "O Explorador", "O Criador"],
        "traits": {"Liderança": 68, "Criatividade": 82, "Inteligência Estratégica": 97, "Influência Social": 54, "Coragem": 61, "Adaptabilidade": 73},
        "color": "#7c5cbf",
    },
    "O Herói": {
        "symbol": "◆",
        "rarity": 9.1,
        "tagline": "Nascido para superar o que nunca foi superado",
        "description": "Você é movido por desafios. Onde outros veem obstáculos, você vê provas. Há uma chama interior que transforma adversidade em combustível — e isso cria resultados que parecem impossíveis aos que ficam de fora. Sua vida é uma jornada de conquistas progressivas.",
        "shadow": "O workaholism e a dificuldade de pedir ajuda são suas sombras. Você pode se tornar tão focado na missão que negligencia relacionamentos e saúde. Também há risco de definir seu valor apenas por realizações externas.",
        "financial": "Perfil empreendedor-agressivo. Alta tolerância ao risco, o que pode gerar grandes ganhos — ou grandes perdas. Você tende a apostar em si mesmo, o que é sua maior força. Equilíbrio com reservas de segurança é essencial.",
        "love": "Você precisa de alguém que admire genuinamente sua missão. Compatível com O Cuidador (suporte emocional) e O Mago (visão compartilhada). Cuidado com o padrão de colocar metas acima de pessoas.",
        "career": ["Empreendedor", "Atleta / Técnico Esportivo", "CEO", "Militar de Alta Patente", "Gestor de Crises"],
        "talent": "Mobilização sob pressão — você performa melhor exatamente quando o ambiente exige o impossível.",
        "evolution": ["Aprenda a descansar sem culpa", "Desenvolva inteligência emocional como ferramenta de liderança", "Construa legado além das conquistas pessoais", "Pratique vulnerabilidade estratégica"],
        "compatible": ["O Sábio", "O Governante", "O Rebelde"],
        "traits": {"Liderança": 91, "Criatividade": 65, "Inteligência Estratégica": 78, "Influência Social": 83, "Coragem": 97, "Adaptabilidade": 72},
        "color": "#c0392b",
    },
    "O Governante": {
        "symbol": "♛",
        "rarity": 5.3,
        "tagline": "Poder, estrutura e a arte de construir impérios",
        "description": "Você pensa em sistemas, estruturas e legados. Sua mente é naturalmente orientada à ordem e ao controle — não por tirania, mas por uma compreensão profunda de que grandes resultados exigem grandes organizações. Você vê o mundo como um tabuleiro de xadrez.",
        "shadow": "O controle excessivo e a dificuldade de delegar podem isolar você e limitar seu crescimento. Você pode confundir autoridade com rigidez, e isso afasta talentos que poderiam multiplcar seus resultados.",
        "financial": "Perfil patrimonialista. Você pensa em ativos, não apenas em renda. Tende a construir portfólios diversificados e a proteger o que tem. Risco: conservadorismo excessivo pode limitar crescimento acelerado.",
        "love": "Você precisa de um parceiro que respeite sua necessidade de estrutura sem se submeter a ela. Compatível com O Cuidador e O Amante. Precisa aprender a abrir mão do controle nos relacionamentos.",
        "career": ["CEO / Diretor Executivo", "Político", "Juiz / Advogado", "General / Comandante", "Gestor Patrimonial"],
        "talent": "Construção de impérios duradouros — você não pensa em trimestres, pensa em décadas.",
        "evolution": ["Pratique delegação radical", "Desenvolva empatia como ferramenta de poder", "Crie espaços de criatividade não estruturada", "Permita que outros liderem partes do seu projeto"],
        "compatible": ["O Herói", "O Sábio", "O Criador"],
        "traits": {"Liderança": 97, "Criatividade": 55, "Inteligência Estratégica": 89, "Influência Social": 86, "Coragem": 74, "Adaptabilidade": 48},
        "color": "#d4af37",
    },
    "O Mago": {
        "symbol": "✦",
        "rarity": 4.7,
        "tagline": "Transformador de realidades, arquiteto do impossível",
        "description": "Você possui um talento inexplicável para transformar contextos. Onde outros veem o que é, você enxerga o que pode ser — e tem a habilidade de catalizar essa transformação. Pessoas ao seu redor frequentemente descrevem experiências ao seu lado como 'transformadoras' sem saber exatamente por quê.",
        "shadow": "A manipulação e o messianismo são seus riscos. Sua habilidade de influenciar pode ser usada para controlar ao invés de libertar. Você também pode acreditar tanto no seu poder de transformação que subestima resistências reais.",
        "financial": "Perfil visionário-volátil. Você enxerga oportunidades onde outros não enxergam e pode criar riqueza de forma não linear. Alto risco de perdas por excesso de confiança. Quando disciplinado, é potencialmente o arquétipo com maior upside financeiro.",
        "love": "Você é intenso e transformador nos relacionamentos. Compatível com O Inocente (despertar) e O Explorador (aventura). Cuidado com o padrão de 'consertar' parceiros.",
        "career": ["Visionário / Fundador de Startup", "Terapeuta / Coach Executivo", "Artista / Performer", "Inventor", "Líder Espiritual / Filósofo"],
        "talent": "Catálise de transformação — você muda ambientes só por estar presente neles.",
        "evolution": ["Desenvolva consistência e disciplina como contrabalança à visão", "Aprenda a distinguir influência de manipulação", "Construa sistemas que funcionem sem você", "Cultive humildade epistêmica"],
        "compatible": ["O Criador", "O Explorador", "O Visionário"],
        "traits": {"Liderança": 79, "Criatividade": 92, "Inteligência Estratégica": 83, "Influência Social": 95, "Coragem": 81, "Adaptabilidade": 88},
        "color": "#8e44ad",
    },
    "O Criador": {
        "symbol": "✶",
        "rarity": 8.4,
        "tagline": "A imaginação que materializa o que ainda não existe",
        "description": "Você é compelido a criar — não como hobby, mas como necessidade existencial. Há em você uma urgência de dar forma ao que existe apenas como visão. Sua mente opera em conexões inesperadas e produções originais que desconcertam e encantam simultaneamente.",
        "shadow": "O perfeccionismo paralisante e a dificuldade de finalizar projetos são seus sabotadores. Você pode ter dezenas de criações pela metade. A crítica externa atinge você profundamente, muitas vezes bloqueando a expressão.",
        "financial": "Perfil criativo-inconsistente. Você tem potencial para criar valor imensurável, mas tende a negligenciar a monetização do que cria. Associação com perfis mais estratégicos (Governante, Sábio) pode multiplicar seus resultados financeiros.",
        "love": "Você precisa de liberdade para criar e de um parceiro que sustente essa liberdade. Compatível com O Cuidador e O Mago. Tende a amar profundamente, mas de forma muitas vezes caótica.",
        "career": ["Artista / Designer", "Arquiteto / Urbanista", "Escritor / Roteirista", "Fundador de Produto", "Diretor Criativo"],
        "talent": "Visão estética e criação de mundos — você não apenas resolve problemas, você os transforma em obras.",
        "evolution": ["Estabeleça rituais de finalização", "Monetize uma criação por vez, antes de começar a próxima", "Separe o valor da obra do julgamento externo", "Colabore com perfis estruturados"],
        "compatible": ["O Mago", "O Visionário", "O Explorador"],
        "traits": {"Liderança": 55, "Criatividade": 98, "Inteligência Estratégica": 63, "Influência Social": 74, "Coragem": 68, "Adaptabilidade": 82},
        "color": "#1abc9c",
    },
    "O Explorador": {
        "symbol": "◉",
        "rarity": 10.2,
        "tagline": "Liberdade, fronteiras e a busca pelo que ainda não foi vivido",
        "description": "Você é atraído pelo desconhecido com uma força gravitacional que não consegue explicar completamente. Fronteiras existem para ser cruzadas, limites para ser testados, territórios para ser desbravados. Sua identidade é construída pela experiência acumulada, não por títulos ou posses.",
        "shadow": "O compromisso é o seu maior desafio. Você pode evitar relacionamentos, carreiras e projetos profundos por medo de perder a liberdade. A inquietude crônica pode impedir a construção de algo verdadeiramente sólido.",
        "financial": "Perfil diversificado-nômade. Você tende a experimentar muitos veículos financeiros sem aprofundar em nenhum. Potencial enorme se canalizar a energia exploratória para investimentos temáticos ou negócios de estilo de vida.",
        "love": "Você precisa de um parceiro que seja também uma aventura. Compatível com O Rebelde e O Criador. Evita relacionamentos que sente como gaiolas.",
        "career": ["Jornalista / Correspondente", "Viajante Profissional / Nômade Digital", "Fotógrafo / Documentarista", "Consultor Internacional", "Antropólogo / Etnógrafo"],
        "talent": "Síntese de experiências diversas — você conecta mundos que nunca se encontrariam sem você.",
        "evolution": ["Escolha uma área e aprofunde-se por pelo menos 2 anos", "Transforme suas experiências em conteúdo ou produto monetizável", "Pratique o comprometimento como forma de liberdade", "Construa uma base antes de partir para a próxima aventura"],
        "compatible": ["O Criador", "O Rebelde", "O Sábio"],
        "traits": {"Liderança": 62, "Criatividade": 85, "Inteligência Estratégica": 69, "Influência Social": 76, "Coragem": 88, "Adaptabilidade": 97},
        "color": "#27ae60",
    },
    "O Rebelde": {
        "symbol": "⊗",
        "rarity": 6.8,
        "tagline": "O catalisador que quebra o que precisa ser quebrado",
        "description": "Você possui uma radar altamente calibrado para hipocrisia, convenção e estruturas que existem apenas para perpetuar a si mesmas. Sua missão não é destruição — é libertação. Você carrega a visão de um mundo diferente do que foi herdado, e essa visão te move com uma energia que desconcerta.",
        "shadow": "A raiva como identidade e a oposição pelo hábito são seus maiores riscos. Você pode se tornar tão definido pelo que rejeita que perde de vista o que constrói. A desconfiança excessiva pode isolar aliados genuínos.",
        "financial": "Perfil anti-establishment. Você tende a preferir ativos alternativos, criptomoedas, negócios fora do mainstream. Alta tolerância ao risco não convencional. Risco: ceticismo excessivo do sistema formal pode afastar oportunidades reguladas.",
        "love": "Você precisa de um parceiro que respeite sua não-conformidade sem precisar ser salvo por ela. Compatível com O Explorador e O Mago. Cuidado com o padrão de seduzir e então resistir à intimidade.",
        "career": ["Ativista / Líder de Movimento", "Empreendedor Disruptivo", "Artista Provocador", "Hacker / Pesquisador de Segurança", "Jornalista Investigativo"],
        "talent": "Disrupção criativa — você vê as falhas nos sistemas que todos fingem que funcionam.",
        "evolution": ["Canalize a energia rebelde em construção, não apenas desconstrução", "Aprenda a usar as regras do sistema para mudá-lo por dentro", "Construa alianças com pessoas que compartilham sua visão", "Desenvolva resiliência emocional para sustentar movimentos longos"],
        "compatible": ["O Explorador", "O Herói", "O Visionário"],
        "traits": {"Liderança": 73, "Criatividade": 88, "Inteligência Estratégica": 71, "Influência Social": 82, "Coragem": 94, "Adaptabilidade": 79},
        "color": "#e74c3c",
    },
    "O Amante": {
        "symbol": "◈",
        "rarity": 11.5,
        "tagline": "A intensidade que transforma conexão em arte",
        "description": "Você experimenta o mundo com uma intensidade sensorial e emocional que a maioria das pessoas nunca experimenta. Beleza, conexão, prazer e profundidade emocional são suas bússolas. Você não apenas vive — você saboreia. Cada experiência passa por um filtro de significado que poucos possuem.",
        "shadow": "A dependência emocional e o medo da perda são suas sombras. Você pode se perder em relacionamentos a ponto de perder a si mesmo. A sensibilidade extrema pode se tornar vulnerabilidade se não for temperada por limites.",
        "financial": "Perfil hedônico-relacional. Você tende a gastar em experiências e em pessoas que ama. Construção de riqueza pode ser desafiadora por priorizar presente em detrimento de futuro. Parceria com perfis mais estruturados é fundamental.",
        "love": "Você é o arquétipo mais profundamente relacional. Compatível com O Herói (proteção) e O Governante (estabilidade). Você transforma qualquer relacionamento em uma experiência única.",
        "career": ["Artista / Músico", "Terapeuta / Conselheiro", "Chef / Sommelier", "Designer de Experiências", "Relações Públicas / Brand Builder"],
        "talent": "Criação de vínculos transformadores — as pessoas que você toca nunca mais são as mesmas.",
        "evolution": ["Desenvolva uma identidade independente de relacionamentos", "Aprenda a amar com limites — não apesar deles", "Canalize a intensidade emocional em criação artística", "Construa reservas financeiras como forma de cuidado próprio"],
        "compatible": ["O Criador", "O Sábio", "O Cuidador"],
        "traits": {"Liderança": 48, "Criatividade": 91, "Inteligência Estratégica": 57, "Influência Social": 93, "Coragem": 61, "Adaptabilidade": 86},
        "color": "#e91e8c",
    },
    "O Cuidador": {
        "symbol": "✿",
        "rarity": 12.3,
        "tagline": "A força silenciosa que sustenta o que importa",
        "description": "Você possui uma capacidade extraordinária de sentir o que o outro precisa — muitas vezes antes que a própria pessoa saiba. Sua presença cria segurança. As pessoas ao seu redor crescem, não por acaso, mas porque você cria o solo fértil para isso. Você é uma força multiplicadora invisível.",
        "shadow": "A auto-negligência e o martírio são seus sabotadores. Você pode passar a vida inteira cuidando de todos e esquecendo de si mesmo. A dificuldade de receber cuidado e de estabelecer limites pode criar ressentimento acumulado.",
        "financial": "Perfil conservador-generoso. Você tende a gastar mais com outros do que consigo mesmo. Risco de decisões financeiras movidas por culpa ou obrigação. Potencial enorme de acumulação se aprender a priorizar a própria estabilidade primeiro.",
        "love": "Você é o parceiro mais sustentador e presente. Compatível com O Herói (que precisa de apoio) e O Rebelde (que precisa de ancoragem). Precisa de um parceiro que também saiba cuidar.",
        "career": ["Médico / Enfermeiro", "Psicólogo / Assistente Social", "Professor", "RH / Desenvolvimento Humano", "Líder Comunitário"],
        "talent": "Criação de ambientes de crescimento — você transforma grupos em comunidades e equipes em famílias.",
        "evolution": ["Pratique dizer não como ato de amor", "Invista em si mesmo com a mesma generosidade que investe nos outros", "Identifique a diferença entre cuidar e controlar", "Receba ajuda — é um ato de coragem, não de fraqueza"],
        "compatible": ["O Governante", "O Herói", "O Amante"],
        "traits": {"Liderança": 61, "Criatividade": 67, "Inteligência Estratégica": 64, "Influência Social": 88, "Coragem": 55, "Adaptabilidade": 83},
        "color": "#3498db",
    },
    "O Inocente": {
        "symbol": "○",
        "rarity": 13.7,
        "tagline": "A fé que move montanhas e enxerga beleza onde outros não veem",
        "description": "Você possui uma qualidade rara no mundo contemporâneo: a capacidade de manter esperança genuína. Você acredita que as coisas podem ser melhores — e essa crença não é ingenuidade, é uma forma de inteligência adaptativa. Sua visão de mundo cria realidades mais positivas ao redor de você.",
        "shadow": "A negação da sombra e o choque com a realidade são seus maiores riscos. Você pode evitar conflitos necessários e aceitar situações nocivas por querer acreditar no melhor. A decepção pode ser devastadora quando a realidade contradiz sua visão.",
        "financial": "Perfil otimista-inconsistente. Você tende a acreditar que vai dar certo sem fazer o planejamento necessário. Risco de ser explorado em transações financeiras. Enorme potencial quando combina otimismo com assessoria estruturada.",
        "love": "Você oferece amor incondicional — o mais raro de todos. Compatível com O Mago (que despertará sua profundidade) e O Governante (que proverá estabilidade). Cuidado com idealização de parceiros.",
        "career": ["Educador / Pedagogo", "Voluntário / Ativista Social", "Animador / Entretenimento Infantil", "Comunicador / Jornalista Positivo", "Empreendedor Social"],
        "talent": "Inspiração autêntica — sua presença faz as pessoas acreditarem em si mesmas novamente.",
        "evolution": ["Desenvolva visão realista sem perder o otimismo", "Aprenda a identificar e nomear dinâmicas nocivas", "Construa limites como proteção da sua luz interior", "Combine fé com plano de ação concreto"],
        "compatible": ["O Cuidador", "O Sábio", "O Criador"],
        "traits": {"Liderança": 43, "Criatividade": 72, "Inteligência Estratégica": 52, "Influência Social": 81, "Coragem": 49, "Adaptabilidade": 91},
        "color": "#f39c12",
    },
    "O Fora da Lei": {
        "symbol": "⊕",
        "rarity": 3.9,
        "tagline": "A força que redefine o jogo quando as regras não servem mais",
        "description": "Você não apenas quebra regras — você as reescreve. Há em você uma inteligência de sobrevivência altamente calibrada que reconhece o que funciona e o que é mera aparência de funcionar. Você opera nas margens porque sabe que é lá onde a realidade não disfarçada reside.",
        "shadow": "A autossabotagem e a dificuldade com autoridade são seus riscos centrais. Você pode sabotar oportunidades genuínas por suspeita habitual. A lealdade excessiva a um código pessoal pode fechar portas que precisariam ser abertas.",
        "financial": "Perfil não convencional-estratégico. Você tende a criar riqueza de formas que outros não considerariam. Alto potencial de ganhos assimétricos. Risco de perda total por subestimar consequências sistêmicas de ações fora do padrão.",
        "love": "Você é intenso, magnético e desafiador. Compatível com O Rebelde e O Mago. Tende a testar parceiros continuamente — o que pode ser enriquecedor ou exaustivo.",
        "career": ["Empreendedor Serial", "Advogado Criminalista", "Negociador Internacional", "Agente de Inteligência", "Estrategista Político"],
        "talent": "Navegação em ambiguidade — você funciona melhor onde as regras são fluidas e o improviso é necessário.",
        "evolution": ["Canalize a energia anticonvencional em sistemas que você mesmo constrói", "Desenvolva confiança seletiva em vez de desconfiança universal", "Crie um código pessoal que alinhe liberdade e responsabilidade", "Construa legado — não apenas conquistas individuais"],
        "compatible": ["O Rebelde", "O Explorador", "O Mago"],
        "traits": {"Liderança": 76, "Criatividade": 82, "Inteligência Estratégica": 87, "Influência Social": 79, "Coragem": 93, "Adaptabilidade": 91},
        "color": "#e67e22",
    },
    "O Visionário": {
        "symbol": "⋆",
        "rarity": 2.8,
        "tagline": "Aquele que vive no futuro e volta para contar",
        "description": "Você possui o perfil mais raro desta análise. Seu processamento temporal é fundamentalmente diferente — enquanto a maioria vive no presente ou no passado, você habita o futuro. Você não planeja o que pode acontecer, você percebe o que inevitavelmente acontecerá e age a partir dessa percepção.",
        "shadow": "O isolamento e a impaciência com o presente são suas sombras mais profundas. Você pode se tornar tão focado no que será que se desconecta do que é — e das pessoas que habitam o presente ao seu redor.",
        "financial": "Perfil visionário-antecipador. Você tende a identificar tendências muito antes do mainstream. Risco de entrada prematura em ciclos. Quando a execução acompanha a visão, potencial de retornos excepcionais.",
        "love": "Você precisa de um parceiro que confie em você mesmo sem ver o que você vê. Compatível com O Cuidador (ancoragem no presente) e O Sábio (compreensão intelectual da visão).",
        "career": ["Futurista / Consultor de Tendências", "Fundador de Tecnologia", "Cientista / Pesquisador de Fronteira", "Investidor Anjo", "Diretor de Inovação"],
        "talent": "Percepção de futuros emergentes — você não prevê tendências, você as percebe antes que existam.",
        "evolution": ["Desenvolva paciência como competência estratégica", "Construa pontes entre sua visão e a realidade atual das pessoas", "Documente sua visão sistematicamente — ela tem valor imenso", "Cerque-se de executores que transformem visão em realidade"],
        "compatible": ["O Mago", "O Criador", "O Sábio"],
        "traits": {"Liderança": 84, "Criatividade": 95, "Inteligência Estratégica": 92, "Influência Social": 79, "Coragem": 86, "Adaptabilidade": 83},
        "color": "#16a085",
    },
}

# ─────────────────────────────────────────────
#  QUESTIONS
# ─────────────────────────────────────────────
QUESTIONS = [
    {
        "text": "Quando você precisa tomar uma decisão importante com pouca informação disponível, qual é sua reação mais honesta?",
        "options": [
            ("Busco mais dados antes de qualquer movimento — decisões sem base são imprudentes.", {"O Sábio": 3, "O Governante": 2}),
            ("Confio no meu instinto. O momento certo pede ação, não análise infinita.", {"O Herói": 3, "O Rebelde": 2}),
            ("Imagino o cenário daqui a 10 anos e trabalho de trás pra frente.", {"O Visionário": 3, "O Mago": 2}),
            ("Converso com pessoas de confiança — decisões coletivas são mais robustas.", {"O Cuidador": 3, "O Amante": 2}),
        ],
    },
    {
        "text": "Como você descreveria sua relação com poder e autoridade?",
        "options": [
            ("Quero ocupar posições de liderança — é onde posso causar maior impacto.", {"O Governante": 3, "O Herói": 2}),
            ("Prefiro influenciar do que comandar — poder formal me interessa pouco.", {"O Mago": 3, "O Visionário": 2}),
            ("Resisto naturalmente a hierarquias que não me parecem legítimas.", {"O Rebelde": 3, "O Fora da Lei": 2}),
            ("Tenho poder quando sei de algo que os outros não sabem.", {"O Sábio": 3, "O Criador": 2}),
        ],
    },
    {
        "text": "Em um projeto colaborativo, qual papel você naturalmente assume?",
        "options": [
            ("O estrategista — defino a direção e os critérios de sucesso.", {"O Sábio": 3, "O Governante": 2}),
            ("O executor — prefiro fazer do que planejar.", {"O Herói": 3, "O Explorador": 2}),
            ("O criativo — gero ideias que ninguém estava considerando.", {"O Criador": 3, "O Mago": 2}),
            ("O conector — facilito a relação entre as pessoas e os talentos.", {"O Cuidador": 3, "O Amante": 2}),
        ],
    },
    {
        "text": "Quando você pensa no dinheiro, qual pensamento surge de forma mais espontânea?",
        "options": [
            ("É um instrumento de liberdade — quanto mais, mais opções tenho.", {"O Explorador": 3, "O Fora da Lei": 2}),
            ("É um indicador de valor entregue — consequência natural do trabalho bem feito.", {"O Herói": 3, "O Governante": 2}),
            ("É um recurso para criar e impactar — não é um fim em si mesmo.", {"O Criador": 3, "O Visionário": 2}),
            ("É um meio de cuidar de quem amo — minha segurança vem de sentir que outros estão bem.", {"O Cuidador": 3, "O Inocente": 2}),
        ],
    },
    {
        "text": "Qual afirmação descreve melhor como você processa emoções difíceis?",
        "options": [
            ("Analiso racionalmente o que causou a emoção e desenvolvo um plano de resposta.", {"O Sábio": 3, "O Governante": 2}),
            ("Uso a tensão emocional como combustível para ação e superação.", {"O Herói": 3, "O Rebelde": 2}),
            ("Mergulho na emoção — sinto profundamente antes de processar.", {"O Amante": 3, "O Cuidador": 2}),
            ("Transformo a experiência em algo criativo, artístico ou simbólico.", {"O Criador": 3, "O Mago": 2}),
        ],
    },
    {
        "text": "O que é mais perturbador para você em um ambiente profissional?",
        "options": [
            ("Falta de lógica e decisões arbitrárias sem embasamento.", {"O Sábio": 3, "O Governante": 2}),
            ("Mediocridade aceita como padrão e falta de ambição coletiva.", {"O Herói": 3, "O Visionário": 2}),
            ("Burocracia que sufoca criatividade e impossibilita inovação.", {"O Criador": 3, "O Rebelde": 2}),
            ("Frieza nas relações e falta de cuidado com as pessoas.", {"O Cuidador": 3, "O Amante": 2}),
        ],
    },
    {
        "text": "Como você tipicamente reage diante de uma regra que considera injusta ou ineficiente?",
        "options": [
            ("Documento evidências e apresento uma proposta de mudança estruturada.", {"O Sábio": 3, "O Governante": 2}),
            ("Ignoro silenciosamente e faço do meu jeito — o resultado justifica.", {"O Fora da Lei": 3, "O Herói": 2}),
            ("Confronto abertamente — aceitar o inaceitável não é uma opção.", {"O Rebelde": 3, "O Herói": 2}),
            ("Busco alternativas criativas que resolvam o problema real por trás da regra.", {"O Mago": 3, "O Criador": 2}),
        ],
    },
    {
        "text": "Qual é a sua visão mais honesta sobre relacionamentos íntimos?",
        "options": [
            ("São parcerias estratégicas — admiração mútua e metas compartilhadas são essenciais.", {"O Governante": 3, "O Sábio": 2}),
            ("São aventuras — preciso de alguém que também queira explorar e crescer.", {"O Explorador": 3, "O Rebelde": 2}),
            ("São minha fonte mais profunda de sentido — conexão é tudo.", {"O Amante": 3, "O Cuidador": 2}),
            ("São laboratórios de transformação — crescemos juntos ou não há sentido.", {"O Mago": 3, "O Visionário": 2}),
        ],
    },
    {
        "text": "O que as pessoas ao seu redor mais frequentemente dizem sobre você?",
        "options": [
            ("Que sou confiável, organizado e que entregas o que prometo.", {"O Governante": 3, "O Herói": 2}),
            ("Que sou intenso, profundo e que minha presença marca.", {"O Mago": 3, "O Amante": 2}),
            ("Que tenho ideias fora do comum e uma visão que impressiona.", {"O Visionário": 3, "O Criador": 2}),
            ("Que faço as pessoas se sentirem vistas, ouvidas e cuidadas.", {"O Cuidador": 3, "O Inocente": 2}),
        ],
    },
    {
        "text": "Quando você imagina seu legado daqui a 30 anos, o que mais importa para você?",
        "options": [
            ("Uma obra — algo que criei e que existe independentemente de mim.", {"O Criador": 3, "O Mago": 2}),
            ("Um sistema — uma organização, método ou estrutura que continua funcionando.", {"O Governante": 3, "O Sábio": 2}),
            ("Pessoas que transformei — indivíduos cuja vida foi diferente por conta do meu impacto.", {"O Cuidador": 3, "O Herói": 2}),
            ("Uma ideia — um pensamento que mudou a forma como o mundo entende algo.", {"O Visionário": 3, "O Rebelde": 2}),
        ],
    },
    {
        "text": "Qual tipo de risco você está mais disposto a assumir?",
        "options": [
            ("Risco calculado com análise profunda de downside e upside.", {"O Sábio": 3, "O Governante": 2}),
            ("Risco físico ou competitivo — o desafio em si é o atrativo.", {"O Herói": 3, "O Explorador": 2}),
            ("Risco criativo — compartilhar algo genuinamente meu com o mundo.", {"O Criador": 3, "O Amante": 2}),
            ("Risco sistêmico — desafiar estruturas estabelecidas por princípio.", {"O Rebelde": 3, "O Fora da Lei": 2}),
        ],
    },
    {
        "text": "Como você aprende melhor e mais profundamente?",
        "options": [
            ("Estudo sistemático, leitura densa, construção de frameworks mentais.", {"O Sábio": 3, "O Visionário": 2}),
            ("Experimentação direta — errando, ajustando e tentando novamente.", {"O Herói": 3, "O Explorador": 2}),
            ("Pela relação com outras pessoas — conversas profundas e observação humana.", {"O Amante": 3, "O Cuidador": 2}),
            ("Pela imersão em experiências radicalmente diferentes.", {"O Explorador": 3, "O Rebelde": 2}),
        ],
    },
    {
        "text": "Qual cenário te provoca maior satisfação interior?",
        "options": [
            ("Resolver um problema complexo que outros desistiram de resolver.", {"O Sábio": 3, "O Herói": 2}),
            ("Criar algo do zero que não existia antes e ver funcionar.", {"O Criador": 3, "O Mago": 2}),
            ("Perceber que alguém cresceu ou foi transformado pela sua influência.", {"O Cuidador": 3, "O Mago": 2}),
            ("Superar um limite que você mesmo achava que não conseguiria superar.", {"O Herói": 3, "O Rebelde": 2}),
        ],
    },
    {
        "text": "Sua relação com solidão é melhor descrita como:",
        "options": [
            ("Solidão é combustível — é quando meu melhor trabalho acontece.", {"O Sábio": 3, "O Criador": 2}),
            ("Tolero bem, mas preciso de missões — solidão sem propósito é angústia.", {"O Herói": 3, "O Governante": 2}),
            ("Sinto falta das pessoas rapidamente — conecto-me melhor em relação.", {"O Amante": 3, "O Cuidador": 2}),
            ("É liberdade — o espaço onde posso ser completamente eu mesmo.", {"O Explorador": 3, "O Fora da Lei": 2}),
        ],
    },
    {
        "text": "Como você lida com o fracasso?",
        "options": [
            ("Analiso o que deu errado com frieza e extraio aprendizados sistemáticos.", {"O Sábio": 3, "O Governante": 2}),
            ("Levanto mais rápido — o fracasso é uma informação, não uma identidade.", {"O Herói": 3, "O Explorador": 2}),
            ("Sinto profundamente, processo emocionalmente e então sigo.", {"O Amante": 3, "O Inocente": 2}),
            ("Vejo como confirmação de que o sistema precisa ser questionado.", {"O Rebelde": 3, "O Fora da Lei": 2}),
        ],
    },
    {
        "text": "Em situações de conflito, qual é sua resposta mais natural?",
        "options": [
            ("Busco a posição racionalmente correta e a defendo com lógica.", {"O Sábio": 3, "O Governante": 2}),
            ("Confronto diretamente — evitar conflito não resolve, apenas adia.", {"O Herói": 3, "O Rebelde": 2}),
            ("Busco mediação e entendimento do ponto de vista do outro.", {"O Cuidador": 3, "O Amante": 2}),
            ("Uso o conflito como oportunidade de reposicionamento estratégico.", {"O Fora da Lei": 3, "O Mago": 2}),
        ],
    },
    {
        "text": "O que te impede de agir mais frequentemente do que gostaria?",
        "options": [
            ("A necessidade de mais informação — quero ter certeza antes de me comprometer.", {"O Sábio": 3, "O Governante": 2}),
            ("O medo do julgamento — o que vão pensar sobre minha criação ou posição.", {"O Criador": 3, "O Inocente": 2}),
            ("A resistência interna ao comprometimento — quero manter opções abertas.", {"O Explorador": 3, "O Rebelde": 2}),
            ("Honestamente? Quase nada. Quando vejo o momento, eu ajo.", {"O Herói": 3, "O Fora da Lei": 2}),
        ],
    },
    {
        "text": "Qual dessas habilidades você desenvolveria primeiro se pudesse escolher?",
        "options": [
            ("Pensamento sistêmico avançado e capacidade analítica profunda.", {"O Sábio": 3, "O Visionário": 2}),
            ("Liderança inspiracional e capacidade de mobilizar pessoas.", {"O Herói": 3, "O Governante": 2}),
            ("Expressão criativa e habilidades artísticas de nível profissional.", {"O Criador": 3, "O Amante": 2}),
            ("Visão estratégica de longo prazo e capacidade antecipatória.", {"O Visionário": 3, "O Mago": 2}),
        ],
    },
    {
        "text": "Qual é a sua relação com convenções sociais e expectativas externas?",
        "options": [
            ("As sigo quando fazem sentido — são contratos sociais úteis.", {"O Governante": 3, "O Sábio": 2}),
            ("As questiono sempre — muitas convenções existem para perpetuar estruturas inadequadas.", {"O Rebelde": 3, "O Fora da Lei": 2}),
            ("As adapto criativamente — uso as formas existentes para criar algo novo.", {"O Criador": 3, "O Mago": 2}),
            ("Sigo o que me parece genuíno — convenções que não refletem quem sou me sufocam.", {"O Explorador": 3, "O Amante": 2}),
        ],
    },
    {
        "text": "O que é integridade para você, na prática?",
        "options": [
            ("Consistência entre valores declarados e ações — fazer o que diz.", {"O Governante": 3, "O Herói": 2}),
            ("Honestidade radical, mesmo quando desconfortável.", {"O Rebelde": 3, "O Sábio": 2}),
            ("Presença e cuidado genuíno com as pessoas ao meu redor.", {"O Cuidador": 3, "O Amante": 2}),
            ("Fidelidade à minha visão, mesmo contra a pressão do ambiente.", {"O Visionário": 3, "O Criador": 2}),
        ],
    },
    {
        "text": "Em que tipo de ambiente você performa melhor?",
        "options": [
            ("Ambientes estruturados com clareza de objetivos e recursos adequados.", {"O Governante": 3, "O Sábio": 2}),
            ("Alta pressão, desafios crescentes e entregas de alto impacto.", {"O Herói": 3, "O Fora da Lei": 2}),
            ("Espaços criativos sem limites rígidos de formato ou processo.", {"O Criador": 3, "O Explorador": 2}),
            ("Contextos relacionais onde o trabalho é essencialmente humano.", {"O Cuidador": 3, "O Amante": 2}),
        ],
    },
    {
        "text": "Qual é o seu maior driver de motivação no trabalho?",
        "options": [
            ("Autonomia e liberdade para fazer do meu jeito.", {"O Explorador": 3, "O Criador": 2}),
            ("Impacto mensurável — saber que o que faço realmente muda algo.", {"O Herói": 3, "O Governante": 2}),
            ("Maestria — ser reconhecidamente excelente no que escolhi.", {"O Sábio": 3, "O Herói": 2}),
            ("Propósito — sentir que o trabalho está alinhado com algo maior.", {"O Visionário": 3, "O Mago": 2}),
        ],
    },
    {
        "text": "Como você age quando percebe que alguém próximo está passando por dificuldades?",
        "options": [
            ("Ofereço análise e soluções concretas — ajudo de forma prática.", {"O Sábio": 2, "O Governante": 2}),
            ("Fico presente, escuto profundamente e ofereço suporte emocional.", {"O Cuidador": 3, "O Amante": 2}),
            ("Inspiro a pessoa a ver o problema de uma perspectiva diferente.", {"O Mago": 3, "O Visionário": 2}),
            ("Mobilizo recursos e ação — problemas pedem soluções, não apenas empatia.", {"O Herói": 3, "O Governante": 2}),
        ],
    },
    {
        "text": "Qual é a sua relação com o status quo e com mudança?",
        "options": [
            ("Mudo o que precisa ser mudado com base em evidência, não em impulso.", {"O Sábio": 3, "O Governante": 2}),
            ("A mudança é meu elemento natural — estagnação me sufoca.", {"O Explorador": 3, "O Rebelde": 2}),
            ("Questiono o que existe não por maldade, mas por ver claramente o que poderia ser.", {"O Visionário": 3, "O Criador": 2}),
            ("Mudo quando o que existe deixa de servir às pessoas — esse é o critério.", {"O Cuidador": 3, "O Mago": 2}),
        ],
    },
    {
        "text": "Qual é o seu maior medo genuíno?",
        "options": [
            ("Ser irrelevante — não deixar nenhuma marca real no mundo.", {"O Herói": 3, "O Governante": 2}),
            ("Ser incompreendido — ter uma visão que ninguém consegue enxergar.", {"O Visionário": 3, "O Criador": 2}),
            ("Perder vínculos importantes — ficar sem as conexões que me definem.", {"O Amante": 3, "O Cuidador": 2}),
            ("Ser controlado — perder a liberdade de agir de acordo com minha própria lógica.", {"O Rebelde": 3, "O Fora da Lei": 2}),
        ],
    },
]


# ─────────────────────────────────────────────
#  SESSION STATE INIT
# ─────────────────────────────────────────────
def init_state():
    defaults = {
        "screen": "cover",
        "name": "",
        "age": "",
        "gender": "",
        "answers": {},
        "scores": {},
        "primary": None,
        "secondary": None,
        "shadow": None,
        "paid": False,
        "potential_index": 0,
        "rarity_pct": 0.0,
        "current_q": 0,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
def gold(text, size="1rem", weight=400):
    return f'<span style="color:#d4af37;font-size:{size};font-weight:{weight};">{text}</span>'

def dim(text, size="0.82rem"):
    return f'<span style="color:#7d8590;font-size:{size};">{text}</span>'

def eyebrow(text):
    return f'<div class="section-eyebrow">{text}</div>'

def divider():
    st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

def glass(content_html):
    st.markdown(f'<div class="glass-card">{content_html}</div>', unsafe_allow_html=True)

def go_to(screen):
    st.session_state["screen"] = screen
    st.rerun()


# ─────────────────────────────────────────────
#  SCORE ENGINE
# ─────────────────────────────────────────────
def compute_scores():
    scores = {k: 0 for k in ARCHETYPES}
    for q_idx, choice_idx in st.session_state["answers"].items():
        q = QUESTIONS[q_idx]
        _, weights = q["options"][choice_idx]
        for arch, pts in weights.items():
            if arch in scores:
                scores[arch] += pts

    # Add small randomisation for personality diversity
    for k in scores:
        scores[k] += random.uniform(0, 1.5)

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    st.session_state["scores"] = scores
    st.session_state["primary"] = sorted_scores[0][0]
    st.session_state["secondary"] = sorted_scores[1][0]
    # Shadow = weakest archetype
    st.session_state["shadow"] = sorted_scores[-1][0]

    p_arch = ARCHETYPES[sorted_scores[0][0]]
    base = (sorted_scores[0][1] / (len(QUESTIONS) * 3)) * 100
    idx = min(98, max(62, int(base * 0.6 + sum(p_arch["traits"].values()) / 6 * 0.4)))
    st.session_state["potential_index"] = idx
    st.session_state["rarity_pct"] = ARCHETYPES[st.session_state["primary"]]["rarity"]


# ─────────────────────────────────────────────
#  RADAR CHART
# ─────────────────────────────────────────────
def make_radar(traits: dict, color: str = "#d4af37", title: str = ""):
    cats = list(traits.keys())
    vals = list(traits.values())
    cats_closed = cats + [cats[0]]
    vals_closed = vals + [vals[0]]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=vals_closed,
        theta=cats_closed,
        fill='toself',
        fillcolor=color.replace(")", ",0.15)").replace("rgb", "rgba") if "rgb" in color else color + "26",
        line=dict(color=color, width=2),
        marker=dict(color=color, size=5),
        name="Perfil",
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(color="#7d8590", size=9),
                gridcolor="#21262d",
                linecolor="#21262d",
            ),
            angularaxis=dict(
                tickfont=dict(color="#c9ced8", size=10, family="Space Grotesk"),
                gridcolor="#21262d",
                linecolor="#21262d",
            ),
            bgcolor="#0d1117",
        ),
        paper_bgcolor="#0d1117",
        plot_bgcolor="#0d1117",
        showlegend=False,
        title=dict(text=title, font=dict(color="#d4af37", size=12, family="Space Grotesk"), x=0.5) if title else None,
        margin=dict(l=30, r=30, t=30 if not title else 50, b=30),
        height=340,
    )
    return fig


def make_gauge(value: int, color: str = "#d4af37"):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={"x": [0, 1], "y": [0, 1]},
        number={"font": {"color": color, "size": 42, "family": "Cormorant Garamond"}, "suffix": ""},
        gauge={
            "axis": {"range": [0, 100], "tickwidth": 0, "tickcolor": "#21262d", "tickfont": {"color": "#7d8590", "size": 9}},
            "bar": {"color": color, "thickness": 0.25},
            "bgcolor": "#161b22",
            "borderwidth": 0,
            "steps": [
                {"range": [0, 33], "color": "#161b22"},
                {"range": [33, 66], "color": "#1a1f2e"},
                {"range": [66, 100], "color": "#21262d"},
            ],
            "threshold": {"line": {"color": color, "width": 3}, "thickness": 0.8, "value": value},
        },
    ))
    fig.update_layout(
        paper_bgcolor="#0d1117",
        plot_bgcolor="#0d1117",
        height=220,
        margin=dict(l=20, r=20, t=10, b=10),
        font=dict(color="#f0f1f3"),
    )
    return fig


# ─────────────────────────────────────────────
#  PDF GENERATION
# ─────────────────────────────────────────────
def generate_pdf_bytes() -> bytes:
    """Generate a premium PDF report using ReportLab."""
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import cm
        from reportlab.platypus import (
            SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
            HRFlowable, PageBreak,
        )
        from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
        from reportlab.pdfgen import canvas
        from io import BytesIO

        primary = st.session_state["primary"]
        secondary = st.session_state["secondary"]
        shadow = st.session_state["shadow"]
        arch = ARCHETYPES[primary]
        arch2 = ARCHETYPES[secondary]
        arch_s = ARCHETYPES[shadow]
        name = st.session_state["name"] or "Usuário"
        idx = st.session_state["potential_index"]
        rarity = st.session_state["rarity_pct"]
        now = datetime.now().strftime("%d/%m/%Y")

        GOLD = colors.HexColor("#d4af37")
        BLACK = colors.HexColor("#0a0c0f")
        DARK = colors.HexColor("#161b22")
        GRAY = colors.HexColor("#7d8590")
        WHITE = colors.HexColor("#f0f1f3")
        WHITE2 = colors.HexColor("#c9ced8")

        buf = BytesIO()
        doc = SimpleDocTemplate(
            buf,
            pagesize=A4,
            leftMargin=2*cm, rightMargin=2*cm,
            topMargin=2*cm, bottomMargin=2*cm,
            title=f"AuraDex — Dossiê {name}",
        )

        styles = getSampleStyleSheet()

        def sty(name_s, **kwargs):
            return ParagraphStyle(name_s, **{"fontName": "Helvetica", "textColor": WHITE, "fontSize": 10, "leading": 16, **kwargs})

        S = {
            "cover_title": sty("ct", fontName="Helvetica-Bold", fontSize=32, textColor=GOLD, leading=38, alignment=TA_CENTER),
            "cover_sub": sty("cs", fontSize=13, textColor=WHITE2, leading=20, alignment=TA_CENTER),
            "eyebrow": sty("ey", fontSize=7, textColor=GOLD, leading=10, fontName="Helvetica-Bold", spaceAfter=4),
            "h1": sty("h1", fontName="Helvetica-Bold", fontSize=22, textColor=GOLD, leading=28, spaceBefore=12, spaceAfter=6),
            "h2": sty("h2", fontName="Helvetica-Bold", fontSize=15, textColor=WHITE, leading=20, spaceBefore=10, spaceAfter=5),
            "body": sty("bd", fontSize=10, textColor=WHITE2, leading=17, spaceAfter=8),
            "small": sty("sm", fontSize=8, textColor=GRAY, leading=13),
            "gold_stat": sty("gs", fontName="Helvetica-Bold", fontSize=12, textColor=GOLD, leading=18),
            "center": sty("cen", fontSize=10, textColor=WHITE2, leading=16, alignment=TA_CENTER),
            "tag": sty("tg", fontSize=9, textColor=GOLD, leading=14, fontName="Helvetica-Bold"),
        }

        def hr():
            return HRFlowable(width="100%", thickness=0.5, color=GOLD, spaceAfter=12, spaceBefore=12)

        def section(label, title):
            return [
                Spacer(1, 0.3*cm),
                Paragraph(label.upper(), S["eyebrow"]),
                Paragraph(title, S["h1"]),
                hr(),
            ]

        story = []

        # ── COVER PAGE ──
        story += [
            Spacer(1, 3*cm),
            Paragraph("◈  AURADEX", sty("logo", fontName="Helvetica-Bold", fontSize=11, textColor=GOLD, alignment=TA_CENTER, letterSpacing=6)),
            Spacer(1, 0.5*cm),
            Paragraph("DOSSIÊ ARQUÉTIPO SUPREMO", S["cover_title"]),
            Spacer(1, 0.4*cm),
            Paragraph("Relatório de Inteligência Comportamental", S["cover_sub"]),
            Spacer(1, 2.5*cm),
        ]

        cover_data = [
            ["ANALISADO", name],
            ["ARQUÉTIPO PRINCIPAL", primary],
            ["ÍNDICE DE POTENCIAL", f"{idx}/100"],
            ["RARIDADE DO PERFIL", f"Top {rarity}% da população"],
            ["DATA DO RELATÓRIO", now],
            ["VERSÃO", "Supremo Premium"],
        ]
        cover_table = Table(cover_data, colWidths=[5.5*cm, 10*cm])
        cover_table.setStyle(TableStyle([
            ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
            ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("TEXTCOLOR", (0, 0), (0, -1), GOLD),
            ("TEXTCOLOR", (1, 0), (1, -1), WHITE2),
            ("BACKGROUND", (0, 0), (-1, -1), DARK),
            ("ROWBACKGROUNDS", (0, 0), (-1, -1), [DARK, colors.HexColor("#1a1f2e")]),
            ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#21262d")),
            ("PADDING", (0, 0), (-1, -1), 9),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ]))
        story += [cover_table, Spacer(1, 3*cm)]
        story.append(Paragraph("Este relatório é de uso pessoal e exclusivo. Gerado por Inteligência Artificial Comportamental AuraDex.", S["small"]))
        story.append(PageBreak())

        # ── ÍNDICE ──
        story += section("Sumário", "Índice do Relatório")
        index_items = [
            "1. Índice Geral de Potencial",
            "2. Arquétipo Principal",
            "3. Arquétipo Secundário",
            "4. Arquétipo Sombra",
            "5. Perfil Financeiro",
            "6. Perfil Amoroso",
            "7. Perfil de Carreira",
            "8. Talento Oculto",
            "9. Plano de Evolução",
            "10. Radar Comportamental",
            "11. Compatibilidades",
            "12. Certificado de Raridade",
        ]
        for item in index_items:
            story.append(Paragraph(item, S["body"]))
        story.append(PageBreak())

        # ── POTENCIAL ──
        story += section("Diagnóstico Geral", "Índice Geral de Potencial")
        story.append(Paragraph(f"Score: {idx} / 100", sty("sc", fontName="Helvetica-Bold", fontSize=28, textColor=GOLD, alignment=TA_CENTER)))
        story.append(Spacer(1, 0.3*cm))
        story.append(Paragraph(
            f"Este índice representa a síntese de todos os vetores comportamentais identificados na análise de {name}. "
            "Combina inteligência estratégica, potencial de liderança, criatividade operacional e resiliência adaptativa.",
            S["body"]
        ))

        trait_data = [["DIMENSÃO", "ÍNDICE", "NÍVEL"]] + [
            [k, f"{v}/100", "Alto" if v >= 80 else "Médio" if v >= 60 else "Desenvolvimento"]
            for k, v in arch["traits"].items()
        ]
        trait_table = Table(trait_data, colWidths=[6*cm, 3*cm, 5*cm])
        trait_table.setStyle(TableStyle([
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, -1), 9),
            ("TEXTCOLOR", (0, 0), (-1, 0), GOLD),
            ("TEXTCOLOR", (0, 1), (-1, -1), WHITE2),
            ("TEXTCOLOR", (1, 1), (1, -1), GOLD),
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#21262d")),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [DARK, colors.HexColor("#1a1f2e")]),
            ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#21262d")),
            ("PADDING", (0, 0), (-1, -1), 8),
            ("ALIGN", (1, 0), (1, -1), "CENTER"),
        ]))
        story += [Spacer(1, 0.5*cm), trait_table, PageBreak()]

        # ── ARQUÉTIPO PRINCIPAL ──
        story += section("Arquétipo Principal", primary)
        story.append(Paragraph(arch["symbol"] + "  " + arch["tagline"], S["gold_stat"]))
        story.append(Spacer(1, 0.3*cm))
        story.append(Paragraph(arch["description"], S["body"]))
        story.append(PageBreak())

        # ── SECUNDÁRIO ──
        story += section("Arquétipo Secundário", secondary)
        story.append(Paragraph(arch2["symbol"] + "  " + arch2["tagline"], S["gold_stat"]))
        story.append(Spacer(1, 0.3*cm))
        story.append(Paragraph(arch2["description"], S["body"]))
        story.append(PageBreak())

        # ── SOMBRA ──
        story += section("Arquétipo Sombra", shadow)
        story.append(Paragraph(
            "O arquétipo sombra representa os padrões de comportamento reprimidos ou não integrados. "
            "Conhecer sua sombra é o ato mais avançado de autoconhecimento.", S["body"]
        ))
        story.append(Paragraph(arch_s["shadow"], S["body"]))
        story.append(PageBreak())

        # ── FINANCEIRO ──
        story += section("Perfil Financeiro", "Inteligência Monetária")
        story.append(Paragraph(arch["financial"], S["body"]))
        story.append(PageBreak())

        # ── AMOROSO ──
        story += section("Perfil Amoroso", "Padrões de Conexão")
        story.append(Paragraph(arch["love"], S["body"]))
        story.append(PageBreak())

        # ── CARREIRA ──
        story += section("Perfil de Carreira", "Vocação e Potencial Profissional")
        story.append(Paragraph("Carreiras com maior alinhamento arquetípico:", S["body"]))
        for c in arch["career"]:
            story.append(Paragraph(f"◆  {c}", S["tag"]))
        story.append(PageBreak())

        # ── TALENTO OCULTO ──
        story += section("Talento Oculto", "O Dom Ainda Não Explorado")
        story.append(Paragraph(arch["talent"], sty("tl", fontName="Helvetica-Bold", fontSize=12, textColor=WHITE, leading=20)))
        story.append(PageBreak())

        # ── PLANO DE EVOLUÇÃO ──
        story += section("Plano de Evolução", "Próximos Passos")
        for i, step in enumerate(arch["evolution"], 1):
            story.append(Paragraph(f"{i}.  {step}", S["body"]))
        story.append(PageBreak())

        # ── COMPATIBILIDADES ──
        story += section("Compatibilidades", "Mapa de Conexões Arquetípicas")
        story.append(Paragraph("Arquétipos com maior sinergia:", S["body"]))
        for c in arch["compatible"]:
            a = ARCHETYPES[c]
            story.append(Paragraph(f"{a['symbol']}  {c} — {a['tagline']}", S["gold_stat"]))
            story.append(Spacer(1, 0.15*cm))
        story.append(PageBreak())

        # ── CERTIFICADO ──
        story.append(Spacer(1, 2*cm))
        story.append(Paragraph("◈  AURADEX · CERTIFICADO DE RARIDADE", sty("cert_h", fontName="Helvetica-Bold", fontSize=10, textColor=GOLD, alignment=TA_CENTER, letterSpacing=4)))
        story.append(Spacer(1, 1*cm))
        story.append(Paragraph(name, sty("cert_name", fontName="Helvetica-Bold", fontSize=26, textColor=WHITE, alignment=TA_CENTER)))
        story.append(Spacer(1, 0.5*cm))
        story.append(Paragraph(
            f"possui o arquétipo <b>{primary}</b>, identificado em apenas <b>{rarity}%</b> da população analisada.",
            sty("cert_body", fontSize=11, textColor=WHITE2, alignment=TA_CENTER, leading=20)
        ))
        story.append(Spacer(1, 0.5*cm))
        story.append(Paragraph(f"Índice de Potencial: {idx}/100", sty("cert_idx", fontName="Helvetica-Bold", fontSize=14, textColor=GOLD, alignment=TA_CENTER)))
        story.append(Spacer(1, 1.5*cm))
        story.append(Paragraph(f"Emitido em {now} por AuraDex Inteligência Comportamental", S["small"]))

        doc.build(story)
        return buf.getvalue()

    except ImportError:
        # Fallback minimal text PDF
        buf = io.BytesIO()
        buf.write(b"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj 2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj 3 0 obj<</Type/Page/MediaBox[0 0 595 842]/Parent 2 0 R>>endobj\nxref\n0 4\n0000000000 65535 f\n0000000009 00000 n\n0000000058 00000 n\n0000000115 00000 n\ntrailer<</Size 4/Root 1 0 R>>\nstartxref\n197\n%%EOF")
        return buf.getvalue()


# ═══════════════════════════════════════════════════════════════════
#
#  SCREENS
#
# ═══════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────
#  SCREEN 1: COVER
# ─────────────────────────────────────────────
def screen_cover():
    st.markdown("""
    <div style="text-align:center; padding: 2.5rem 0 1.5rem 0;">
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.65rem; font-weight:700;
                    letter-spacing:0.35em; text-transform:uppercase; color:#d4af37; margin-bottom:1.2rem;">
            ◈ &nbsp; A U R A D E X &nbsp; ◈
        </div>
        <h1 style="font-family:'Cormorant Garamond',serif !important; font-size:2.6rem; font-weight:700;
                   color:#f0f1f3; line-height:1.2; margin:0 0 1rem 0;">
            Apenas <span style="color:#d4af37;">4,7%</span> das pessoas<br>
            possuem um perfil tão raro<br>quanto o seu.
        </h1>
        <p style="font-family:'Space Grotesk',sans-serif; font-size:1rem; color:#c9ced8;
                  line-height:1.7; max-width:500px; margin:0 auto 2rem auto;">
            Descubra os padrões ocultos que influenciam suas decisões,<br>
            relacionamentos, dinheiro e destino.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Trust metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="text-align:center; padding:1rem; background:#161b22; border:1px solid #21262d; border-radius:6px;">
            <div style="font-family:'Cormorant Garamond',serif; font-size:1.8rem; font-weight:700; color:#d4af37;">25k+</div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.65rem; color:#7d8590; letter-spacing:0.1em; text-transform:uppercase; margin-top:0.2rem;">Perfis Analisados</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="text-align:center; padding:1rem; background:#161b22; border:1px solid #21262d; border-radius:6px;">
            <div style="font-family:'Cormorant Garamond',serif; font-size:1.8rem; font-weight:700; color:#d4af37;">93%</div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.65rem; color:#7d8590; letter-spacing:0.1em; text-transform:uppercase; margin-top:0.2rem;">Precisão Comportamental</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style="text-align:center; padding:1rem; background:#161b22; border:1px solid #21262d; border-radius:6px;">
            <div style="font-family:'Cormorant Garamond',serif; font-size:1.8rem; font-weight:700; color:#d4af37;">5 min</div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.65rem; color:#7d8590; letter-spacing:0.1em; text-transform:uppercase; margin-top:0.2rem;">Resultado Imediato</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    divider()
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin-bottom:1rem;">
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.72rem; color:#7d8590; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.5rem;">
            O que você vai descobrir
        </div>
    </div>""", unsafe_allow_html=True)

    features = [
        ("◆", "Arquétipo Principal", "O núcleo da sua personalidade e potencial"),
        ("✦", "Perfil Financeiro", "Seus padrões ocultos com dinheiro e prosperidade"),
        ("◈", "Perfil Amoroso", "Seus padrões de vínculo e compatibilidade"),
        ("⋆", "Talento Oculto", "O dom que ainda não foi plenamente ativado"),
        ("◎", "Plano de Evolução", "Próximos passos concretos para seu desenvolvimento"),
    ]
    for sym, title, desc in features:
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:0.85rem; padding:0.75rem 0;
                    border-bottom:1px solid #21262d;">
            <div style="color:#d4af37; font-size:1rem; min-width:1.5rem;">{sym}</div>
            <div>
                <div style="font-family:'Space Grotesk',sans-serif; font-size:0.88rem; font-weight:600; color:#f0f1f3;">{title}</div>
                <div style="font-family:'Space Grotesk',sans-serif; font-size:0.75rem; color:#7d8590; margin-top:0.1rem;">{desc}</div>
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("INICIAR ANÁLISE", key="btn_start"):
        go_to("identify")

    st.markdown("""
    <div style="text-align:center; margin-top:1.5rem;">
        <span style="font-family:'Space Grotesk',sans-serif; font-size:0.7rem; color:#7d8590;">
            Análise baseada em psicologia junguiana e modelos comportamentais contemporâneos.<br>
            Seus dados são processados com total privacidade.
        </span>
    </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  SCREEN 2: IDENTIFY
# ─────────────────────────────────────────────
def screen_identify():
    st.markdown("""
    <div style="text-align:center; padding:2rem 0 1.5rem 0;">
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.65rem; font-weight:700;
                    letter-spacing:0.3em; text-transform:uppercase; color:#d4af37; margin-bottom:0.75rem;">
            ◈ Etapa 1 de 3 — Identificação
        </div>
        <h2 style="font-family:'Cormorant Garamond',serif !important; font-size:2rem; font-weight:600;
                   color:#f0f1f3; margin:0 0 0.5rem 0;">
            Antes de começar
        </h2>
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.9rem; color:#7d8590;">
            Essas informações personalizam seu diagnóstico.
        </p>
    </div>""", unsafe_allow_html=True)

    divider()

    name = st.text_input("Seu nome", placeholder="Como você prefere ser chamado?", value=st.session_state["name"])
    age = st.text_input("Sua idade", placeholder="Ex: 28", value=st.session_state["age"])
    gender = st.selectbox("Identidade de gênero (opcional)", ["Prefiro não informar", "Masculino", "Feminino", "Não-binário", "Outro"])

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("COMEÇAR DIAGNÓSTICO", key="btn_identify"):
        if not name.strip():
            st.warning("Por favor, insira seu nome para continuar.")
        else:
            st.session_state["name"] = name.strip()
            st.session_state["age"] = age.strip()
            st.session_state["gender"] = gender
            st.session_state["current_q"] = 0
            st.session_state["answers"] = {}
            go_to("quiz")


# ─────────────────────────────────────────────
#  SCREEN 3: QUIZ
# ─────────────────────────────────────────────
def screen_quiz():
    total = len(QUESTIONS)
    current = st.session_state["current_q"]
    answered = len(st.session_state["answers"])
    progress = answered / total

    # Header
    st.markdown(f"""
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.65rem; font-weight:700;
                    letter-spacing:0.25em; text-transform:uppercase; color:#d4af37;">
            ◈ Diagnóstico Comportamental
        </div>
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.72rem; color:#7d8590;">
            {answered}/{total} respondidas
        </div>
    </div>""", unsafe_allow_html=True)

    st.progress(progress)
    st.markdown("<br>", unsafe_allow_html=True)

    if current >= total:
        # All answered — go to loading
        compute_scores()
        go_to("loading")
        return

    q = QUESTIONS[current]
    option_texts = [opt[0] for opt in q["options"]]

    st.markdown(f"""
    <div class="question-card">
        <div class="q-number">Pergunta {current + 1} de {total}</div>
        <div class="q-text">{q["text"]}</div>
    </div>""", unsafe_allow_html=True)

    choice = st.radio(
        "Selecione a opção que melhor representa você:",
        options=range(len(option_texts)),
        format_func=lambda i: option_texts[i],
        key=f"q_{current}",
        label_visibility="collapsed",
    )

    st.markdown("<br>", unsafe_allow_html=True)
    col_back, col_next = st.columns([1, 2])
    with col_back:
        if current > 0:
            if st.button("← Anterior", key="btn_prev"):
                st.session_state["current_q"] = current - 1
                st.rerun()
    with col_next:
        label = "PRÓXIMA →" if current < total - 1 else "VER RESULTADO →"
        if st.button(label, key="btn_next"):
            st.session_state["answers"][current] = choice
            if current < total - 1:
                st.session_state["current_q"] = current + 1
                st.rerun()
            else:
                compute_scores()
                go_to("loading")


# ─────────────────────────────────────────────
#  SCREEN 4: LOADING
# ─────────────────────────────────────────────
def screen_loading():
    st.markdown("""
    <div style="text-align:center; padding:3rem 0 2rem 0;">
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.65rem; font-weight:700;
                    letter-spacing:0.3em; text-transform:uppercase; color:#d4af37; margin-bottom:1rem;">
            ◈ Processando Análise
        </div>
        <h2 style="font-family:'Cormorant Garamond',serif !important; font-size:2.2rem; font-weight:600;
                   color:#f0f1f3; margin:0;">
            Seu perfil está sendo gerado
        </h2>
    </div>""", unsafe_allow_html=True)

    divider()

    steps = [
        ("Mapeando padrões cognitivos...", 0.18),
        ("Calculando perfil emocional...", 0.18),
        ("Detectando arquétipos secundários...", 0.18),
        ("Analisando tendências financeiras...", 0.18),
        ("Identificando talentos ocultos...", 0.14),
        ("Finalizando relatório supremo...", 0.14),
    ]

    progress_bar = st.progress(0)
    status_placeholder = st.empty()
    cumulative = 0.0

    for step_text, duration in steps:
        status_placeholder.markdown(f"""
        <div style="text-align:center; padding:1.5rem;">
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.88rem; color:#c9ced8; margin-bottom:0.5rem;">
                {step_text}
            </div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.7rem; color:#7d8590; letter-spacing:0.08em;">
                {int(cumulative * 100)}% concluído
            </div>
        </div>""", unsafe_allow_html=True)
        time.sleep(duration)
        cumulative = min(1.0, cumulative + (1 / len(steps)))
        progress_bar.progress(min(1.0, cumulative))

    progress_bar.progress(1.0)
    status_placeholder.markdown("""
    <div style="text-align:center; padding:1.5rem;">
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.88rem; color:#d4af37; margin-bottom:0.5rem;">
            ✓ Análise concluída com sucesso
        </div>
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.7rem; color:#7d8590; letter-spacing:0.08em;">
            100% concluído
        </div>
    </div>""", unsafe_allow_html=True)
    time.sleep(0.5)
    go_to("result_free")


# ─────────────────────────────────────────────
#  SCREEN 5: FREE RESULT
# ─────────────────────────────────────────────
def screen_result_free():
    primary = st.session_state["primary"]
    arch = ARCHETYPES[primary]
    name = st.session_state["name"]
    idx = st.session_state["potential_index"]
    rarity = st.session_state["rarity_pct"]

    st.markdown(f"""
    <div style="text-align:center; padding:2rem 0 1rem 0;">
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.65rem; font-weight:700;
                    letter-spacing:0.3em; text-transform:uppercase; color:#d4af37; margin-bottom:0.75rem;">
            ◈ Resultado da Análise — {name}
        </div>
        <div style="font-family:'Cormorant Garamond',serif; font-size:5rem; color:{arch['color']}; line-height:1; margin-bottom:0.5rem;">
            {arch['symbol']}
        </div>
        <h1 style="font-family:'Cormorant Garamond',serif !important; font-size:2.8rem; font-weight:700;
                   color:#d4af37; margin:0 0 0.35rem 0; line-height:1.1;">
            {primary}
        </h1>
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.9rem; color:#c9ced8; margin:0 auto;
                  max-width:420px; line-height:1.6;">
            {arch['tagline']}
        </p>
    </div>""", unsafe_allow_html=True)

    divider()

    # Rarity & Score
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div style="background:#161b22; border:1px solid #21262d; border-radius:6px; padding:1.25rem; text-align:center;">
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.65rem; color:#7d8590; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.5rem;">Raridade do Perfil</div>
            <div style="font-family:'Cormorant Garamond',serif; font-size:2.2rem; font-weight:700; color:#d4af37; line-height:1;">{rarity}%</div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.72rem; color:#7d8590; margin-top:0.25rem;">da população</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div style="background:#161b22; border:1px solid #21262d; border-radius:6px; padding:1.25rem; text-align:center;">
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.65rem; color:#7d8590; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.5rem;">Índice de Potencial</div>
            <div style="font-family:'Cormorant Garamond',serif; font-size:2.2rem; font-weight:700; color:#d4af37; line-height:1;">{idx}</div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.72rem; color:#7d8590; margin-top:0.25rem;">de 100</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Description
    st.markdown(f"""
    <div class="glass-card">
        <div class="section-eyebrow">Diagnóstico Principal</div>
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.88rem; color:#c9ced8; line-height:1.75; margin:0;">
            {arch['description']}
        </p>
    </div>""", unsafe_allow_html=True)

    divider()

    # Locked sections
    st.markdown("""
    <div style="margin-bottom:0.75rem;">
        <div class="section-eyebrow">Conteúdo do Relatório Completo</div>
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.82rem; color:#7d8590; margin:0.25rem 0 1rem 0;">
            Os itens abaixo estão incluídos no Dossiê Supremo.
        </p>
    </div>""", unsafe_allow_html=True)

    unlocked = [("◆", "Arquétipo Principal", True), ("◎", "Descrição Comportamental", True)]
    locked = [
        ("✦", "Arquétipo Secundário"),
        ("⊗", "Arquétipo Sombra"),
        ("◉", "Perfil Financeiro Completo"),
        ("◈", "Perfil Amoroso e Compatibilidades"),
        ("✶", "Talento Oculto"),
        ("⋆", "Plano de Evolução — 4 passos"),
        ("♛", "Radar Comportamental — 6 dimensões"),
        ("○", "Carreiras com Maior Alinhamento"),
        ("⊕", "PDF Premium para Download"),
    ]

    for sym, label in unlocked:
        st.markdown(f"""
        <div class="lock-item unlocked">
            <span class="lock-icon" style="color:#d4af37;">{sym}</span>
            <span>{label}</span>
            <span style="margin-left:auto; color:#d4af37; font-size:0.75rem;">✓ Disponível</span>
        </div>""", unsafe_allow_html=True)

    for sym, label in locked:
        st.markdown(f"""
        <div class="lock-item">
            <span class="lock-icon">🔒</span>
            <span style="filter:blur(0px);">{label}</span>
            <span style="margin-left:auto; color:#d4af37; font-size:0.75rem;">Premium</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Warning box
    st.markdown(f"""
    <div class="warning-box">
        ⚠️ <strong>ATENÇÃO:</strong> Detectamos um arquétipo sombra com padrões de sabotagem financeira
        diretamente ligados ao seu perfil como <strong>{primary}</strong>.
        Este padrão afeta as decisões de {random.randint(60, 85)}% dos indivíduos com seu perfil sem que eles
        percebam. O Dossiê Supremo detalha exatamente como neutralizar esse padrão.
    </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("VER OFERTA — DOSSIÊ SUPREMO →", key="btn_offer"):
        go_to("offer")


# ─────────────────────────────────────────────
#  SCREEN 6: OFFER
# ─────────────────────────────────────────────
def screen_offer():
    primary = st.session_state["primary"]
    name = st.session_state["name"]

    st.markdown(f"""
    <div style="text-align:center; padding:2rem 0 0.5rem 0;">
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.65rem; font-weight:700;
                    letter-spacing:0.3em; text-transform:uppercase; color:#d4af37; margin-bottom:0.75rem;">
            ◈ Oferta Exclusiva · Tempo Limitado
        </div>
        <h1 style="font-family:'Cormorant Garamond',serif !important; font-size:2.3rem; font-weight:700;
                   color:#f0f1f3; margin:0 0 0.5rem 0; line-height:1.25;">
            {name}, seu diagnóstico está<br>
            <span style="color:#d4af37;">90% incompleto</span>
        </h1>
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.9rem; color:#7d8590; max-width:420px; margin:0 auto;">
            Você viu apenas a superfície. O que realmente define suas decisões está no nível mais profundo do relatório.
        </p>
    </div>""", unsafe_allow_html=True)

    divider()

    # Product box
    st.markdown("""
    <div style="background:linear-gradient(135deg, rgba(212,175,55,0.06), rgba(124,92,191,0.04));
                border:1px solid rgba(212,175,55,0.25); border-radius:8px; padding:2rem; margin-bottom:1.25rem;">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:1rem;">
            <div>
                <div style="font-family:'Space Grotesk',sans-serif; font-size:0.65rem; font-weight:700;
                            letter-spacing:0.2em; text-transform:uppercase; color:#d4af37; margin-bottom:0.4rem;">
                    Produto Premium
                </div>
                <div style="font-family:'Cormorant Garamond',serif; font-size:1.7rem; font-weight:700; color:#f0f1f3; line-height:1.2;">
                    Dossiê Arquétipo Supremo
                </div>
                <div style="font-family:'Space Grotesk',sans-serif; font-size:0.8rem; color:#7d8590; margin-top:0.3rem;">
                    Relatório completo · PDF Premium · Acesso imediato
                </div>
            </div>
            <div style="text-align:right;">
                <div style="font-family:'Space Grotesk',sans-serif; font-size:0.72rem; color:#7d8590;
                            text-decoration:line-through; margin-bottom:0.1rem;">De R$ 47,00</div>
                <div style="font-family:'Cormorant Garamond',serif; font-size:3rem; font-weight:700;
                            color:#d4af37; line-height:1;">R$ 4,90</div>
                <div style="font-family:'Space Grotesk',sans-serif; font-size:0.68rem; color:#7d8590;">pagamento único</div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    # Benefits
    benefits = [
        ("◆", "Arquétipo Principal — análise profunda e expandida"),
        ("✦", "Arquétipo Secundário — como ele modifica seu perfil"),
        ("⊗", "Arquétipo Sombra — sabotadores e como neutralizá-los"),
        ("⋆", "Talento Oculto — o dom ainda não ativado"),
        ("◈", "Perfil Amoroso — compatibilidades e padrões de vínculo"),
        ("♛", "Perfil Financeiro — forças, riscos e estratégias"),
        ("◉", "Perfil Profissional — vocação e ambiente ideal"),
        ("○", "Radar Comportamental — 6 dimensões com pontuações"),
        ("✶", "Mapa de Compatibilidades entre arquétipos"),
        ("⊕", "Plano de Evolução — 4 passos concretos"),
        ("◎", "PDF Premium — 10+ páginas, design exclusivo"),
    ]
    for sym, label in benefits:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.65rem; padding:0.45rem 0;
                    font-family:'Space Grotesk',sans-serif; font-size:0.85rem; color:#c9ced8;">
            <span style="color:#d4af37; font-size:0.9rem; margin-top:0.05rem;">{sym}</span>
            <span>{label}</span>
        </div>""", unsafe_allow_html=True)

    divider()

    # Social proof
    testimonials = [
        ("A.M., 34 anos", "\"O diagnóstico do meu arquétipo sombra foi perturbadoramente preciso. Reconheci padrões que nunca tinha nomeado antes.\""),
        ("C.R., 28 anos", "\"Compartilhei com meu terapeuta. Ela disse que em 20 minutos o relatório identificou o que levamos 3 sessões para mapear.\""),
        ("F.L., 41 anos", "\"A parte do perfil financeiro me fez repensar decisões que eu estava prestes a tomar. Valeu muito mais do que paguei.\""),
    ]
    for author, text in testimonials:
        st.markdown(f"""
        <div style="background:#161b22; border:1px solid #21262d; border-left:2px solid #d4af37;
                    border-radius:4px; padding:1rem 1.25rem; margin-bottom:0.75rem;">
            <p style="font-family:'Cormorant Garamond',serif; font-size:1rem; color:#c9ced8;
                      line-height:1.6; margin:0 0 0.5rem 0; font-style:italic;">{text}</p>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.72rem; color:#7d8590;">{author}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Demo/simulation of payment
    st.markdown("""
    <div style="text-align:center; margin-bottom:0.75rem;">
        <span style="font-family:'Space Grotesk',sans-serif; font-size:0.72rem; color:#7d8590;">
            🔒 Ambiente seguro · Acesso imediato após confirmação
        </span>
    </div>""", unsafe_allow_html=True)

    if st.button("QUERO MEU DOSSIÊ SUPREMO — R$ 4,90 →", key="btn_pay"):
        # In a real app, this would redirect to payment gateway
        # For demo, we unlock directly
        st.session_state["paid"] = True
        go_to("premium")

    if st.button("Ver resultado gratuito novamente", key="btn_back_free"):
        go_to("result_free")

    st.markdown("""
    <div style="text-align:center; margin-top:1rem;">
        <span style="font-family:'Space Grotesk',sans-serif; font-size:0.68rem; color:#7d8590;">
            Garantia: Se não ficar satisfeito, devolvemos seu dinheiro em 7 dias.
        </span>
    </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  SCREEN 7: PREMIUM REPORT
# ─────────────────────────────────────────────
def screen_premium():
    primary = st.session_state["primary"]
    secondary = st.session_state["secondary"]
    shadow = st.session_state["shadow"]
    arch = ARCHETYPES[primary]
    arch2 = ARCHETYPES[secondary]
    arch_s = ARCHETYPES[shadow]
    name = st.session_state["name"]
    idx = st.session_state["potential_index"]
    rarity = st.session_state["rarity_pct"]

    # ── HEADER ──
    st.markdown(f"""
    <div style="text-align:center; padding:1.5rem 0 1rem 0;">
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.65rem; font-weight:700;
                    letter-spacing:0.3em; text-transform:uppercase; color:#d4af37; margin-bottom:0.75rem;">
            ◈ Dossiê Supremo · Acesso Premium
        </div>
        <h1 style="font-family:'Cormorant Garamond',serif !important; font-size:2.2rem; font-weight:700;
                   color:#f0f1f3; margin:0 0 0.25rem 0;">
            Relatório de {name}
        </h1>
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.75rem; color:#7d8590;">
            Gerado em {datetime.now().strftime('%d/%m/%Y às %H:%M')} · Dossiê Arquétipo Supremo
        </div>
    </div>""", unsafe_allow_html=True)

    divider()

    # ── POTENCIAL INDEX ──
    st.markdown(f"""
    <div class="section-eyebrow">Diagnóstico Geral</div>
    <h2 style="font-family:'Cormorant Garamond',serif !important; font-size:1.8rem; color:#f0f1f3; margin:0 0 1rem 0;">
        Índice Geral de Potencial
    </h2>""", unsafe_allow_html=True)

    col_gauge, col_info = st.columns([1, 1])
    with col_gauge:
        st.plotly_chart(make_gauge(idx, arch["color"]), use_container_width=True, config={"displayModeBar": False})
    with col_info:
        st.markdown(f"""
        <div style="padding:1rem 0;">
            <div style="font-family:'Cormorant Garamond',serif; font-size:3.5rem; font-weight:700;
                        color:{arch['color']}; line-height:1; margin-bottom:0.25rem;">{idx}/100</div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem; color:#c9ced8; line-height:1.6; margin-bottom:1rem;">
                Seu índice combina inteligência estratégica, liderança, criatividade e resiliência adaptativa.
            </div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.75rem; color:#7d8590; margin-bottom:0.5rem;">
                Raridade do perfil
            </div>
            <div class="rarity-bar">
                <div class="rarity-fill" style="width:{min(rarity*4, 100)}%;"></div>
            </div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem; color:#d4af37; font-weight:600;">
                Top {rarity}% da população
            </div>
        </div>""", unsafe_allow_html=True)

    divider()

    # ── RADAR ──
    st.markdown(f"""
    <div class="section-eyebrow">Mapa Comportamental</div>
    <h2 style="font-family:'Cormorant Garamond',serif !important; font-size:1.8rem; color:#f0f1f3; margin:0 0 1rem 0;">
        Radar de Competências
    </h2>""", unsafe_allow_html=True)

    st.plotly_chart(make_radar(arch["traits"], arch["color"]), use_container_width=True, config={"displayModeBar": False})

    # Trait breakdown
    for trait, val in arch["traits"].items():
        level = "Alto" if val >= 80 else "Médio" if val >= 60 else "Em Desenvolvimento"
        level_color = "#27ae60" if val >= 80 else "#f39c12" if val >= 60 else "#7d8590"
        st.markdown(f"""
        <div class="stat-row">
            <span class="stat-label">{trait}</span>
            <span style="color:{level_color}; font-family:'Space Grotesk',sans-serif; font-size:0.75rem;">{level}</span>
            <span class="stat-value">{val}/100</span>
        </div>""", unsafe_allow_html=True)

    divider()

    # ── ARQUÉTIPO PRINCIPAL ──
    st.markdown(f"""
    <div class="section-eyebrow">Arquétipo Principal</div>
    <div style="display:flex; align-items:center; gap:1rem; margin-bottom:1rem;">
        <div style="font-size:3rem; color:{arch['color']};">{arch['symbol']}</div>
        <div>
            <h2 style="font-family:'Cormorant Garamond',serif !important; font-size:2rem;
                       color:#d4af37; margin:0 0 0.25rem 0;">{primary}</h2>
            <p style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem; color:#7d8590; margin:0;">
                {arch['tagline']}
            </p>
        </div>
    </div>
    <div class="glass-card">
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.88rem; color:#c9ced8; line-height:1.75; margin:0;">
            {arch['description']}
        </p>
    </div>""", unsafe_allow_html=True)

    divider()

    # ── ARQUÉTIPO SECUNDÁRIO ──
    st.markdown(f"""
    <div class="section-eyebrow">Arquétipo Secundário</div>
    <div style="display:flex; align-items:center; gap:1rem; margin-bottom:1rem;">
        <div style="font-size:2.5rem; color:{arch2['color']};">{arch2['symbol']}</div>
        <div>
            <h2 style="font-family:'Cormorant Garamond',serif !important; font-size:1.7rem;
                       color:#f0f1f3; margin:0 0 0.2rem 0;">{secondary}</h2>
            <p style="font-family:'Space Grotesk',sans-serif; font-size:0.82rem; color:#7d8590; margin:0;">
                {arch2['tagline']}
            </p>
        </div>
    </div>
    <div class="glass-card">
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.88rem; color:#c9ced8; line-height:1.75; margin:0;">
            {arch2['description'][:400]}...
        </p>
        <div style="margin-top:1rem; padding-top:0.75rem; border-top:1px solid #21262d;">
            <p style="font-family:'Space Grotesk',sans-serif; font-size:0.8rem; color:#7d8590; margin:0;">
                <strong style="color:#d4af37;">Influência combinada:</strong> O arquétipo {secondary} amplifica as características
                de {primary} nos contextos de {', '.join(list(arch2['traits'].keys())[:2]).lower()}.
            </p>
        </div>
    </div>""", unsafe_allow_html=True)

    divider()

    # ── ARQUÉTIPO SOMBRA ──
    st.markdown(f"""
    <div class="section-eyebrow">Arquétipo Sombra</div>
    <div style="display:flex; align-items:center; gap:1rem; margin-bottom:1rem;">
        <div style="font-size:2.5rem; color:#7d8590;">{arch_s['symbol']}</div>
        <div>
            <h2 style="font-family:'Cormorant Garamond',serif !important; font-size:1.7rem;
                       color:#f0f1f3; margin:0 0 0.2rem 0;">{shadow}</h2>
            <p style="font-family:'Space Grotesk',sans-serif; font-size:0.82rem; color:#7d8590; margin:0;">
                Padrões reprimidos e sabotadores internos
            </p>
        </div>
    </div>
    <div class="glass-card" style="border-color:rgba(200,50,50,0.2);">
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.78rem; color:#7d8590; margin:0 0 0.75rem 0; letter-spacing:0.05em; text-transform:uppercase;">
            Padrão de sabotagem identificado
        </p>
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.88rem; color:#c9ced8; line-height:1.75; margin:0;">
            {arch["shadow"]}
        </p>
    </div>""", unsafe_allow_html=True)

    divider()

    # ── FINANCIAL ──
    st.markdown(f"""
    <div class="section-eyebrow">Inteligência Financeira</div>
    <h2 style="font-family:'Cormorant Garamond',serif !important; font-size:1.8rem; color:#f0f1f3; margin:0 0 1rem 0;">
        Perfil Financeiro
    </h2>
    <div class="glass-card">
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.88rem; color:#c9ced8; line-height:1.75; margin:0;">
            {arch['financial']}
        </p>
    </div>""", unsafe_allow_html=True)

    divider()

    # ── LOVE ──
    st.markdown(f"""
    <div class="section-eyebrow">Inteligência Relacional</div>
    <h2 style="font-family:'Cormorant Garamond',serif !important; font-size:1.8rem; color:#f0f1f3; margin:0 0 1rem 0;">
        Perfil Amoroso
    </h2>
    <div class="glass-card">
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.88rem; color:#c9ced8; line-height:1.75; margin:0;">
            {arch['love']}
        </p>
    </div>""", unsafe_allow_html=True)

    divider()

    # ── CAREER ──
    st.markdown(f"""
    <div class="section-eyebrow">Vocação e Potencial</div>
    <h2 style="font-family:'Cormorant Garamond',serif !important; font-size:1.8rem; color:#f0f1f3; margin:0 0 1rem 0;">
        Perfil de Carreira
    </h2>""", unsafe_allow_html=True)

    for career in arch["career"]:
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:0.75rem; padding:0.75rem 1rem;
                    background:#161b22; border:1px solid #21262d; border-radius:4px; margin-bottom:0.5rem;">
            <span style="color:#d4af37;">◆</span>
            <span style="font-family:'Space Grotesk',sans-serif; font-size:0.88rem; color:#c9ced8;">{career}</span>
        </div>""", unsafe_allow_html=True)

    divider()

    # ── HIDDEN TALENT ──
    st.markdown(f"""
    <div class="section-eyebrow">Potencial Não Ativado</div>
    <h2 style="font-family:'Cormorant Garamond',serif !important; font-size:1.8rem; color:#f0f1f3; margin:0 0 1rem 0;">
        Talento Oculto
    </h2>
    <div class="glass-card" style="border-color:rgba(212,175,55,0.3); background:rgba(212,175,55,0.04);">
        <div style="font-family:'Cormorant Garamond',serif; font-size:1.3rem; font-weight:600;
                    color:#d4af37; margin-bottom:0.75rem;">
            {arch['talent'].split('—')[0].strip() if '—' in arch['talent'] else arch['talent'][:50]}
        </div>
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.88rem; color:#c9ced8; line-height:1.75; margin:0;">
            {arch['talent']}
        </p>
    </div>""", unsafe_allow_html=True)

    divider()

    # ── EVOLUTION PLAN ──
    st.markdown(f"""
    <div class="section-eyebrow">Desenvolvimento Pessoal</div>
    <h2 style="font-family:'Cormorant Garamond',serif !important; font-size:1.8rem; color:#f0f1f3; margin:0 0 1rem 0;">
        Plano de Evolução
    </h2>""", unsafe_allow_html=True)

    for i, step in enumerate(arch["evolution"], 1):
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:1rem; padding:1rem;
                    background:#161b22; border:1px solid #21262d; border-radius:4px; margin-bottom:0.75rem;">
            <div style="font-family:'Cormorant Garamond',serif; font-size:1.5rem; font-weight:700;
                        color:#d4af37; line-height:1; min-width:1.5rem;">{i}</div>
            <p style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem; color:#c9ced8;
                      line-height:1.65; margin:0;">{step}</p>
        </div>""", unsafe_allow_html=True)

    divider()

    # ── COMPATIBILITIES ──
    st.markdown(f"""
    <div class="section-eyebrow">Mapa de Conexões</div>
    <h2 style="font-family:'Cormorant Garamond',serif !important; font-size:1.8rem; color:#f0f1f3; margin:0 0 1rem 0;">
        Compatibilidades Arquetípicas
    </h2>""", unsafe_allow_html=True)

    for compat_name in arch["compatible"]:
        c_arch = ARCHETYPES[compat_name]
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:1rem; padding:0.85rem 1rem;
                    background:#161b22; border:1px solid #21262d; border-radius:4px; margin-bottom:0.5rem;">
            <div style="font-size:1.5rem; color:{c_arch['color']};">{c_arch['symbol']}</div>
            <div>
                <div style="font-family:'Space Grotesk',sans-serif; font-size:0.88rem; font-weight:600; color:#d4af37;">
                    {compat_name}
                </div>
                <div style="font-family:'Space Grotesk',sans-serif; font-size:0.75rem; color:#7d8590;">
                    {c_arch['tagline']}
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

    divider()

    # ── RARITY CERTIFICATE ──
    st.markdown(f"""
    <div style="background:linear-gradient(135deg, rgba(212,175,55,0.08), rgba(124,92,191,0.05));
                border:1px solid rgba(212,175,55,0.3); border-radius:8px; padding:2.5rem; text-align:center; margin-bottom:2rem;">
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.65rem; font-weight:700;
                    letter-spacing:0.3em; text-transform:uppercase; color:#d4af37; margin-bottom:1rem;">
            ◈ Certificado de Raridade · AuraDex
        </div>
        <div style="font-family:'Cormorant Garamond',serif; font-size:1.6rem; font-weight:600; color:#f0f1f3; margin-bottom:0.5rem;">
            {name}
        </div>
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.9rem; color:#c9ced8; line-height:1.7; margin-bottom:1rem;">
            possui o arquétipo <strong style="color:#d4af37;">{primary}</strong>,<br>
            identificado em apenas <strong style="color:#d4af37;">{rarity}%</strong> da população analisada.
        </div>
        <div style="font-family:'Cormorant Garamond',serif; font-size:2.5rem; font-weight:700; color:{arch['color']};">
            {arch['symbol']}
        </div>
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.68rem; color:#7d8590; margin-top:1rem;">
            Índice de Potencial: {idx}/100 · {datetime.now().strftime('%d/%m/%Y')}
        </div>
    </div>""", unsafe_allow_html=True)

    # ── PDF DOWNLOAD ──
    st.markdown("""
    <div class="section-eyebrow" style="margin-bottom:0.75rem;">Downloads e Compartilhamento</div>""", unsafe_allow_html=True)

    col_pdf, col_wa = st.columns(2)

    with col_pdf:
        try:
            pdf_bytes = generate_pdf_bytes()
            st.download_button(
                label="⬇ BAIXAR PDF PREMIUM",
                data=pdf_bytes,
                file_name=f"AuraDex_{name.replace(' ', '_')}_Dossie_Supremo.pdf",
                mime="application/pdf",
                key="btn_pdf",
            )
        except Exception as e:
            st.error(f"Erro ao gerar PDF: {e}")

    with col_wa:
        wa_text = f"Acabei de descobrir meu Arquétipo Supremo no AuraDex! Sou {primary} — um perfil que ocorre em apenas {rarity}% das pessoas. Faça seu teste:"
        wa_url = f"https://wa.me/?text={wa_text.replace(' ', '%20')}"
        st.markdown(f"""
        <a href="{wa_url}" target="_blank" style="
            display:block; width:100%; text-align:center;
            background:#25D366; color:#fff; border-radius:4px;
            padding:0.85rem 1rem; font-family:'Space Grotesk',sans-serif;
            font-weight:700; font-size:0.88rem; letter-spacing:0.08em;
            text-transform:uppercase; text-decoration:none;
            box-shadow:0 0 20px rgba(37,211,102,0.2);
        ">
            📲 COMPARTILHAR NO WHATSAPP
        </a>""", unsafe_allow_html=True)

    divider()

    if st.button("↩ Refazer análise", key="btn_restart"):
        for key in ["screen", "name", "age", "gender", "answers", "scores",
                    "primary", "secondary", "shadow", "paid", "potential_index",
                    "rarity_pct", "current_q"]:
            if key in st.session_state:
                del st.session_state[key]
        init_state()
        go_to("cover")


# ═══════════════════════════════════════════════════════════════════
#  ROUTER
# ═══════════════════════════════════════════════════════════════════
def main():
    screen = st.session_state.get("screen", "cover")

    if screen == "cover":
        screen_cover()
    elif screen == "identify":
        screen_identify()
    elif screen == "quiz":
        screen_quiz()
    elif screen == "loading":
        screen_loading()
    elif screen == "result_free":
        screen_result_free()
    elif screen == "offer":
        screen_offer()
    elif screen == "premium":
        screen_premium()
    else:
        go_to("cover")


if __name__ == "__main__":
    main()

    
   
