🌿 PlantVerse AR - Advanced Plant Identification
PlantVerse AR is a modern, multilingual interactive tool designed to identify plants using cutting-edge AI and explore their natural habitats. This version features a significant upgrade including a dual-model verification system.
✨ Key Features
Hybrid AI Identification: A sophisticated pipeline combining the local FloraSense model with Gemini 2.0 Flash for expert-level verification.
Multilingual Support: Full interface and botanical analysis available in both English (Default) and Polish.
Location Mapping: Discover real-time plant observations nearby using integrated iNaturalist data.
Botanical Insights: Comprehensive reports featuring scientific taxonomy, detailed descriptions, and traditional medicinal uses.
🛠️ Identification Engines
Original (FloraSense): Fast, local classification using the FloraSense (Hugging Face) model, ideal for quick species labeling.
Advanced (Gemini AI): Deep multimodal analysis powered by Google's latest Gemini 2.0 Flash model.
Hybrid (Verification): The most accurate mode. The local model provides an initial prediction which is then analyzed, verified, or corrected by Gemini AI.
🚀 Getting Started
Prerequisites:
Python 3.10 or higher.
A Google Gemini API Key (Available for free at Google AI Studio).
Installation Steps:
Clone the repository: Use the git clone command followed by your fork's URL.
Enter the directory: Use the cd PlantVerse command.
Install dependencies: Run pip install -r requirements.txt in your terminal.
Launch the application: Run streamlit run app.py to start the web interface.
📦 Technology Stack
Framework: Streamlit
AI Models: Gemini 2.0 Flash, FloraSense (Transformers/PyTorch)
APIs: iNaturalist, Google AI Studio
Core Language: Python 3.10+
This project has been modernized to support advanced AI ensembles and improved user accessibility.
