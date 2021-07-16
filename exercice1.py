print("Hello 😝")

# Je reprend l'exo Todolist :

# Initialisation du dictionnaire : la clé/index sera le nom de nos taches
#                                  la valeur sera un boolean et representant le statut (false : pas fait, true : fait).
todo:dict = {}

# Affichage de la liste de tache (Elle est vide, pas besoin de boucle pour le moment.)
print("Liste des tâches ✌ :")
print("---------------------")
print("Pour ajoutez appuyé sur '+' ")
print("Pour modifié le statut appuyé sur le numéro correspondant.😎")

# Par rapport aux options donnés a l'utilisateur, je boucle si '+' ou valeur numérique.
user_input:str = input()

while user_input == "+" or user_input.isdigit():
    # Si l'utilisateur a entré '+', on se doit d'ajoutez dans notre dico une nouvelle tâche.
    if user_input == "+":
        task_name:str = input("Entrez le nom de la tache :\n")
        # On verifie que la tache n'existe pas deja dans le dico ;
        if task_name in todo.keys() :         # Keys = élément entré dans le dict.(liste)
            print("Tâche déja encodée.")
        # Sinon , on ajoute la tache avec la valeur False , statut donc NON-FAIT
        else :
            todo[task_name] = False
    # Si il s'agit d'un nomvre compris entre 1 et la taille du tableau
    elif len(todo) > 0 and int(user_input) >= 1 and int(user_input) <= len(todo):
        # On recupere le nom de notre cle : parmis la liste des cle, on la transforme en une liste pour utiliser l'index numérique
        task_name:str = list(todo.keys())[int(user_input)-1]
        # Inversion du boolean avec le not de la tache:
        todo[task_name] = not todo[task_name]

    # Si pas "+" ou un nombre correct, mauvaise commande..
    else :
        print("Mauvaise commande.😢")

    # Affiche la liste
    print("Liste des tâches ✌ :")
    print("---------------------")
    # Boucle sur la liste avec un enumerate l'index sera l'index des cle et la valeur , le nom de vos cle.
    for index, task in enumerate(todo):
        # Si le statut est true : ces fait on ajuste un "X - "
        if (todo[task]) :
            print(f'{index+1}. X - {task}')
        #Sinon on ajoute rien.
        else :
            print(f'{index+1}. {task}')
    print("Pour ajoutez appuyé sur '+' ")
    print("Pour modifié le statut appuyé sur le numéro correspondant.😎")
    user_input:str = input()

print("Merci d'avoir utilisez To Do List 3000 😉 !")