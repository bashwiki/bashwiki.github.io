# [Linux] Bash curl utilizzo: Strumento per trasferire dati da o verso un server

## Overview
Il comando `curl` è uno strumento da riga di comando utilizzato per trasferire dati da o verso un server. Supporta vari protocolli, tra cui HTTP, HTTPS, FTP e molti altri. È particolarmente utile per testare API e scaricare file.

## Usage
La sintassi di base del comando `curl` è la seguente:

```bash
curl [options] [arguments]
```

## Common Options
Ecco alcune opzioni comuni di `curl` con brevi spiegazioni:

- `-X`: Specifica il metodo HTTP da utilizzare (GET, POST, PUT, DELETE, ecc.).
- `-d`: Invia dati nel corpo della richiesta (utilizzato principalmente con POST).
- `-H`: Aggiunge un'intestazione HTTP personalizzata.
- `-o`: Salva l'output in un file specificato.
- `-I`: Recupera solo le intestazioni della risposta.
- `-L`: Segue i reindirizzamenti.

## Common Examples
Ecco alcuni esempi pratici di utilizzo di `curl`:

### Esempio 1: Effettuare una richiesta GET
```bash
curl https://api.example.com/data
```

### Esempio 2: Effettuare una richiesta POST con dati
```bash
curl -X POST -d "nome=Mario&cognome=Rossi" https://api.example.com/submit
```

### Esempio 3: Aggiungere un'intestazione personalizzata
```bash
curl -H "Authorization: Bearer TOKEN" https://api.example.com/protected
```

### Esempio 4: Salvare l'output in un file
```bash
curl -o file.txt https://example.com/download
```

### Esempio 5: Recuperare solo le intestazioni della risposta
```bash
curl -I https://example.com
```

## Tips
- Utilizza l'opzione `-L` se stai lavorando con URL che potrebbero reindirizzare a un'altra posizione.
- Per testare rapidamente le API, puoi utilizzare `curl` insieme a `jq` per formattare l'output JSON.
- Ricorda di proteggere le informazioni sensibili, come i token di accesso, quando utilizzi `curl` in script o nella riga di comando.