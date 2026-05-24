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
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
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
            margin: 0;
            padding: 0;
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

        /* SAYFA GÖSTERİM SİSTEMİ */
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
            position: absolute;
            top: -8px; left: 50%; transform: translateX(-50%);
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
        .settings
