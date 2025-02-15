# [리눅스] Bash tput 사용법

## Overview
Il comando `tput` è uno strumento della shell Unix che consente di controllare le proprietà del terminale. La sua funzione principale è quella di fornire un'interfaccia per l'accesso alle capacità del terminale definite nel database terminfo. Con `tput`, gli sviluppatori possono modificare l'aspetto del testo nel terminale, come il colore, lo stile e la posizione del cursore, migliorando l'interazione dell'utente con le applicazioni a riga di comando.

## Usage
La sintassi di base del comando `tput` è la seguente:

```bash
tput [opzione] [parametro]
```

Alcune delle opzioni comuni includono:

- `setaf`: Imposta il colore del testo (foreground).
- `setab`: Imposta il colore dello sfondo (background).
- `clear`: Pulisce lo schermo del terminale.
- `cup`: Posiziona il cursore a una posizione specifica (righe e colonne).
- `bold`: Attiva il testo in grassetto.
- `smso`: Attiva il testo in modalità sottolineata.

## Examples
Ecco alcuni esempi pratici di utilizzo del comando `tput`.

### Esempio 1: Cambiare il colore del testo
Per cambiare il colore del testo in rosso, puoi utilizzare il seguente comando:

```bash
tput setaf 1; echo "Questo testo è rosso"; tput sgr0
```

In questo esempio, `setaf 1` imposta il colore del testo su rosso (1 è il codice del colore rosso), e `sgr0` ripristina le impostazioni predefinite del terminale.

### Esempio 2: Pulire lo schermo e posizionare il cursore
Per pulire lo schermo e posizionare il cursore nella riga 5, colonna 10, utilizza il comando:

```bash
tput clear; tput cup 5 10; echo "Cursore posizionato qui"
```

Qui, `clear` pulisce lo schermo e `cup 5 10` sposta il cursore alla posizione specificata.

## Tips
- Utilizza `tput` in script per migliorare l'interfaccia utente dei tuoi programmi a riga di comando.
- Puoi combinare più comandi `tput` in una singola riga per creare effetti complessi.
- Ricorda di ripristinare le impostazioni del terminale con `tput sgr0` dopo aver applicato modifiche per evitare che le impostazioni rimangano attive dopo l'esecuzione del tuo script.
- Per scoprire quali capacità sono disponibili nel tuo terminale, puoi utilizzare il comando `infocmp`.