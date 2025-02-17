# [Linux] Bash tput utilizzo: Controlla l'aspetto del terminale

## Overview
Il comando `tput` è utilizzato per controllare le capacità del terminale, come il cambiamento dei colori del testo, la posizione del cursore e altre funzionalità di formattazione. Questo comando è particolarmente utile per migliorare l'interfaccia utente nei terminali.

## Usage
La sintassi di base del comando `tput` è la seguente:

```bash
tput [opzioni] [argomenti]
```

## Common Options
- `setaf [n]`: Imposta il colore del testo foreground (n è il numero del colore).
- `setab [n]`: Imposta il colore dello sfondo (n è il numero del colore).
- `clear`: Pulisce lo schermo del terminale.
- `cup [y] [x]`: Sposta il cursore alla posizione specificata (y è la riga, x è la colonna).
- `bold`: Imposta il testo in grassetto.

## Common Examples
Ecco alcuni esempi pratici dell'uso di `tput`:

1. **Impostare il colore del testo su rosso:**
   ```bash
   tput setaf 1
   echo "Questo testo è rosso"
   ```

2. **Impostare il colore dello sfondo su blu:**
   ```bash
   tput setab 4
   echo "Questo testo ha uno sfondo blu"
   ```

3. **Pulire lo schermo del terminale:**
   ```bash
   tput clear
   ```

4. **Spostare il cursore alla riga 5, colonna 10:**
   ```bash
   tput cup 5 10
   echo "Cursore spostato!"
   ```

5. **Impostare il testo in grassetto:**
   ```bash
   tput bold
   echo "Questo testo è in grassetto"
   ```

## Tips
- Ricorda di ripristinare i colori originali del terminale alla fine del tuo script utilizzando `tput sgr0` per evitare confusione.
- Puoi combinare più comandi `tput` in un'unica riga per creare messaggi colorati e formattati.
- Verifica la compatibilità del tuo terminale con i colori e le opzioni di `tput`, poiché alcune funzionalità potrebbero non essere supportate in tutti gli ambienti.