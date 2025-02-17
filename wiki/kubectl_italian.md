# [Linux] Bash kubectl utilizzo: Gestire i cluster Kubernetes

## Overview
Il comando `kubectl` è uno strumento da riga di comando utilizzato per interagire con i cluster Kubernetes. Permette agli utenti di eseguire operazioni come il deployment di applicazioni, il monitoraggio delle risorse e la gestione dei servizi all'interno di un cluster.

## Usage
La sintassi di base del comando `kubectl` è la seguente:

```bash
kubectl [options] [arguments]
```

## Common Options
Ecco alcune opzioni comuni per `kubectl`:

- `get`: Recupera informazioni su risorse specifiche.
- `apply`: Applica modifiche a risorse Kubernetes da un file di configurazione.
- `delete`: Elimina risorse specifiche dal cluster.
- `describe`: Mostra dettagli su una risorsa specifica.
- `logs`: Recupera i log di un pod.

## Common Examples
Ecco alcuni esempi pratici di utilizzo di `kubectl`:

### 1. Ottenere informazioni sui pod
```bash
kubectl get pods
```

### 2. Applicare una configurazione da un file YAML
```bash
kubectl apply -f deployment.yaml
```

### 3. Eliminare un pod specifico
```bash
kubectl delete pod nome-del-pod
```

### 4. Descrivere un servizio
```bash
kubectl describe service nome-del-servizio
```

### 5. Visualizzare i log di un pod
```bash
kubectl logs nome-del-pod
```

## Tips
- Utilizza `kubectl get all` per visualizzare tutte le risorse nel tuo namespace corrente.
- Aggiungi l'opzione `-n nome-namespace` per specificare un namespace diverso.
- Usa `kubectl config use-context nome-contesto` per cambiare il contesto attivo se gestisci più cluster.
- Salva frequentemente i tuoi file di configurazione in un sistema di controllo versione per tenere traccia delle modifiche.