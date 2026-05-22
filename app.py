import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Bilgisayarındaki index.html kodunu buraya yapıştıracaksın
html_kodu = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Lich AI</title>
    <style>
        /* BİLGİSAYARINDAKİ style.css KODLARINI TAMAMEN BURAYA YAPIŞTIR */
    </style>
</head>
<body>

    <!-- BİLGİSAYARINDAKİ index.html İÇİNDEKİ BODY KISMINI BURAYA YAPIŞTIR -->

    <script>
        // BİLGİSAYARINDAKİ app.js KODLARINI TAMAMEN BURAYA YAPIŞTIR
    </script>
</body>
</html>
"""

# HTML'i Streamlit sayfasında tam ekran çalıştırır
components.html(html_kodu, height=800, scroller=True)
