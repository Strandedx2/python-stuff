import pyttsx3
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import threading

def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            content = ""
            for page in reader.pages:
                content += page.extract_text() or ""
            return content
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read PDF: {e}")
        return None

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")],
        title="Select a PDF file"
    )
    if file_path:
        messagebox.showinfo("Reading", "Extracting text from PDF. Please wait...")
        content = read_pdf(file_path)
        if content and content.strip():
            clean_preview = ' '.join(content.split())
            preview = clean_preview[:500] + ("..." if len(clean_preview) > 500 else "")
            messagebox.showinfo("Text Extracted", f"Preview:\n{preview}")
            # Run speak_text in a new thread
            threading.Thread(target=speak_text, args=(content,), daemon=True).start()
        else:
            messagebox.showwarning("No Text Found", "No extractable text found in this PDF.")

def main():
    root = tk.Tk()
    root.title("Auto Book Reader")
    root.geometry("400x200")

    label = tk.Label(root, text="Drag and drop a PDF or click to select", font=("Arial", 14))
    label.pack(pady=40)

    button = tk.Button(root, text="Select PDF", command=open_file, font=("Arial", 12))
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()