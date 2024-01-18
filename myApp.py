import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

# Создаем базовое окно
root = tk.Tk()
# Создаем холст и менеджер разметки grid
""" Определяем размеры холста width=600, height=300
 А в grid определяем сколько столбцов и строк должен занимать элемент columnspan=3, rowspan=3
 """
canvas = tk.Canvas(root, width=600, height=300).grid(columnspan=3, rowspan=3)
# Создаем логотип
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Создаем лейбл для текста, определяем шрифт font='Constantia'
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font='Constantia')
# Определяем columnspan=3-сколько будет занимать колон Label, column=0, row=1 -определяем какое место будет занимать Label
instructions.grid(columnspan=3, column=0, row=1)

# Создаем функцию для обработки события нажатие кнопки
def open_file():
    browse_text.set('loading...')
    file = askopenfile(parent=root, mode='rb', title='chose a file', filetype=[('pdf file', '*.pdf')])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]
        page_content = page.extract_text()
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure('center', justify='center')
        text_box.tag_add('center', 1.0, 'end')
        text_box.grid(column=1, row=3)

        browse_text.set('Browse')


browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), font='Constantia', bg="#20bebe",
                       fg="white", height=2, width=15)
browse_text.set('Browse')
browse_btn.grid(column=1, row=2)
canvas = tk.Canvas(root, width=600, height=300).grid(columnspan=3)
if __name__ == '__main__':
    root.mainloop()
