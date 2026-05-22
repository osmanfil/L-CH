import streamlit as st
import openai

# Sayfa Genişliği ve Başlık Ayarları
st.set_page_config(
    page_title="Lich AI",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Koyu Tema ve Şık Arayüz İçin Özel CSS (Dark Mode)
st.markdown("""
    <style>
    /* Ana arka plan ve yazı renkleri */
    .stApp {
        background-color: #0e1117;
        color: #ecf0f1;
    }
    /* Kenar çubuğu (Sidebar) tasarımı */
    section[data-testid="stSidebar"] {
        background-color: #1a1c23;
        border-right: 1px solid #2d3139;
    }
    /* Giriş kutuları ve butonlar */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #252834 !important;
        color: #ffffff !important;
        border: 1px solid #3f4456 !important;
        border-radius: 8px !important;
    }
    /* Gönder butonu stili */
    div.stButton > button:first-child {
        background-color: #6200ea !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100%;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #7c4dff !important;
    }
    /* Kullanıcı ve Asistan mesaj kutuları */
    .user-box {
        background-color: #2d3139;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
        border-left: 5px solid #00bcff;
    }
    .ai-box {
        background-color: #1f232d;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
        border-left: 5px solid #6200ea;
    }
    </style>
""", unsafe_transform_html=True)

# Kenar Çubuğu (Sidebar) - Ayarlar
st.sidebar.title("🔮 Lich AI Kontrol Paneli")
st.sidebar.subheader("Erişim Ayarları")

# Kullanıcının kendi API anahtarını girmesi için alan
api_key_input = st.sidebar.text_input("OpenAI API Key Giriniz:", type="password", help="Hesabınızın güvenliği için API anahtarınız sunucularımızda saklanmaz.")

# Model Seçimi
model_secimi = st.sidebar.selectbox(
    "Kullanılacak Yapay Zeka Modeli:",
    ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"]
)

st.sidebar.divider()
st.sidebar.caption("Lich AI v1.0.0 - İstediğiniz API anahtarını kullanarak özgürce chat yapın.")

# Ana Sayfa Başlıkları
st.title("🔮 Lich AI")
st.markdown("Kendi API anahtarınızla çalışan, esnek ve özgür yapay zeka platformu.")
st.divider()

# Sohbet Geçmişi Hafızası (Session State)
if "lich_messages" not in st.session_state:
    st.session_state.lich_messages = []

# Eski mesajları ekrana yazdırma
for mesaj in st.session_state.lich_messages:
    if mesaj["role"] == "user":
        st.markdown(f'<div class="user-box"><b>Siz:</b><br>{mesaj["content"]}</div>', unsafe_transform_html=True)
    else:
        st.markdown(f'<div class="ai-box"><b>Lich AI:</b><br>{mesaj["content"]}</div>', unsafe_transform_html=True)

# Mesaj Giriş Formu
with st.form(key="sohbet_formu", clear_on_submit=True):
    kullanici_mesaji = st.text_input("Mesajınızı yazın...", placeholder="Lich AI ile konuşmaya başlayın...")
    gonder_butonu = st.form_submit_button(label="Gönder")

# Gönder butonuna basıldığında çalışacak mantık
if gonder_butonu and kullanici_mesaji:
    if not api_key_input:
        st.error("Lütfen sol taraftaki panelden geçerli bir OpenAI API Key giriniz!")
    else:
        # Mesajı geçmişe ekle ve hemen ekranda göster
        st.session_state.lich_messages.append({"role": "user", "content": kullanici_mesaji})
        st.markdown(f'<div class="user-box"><b>Siz:</b><br>{kullanici_mesaji}</div>', unsafe_transform_html=True)
        
        # OpenAI API Ayarı
        openai.api_key = api_key_input
        
        try:
            with st.spinner("Lich AI düşünüyor..."):
                # API Çağrısı
                response = openai.ChatCompletion.create(
                    model=model_secimi,
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.lich_messages]
                )
                ai_cevap = response.choices[0].message.content
                
                # Cevabı geçmişe ekle ve ekrana yazdır
                st.session_state.lich_messages.append({"role": "assistant", "content": ai_cevap})
                st.markdown(f'<div class="ai-box"><b>Lich AI:</b><br>{ai_cevap}</div>', unsafe_transform_html=True)
                
        except Exception as e:
            st.error(f"Bir hata oluştu! API anahtarınızı veya internetinizi kontrol edin. Hata detayı: {str(e)}")
