ouai les gens voici les commandes dont vous aurez potentiellement besoins. a noter que ce sont des commande a éxécuter depuis un terminal dans un dossier contenant un dossier .git (le dossier est caché si vous avez désactivé les fichier cachés)

si vous voulez créer une branche sur git la commande c'est 'git checkout -b nomBranche' n'oubliez pas de push au moins une fois pour que la branche soit créee.

si vous voulez changer de branche : git checkout nomBranche

si vous voulez push votre travail sur github utiliser les 3 commandes consécutives :

git add *
git commit -m 'mettre une description des changements apportés'
git push origin nomBranche
pour récupérer la dernière version du code qui est sur github vous utiliserez la commande 'git pull origin nomBranche'

pour récupérer un clone du projet utilisez 'git clone urlRepository'