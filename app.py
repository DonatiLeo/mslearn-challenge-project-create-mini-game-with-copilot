
# Créez un mini-jeu Pierre-Feuille-Ciseaux contre l’ordinateur en python.
# L’ordinateur devra choisir aléatoirement entre Pierre, Feuille ou Ciseaux.
# Vous devrez choisir vous-même entre Pierre, Feuille ou Ciseaux.
# Ensuite le programme doit comparer les choix et afficher le résultat.
# Le programme doit également demander si vous voulez recommencer une partie.

# Liste des réponses possibles
answers = ['Pierre', 'Feuille', 'Ciseaux']

# Importation de la librairie random
import random

# Fonction pour demander à l'utilisateur de choisir entre Pierre, Feuille ou Ciseaux
def ask_user():
    user_answer = input("Choisissez entre Pierre, Feuille ou Ciseaux: ")
    return user_answer

# Fonction pour que l'ordinateur choisisse aléatoirement entre Pierre, Feuille ou Ciseaux
def computer_choice():
    computer_answer = random.choice(answers)
    return computer_answer

# Fonction pour comparer les choix de l'utilisateur et de l'ordinateur
def compare_choices(user_answer, computer_answer):
    if user_answer == computer_answer:
        return "Egalité"
    elif user_answer == "Pierre" and computer_answer == "Ciseaux":
        return "Vous avez gagné"
    elif user_answer == "Feuille" and computer_answer == "Pierre":
        return "Vous avez gagné"
    elif user_answer == "Ciseaux" and computer_answer == "Feuille":
        return "Vous avez gagné"
    else:
        return "Vous avez perdu"

# Fonction pour demander à l'utilisateur s'il veut recommencer une partie
def ask_replay():
    replay = input("Voulez-vous recommencer une partie? (oui/non): ")
    return replay

# Fonction principale
def main():
    replay = "oui"
    while replay == "oui":
        user_answer = ask_user()
        computer_answer = computer_choice()
        print(f"L'ordinateur a choisi: {computer_answer}")
        result = compare_choices(user_answer, computer_answer)
        print(result)
        replay = ask_replay()

# Appel de la fonction principale
main()

# Exécutez le code et testez le jeu Pierre-Feuille-Ciseaux contre l’ordinateur en python.

