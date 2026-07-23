# CLI Task Manager

## Features

Le client peut:

- Créer une nouvelle task
- Afficher toutes les tasks
- Consulter une task particulière
- Modifier une task existante
- Supprimer une task
- Marquer une task comme terminée
- Remettre une task en cours
- Filtrer les tasks (en cours , terminées, les 2 à la fois)

## Architecture du projet

- Un fichier pour implémenter chaque feature, (ou un dossier de features avec plusieurs dossiers ou seront les features sous forme de fichier )
- Un dossier  qui possede le format de stockage des datas c'st a dire les tasks(soit dans une liste liste , soit dans un fichier),
- Un fichier  principal

## Contraintes du projet

- Chaque task doit avoir un *identifiant , un nom , une description , une date de création.*
- Des tasks peuvent avoir le même nom
- Un *user* ne peut ni modifier , ni supprimer une task inexistante.

## Utilisateur du système

Le *gestionnaire des tasks*
