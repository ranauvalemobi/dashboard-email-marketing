"""
📊 DASHBOARD DE CONVERSÃO - MINHAS ECONOMIAS V1
Upload Excel → Análise Automática + Botão Claude
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Configuração
st.set_page_config(
    page_title="Análise de Conversão - Minhas Economias",
    page_icon="🎯",
    layout="wide"
)

# CSS
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; color: #4CAF50; font-weight: bold;}
    .metric-big {font-size: 3rem; font-weight: bold; color: #4CAF50;}
    .copy-box {
        background: #F0F8F0;
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 15px;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

# Funções
def process_wake_data(df):
    """Processa dados da Wake"""
    df.columns = df.columns.str.lower().str.strip()
    email_col = next((col for col in df.columns if 'email' in col or 'mail' in col), None)
    
    if not email_col:
        st.error("❌ Coluna de email não encontrada!")
        return None
    
    df['email_clean'] = df[email_col].str.lower().str.strip()
    df_unique = df.drop_duplicates(subset=['email_clean'])
    st.success(f"✅ Wake: {len(df_unique)} emails únicos")
    return df_unique

def process_purchase_data(df):
    """Processa dados de compras"""
    df.columns = df.columns.str.lower().str.strip()
    email_col = next((col for col in df.columns if 'email' in col or 'mail' in col), None)
    
    if not email_col:
        st.error("❌ Coluna de email não encontrada!")
        return None
    
    df['email_clean'] = df[email_col].str.lower().str.strip()
    
    value_col = next((col for col in df.columns if any(x in col for x in ['valor', 'value', 'amount', 'price'])), None)
    if value_col:
        df['valor_compra'] = pd.to_numeric(df[value_col], errors='coerce')
    
    st.success(f"✅ Compras: {len(df)} transações")
    return df

def analyze_conversion(df_wake, df_purchases):
    """Cruza dados e calcula conversão"""
    emails_opened = set(df_wake['email_clean'].unique())
    emails_purchased = set(df_purchases['email_clean'].unique())
    emails_converted = emails_opened.intersection(emails_purchased)
    
    total_opened = len(emails_opened)
    total_purchased = len(emails_purchased)
    total_converted = len(emails_converted)
    conversion_rate = (total_converted / total_opened * 100) if total_opened > 0 else 0
    
    df_converted = df_purchases[df_purchases['email_clean'].isin(emails_converted)].copy()
    total_revenue = df_converted['valor_compra'].sum() if 'valor_compra' in df_converted.columns else 0
    
    return {
        'total_opened': total_opened,
        'total_purchased': total_purchased,
        'total_converted': total_converted,
        'conversion_rate': conversion_rate,
        'total_revenue': total_revenue,
        'emails_opened_not_purchased': list(emails_opened - emails_converted),
        'emails_purchased_not_opened': list(emails_purchased - emails_opened),
        'df_converted': df_converted
    }

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:
    st.image("https://via.placeholder.com/200x80/4CAF50/FFFFFF?text=Minhas+Economias", use_container_width=True)
    
    st.markdown("---")
    st.markdown("## 📋 Info da Campanha")
    
    campaign_name = st.text_input("Nome", value=f"Campanha {datetime.now().strftime('%d/%m/%Y')}")
    campaign_date = st.date_input("Data", value=datetime.now())
    
    st.markdown("---")
    st.markdown("## ℹ️ Como Usar")
    st.info("""
    **1.** Upload Excel da Wake
    **2.** Upload Excel de Compras  
    **3.** Veja análise automática
    **4.** Use botão Claude para IA! 💬
    """)

# ==========================================
# MAIN
# ==========================================

st.markdown('<p class="main-header">🎯 Análise de Conversão</p>', unsafe_allow_html=True)
st.markdown(f"**{campaign_name}** | {campaign_date.strftime('%d/%m/%Y')}")
st.markdown("---")

# Upload
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📨 Upload: Quem ABRIU")
    uploaded_wake = st.file_uploader("Excel da Wake", type=['xlsx', 'csv', 'xls'], key='wake')
    
    if uploaded_wake:
        try:
            df_wake = pd.read_excel(uploaded_wake) if uploaded_wake.name.endswith(('.xlsx', '.xls')) else pd.read_csv(uploaded_wake)
            st.success(f"✅ {len(df_wake)} linhas")
            df_wake_processed = process_wake_data(df_wake)
        except Exception as e:
            st.error(f"❌ Erro: {e}")
            df_wake_processed = None
    else:
        df_wake_processed = None

with col2:
    st.markdown("### 🛒 Upload: Quem COMPROU")
    uploaded_purchases = st.file_uploader("Excel de Compras", type=['xlsx', 'csv', 'xls'], key='purchases')
    
    if uploaded_purchases:
        try:
            df_purchases = pd.read_excel(uploaded_purchases) if uploaded_purchases.name.endswith(('.xlsx', '.xls')) else pd.read_csv(uploaded_purchases)
            st.success(f"✅ {len(df_purchases)} linhas")
            df_purchases_processed = process_purchase_data(df_purchases)
        except Exception as e:
            st.error(f"❌ Erro: {e}")
            df_purchases_processed = None
    else:
        df_purchases_processed = None

st.markdown("---")

# Análise
if df_wake_processed is not None and df_purchases_processed is not None:
    
    with st.spinner("🔄 Cruzando dados..."):
        results = analyze_conversion(df_wake_processed, df_purchases_processed)
    
    st.success("✅ Análise concluída!")
    st.markdown("---")
    
    # ==========================================
    # BOTÃO MÁGICO COPIAR PARA CLAUDE
    # ==========================================
    
    st.markdown("## 💬 Precisa de Análise com IA?")
    
    # Mensagem formatada
    claude_message = f"""📊 ANÁLISE DE CAMPANHA - {campaign_name}

Olá Claude! Preciso de sua análise sobre esta campanha.

═══════════════════════════════════════
📊 MÉTRICAS PRINCIPAIS
═══════════════════════════════════════

📨 Emails Abertos: {results['total_opened']:,}
✅ Conversões: {results['total_converted']:,}
📈 Taxa de Conversão: {results['conversion_rate']:.1f}%
💰 Receita: R$ {results['total_revenue']:,.2f}

═══════════════════════════════════════
🎯 DETALHAMENTO
═══════════════════════════════════════

❌ Abriram mas NÃO compraram: {len(results['emails_opened_not_purchased']):,}
🛒 Compraram SEM abrir: {len(results['emails_purchased_not_opened']):,}

═══════════════════════════════════════
❓ MINHA PERGUNTA:
═══════════════════════════════════════

[Digite sua pergunta aqui]

Exemplos:
• Esta taxa é boa?
• Vale fazer follow-up?
• Como melhorar?
• Qual próxima ação?

──────────────────────────────────────
Minhas Economias - {datetime.now().strftime('%d/%m/%Y %H:%M')}
"""
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.text_area(
            "📋 Mensagem Pronta (copie tudo):",
            value=claude_message,
            height=250,
            help="Selecione tudo (Ctrl+A) e copie (Ctrl+C)"
        )
    
    with col2:
        st.markdown("### 🚀 Passo a Passo:")
        st.markdown("""
        **1.** Selecione a mensagem
        
        **2.** Copie (Ctrl+A + Ctrl+C)
        
        **3.** Clique no botão 👇
        
        **4.** Cole no Claude (Ctrl+V)
        
        **5.** Adicione sua pergunta
        
        **6.** Receba resposta! ✅
        """)
        
        st.link_button(
            "💬 ABRIR CLAUDE",
            "https://claude.ai/new",
            use_container_width=True,
            type="primary"
        )
        
        st.success("💡 Salve claude.ai nos favoritos!")
    
    st.markdown("---")
    
    # MÉTRICAS
    st.markdown("## 📊 Resultados")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📨 Abriram", f"{results['total_opened']:,}")
    with col2:
        st.metric("✅ Converteram", f"{results['total_converted']:,}")
    with col3:
        st.markdown(f'<p class="metric-big" style="text-align: center;">{results["conversion_rate"]:.1f}%</p>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; color: #666;">Taxa Conversão</p>', unsafe_allow_html=True)
    with col4:
        if results['total_revenue'] > 0:
            st.metric("💰 Receita", f"R$ {results['total_revenue']:,.2f}")
        else:
            st.metric("🛒 Compras", f"{results['total_purchased']:,}")
    
    st.markdown("---")
    
    # FUNIL
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🎯 Funil de Conversão")
        
        fig = go.Figure(go.Funnel(
            y=['📨 Abriram', '✅ Converteram', '🛒 Total Compras'],
            x=[results['total_opened'], results['total_converted'], results['total_purchased']],
            textinfo="value+percent initial",
            marker=dict(color=['#4CAF50', '#2196F3', '#FF9800'])
        ))
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 📈 Breakdown")
        st.metric("❌ Não Compraram", f"{len(results['emails_opened_not_purchased']):,}", help="Abriram mas não compraram - oportunidade de follow-up!")
        st.metric("🛒 Orgânico", f"{len(results['emails_purchased_not_opened']):,}", help="Compraram sem abrir email")
        
        if results['conversion_rate'] >= 3:
            st.success("🎉 Taxa EXCELENTE!")
        elif results['conversion_rate'] >= 2:
            st.info("👍 Taxa BOA!")
        else:
            st.warning("⚠️ Pode melhorar")
    
    st.markdown("---")
    
    # DETALHAMENTO
    st.markdown("## 📋 Detalhamento")
    
    tab1, tab2, tab3 = st.tabs([
        f"✅ Converteram ({results['total_converted']})",
        f"❌ Não Compraram ({len(results['emails_opened_not_purchased'])})",
        f"🛒 Orgânico ({len(results['emails_purchased_not_opened'])})"
    ])
    
    with tab1:
        if len(results['df_converted']) > 0:
            st.dataframe(results['df_converted'], use_container_width=True, height=300)
            csv = results['df_converted'].to_csv(index=False).encode('utf-8')
            st.download_button("📥 Baixar Lista", csv, f"convertidos_{datetime.now().strftime('%Y%m%d')}.csv")
    
    with tab2:
        if len(results['emails_opened_not_purchased']) > 0:
            df_not = pd.DataFrame({'Email': results['emails_opened_not_purchased']})
            st.dataframe(df_not, use_container_width=True, height=300)
            st.info(f"💡 {len(results['emails_opened_not_purchased'])} leads quentes para follow-up!")
            csv = df_not.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Baixar para Follow-up", csv, f"followup_{datetime.now().strftime('%Y%m%d')}.csv")
    
    with tab3:
        if len(results['emails_purchased_not_opened']) > 0:
            df_org = pd.DataFrame({'Email': results['emails_purchased_not_opened']})
            st.dataframe(df_org, use_container_width=True, height=300)
            st.info("🤔 Compraram por outros canais (anúncio, indicação, etc)")

else:
    st.info("""
    ### 📤 Aguardando Upload dos Arquivos
    
    **Para começar:**
    1. Faça upload da base da Wake (quem abriu)
    2. Faça upload da base de compras
    3. Veja análise instantânea! ⚡
    """)

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**📊 Minhas Economias**")
with col2:
    st.markdown("**🤖 Sistema v1.0**")
with col3:
    st.markdown(f"**📅 {datetime.now().strftime('%d/%m/%Y')}**")
