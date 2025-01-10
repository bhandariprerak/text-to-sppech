# Text-to-Speech Converter

This is a simple Python application that converts user-provided text into an audio file using the Google Text-to-Speech (gTTS) library. The program supports multiple languages and allows users to dynamically switch between them.

---

## Features

- Converts text input into an audio file.
- Supports multiple languages (e.g., English, Spanish, French, etc.).
- Allows the user to select a language and switch it anytime.
- Offers an option to name the audio file or automatically generate one with a timestamp.

---

## Requirements

- Python 3.6 or higher
- `gTTS` library

---

## Installation

1. Clone the repository or download the script.
2. Install the required dependencies:

   ```bash
   pip install gtts

## Usage

1. Run the script:

   ```bash
   python3 main.py

2.	Follow the prompts:
	•	Select a language from the available options.
	•	Enter the text to convert into speech.
	•	Save the audio file with a custom name or let the program generate a timestamped filename.

## Example Interaction

### **Startup**
Welcome to the Text-to-Speech Converter!

Available Languages:
en: English
es: Spanish
fr: French
de: German
hi: Hindi
zh-cn: Chinese (Simplified)
ja: Japanese

Enter the language code of your choice: en
Language set to: English

### **Converting Text**
Options:
	1.	Convert text to speech
	2.	Change language
	3.	Exit

Enter your choice: 1

Enter the text you want to convert to speech: Hello, welcome to the text-to-speech program.
Enter a filename to save the audio or press Enter to auto-name the file:
Audio saved as: 2025-01-08_14-30-45.mp3

### **Switching Language**
Enter your choice: 2

Available Languages:
en: English
es: Spanish
fr: French
de: German
hi: Hindi
zh-cn: Chinese (Simplified)
ja: Japanese

Enter the language code of your choice: es
Language set to: Spanish

## Customization

- Modify the `languages` dictionary in the script to add or remove supported languages.
- Adjust the `strftime` format in the `text_to_speech` function to change the auto-generated filename format.

## License

This project is licensed under the [MIT License](LICENSE).