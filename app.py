import streamlit as st
import time
import random
import plotly.graph_objects as go
from fpdf import FPDF
import base64
from io import BytesIO
import urllib.parse

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(page_title="AuraDex Arquétipos", page_icon="✨", layout="centered")

# ==========================================
# ESTILO CSS PREMIUM (DARK & GOLD)
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #e6e6e6; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Georgia', serif; text-align: center;}
    .subtitle { text-align: center; font-size: 1.2rem; color: #a3a3a3; margin-bottom: 30px; }
    .stats-box { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #d4af37; text-align: center; margin-bottom: 20px;}
    .stat-text { font-size: 1.1rem; color: #f0f0f0; margin: 5px 0;}
    .stat-highlight { color: #d4af37; font-weight: bold; }
    .premium-card { background: linear-gradient(145deg, #1a1a1a, #262626); padding: 25px; border-radius: 12px; border-left: 4px solid #d4af37; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.1); }
    .premium-title { color: #d4af37; font-size: 1.3rem; margin-bottom: 10px; border-bottom: 1px solid #333; padding-bottom: 5px;}
    
    /* Estilização de Botões */
    .stButton>button { width: 100%; background: linear-gradient(90deg, #b8860b, #d4af37); color: #000; font-weight: bold; border-radius: 8px; border: none; padding: 10px; transition: all 0.3s ease;}
    .stButton>button:hover { background: linear-gradient(90deg, #d4af37, #f3e5ab); box-shadow: 0 0 15px rgba(212, 175, 55, 0.5); transform: scale(1.02); color: #000;}
    
    .progress-text { text-align: center; font-style: italic; color: #d4af37; margin-top: 20px; font-size: 1.1rem;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# BANCO DE DADOS DE ARQUÉTIPOS
# ==========================================
archetypes_data = {
    "O Sábio": {"compat": 82, "desc": "Você busca a verdade e a sabedoria acima de tudo. Sua mente analítica é seu maior trunfo.", "radar": [60, 80, 70, 50, 95, 60], "sombra": "O Dogmático (Fica preso em teorias e perde a ação).", "oculto": "O Bobo (Precisa aprender a rir de si mesmo).", "financas": 75, "amor": 60, "profissoes": "Pesquisador, Professor, Consultor Estratégico, Analista.", "missao": "Iluminar o caminho dos outros através do conhecimento e da reflexão profunda.", "frase": "Quem domina a si mesmo nunca é dominado pelo mundo."},
    "O Herói": {"compat": 88, "desc": "A coragem dita suas regras. Você nasceu para superar limites e proteger os mais fracos.", "radar": [90, 50, 60, 100, 70, 80], "sombra": "O Arrogante (Acredita que só ele pode resolver tudo).", "oculto": "O Cuidador (Esconde uma profunda necessidade de nutrir).", "financas": 85, "amor": 70, "profissoes": "Empreendedor, Atleta, Militar, Líder de Projetos.", "missao": "Provar seu valor através de atos corajosos e inspirar o mundo a ser forte.", "frase": "A verdadeira força não está em nunca cair, mas em levantar todas as vezes."},
    "O Mago": {"compat": 91, "desc": "Você enxerga como o universo funciona. Seu dom é transformar o ordinário no extraordinário.", "radar": [70, 95, 60, 60, 85, 90], "sombra": "O Manipulador (Usa seu conhecimento para controle).", "oculto": "O Governante (Deseja ordem no caos que cria).", "financas": 90, "amor": 65, "profissoes": "Visionário, Inventor, Terapeuta, Estrategista de Marketing.", "missao": "Compreender as leis do universo e transformar a realidade à sua volta.", "frase": "A mágica acontece quando a intenção encontra a intuição."},
    "O Criador": {"compat": 85, "desc": "A inovação corre nas suas veias. Você não se contenta com o que existe, você inventa o que falta.", "radar": [50, 100, 70, 60, 60, 80], "sombra": "O Perfeccionista (Nunca termina nada porque nunca está perfeito).", "oculto": "O Rebelde (Vontade de destruir o antigo para criar o novo).", "financas": 80, "amor": 75, "profissoes": "Designer, Artista, Arquiteto, Diretor de Criação.", "missao": "Dar forma a ideias e deixar uma marca duradoura no mundo.", "frase": "A imaginação é a única fronteira da realidade."},
    "O Governante": {"compat": 89, "desc": "A ordem e o controle são naturais para você. Você constrói estruturas para que as coisas prosperem.", "radar": [100, 40, 50, 70, 90, 40], "sombra": "O Tirano (Controla por medo da perda de poder).", "oculto": "O Amante (Deseja intimidade longe do trono).", "financas": 95, "amor": 55, "profissoes": "CEO, Gestor, Político, Administrador.", "missao": "Criar prosperidade e estabilidade para sua família e comunidade.", "frase": "O poder sem propósito é apenas tirania."},
    "O Explorador": {"compat": 78, "desc": "A liberdade é o seu oxigênio. Você busca novas experiências e odeia rotinas claustrofóbicas.", "radar": [50, 70, 60, 80, 40, 100], "sombra": "O Inconstante (Incapaz de se comprometer).", "oculto": "O Sábio (Busca sentido nas viagens, não apenas fuga).", "financas": 60, "amor": 50, "profissoes": "Fotógrafo, Jornalista, Nômade Digital, Guia.", "missao": "Viver uma vida autêntica, livre de amarras e cheia de descobertas.", "frase": "Nem todos que vagam estão perdidos."},
    # Para economia de espaço, usaremos estes 6 principais como base na simulação. 
    # Em produção, você expande a lista para os 12.
}

# ==========================================
# ESTADO DA SESSÃO
# ==========================================
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'user_name' not in st.session_state:
    st.session_state.user_name = ''
if 'archetype' not in st.session_state:
    st.session_state.archetype = ''
if 'is_premium' not in st.session_state:
    st.session_state.is_premium = False

def change_page(page):
    st.session_state.page = page

# ==========================================
# FUNÇÕES DE UI E LÓGICA
# ==========================================

def home_page():
    st.markdown("<h1>✨ AuraDex Arquétipos</h1>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Qual é o Arquétipo que controla suas decisões sem você perceber?</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ccc; margin-bottom: 20px;'>Descubra os padrões ocultos da sua personalidade em menos de 5 minutos.</p>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="stats-box">
            <p class="stat-text">📊 Mais de <span class="stat-highlight">10.000 perfis</span> analisados.</p>
            <p class="stat-text">🎯 Precisão comportamental de <span class="stat-highlight">92%</span>.</p>
            <p class="stat-text">⚡ Resultado imediato.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("INICIAR ANÁLISE PROFUNDA", use_container_width=True):
        change_page('register')

def register_page():
    st.markdown("<h2>Seu Perfil Inicial</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center'>Para calibrar nossa IA psicológica, precisamos de dados básicos.</p>", unsafe_allow_html=True)
    
    with st.form("register_form"):
        name = st.text_input("Seu Primeiro Nome *", max_chars=20)
        age = st.number_input("Sua Idade", min_value=12, max_value=100, step=1)
        nickname = st.text_input("Apelido (Opcional)")
        
        submitted = st.form_submit_button("Começar Teste")
        if submitted:
            if name.strip() == "":
                st.error("Por favor, insira seu primeiro nome.")
            else:
                st.session_state.user_name = name.strip().capitalize()
                change_page('quiz')

def quiz_page():
    st.markdown("<h2>Análise Comportamental</h2>", unsafe_allow_html=True)
    st.progress(0.5, text="Progresso: Questão 1 de 15")
    
    # Simulação de quiz para o script. 
    # Para 15 questões, você repetiria esta estrutura.
    st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
    st.markdown("**1. Quando um problema inesperado surge no trabalho, sua primeira reação é:**")
    st.radio("Escolha uma opção:", [
        "Analisar todos os dados antes de agir. (Sábio)",
        "Tomar a frente e liderar a resolução. (Herói/Governante)",
        "Buscar uma solução criativa e fora da caixa. (Criador/Mago)",
        "Ver como isso afeta a equipe e oferecer suporte. (Cuidador)"
    ], key="q1")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align:center; font-size:12px; color:#666;'>*Simulação: Exibindo 1 de 15 perguntas reais.*</p>", unsafe_allow_html=True)

    if st.button("Finalizar Teste e Analisar"):
        change_page('loading')

def loading_page():
    st.markdown("<h2>Processando seu Perfil...</h2>", unsafe_allow_html=True)
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    messages = [
        "Analisando padrões emocionais...",
        "Mapeando tendências comportamentais...",
        "Calculando compatibilidades...",
        "Detectando arquétipos ocultos...",
        "Finalizando relatório..."
    ]
    
    for i in range(100):
        time.sleep(0.04) # Simula o delay de carregamento
        progress_bar.progress(i + 1)
        if i % 20 == 0:
            status_text.markdown(f"<div class='progress-text'>{messages[i//20]}</div>", unsafe_allow_html=True)
            
    # Atribui um arquétipo aleatório da nossa lista para a demonstração
    st.session_state.archetype = random.choice(list(archetypes_data.keys()))
    change_page('results_free')
    st.rerun()

def generate_radar_chart(data):
    categories = ['Liderança', 'Criatividade', 'Empatia', 'Coragem', 'Estratégia', 'Adaptabilidade']
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=data,
        theta=categories,
        fill='toself',
        fillcolor='rgba(212, 175, 55, 0.4)',
        line=dict(color='#d4af37', width=2),
        marker=dict(color='#d4af37', size=8)
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], color='#666'),
            angularaxis=dict(color='#d4af37')
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=20, b=20)
    )
    return fig

def generate_pdf(name, arch_name, data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(13, 17, 23)
    pdf.rect(0, 0, 210, 297, 'F')
    
    pdf.set_text_color(212, 175, 55)
    pdf.set_font("Arial", 'B', 24)
    pdf.cell(200, 20, txt="AuraDex Arquétipos - Relatório Premium", ln=True, align='C')
    
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=f"Perfil de: {name}", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Arquétipo Dominante: {arch_name}", ln=True, align='C')
    
    pdf.ln(10)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, txt=f"Descrição: {data['desc']}")
    pdf.multi_cell(0, 10, txt=f"Sombra: {data['sombra']}")
    pdf.multi_cell(0, 10, txt=f"Arquétipo Oculto: {data['oculto']}")
    pdf.multi_cell(0, 10, txt=f"Potencial Profissional: {data['profissoes']}")
    pdf.multi_cell(0, 10, txt=f"Missão de Vida: {data['missao']}")
    
    pdf.ln(10)
    pdf.set_text_color(212, 175, 55)
    pdf.set_font("Arial", 'I', 14)
    pdf.multi_cell(0, 10, txt=f'"{data["frase"]}"', align='C')
    
    # Retorna string no formato Latin-1
    return pdf.output(dest='S').encode('latin-1')

def results_free_page():
    arch_name = st.session_state.archetype
    arch_data = archetypes_data[arch_name]
    
    st.markdown(f"<h2>Parabéns, {st.session_state.user_name}.</h2>", unsafe_allow_html=True)
    st.markdown(f"<h3>Seu Arquétipo Dominante é: <br><span style='font-size:2.5rem; text-transform:uppercase;'>{arch_name}</span></h3>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="stats-box" style="margin-top:20px;">
            <h2>{arch_data['compat']}%</h2>
            <p>de afinidade profunda com este padrão</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.info(arch_data['desc'])
    
    st.warning("⚠️ **Alerta do Sistema:** Existe um **segundo arquétipo extremamente forte** em você que influencia secretamente suas decisões financeiras e seus relacionamentos.")
    
    st.markdown("<hr style='border: 1px solid #333'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:white;'>Desbloqueie seu Relatório Completo por apenas R$1,99</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Descubra sua sombra, perfil financeiro, amoroso e gráfico comportamental.</p>", unsafe_allow_html=True)
    
    # Simulação de Pagamento
    if st.button("💳 DESBLOQUEAR RELATÓRIO PREMIUM (R$1,99)"):
        st.session_state.is_premium = True
        change_page('results_premium')
        st.rerun()

def results_premium_page():
    arch_name = st.session_state.archetype
    arch_data = archetypes_data[arch_name]
    
    st.markdown(f"<h1>Relatório Premium: {arch_name}</h1>", unsafe_allow_html=True)
    st.success("Relatório desbloqueado com sucesso! Bem-vindo(a) à profundidade da sua mente.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("<div class='premium-title'> Radar Comportamental</div>", unsafe_allow_html=True)
        fig = generate_radar_chart(arch_data['radar'])
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("<div class='premium-title'>💰 Potencial Financeiro</div>", unsafe_allow_html=True)
        st.progress(arch_data['financas'] / 100)
        st.write(f"Pontuação: **{arch_data['financas']}/100**")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("<div class='premium-title'>🌑 Arquétipo Sombra</div>", unsafe_allow_html=True)
        st.write("É o lado oculto da sua personalidade. Onde seus sabotadores moram.")
        st.error(arch_data['sombra'])
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("<div class='premium-title'>🎭 Arquétipo Oculto</div>", unsafe_allow_html=True)
        st.write("Potencial ainda pouco explorado dentro de você.")
        st.info(arch_data['oculto'])
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("<div class='premium-title'>❤️ Perfil Amoroso</div>", unsafe_allow_html=True)
        st.progress(arch_data['amor'] / 100)
        st.write(f"Pontuação: **{arch_data['amor']}/100**")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
    st.markdown("<div class='premium-title'>💼 Potencial Profissional</div>", unsafe_allow_html=True)
    st.write(f"**Profissões altamente compatíveis:** {arch_data['profissoes']}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='premium-card' style='text-align:center;'>", unsafe_allow_html=True)
    st.markdown("<div class='premium-title'>🌟 Missão de Vida</div>", unsafe_allow_html=True)
    st.write(arch_data['missao'])
    st.markdown(f"<h3 style='margin-top:20px; font-style:italic;'>\"{arch_data['frase']}\"</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Geração de PDF e Compartilhamento
    st.markdown("---")
    col_pdf, col_wpp = st.columns(2)
    
    with col_pdf:
        pdf_bytes = generate_pdf(st.session_state.user_name, arch_name, arch_data)
        st.download_button(
            label="📄 BAIXAR PDF EXCLUSIVO",
            data=pdf_bytes,
            file_name=f"AuraDex_{st.session_state.user_name}_{arch_name}.pdf",
            mime="application/pdf"
        )
        
    with col_wpp:
        msg = f"Descobri meu Arquétipo Dominante no AuraDex. Sou '{arch_name}'. Faça o seu teste agora!"
        url_msg = urllib.parse.quote(msg)
        st.markdown(f"""
            <a href="https://wa.me/?text={url_msg}" target="_blank" style="text-decoration:none;">
                <button style="width: 100%; background: #25D366; color: white; font-weight: bold; border-radius: 8px; border: none; padding: 10px; cursor:pointer;">
                    📱 COMPARTILHAR NO WHATSAPP
                </button>
            </a>
        """, unsafe_allow_html=True)

# ==========================================
# ROTEAMENTO
# ==========================================
if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'register':
    register_page()
elif st.session_state.page == 'quiz':
    quiz_page()
elif st.session_state.page == 'loading':
    loading_page()
elif st.session_state.page == 'results_free':
    results_free_page()
elif st.session_state.page == 'results_premium':
    results_premium_page()
