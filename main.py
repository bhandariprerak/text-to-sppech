from datetime import datetime
from gtts import gTTS
import os

# Supported languages dictionary
languages = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "hi": "Hindi",
    "zh-cn": "Chinese (Simplified)",
    "ja": "Japanese"
}

def show_language_options():
    print("\nAvailable Languages:")
    for code, name in languages.items():
        print(f"{code}: {name}")

def get_language_choice():
    while True:
        show_language_options()
        lang = input("\nEnter the language code of your choice: ").strip().lower()
        if lang in languages:
            print(f"Language set to: {languages[lang]}")
            return lang
        else:
            print("Invalid choice. Please choose a valid language code.")

def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language)
    filename = input("Enter a filename to save the audio or press Enter to auto-name the file: ").strip()
    if not filename:
        filename =  datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".mp3"
    tts.save(filename)
    print(f"Audio saved as: {filename}")

def main():
    print("Welcome to the Text-to-Speech Converter!")
    current_language = get_language_choice()
    
    while True:
        print("\nOptions:")
        print("1. Convert text to speech")
        print("2. Change language")
        print("3. Exit")
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            text = input("\nEnter the text you want to convert to speech: ").strip()
            text_to_speech(text, current_language)
        elif choice == "2":
            current_language = get_language_choice()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()