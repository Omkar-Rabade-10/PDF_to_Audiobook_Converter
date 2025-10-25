# PDF_to_Audiobook_Converter
"A Python project that converts PDF text into spoken audio (audiobook).”
📘 PDF to Audiobook Converter
🎯 Project Overview

The PDF to Audiobook Converter is a Python-based application that extracts text from PDF files and converts it into spoken audio.
This project helps users — especially students, audiobook enthusiasts, and visually impaired individuals — listen to their documents instead of reading them.

🧠 Key Features

🎤 Converts any PDF text into MP3 audio format

🪟 Simple and user-friendly GUI using Tkinter

⚙️ Works completely offline (uses pyttsx3)

🧾 Saves audio file automatically in the same folder as the selected PDF

📂 Supports any standard .pdf file

🧰 Tools and Libraries Used
Library	Purpose
PyMuPDF (fitz)	Extracts text from PDF files
pyttsx3	Converts text into speech
Tkinter	Builds the graphical user interface
os	Handles file paths and saving output
⚙️ How to Run the Project
1️⃣ Install Required Libraries

Open terminal or PowerShell and run:

pip install PyMuPDF pyttsx3

2️⃣ Run the Application
python pdf_to_audiobook.py

3️⃣ Convert Your PDF

Click “Select PDF & Convert”

Choose your .pdf file

Wait a few seconds — a success pop-up will appear

Your audiobook (_audiobook.mp3) is saved in the same folder as your PDF
