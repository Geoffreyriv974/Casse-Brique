from tkinter import *


def score():

    file_path = "tableau_scores.xlsx"

    try:

        with open(file_path, "r") as file:
            file_content = file.read()

        board_windows = Toplevel()
        board_windows.title("Contenu du fichier texte")
        board_windows.resizable(height=False, width=False)

        text_label = Label(board_windows, text=file_content)
        text_label.pack()

    except FileNotFoundError:
        print("Le fichier prédéfini n'a pas été trouvé.")