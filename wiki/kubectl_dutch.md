# [Linux] Bash kubectl gebruik: Beheer Kubernetes-clusters

## Overzicht
De `kubectl`-opdracht is een krachtige commandoregeltool die wordt gebruikt om te communiceren met Kubernetes-clusters. Met `kubectl` kunnen gebruikers verschillende taken uitvoeren, zoals het implementeren van applicaties, het beheren van clusterbronnen en het bekijken van logs.

## Gebruik
De basis syntaxis van de `kubectl`-opdracht is als volgt:

```bash
kubectl [opties] [argumenten]
```

## Veelvoorkomende opties
- `get`: Haal informatie op over verschillende Kubernetes-resources.
- `apply`: Pas configuraties toe op resources in het cluster.
- `delete`: Verwijder resources uit het cluster.
- `describe`: Toon gedetailleerde informatie over een specifieke resource.
- `logs`: Bekijk de logs van een specifieke pod.

## Veelvoorkomende voorbeelden

### 1. Informatie over pods ophalen
```bash
kubectl get pods
```

### 2. Een nieuwe deployment toepassen
```bash
kubectl apply -f deployment.yaml
```

### 3. Een specifieke pod verwijderen
```bash
kubectl delete pod naam-van-de-pod
```

### 4. Gedetailleerde informatie over een service bekijken
```bash
kubectl describe service naam-van-de-service
```

### 5. Logs van een pod bekijken
```bash
kubectl logs naam-van-de-pod
```

## Tips
- Gebruik de `--help` optie om meer te leren over specifieke commando's: `kubectl get --help`.
- Maak gebruik van contexten om eenvoudig tussen verschillende clusters te schakelen.
- Houd je Kubernetes-configuratiebestanden georganiseerd voor een betere beheersbaarheid.