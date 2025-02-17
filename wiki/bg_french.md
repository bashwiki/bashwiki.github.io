# [Linux] Bash bg Utilisation : Mettre un processus en arrière-plan

## Overview
La commande `bg` est utilisée dans un terminal Bash pour reprendre un processus suspendu et le faire fonctionner en arrière-plan. Cela permet à l'utilisateur de continuer à utiliser le terminal pour d'autres tâches tout en laissant le processus en cours d'exécution.

## Usage
La syntaxe de base de la commande `bg` est la suivante :

```bash
bg [options] [job_spec]
```

## Common Options
- `job_spec` : Spécifie le travail à reprendre en arrière-plan. Cela peut être un numéro de travail (par exemple, `%1`) ou un identifiant de processus (PID).

## Common Examples

### Exemple 1 : Reprendre un processus suspendu
Si vous avez suspendu un processus avec `Ctrl+Z`, vous pouvez le reprendre en arrière-plan avec :

```bash
bg
```

### Exemple 2 : Reprendre un processus spécifique
Pour reprendre un processus spécifique (par exemple, le travail numéro 1), utilisez :

```bash
bg %1
```

### Exemple 3 : Reprendre un processus avec un PID
Si vous connaissez le PID du processus, vous pouvez le reprendre en arrière-plan avec :

```bash
bg %<PID>
```

## Tips
- Utilisez `jobs` pour lister tous les travaux en cours et leurs états avant d'utiliser `bg`.
- Vous pouvez combiner `bg` avec `disown` pour détacher un processus de votre terminal, ce qui permet à ce dernier de continuer à s'exécuter même après la fermeture du terminal.
- Faites attention à la gestion des ressources, car plusieurs processus en arrière-plan peuvent consommer beaucoup de mémoire ou de CPU.