from tkinter import *

expression = ""


def appuyer(touch):
    if touch == "=":
        calculator()
        return

    global expression
    expression += str(touch)
    equation.set(expression)


def calculator():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("erreur")
        expression = ""


def effacer():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="#101419")

    gui.title("Calculatrice")

    gui.geometry("235x385")
    equation = StringVar()

    resulta = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height="2")
    resulta.grid(columnspan=4)

    boutons = [7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", 0, ".", "/", "="]
    ligne = 1
    colonne = 0
    for bouton in boutons:
        b = Label(gui, text=str(bouton), bg="#476C9B", fg="white", height=4, width=6)
        b.bind("<Button-1>", lambda event, bouton=bouton: appuyer(bouton))
        b.grid(row=ligne, column=colonne)

        colonne += 1
        if colonne == 4:
            colonne = 0
            ligne += 1

    # Utiliser une nouvelle variable pour le Label "EFFACER"
    effacer_label = Label(gui, text="EFFACER", bg="#9B4447", fg="white", height=4, width=26)
    effacer_label.bind("<Button-1>", lambda event: effacer())
    effacer_label.grid(columnspan=4)

    gui.mainloop()
