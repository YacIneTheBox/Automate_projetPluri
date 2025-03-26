import tkinter as tk

# Définition de l'automate
states = {'q0', 'q1', 'q2', 'sink'}
alphabet = {'A', '$', '£', 'e', 'o'}
initial_state = 'q0'
accepting_state = 'q2'

transition = {
    ('q0', 'A'): 'q2',
    ('q0', '$'): 'q1',
    ('q0', '£'): 'q1',
    ('q1', 'A'): 'q2',
    ('q1', '$'): 'sink',
    ('q1', '£'): 'sink',
    ('q2', 'A'): 'sink',
    ('q2', '$'): 'sink',
    ('q2', '£'): 'sink',
    ('q2', 'e'): 'q0',
    ('q2', 'o'): 'q0',
}

# Fonction pour simuler l'automate (corrigée)
def run_dfa(input_string):
    current_state = initial_state
    for symbol in input_string:
        if symbol not in alphabet:
            return False, f"{symbol} n'est pas dans l'alphabet"
        # Utilisation de .get() pour gérer les transitions non définies
        current_state = transition.get((current_state, symbol), 'sink')
        print(f"Après lecture de '{symbol}', état actuel : {current_state}")
    if current_state == accepting_state:
        return True, "Chaîne acceptée"
    else:
        return False, "Chaîne rejetée"

# Fonction pour tester la chaîne entrée
def test_string():
    input_string = entry.get()
    accepted, message = run_dfa(input_string)
    result_label.config(text=message)

# Fonction pour quitter l'application
def quit_app():
    root.destroy()

# Création de l'interface graphique
root = tk.Tk()
root.title("Testeur d'automate")
root.minsize(300, 200)
# Champ de texte pour entrer la chaîne
tk.Label(root, text="Entrez une chaîne :").pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack()

# Bouton pour tester la chaîne
test_button = tk.Button(root, text="Tester", command=test_string)
test_button.pack(pady=10)

# Label pour afficher le résultat
result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack(pady=10)

# Bouton pour quitter
quit_button = tk.Button(root, text="Quitter", command=quit_app)
quit_button.pack(pady=10)

# Lancer l'application
root.mainloop()