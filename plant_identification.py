import streamlit as st
from google import genai
from PIL import Image
from transformers import pipeline

# 1. Słownik tłumaczeń (English jako domyślny)
TRANSLATIONS = {
    "English": {
        "title": "🌿 PlantVerse AI Identification",
        "mode_selection": "Choose Identification Engine",
        "mode_1": "Original (FloraSense HF)",
        "mode_2": "Advanced (Gemini AI)",
        "mode_3": "Hybrid (FloraSense + Gemini Verification)",
        "header_upload": "📷 Upload plant photo",
        "btn_identify": "Identify Plant 🔍",
        "sidebar_settings": "Settings",
        "api_key_label": "Gemini API Key (Modes 2 & 3)",
        "api_key_help": "Get it for free at aistudio.google.com",
        "result_header": "📊 Results:",
        "spinner_running": "Processing image with {mode}...",
        "prompt_gemini": "Identify this plant. Provide: Name, Description, Taxonomy, and Uses. Answer in English using Markdown.",
        "prompt_hybrid": """
            The local model (FloraSense) identified this plant as '{label}'. 
            Analyze the attached image and:
            1. Check if this identification is correct.
            2. If FloraSense is wrong, identify the plant correctly and explain why.
            3. Provide a detailed botanical report (Name, Taxonomy, Description, Uses).
            Answer in English using Markdown. Do not use conversational filler.
        """
    },
    "Polski": {
        "title": "🌿 PlantVerse AI - Identyfikacja",
        "mode_selection": "Wybierz silnik identyfikacji",
        "mode_1": "Oryginalny (FloraSense HF)",
        "mode_2": "Zaawansowany (Gemini AI)",
        "mode_3": "Hybrydowy (FloraSense + Weryfikacja Gemini)",
        "header_upload": "📷 Prześlij zdjęcie rośliny",
        "btn_identify": "Zidentyfikuj roślinę 🔍",
        "sidebar_settings": "Ustawienia",
        "api_key_label": "Klucz API Gemini (Tryb 2 i 3)",
        "api_key_help": "Pobierz darmowy klucz na aistudio.google.com",
        "result_header": "📊 Wyniki:",
        "spinner_running": "Przetwarzanie w trybie {mode}...",
        "prompt_gemini": "Zidentyfikuj tę roślinę. Podaj: Nazwę, Opis, Taksonomię i Zastosowania. Odpowiedz po polsku używając Markdown.",
        "prompt_hybrid": """
            Model lokalny (FloraSense) zidentyfikował tę roślinę jako '{label}'. 
            Przeanalizuj załączone zdjęcie i:
            1. Sprawdź, czy ta identyfikacja jest poprawna.
            2. Jeśli model lokalny się pomylił, podaj poprawną nazwę i wyjaśnij dlaczego.
            3. Przygotuj szczegółowy raport botaniczny (Nazwa, Taksonomia, Opis, Zastosowania).
            Odpowiedz po polsku używając Markdown. Nie używaj zbędnych wstępów.
        """
    }
}

# --- Silniki AI ---

@st.cache_resource
def load_hf_model():
    """Ładuje model Hugging Face do pamięci podręcznej."""
    return pipeline("image-classification", model="Sisigoks/FloraSense")

def run_hf_prediction(image):
    """Uruchamia klasyfikację modelem lokalnym."""
    classifier = load_hf_model()
    if image.mode != "RGB":
        image = image.convert("RGB")
    preds = classifier(image)
    return preds[0]["label"], preds[0]["score"]

def run_gemini_analysis(image, prompt, api_key):
    """Uruchamia analizę modelem Gemini 2.0 Flash."""
    if not api_key:
        return "⚠️ Error: API Key is missing! Please check the sidebar."
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=[prompt, image]
        )
        return response.text
    except Exception as e:
        return f"❌ API Error: {str(e)}"

# --- Główne UI ---

def main():
    # Wybór języka (Domyślnie pierwszy na liście - English)
    selected_lang = st.selectbox("🌐 Language / Język", list(TRANSLATIONS.keys()))
    lang = TRANSLATIONS[selected_lang]

    st.title(lang["title"])
    
    # Sidebar - Ustawienia
    with st.sidebar:
        st.header(lang["sidebar_settings"])
        
        mode_map = {
            lang["mode_1"]: "ORIGINAL",
            lang["mode_2"]: "GEMINI",
            lang["mode_3"]: "HYBRID"
        }
        selected_mode_label = st.radio(lang["mode_selection"], list(mode_map.keys()))
        current_mode = mode_map[selected_mode_label]
        
        api_key = ""
        if current_mode in ["GEMINI", "HYBRID"]:
            api_key = st.text_input(lang["api_key_label"], type="password", help=lang["api_key_help"])
        
        st.divider()
        if current_mode == "ORIGINAL":
            st.info("Using local model: FloraSense")
        else:
            st.info("Using cloud model: Gemini 2.0 Flash")

    # Upload zdjęcia
    st.subheader(lang["header_upload"])
    img_file = st.file_uploader(lang["header_upload"], type=["jpg", "jpeg", "png"], label_visibility="collapsed")

    if img_file:
        img = Image.open(img_file)
        # Podgląd zdjęcia (ograniczona szerokość dla estetyki)
        st.image(img, width=450)

        if st.button(lang["btn_identify"], type="primary"):
            with st.spinner(lang["spinner_running"].format(mode=selected_mode_label)):
                
                if current_mode == "ORIGINAL":
                    label, score = run_hf_prediction(img)
                    st.divider()
                    st.success(f"**Identified Species:** {label}")
                    st.info(f"**Confidence Score:** {score:.2%}")

                elif current_mode == "GEMINI":
                    result = run_gemini_analysis(img, lang["prompt_gemini"], api_key)
                    st.divider()
                    st.subheader(lang["result_header"])
                    st.markdown(result)

                elif current_mode == "HYBRID":
                    # Krok 1: Predykcja FloraSense
                    label, score = run_hf_prediction(img)
                    st.write(f"🔍 **FloraSense Suggestion:** {label} ({score:.2%})")
                    
                    # Krok 2: Weryfikacja przez Gemini
                    hybrid_prompt = lang["prompt_hybrid"].format(label=label)
                    result = run_gemini_analysis(img, hybrid_prompt, api_key)
                    
                    st.divider()
                    st.subheader(lang["result_header"])
                    st.markdown(result)

if __name__ == "__main__":
    main()