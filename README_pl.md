# 🌿 PlantVerse AR - Advanced Plant Identification

**PlantVerse AR** to nowoczesne, wielojęzyczne narzędzie zaprojektowane do identyfikacji roślin przy użyciu zaawansowanej sztucznej inteligencji oraz eksploracji ich naturalnych siedlisk. Ta wersja została znacząco ulepszona o system podwójnej weryfikacji modeli AI.

## ✨ Nowe Funkcje

* **Hybrydowa Identyfikacja AI:** Połączenie lokalnego modelu FloraSense z modelem Gemini 2.0 Flash w celu uzyskania eksperckiej weryfikacji.
* **Wsparcie Wielojęzyczne:** Pełny interfejs i analizy dostępne w języku Angielskim (English) oraz Polskim.
* **Mapowanie Lokalizacji:** Znajdowanie pobliskich obserwacji roślin przy użyciu danych w czasie rzeczywistym z serwisu iNaturalist.
* **Wiedza Botaniczna:** Szczegółowe raporty zawierające taksonomię, opisy oraz tradycyjne zastosowania roślin.

## 🛠️ Tryby Identyfikacji

1. **Original (FloraSense):** Szybka, lokalna identyfikacja przy użyciu modelu Sisigoks/FloraSense (Hugging Face).
2. **Advanced (Gemini AI):** Głęboka analiza multimodalna dostarczana przez najnowszy model Google Gemini 2.0 Flash.
3. **Hybrid (Weryfikacja):** Nasz najdokładniejszy tryb. Model lokalny stawia wstępną diagnozę, która jest następnie sprawdzana i szczegółowo opisywana przez Gemini AI.

## 🚀 Jak zacząć

**Wymagania wstępne:**
* Python w wersji 3.10 lub nowszej.
* Klucz API Google Gemini (dostępny bezpłatnie w Google AI Studio).

**Instalacja krok po kroku:**
1. Sklonuj swoje repozytorium (fork) używając polecenia **git clone** z adresem Twojego projektu.
2. Wejdź do folderu projektu za pomocą komendy **cd PlantVerse**.
3. Zainstaluj wymagane biblioteki wpisując polecenie **pip install -r requirements.txt**.
4. Uruchom aplikację komendą **streamlit run app.py**.

## 📦 Wykorzystane technologie

* **Framework:** Streamlit
* **Modele AI:** Gemini 2.0 Flash, FloraSense (Transformers)
* **API:** iNaturalist, Google AI Studio
* **Język:** Python

---
*Projekt zaktualizowany i utrzymywany w celu wspierania nowoczesnych potoków przetwarzania AI (AI Pipelines).*
