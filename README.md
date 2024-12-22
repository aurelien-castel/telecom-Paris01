# Wrapper avec Seccomp

Ce projet est un script Python qui utilise `seccomp` pour interdire l'ouverture de fichiers en écriture et exécuter des commandes en tant que sous-processus.

## Utilisation

### Exécution directe

1. Installez les dépendances :
   ```bash
   pip install seccomp
   ```
2. Lancez le script:
   ```bash
   python wrapper.py [command]
   ```
