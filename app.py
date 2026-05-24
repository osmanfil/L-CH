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
            -webkit-backdrop-filter: blur
