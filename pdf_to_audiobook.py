# 📘 PDF to Audiobook Converter
# Developed by: [Your Name]
# Description: Converts PDF text into spoken audio (MP3 format)

import fitz          # PyMuPDF
import pyttsx3       # Text-to-Speech
from tkinter import *
from tkinter import filedialog, messagebox
import os

# Function to extract text from selected PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        pdf = fitz.open(pdf_path)
        for page in pdf:
            text += page.get_text()
        pdf.close()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read PDF:\n{e}")
    return text

# Function to convert extracted text to audio
def convert_to_audio(text, output_file):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)      # speaking speed
        engine.setProperty('volume', 0.9)    # volume level
        engine.save_to_file(text, output_file)
        engine.runAndWait()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate audio:\n{e}")

# Function triggered by "Convert" button
def convert_pdf_to_audio():
    pdf_path = filedialog.askopenfilename(
        title="Select PDF File", filetypes=[("PDF Files", "*.pdf")]
    )
    if not pdf_path:
        return

    messagebox.showinfo("Processing", "Extracting text from PDF, please wait...")
    text = extract_text_from_pdf(pdf_path)

    if not text.strip():
        messagebox.showerror("Empty PDF", "No readable text found in PDF!")
        return

    output_file = os.path.splitext(pdf_path)[0] + "_audiobook.mp3"
    convert_to_audio(text, output_file)

    messagebox.showinfo("Success", f"Audiobook created:\n{output_file}")

# --- GUI Section ---
root = Tk()
root.title("📘 PDF to Audiobook Converter")
root.geometry("400x250")
root.config(bg="#f0f0f0")

Label(
    root,
    text="PDF to Audiobook Converter",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    fg="#1a73e8"
).pack(pady=20)

Label(
    root,
    text="Select a PDF and convert it into an MP3 audiobook",
    bg="#f0f0f0"
).pack(pady=5)

Button(
    root,
    text="Select PDF & Convert",
    command=convert_pdf_to_audio,
    bg="#1a73e8",
    fg="white",
    font=("Arial", 12),
    width=20,
    height=2
).pack(pady=30)

Label(
    root,
    text="Developed in Python 🐍",
    bg="#f0f0f0",
    fg="gray"
).pack(side=BOTTOM, pady=10)

root.mainloop()
