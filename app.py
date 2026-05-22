import streamlit as st
import streamlit.components.v1 as components

# Sayfanın geniş açıyla güzel görünmesi için
st.set_page_config(
    page_title="Lich AI",
    page_icon="🔮",
    layout="wide"
)

# Bilgisayarındaki tüm kodları bu tek HTML yapısının içine yerleştiriyoruz
html_kodu = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lich AI</title>
    <style>
        /* ================= TEMA VE RENK DEĞİŞKENLERİ ================= */
:root {
    --bg-dark: #07050a;
    --bg-card: #0f0b18;
    --bg-card-header: #161024;
    --text-main: #ffffff;
    --text-muted: #8e82a3;
    --border-color: #211834;
    
    /* Varsayılan Tema (Lich - Mor) */
    --main-color: #a855f7;
    --main-color-rgb: 168, 85, 247;
}

/* Dinamik Temalar */
body.theme-lev { --main-color: #f97316; --main-color-rgb: 249, 115, 22; }
body.theme-okyanus { --main-color: #0ea5e9; --main-color-rgb: 14, 165, 233; }
body.theme-orman { --main-color: #22c55e; --main-color-rgb: 34, 197, 94; }
body.theme-kozmik { --main-color: #ec4899; --main-color-rgb: 236, 72, 153; }

/* Ayarlar Tema Noktaları */
.color-lich { background-color: #a855f7; box-shadow: 0 0 10px #a855f7; }
.color-lev { background-color: #f97316; box-shadow: 0 0 10px #f97316; }
.color-okyanus { background-color: #0ea5e9; box-shadow: 0 0 10px #0ea5e9; }
.color-orman { background-color: #22c55e; box-shadow: 0 0 10px #22c55e; }
.color-kozmik { background-color: #ec4899; box-shadow: 0 0 10px #ec4899; }

/* ================= SIFIRLAMA VE GENEL MIMARI ================= */
* {
    margin: 0; padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    -webkit-tap-highlight-color: transparent;
}

body {
    background-color: var(--bg-dark);
    color: var(--text-main);
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    overflow: hidden;
    padding: 10px;
}

/* Mobil Container Cihaz Kılıfı */
.app-container {
    width: 100%;
    max-width: 420px;
    height: 92vh;
    max-height: 850px;
    background-color: var(--bg-dark);
    border: 1px solid var(--border-color);
    border-radius: 32px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);
    display: flex;
    flex-direction: column;
}

/* SAYFA GÖSTERİM SİSTEMİ (Çakışmalar Tamamen Çözüldü) */
.app-page {
    position: absolute;
    top: 0; left: 0; right: 0;
    bottom: 70px; /* Navbar yüksekliği */
    padding: 20px;
    overflow-y: auto;
    display: none; 
    flex-direction: column;
    opacity: 0;
    z-index: 1;
    transition: opacity 0.2s ease-in-out;
}

.app-page.active {
    display: flex !important;
    opacity: 1;
    z-index: 5;
}

/* Sayfa Başlıkları */
.page-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border-color);
}

.page-header h2 {
    font-size: 18px;
    font-weight: 600;
    letter-spacing: 0.5px;
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--main-color);
    text-shadow: 0 0 15px rgba(var(--main-color-rgb), 0.3);
}

/* ================= LICH HAYALETI VE YENI SOHBET BUTONU ================= */
.lich-ghost-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: 20px 0;
    position: relative;
}

.lich-ghost {
    width: 95px;
    height: 115px;
    cursor: pointer;
    filter: drop-shadow(0 0 15px rgba(var(--main-color-rgb), 0.5));
    animation: ghostFloat 4s ease-in-out infinite;
    transition: transform 0.3s ease, filter 0.3s ease;
}

.lich-ghost .ghost-body {
    fill: rgba(var(--main-color-rgb), 0.12);
    stroke: var(--main-color);
    stroke-width: 2.5;
}

.lich-ghost .eye-glow {
    fill: var(--main-color);
    filter: drop-shadow(0 0 5px var(--main-color));
}

.lich-ghost:hover {
    transform: scale(1.08);
    filter: drop-shadow(0 0 25px rgba(var(--main-color-rgb), 0.8));
}

.lich-ghost.spook-action {
    animation: ghostSpook 0.5s ease-in-out;
}

/* Balon Efekti */
.lich-chat-bubble {
    background: rgba(var(--main-color-rgb), 0.08);
    border: 1px solid rgba(var(--main-color-rgb), 0.25);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    padding: 12px 16px;
    border-radius: 16px;
    color: var(--text-main);
    font-size: 13px;
    max-width: 85%;
    text-align: center;
    cursor: pointer;
    margin-top: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    animation: bubblePulse 2.5s infinite ease-in-out;
    transition: transform 0.2s;
}
.lich-chat-bubble:hover { transform: translateY(-2px); background: rgba(var(--main-color-rgb), 0.15); }

.bubble-arrow {
    position: absolute; top: -8px; left: 50%; transform: translateX(-50%);
    width: 0; height: 0;
    border-left: 8px solid transparent; border-right: 8px solid transparent;
    border-bottom: 8px solid rgba(var(--main-color-rgb), 0.25);
}

/* YENİDEN TASARLANAN YALNIZCA SOHBET BUTONLU API ALANI */
.api-key-panel {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 20px;
    padding: 24px;
    margin-top: 15px;
}
.api-panel-content p {
    font-size: 13.5px;
    color: var(--text-muted);
    text-align: center;
    margin-bottom: 18px;
    line-height: 1.5;
}
.api-input-row {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 14px;
}
.api-input {
    width: 100%;
    background-color: var(--bg-dark);
    border: 1px solid var(--border-color);
    padding: 14px;
    border-radius: 12px;
    color: white;
    font-size: 14px;
    outline: none;
    text-align: center;
    transition: border-color 0.2s;
}
.api-input:focus { border-color: var(--main-color); }

.api-save-btn {
    width: 100%;
    background-color: var(--main-color);
    color: white;
    border: none;
    padding: 14px;
    border-radius: 12px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    box-shadow: 0 4px 15px rgba(var(--main-color-rgb), 0.3);
    transition: transform 0.2s, opacity 0.2s;
}
.api-save-btn:hover { transform: translateY(-1px); opacity: 0.9; }
.api-hint { font-size: 11px !important; color: var(--text-muted); text-align: center; margin-top: 5px; }

/* ================= CHAT GÖRÜNÜMÜ ================= */
.hide { display: none !important; }

.chat-panel { flex: 1; display: flex; flex-direction: column; min-height: 200px; }
.chat-messages { flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; margin-bottom: 12px; }
.chat-placeholder { margin: auto; text-align: center; padding: 20px; }
.big-icon { font-size: 45px; color: var(--text-muted); margin-bottom: 10px; }
.chat-placeholder h3 { font-size: 16px; margin-bottom: 5px; }
.chat-placeholder p { font-size: 12px; color: var(--text-muted); }

.message { max-width: 80%; padding: 12px 16px; border-radius: 16px; font-size: 14px; line-height: 1.4; word-break: break-word; }
.user-message { background-color: var(--main-color); color: white; align-self: flex-end; border-bottom-right-radius: 4px; }
.lich-message { background-color: var(--bg-card); border: 1px solid var(--border-color); color: var(--text-main); align-self: flex-start; border-bottom-left-radius: 4px; }
.loading-message { opacity: 0.6; font-style: italic; }

.chat-input-area { display: flex; gap: 8px; align-items: center; background-color: var(--bg-card); border: 1px solid var(--border-color); padding: 8px 12px; border-radius: 16px; }
.chat-input-area input { flex: 1; background: transparent; border: none; color: white; font-size: 14px; outline: none; }
.clear-chat-btn, .send-btn { background: transparent; border: none; color: var(--text-muted); cursor: pointer; font-size: 16px; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border-radius: 10px; }
.clear-chat-btn:hover { color: #ef4444; background-color: rgba(239, 68, 68, 0.1); }
.send-btn { color: var(--main-color); }

/* ================= OYUNLAR SOKAĞI ================= */
.games-grid { display: flex; flex-direction: column; gap: 12px; }
.game-card { background-color: var(--bg-card); border: 1px solid var(--border-color); border-radius: 16px; padding: 16px; display: flex; align-items: center; gap: 14px; cursor: pointer; transition: transform 0.2s, border-color 0.2s; }
.game-card:hover { transform: translateY(-2px); border-color: var(--main-color); }
.game-icon { width: 48px; height: 48px; background-color: var(--bg-dark); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: var(--main-color); font-size: 18px; }
.game-details h3 { font-size: 15px; margin-bottom: 2px; }
.game-details p { font-size: 12px; color: var(--text-muted); }

.center-content { display: flex; flex-direction: column; align-items: center; justify-content: center; margin: auto 0; }
.back-btn { background: transparent; border: none; color: white; font-size: 16px; cursor: pointer; }
.game-status { font-size: 16px; font-weight: 600; margin-bottom: 15px; color: var(--main-color); }
.game-info-text { font-size: 12.5px; color: var(--text-muted); margin-bottom: 15px; }
.game-feedback { font-size: 14px; margin: 14px 0; text-align: center; min-height: 20px; }

/* XOX Board */
.ttt-board { display: grid; grid-template-columns: repeat(3, 85px); grid-template-rows: repeat(3, 85px); gap: 8px; margin-bottom: 20px; }
.ttt-cell { background-color: var(--bg-card); border: 1px solid var(--border-color); border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 26px; font-weight: bold; cursor: pointer; }
.ttt-cell.X { color: var(--main-color); }
.ttt-cell.O { color: #f43f5e; }

#guess-input { width: 70px; background-color: var(--bg-card); border: 1px solid var(--border-color); color: white; padding: 10px; border-radius: 10px; text-align: center; outline: none; }
.guess-row { display: flex; gap: 8px; margin-bottom: 10px; }

.tkm-score { font-size: 16px; font-weight: bold; margin-bottom: 20px; }
.tkm-choices { display: flex; gap: 10px; margin-bottom: 10px; }
.tkm-btn { background-color: var(--bg-card); border: 1px solid var(--border-color); color: white; padding: 12px 16px; border-radius: 12px; cursor: pointer; }

.action-btn { background-color: var(--main-color); color: white; border: none; padding: 10px 20px; border-radius: 10px; cursor: pointer; font-size: 13.5px; }
.outline-btn { background: transparent; border: 1px solid var(--border-color); color: var(--text-muted); margin-top: 8px; padding: 6px 12px; font-size: 11px; }
.danger-btn { background-color: #ef4444 !important; }

/* ================= KİŞİSEL NOTLAR ================= */
.notlar-container { display: flex; flex-direction: column; gap: 12px; }
.note-input-box { background-color: var(--bg-card); border: 1px solid var(--border-color); padding: 12px; border-radius: 14px; display: flex; flex-direction: column; gap: 8px; }
.note-input-box textarea { background: transparent; border: none; color: white; font-size: 14px; resize: none; height: 65px; outline: none; }
.notes-list { display: flex; flex-direction: column; gap: 8px; }
.note-item { background-color: var(--bg-card); border: 1px solid var(--border-color); border-left: 3px solid var(--main-color); padding: 12px; border-radius: 10px; display: flex; justify-content: space-between; align-items: flex-start; }
.note-text { font-size: 13px; line-height: 1.4; white-space: pre-wrap; }
.delete-note-btn { background: transparent; border: none; color: var(--text-muted); cursor: pointer; }

/* ================= SİSTEM AYARLARI ================= */
.settings-list { display: flex; flex-direction: column; gap: 16px; }
.settings-group { background-color: var(--bg-card); border: 1px solid var(--border-color); border-radius: 16px; padding: 14px; }
.settings-group h3 { font-size: 13.5px; color: var(--text-muted); margin-bottom: 10px; font-weight: 500; }
.theme-grid { display: flex; flex-direction: column; gap: 6px; }
.theme-select-card { display: flex; align-items: center; gap: 10px; padding: 10px; border-radius: 10px; background-color: var(--bg-dark); border: 1px solid var(--border-color); cursor: pointer; }
.theme-select-card.active { border-color: var(--main-color); background-color: rgba(var(--main-color-rgb), 0.04); }
.theme-dot { width: 12px; height: 12px; border-radius: 50%; }
.api-status-box { display: flex; justify-content: space-between; align-items: center; background-color: var(--bg-dark); padding: 10px; border-radius: 10px; border: 1px solid var(--border-color); margin-bottom: 10px; font-size: 12.5px; }
.badge { padding: 3px 8px; border-radius: 12px; font-size: 10px; font-weight: 600; }
.badge.red { background-color: rgba(239, 68, 68, 0.15); color: #ef4444; }
.badge.green { background-color: rgba(34, 197, 94, 0.15); color: #22c55e; }

/* ================= DESTEK SAYFASI ================= */
.support-container { display: flex; flex-direction: column; gap: 12px; }
.support-card { background-color: var(--bg-card); border: 1px solid var(--border-color); border-radius: 20px; padding: 20px; text-align: center; }
.support-card h2 { font-size: 18px; margin-bottom: 6px; color: var(--main-color); }
.support-desc { font-size: 12.5px; color: var(--text-muted); margin-bottom: 18px; }
.support-options { display: flex; gap: 10px; margin-bottom: 10px; justify-content: center; }
.support-btn { flex: 1; background-color: var(--bg-dark); border: 1px solid var(--border-color); color: white; padding: 12px; border-radius: 12px; font-size: 11.5px; font-weight: 600; cursor: pointer; }
.support-manager-btn { width: 100%; background: linear-gradient(135deg, var(--main-color), #6b21a8); color: white; border: none; padding: 12px; border-radius: 12px; font-size: 13px; font-weight: bold; cursor: pointer; margin-bottom: 12px; }
.support-footer { font-size: 11.5px; color: var(--text-muted); line-height: 1.4; }

/* ================= MÖHTEŞEM ALT BAR (NAVBAR) ================= */
.bottom-nav {
    position: absolute; bottom: 0; left: 0; right: 0; height: 70px;
    background: rgba(15, 11, 24, 0.9) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
    border-top: 1px solid rgba(var(--main-color-rgb), 0.25) !important;
    display: flex; justify-content: space-around; align-items: center; z-index: 100;
}
.nav-btn {
    flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px;
    color: var(--text-muted); cursor: pointer; height: 100%; position: relative; transition: color 0.2s, transform 0.1s;
}
.nav-btn::before {
    content: ''; position: absolute; top: 0; left: 50%; transform: translateX(-50%) scaleX(0);
    width: 45%; height: 3px; background: var(--main-color); box-shadow: 0 0 8px var(--main-color); transition: transform 0.2s ease;
}
.nav-btn.active::before { transform: translateX(-50%) scaleX(1); }
.nav-btn i { font-size: 17px; }
.nav-btn span { font-size: 10.5px; font-weight: 500; }
.nav-btn:active { transform: scale(0.92); }
.nav-btn.active { color: var(--main-color) !important; }

/* ANIMASYONLAR */
@keyframes ghostFloat { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-8px); } }
@keyframes bubblePulse { 0%, 100% { box-shadow: 0 8px 20px rgba(0,0,0,0.4); } 50% { box-shadow: 0 8px 20px rgba(var(--main-color-rgb), 0.25); } }
@keyframes ghostSpook { 0% { transform: scale(1); } 30% { transform: scale(1.08) rotate(-4deg); } 70% { transform: scale(0.96) rotate(4deg); } 100% { transform: scale(1); } }
    </style>
</head>
<body>
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lich App</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="theme-lich">

    <div class="app-container">
        
        <section id="page-sohbet" class="app-page active">
            <div class="page-header">
                <h2><i class="fa-solid fa-comment-dots"></i> LİCH SOHBET</h2>
            </div>

            <div class="lich-ghost-container">
                <div class="lich-ghost" id="lichGhost">
                    <svg viewBox="0 0 100 120" xmlns="http://www.w3.org/2000/svg">
                        <path class="ghost-body" d="M20,50 Q20,20 50,20 Q80,20 80,50 Q80,90 70,100 Q60,90 50,100 Q40,90 30,100 Q20,90 20,50 Z" />
                        <g class="ghost-eyes" id="ghostEyes">
                            <circle cx="40" cy="45" r="5" class="eye-glow" />
                            <circle cx="60" cy="45" r="5" class="eye-glow" />
                            <circle cx="40" cy="45" r="2" fill="#000" />
                            <circle cx="60" cy="45" r="2" fill="#000" />
                        </g>
                        <path d="M45,58 Q50,62 55,58" stroke="currentColor" stroke-width="2" fill="none" opacity="0.8"/>
                    </svg>
                </div>
                
                <div class="lich-chat-bubble" onclick="openLichChat()">
                    <span>Merhaba! Benimle konuşmak için dokun... 🔮</span>
                    <div class="bubble-arrow"></div>
                </div>
            </div>

            <div id="api-key-panel" class="api-key-panel">
                <div class="api-panel-content">
                    <p>Lich ile bağlantı kurmak için Gemini API anahtarını girin.</p>
                    <div class="api-input-row">
                        <input type="password" id="api-key-input" placeholder="Gemini API Key..." class="api-input" />
                        <button onclick="saveApiKey()" class="api-save-btn" title="Sohbeti Başlat">
                            <i class="fa-solid fa-bolt"></i> Sohbeti Başlat
                        </button>
                    </div>
                    <p class="api-hint">Anahtarınız yerel tarayıcınızda (localStorage) güvenle saklanır.</p>
                </div>
            </div>

            <div id="chat-panel" class="chat-panel hide">
                <div id="chat-messages" class="chat-messages">
                    <div class="chat-placeholder">
                        <div class="big-icon"><i class="fa-solid fa-ghost"></i></div>
                        <h3>Benim adım Lich</h3>
                        <p>Sana nasıl yardımcı olabilirim? Aşağıdan mesaj atabilirsin.</p>
                    </div>
                </div>

                <div class="chat-input-area">
                    <button class="clear-chat-btn" onclick="clearChat()" title="Sohbeti Temizle">
                        <i class="fa-solid fa-trash-can"></i>
                    </button>
                    <input type="text" id="chat-input" placeholder="Bir şeyler yaz..." onkeydown="if(event.key==='Enter') sendMessage()" />
                    <button class="send-btn" onclick="sendMessage()">
                        <i class="fa-solid fa-paper-plane"></i>
                    </button>
                </div>
            </div>
        </section>

        <section id="page-oyunlar" class="app-page">
            <div class="page-header">
                <h2><i class="fa-solid fa-gamepad"></i> OYUNLAR </h2>
            </div>
            
            <div class="games-grid">
                <div class="game-card" onclick="switchSubPage('subpage-tic-tac-toe')">
                    <div class="game-icon"><i class="fa-solid fa-xmark"></i><i class="fa-solid fa-o"></i></div>
                    <div class="game-details">
                        <h3>XOX Oyunu</h3>
                        <p>Yapay zekaya karşı zekanı yarıştır!</p>
                    </div>
                </div>
                <div class="game-card" onclick="switchSubPage('subpage-sayi-tahmin')">
                    <div class="game-icon"><i class="fa-solid fa-arrow-up-9-1"></i></div>
                    <div class="game-details">
                        <h3>Sayı Tahmin</h3>
                        <p>Lich'in tuttuğu gizli sayıyı bulabilecek misin?</p>
                    </div>
                </div>
                <div class="game-card" onclick="switchSubPage('subpage-tas-kagit')">
                    <div class="game-icon"><i class="fa-solid fa-hand-fist"></i></div>
                    <div class="game-details">
                        <h3>Taş Kağıt Makas</h3>
                        <p>Klasik düello, şansına güvenen gelsin.</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="subpage-tic-tac-toe" class="app-page">
            <div class="page-header">
                <button class="back-btn" onclick="switchPage('page-oyunlar')"><i class="fa-solid fa-arrow-left"></i></button>
                <h2>XOX Oyunu</h2>
            </div>
            <div class="subpage-content center-content">
                <div class="game-status" id="ttt-status">Sıra Sende (X)</div>
                <div class="ttt-board">
                    <div class="ttt-cell" data-index="0" onclick="handleTTTClick(0)"></div>
                    <div class="ttt-cell" data-index="1" onclick="handleTTTClick(1)"></div>
                    <div class="ttt-cell" data-index="2" onclick="handleTTTClick(2)"></div>
                    <div class="ttt-cell" data-index="3" onclick="handleTTTClick(3)"></div>
                    <div class="ttt-cell" data-index="4" onclick="handleTTTClick(4)"></div>
                    <div class="ttt-cell" data-index="5" onclick="handleTTTClick(5)"></div>
                    <div class="ttt-cell" data-index="6" onclick="handleTTTClick(6)"></div>
                    <div class="ttt-cell" data-index="7" onclick="handleTTTClick(7)"></div>
                    <div class="ttt-cell" data-index="8" onclick="handleTTTClick(8)"></div>
                </div>
                <button class="action-btn" onclick="resetTTT()">Yeniden Başlat</button>
            </div>
        </section>

        <section id="subpage-sayi-tahmin" class="app-page">
            <div class="page-header">
                <button class="back-btn" onclick="switchPage('page-oyunlar')"><i class="fa-solid fa-arrow-left"></i></button>
                <h2>Sayı Tahmin Oyunu</h2>
            </div>
            <div class="subpage-content center-content">
                <p class="game-info-text">1 ile 100 arasında gizli bir sayı tuttun. Tahmin et!</p>
                <div class="guess-row">
                    <input type="number" id="guess-input" placeholder="Sayı..." min="1" max="100" />
                    <button class="action-btn" onclick="checkGuess()">Tahmin Et</button>
                </div>
                <div class="game-feedback" id="guess-feedback">İlk tahminini bekliyorum...</div>
                <button class="action-btn outline-btn" onclick="resetGuessGame()">Sayıyı Sıfırla</button>
            </div>
        </section>

        <section id="subpage-tas-kagit" class="app-page">
            <div class="page-header">
                <button class="back-btn" onclick="switchPage('page-oyunlar')"><i class="fa-solid fa-arrow-left"></i></button>
                <h2>Taş Kağıt Makas</h2>
            </div>
            <div class="subpage-content center-content">
                <div class="tkm-score">Skor: <span id="tkm-user-score">0</span> - <span id="tkm-bot-score">0</span></div>
                <div class="tkm-choices">
                    <button class="tkm-btn" onclick="playTKM('tas')">🪨 Taş</button>
                    <button class="tkm-btn" onclick="playTKM('kagit')">📄 Kağıt</button>
                    <button class="tkm-btn" onclick="playTKM('makas')">✂️ Makas</button>
                </div>
                <div class="game-feedback" id="tkm-feedback">Seçimini yap ve savaşı başlat!</div>
            </div>
        </section>

        <section id="page-notlar" class="app-page">
            <div class="page-header">
                <h2><i class="fa-solid fa-note-sticky"></i> KİŞİSEL NOTLAR</h2>
            </div>
            <div class="notlar-container">
                <div class="note-input-box">
                    <textarea id="note-textarea" placeholder="Buraya notunu yaz..."></textarea>
                    <button class="action-btn" onclick="addNote()">Not Ekle</button>
                </div>
                <div id="notes-list" class="notes-list">
                    </div>
            </div>
        </section>

        <section id="page-ayarlar" class="app-page">
            <div class="page-header">
                <h2><i class="fa-solid fa-gear"></i> SİSTEM AYARLARI</h2>
            </div>
            <div class="settings-list">
                <div class="settings-group">
                    <h3>Görsel Tema Seçimi</h3>
                    <div class="theme-grid">
                        <div class="theme-select-card active" onclick="setTheme('lich', 'Mistik Lich', this)">
                            <div class="theme-dot color-lich"></div> <span>Mistik Lich</span>
                        </div>
                        <div class="theme-select-card" onclick="setTheme('lev', 'Alev', this)">
                            <div class="theme-dot color-lev"></div> <span>Alev</span>
                        </div>
                        <div class="theme-select-card" onclick="setTheme('okyanus', 'Okyanus', this)">
                            <div class="theme-dot color-okyanus"></div> <span>Okyanus</span>
                        </div>
                        <div class="theme-select-card" onclick="setTheme('orman', 'Orman', this)">
                            <div class="theme-dot color-orman"></div> <span>Orman</span>
                        </div>
                        <div class="theme-select-card" onclick="setTheme('kozmik', 'Kozmik', this)">
                            <div class="theme-dot color-kozmik"></div> <span>Kozmik</span>
                        </div>
                    </div>
                </div>

                <div class="settings-group">
                    <h3>API Yönetimi</h3>
                    <div class="api-status-box">
                        <p>Kayıtlı API Key durumunuz:</p>
                        <span id="api-status-badge" class="badge red">Yok</span>
                    </div>
                    <button class="action-btn danger-btn" onclick="deleteApiKey()">API Key'i Sistemden Sil</button>
                </div>
            </div>
        </section>

        <section id="page-destek" class="app-page">
            <div class="page-header">
                <h2>👑 Yapımcı Osman</h2>
            </div>
            <div class="support-container">
                <div class="support-card">
                    <h2>Lich Premium Satın Al</h2>
                    <p class="support-desc">Lich yapay zekayı ve yapımcı Osman'ı desteklemek için</p>
                    <div class="support-options">
                        <button class="support-btn">💫 Galaksi 100tl</button>
                        
                        <button class="support-btn">🌌​ Süpernova 200tl</button>
                    </div>
                    <button class="support-manager-btn">👑 Lich Yönetici 500tl</button>
                    <p class="support-footer">Teşekkürler! 🙏<br><small>Made by Osman</small></p>
                </div>
            </div>
        </section>

        <nav class="bottom-nav">
            <div class="nav-btn active" onclick="switchPage('page-sohbet', this)">
                <i class="fa-solid fa-comment"></i>
                <span>Sohbet</span>
            </div>
            <div class="nav-btn" onclick="switchPage('page-oyunlar', this)">
                <i class="fa-solid fa-gamepad"></i>
                <span>Oyunlar</span>
            </div>
            <div class="nav-btn" onclick="switchPage('page-notlar', this)">
                <i class="fa-solid fa-note-sticky"></i>
                <span>Notlar</span>
            </div>
            <div class="nav-btn" onclick="switchPage('page-ayarlar', this)">
                <i class="fa-solid fa-gear"></i>
                <span>Ayarlar</span>
            </div>
            <div class="nav-btn" onclick="switchPage('page-destek', this)">
                <i class="fa-solid fa-heart"></i>
                <span>DESTEK</span>
            </div>
        </nav>

    </div>

    <script src="app.js"></script>
</body>
</html>
   


    <script>
        // ================= UYGULAMA SAYFA YÖNETİMİ =================
function switchPage(pageId, targetBtn = null) {
    // Tüm ana ve alt sayfaları gizle
    document.querySelectorAll('.app-page').forEach(page => {
        page.classList.remove('active');
    });

    // İstenen sayfayı aktif et
    const activePage = document.getElementById(pageId);
    if(activePage) {
        activePage.classList.add('active');
    }

    // Alt navbar aktiflik kontrolü
    if (targetBtn) {
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        targetBtn.classList.add('active');
    }
}

function switchSubPage(subPageId) {
    document.querySelectorAll('.app-page').forEach(page => {
        page.classList.remove('active');
    });
    const subPage = document.getElementById(subPageId);
    if(subPage) {
        subPage.classList.add('active');
    }
}


// ================= TEMA SİSTEMİ MEKANİZMASI =================
function setTheme(themeClass, themeName, element) {
    document.body.className = '';
    document.body.classList.add('theme-' + themeClass);

    document.querySelectorAll('.theme-select-card').forEach(card => {
        card.classList.remove('active');
    });
    if(element) element.classList.add('active');
}


// ================= API KEY YÖNETİM MOTORU =================
let GEMINI_API_KEY = localStorage.getItem('lich_api_key') || "";

window.addEventListener('DOMContentLoaded', () => {
    updateApiUIState();
    loadNotes();
    resetGuessGame();
});

function saveApiKey() {
    const inputEl = document.getElementById('api-key-input');
    if (!inputEl) return;
    
    const key = inputEl.value.trim();
    if(key === "") {
        alert("Lütfen geçerli bir API Anahtarı girin!");
        return;
    }

    localStorage.setItem('lich_api_key', key);
    GEMINI_API_KEY = key;
    updateApiUIState();
    inputEl.value = "";
}

function deleteApiKey() {
    if(confirm("API Anahtarını silmek istediğinize emin misiniz?")) {
        localStorage.removeItem('lich_api_key');
        GEMINI_API_KEY = "";
        updateApiUIState();
        alert("API Anahtarı başarıyla temizlendi.");
    }
}

function updateApiUIState() {
    const keyPanel = document.getElementById('api-key-panel');
    const chatPanel = document.getElementById('chat-panel');
    const statusBadge = document.getElementById('api-status-badge');

    if(GEMINI_API_KEY && GEMINI_API_KEY !== "") {
        if(keyPanel) keyPanel.classList.add('hide');
        if(chatPanel) chatPanel.classList.remove('hide');
        if(statusBadge) {
            statusBadge.innerText = "Aktif";
            statusBadge.className = "badge green";
        }
    } else {
        if(keyPanel) keyPanel.classList.remove('hide');
        if(chatPanel) chatPanel.classList.add('hide');
        if(statusBadge) {
            statusBadge.innerText = "Yok";
            statusBadge.className = "badge red";
        }
    }
}


// ================= GEMINI API BAĞLANTISI VE SOHBET MOTORU =================
async function sendMessage() {
    const inputEl = document.getElementById('chat-input');
    if(!inputEl) return;

    const messageText = inputEl.value.trim();
    if(messageText === "") return;

    appendMessageToChat('user', messageText);
    inputEl.value = "";

    const loadingId = appendMessageToChat('lich', 'Lich düşünceleri topluyor...');
    const loadingEl = document.getElementById(loadingId);
    if(loadingEl) loadingEl.classList.add('loading-message');

    const responseText = await fetchGeminiResponse(messageText);

    removeLoadingMessage(loadingId);
    appendMessageToChat('lich', responseText);
}

async function fetchGeminiResponse(userPrompt) {
    if(!GEMINI_API_KEY || GEMINI_API_KEY === "") {
        return "Sistem hatası: API anahtarı bulunamadı. Ayarlar sekmesinden anahtar ekleyin.";
    }

    const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${GEMINI_API_KEY}`;
    
    const requestBody = {
        contents: [{
            parts: [{
                text: "Sen mistik, karanlık ama yardımsever bir yapay zeka varlığısın. Adın 'Lich'. Yanıtların çok uzun olmasın, gizemli ve bilge bir üslup kullan." + userPrompt
            }]
        }]
    };

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestBody)
        });

        if(!response.ok) {
            return "Karanlık güçler (API Hatası) yanıt vermemi engelledi. Anahtarınızı kontrol edin.";
        }

        const data = await response.json();
        if (data.candidates && data.candidates[0].content.parts[0].text) {
            return data.candidates[0].content.parts[0].text;
        } else {
            return "Lich'ten boş bir yanıt döndü.";
        }
    } catch (error) {
        return "Google sunucularına bağlanırken ağ hatası oluştu.";
    }
}

function appendMessageToChat(sender, text) {
    const chatMessagesContainer = document.getElementById('chat-messages');
    if (!chatMessagesContainer) return null;

    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    messageDiv.innerText = text;

    const uniqueId = 'msg-' + Date.now();
    messageDiv.id = uniqueId;

    chatMessagesContainer.appendChild(messageDiv);
    chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;

    return uniqueId;
}

function removeLoadingMessage(id) {
    const element = document.getElementById(id);
    if (element) element.remove();
}

function clearChat() {
    const chatMessagesContainer = document.getElementById('chat-messages');
    if (!chatMessagesContainer) return;

    if(confirm("Sohbet geçmişini silmek istiyor musunuz?")) {
        chatMessagesContainer.innerHTML = `
            <div class="chat-placeholder">
                <div class="big-icon"><i class="fa-solid fa-ghost"></i></div>
                <h3>Benim adım Lich</h3>
                <p>Sana nasıl yardımcı olabilirim? Aşağıdan mesaj atabilirsin.</p>
            </div>
        `;
    }
}


// ================= OYUNLAR MEKANİĞİ (XOX / SAYI TAHMİN / TKM) =================
let tttBoard = ["", "", "", "", "", "", "", "", ""];
let tttActive = true;

function handleTTTClick(index) {
    const cell = document.querySelector(`.ttt-cell[data-index='${index}']`);
    if(tttBoard[index] !== "" || !tttActive) return;

    tttBoard[index] = "X";
    cell.innerText = "X";
    cell.classList.add("X");

    if(checkTTTWinner("X")) {
        document.getElementById('ttt-status').innerText = "Tebrikler, Kazandın! 🎉";
        tttActive = false;
        return;
    }

    if(!tttBoard.includes("")) {
        document.getElementById('ttt-status').innerText = "Berabere! 🤝";
        tttActive = false;
        return;
    }

    tttActive = false;
    document.getElementById('ttt-status').innerText = "Lich düşünüyor...";
    setTimeout(() => { makeBotMove(); }, 600);
}

function makeBotMove() {
    let emptyCells = [];
    for(let i=0; i<tttBoard.length; i++) {
        if(tttBoard[i] === "") emptyCells.push(i);
    }

    if(emptyCells.length > 0) {
        const randomIndex = emptyCells[Math.floor(Math.random() * emptyCells.length)];
        tttBoard[randomIndex] = "O";
        const cell = document.querySelector(`.ttt-cell[data-index='${randomIndex}']`);
        if(cell) {
            cell.innerText = "O";
            cell.classList.add("O");
        }

        if(checkTTTWinner("O")) {
            document.getElementById('ttt-status').innerText = "Lich kazandı! 💀";
            tttActive = false;
            return;
        }
    }

    if(!tttBoard.includes("") && tttActive) {
        document.getElementById('ttt-status').innerText = "Berabere! 🤝";
        tttActive = false;
        return;
    }

    tttActive = true;
    document.getElementById('ttt-status').innerText = "Sıra Sende (X)";
}

function checkTTTWinner(player) {
    const winPatterns = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]];
    return winPatterns.some(pattern => pattern.every(idx => tttBoard[idx] === player));
}

function resetTTT() {
    tttBoard = ["", "", "", "", "", "", "", "", ""];
    tttActive = true;
    document.getElementById('ttt-status').innerText = "Sıra Sende (X)";
    document.querySelectorAll('.ttt-cell').forEach(cell => { cell.innerText = ""; cell.className = "ttt-cell"; });
}

let secretBgNumber = 0;
function resetGuessGame() {
    secretBgNumber = Math.floor(Math.random() * 100) + 1;
    const feedback = document.getElementById('guess-feedback');
    if(feedback) feedback.innerText = "İlk tahminini bekliyorum...";
    const input = document.getElementById('guess-input');
    if(input) input.value = "";
}

function checkGuess() {
    const inputEl = document.getElementById('guess-input');
    const feedbackEl = document.getElementById('guess-feedback');
    if(!inputEl || !feedbackEl) return;

    const currentGuess = parseInt(inputEl.value);
    if(isNaN(currentGuess) || currentGuess < 1 || currentGuess > 100) {
        feedbackEl.innerText = "Lütfen 1 ile 100 arasında bir sayı girin!";
        return;
    }

    if(currentGuess === secretBgNumber) {
        feedbackEl.innerText = `Mükemmel! Doğru Sayı: ${secretBgNumber} 🎉`;
    } else if(currentGuess > secretBgNumber) {
        feedbackEl.innerText = "Daha KÜÇÜK bir sayı dene! ⬇️";
    } else {
        feedbackEl.innerText = "Daha BÜYÜK bir sayı dene! ⬆️";
    }
}

let userScoreTKM = 0;
let botScoreTKM = 0;
function playTKM(userSelection) {
    const options = ['tas', 'kagit', 'makas'];
    const botSelection = options[Math.floor(Math.random() * 3)];
    const feedbackEl = document.getElementById('tkm-feedback');
    const emojiMap = { 'tas': '🪨 Taş', 'kagit': '📄 Kağıt', 'makas': '✂️ Makas' };

    if(userSelection === botSelection) {
        feedbackEl.innerText = `İki taraf da ${emojiMap[userSelection]} seçti. Berabere!`;
    } else if((userSelection === 'tas' && botSelection === 'makas') || (userSelection === 'kagit' && botSelection === 'tas') || (userSelection === 'makas' && botSelection === 'kagit')) {
        userScoreTKM++;
        feedbackEl.innerText = `Sen: ${emojiMap[userSelection]} | Lich: ${emojiMap[botSelection]}\nKazandın! 🔥`;
    } else {
        botScoreTKM++;
        feedbackEl.innerText = `Sen: ${emojiMap[userSelection]} | Lich: ${emojiMap[botSelection]}\nLich vurdu ve gol oldu! 💀`;
    }
    document.getElementById('tkm-user-score').innerText = userScoreTKM;
    document.getElementById('tkm-bot-score').innerText = botScoreTKM;
}


// ================= KİŞİSEL NOTLAR MOTORU =================
function addNote() {
    const txtArea = document.getElementById('note-textarea');
    if(!txtArea) return;
    const text = txtArea.value.trim();
    if(text === "") return;

    let existingNotes = JSON.parse(localStorage.getItem('lich_notes') || "[]");
    existingNotes.push({ id: Date.now(), content: text });
    localStorage.setItem('lich_notes', JSON.stringify(existingNotes));
    txtArea.value = "";
    loadNotes();
}

function deleteNote(id) {
    let existingNotes = JSON.parse(localStorage.getItem('lich_notes') || "[]");
    existingNotes = existingNotes.filter(n => n.id !== id);
    localStorage.setItem('lich_notes', JSON.stringify(existingNotes));
    loadNotes();
}

function loadNotes() {
    const notesListContainer = document.getElementById('notes-list');
    if(!notesListContainer) return;
    notesListContainer.innerHTML = "";
    const notes = JSON.parse(localStorage.getItem('lich_notes') || "[]");

    if(notes.length === 0) {
        notesListContainer.innerHTML = "<p style='font-size:12px;color:var(--text-muted);text-align:center;'>Kayıtlı notunuz bulunmuyor.</p>";
        return;
    }
    notes.forEach(note => {
        const item = document.createElement('div');
        item.className = "note-item";
        item.innerHTML = `
            <div class="note-text">${note.content}</div>
            <button class="delete-note-btn" onclick="deleteNote(${note.id})"><i class="fa-solid fa-trash"></i></button>
        `;
        notesListContainer.appendChild(item);
    });
}


// ================= LICH ANIMASYONU VE ETKİLEŞİM MEKANİZMASI =================
document.addEventListener('DOMContentLoaded', () => {
    const ghost = document.getElementById('lichGhost');
    const eyes = document.getElementById('ghostEyes');

    if (!ghost || !eyes) return;

    // Mouse Göz Takip Efekti
    document.addEventListener('mousemove', (e) => {
        if (!document.getElementById('page-sohbet').classList.contains('active')) return;

        const rect = ghost.getBoundingClientRect();
        const ghostX = rect.left + rect.width / 2;
        const ghostY = rect.top + rect.height / 2;
        const angle = Math.atan2(e.clientY - ghostY, e.clientX - ghostX);
        
        const distance = 3; 
        const moveX = Math.cos(angle) * distance;
        const moveY = Math.sin(angle) * distance;

        eyes.style.transform = `translate(${moveX}px, ${moveY}px)`;
    });

    // Rastgele Ürpertme Hareketi
    setInterval(() => {
        if (!document.getElementById('page-sohbet').classList.contains('active')) return;
        if (Math.random() > 0.6) {
            ghost.classList.add('spook-action');
            setTimeout(() => ghost.classList.remove('spook-action'), 500);
        }
    }, 5000);
});

function openLichChat() {
    const chatInput = document.getElementById('chat-input');
    const apiKeyPanel = document.getElementById('api-key-panel');
    const ghost = document.getElementById('lichGhost');

    if (ghost) {
        ghost.classList.add('spook-action');
        setTimeout(() => ghost.classList.remove('spook-action'), 500);
    }

    if (apiKeyPanel && apiKeyPanel.classList.contains('hide')) {
        if (chatInput) chatInput.focus();
    } else {
        const inputKey = document.getElementById('api-key-input');
        if (inputKey) inputKey.focus();
    }
}
    </script>
</body>
</html>
"""

# Senin hazırladığın arayüzü Streamlit ekranında tam sayfa çalıştırır
components.html(html_kodu, height=850, scrolling=True)
