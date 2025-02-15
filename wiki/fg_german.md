# [리눅스] Bash fg 사용법

## Übersicht
Der Befehl `fg` (foreground) in Bash wird verwendet, um einen Hintergrundprozess in den Vordergrund zu bringen. Dies ist besonders nützlich, wenn Sie einen Prozess gestartet haben, der im Hintergrund läuft und Sie ihn wieder aktivieren möchten, um mit ihm zu interagieren. Der Befehl ermöglicht es Ihnen, die Kontrolle über diesen Prozess zurückzugewinnen, sodass Sie Eingaben tätigen und Ausgaben sehen können.

## Verwendung
Die grundlegende Syntax des Befehls `fg` lautet:

```bash
fg [Job-Nummer]
```

- **Job-Nummer**: Dies ist die optionale Argument, die angibt, welcher Hintergrundprozess in den Vordergrund gebracht werden soll. Wenn keine Job-Nummer angegeben wird, wird standardmäßig der zuletzt gestoppte oder in den Hintergrund geschobene Prozess verwendet.

## Beispiele
Hier sind einige praktische Beispiele zur Verwendung des Befehls `fg`:

1. **Einen Hintergrundprozess in den Vordergrund bringen**:
   Angenommen, Sie haben einen Prozess im Hintergrund gestartet, z.B. mit `sleep 60 &`. Um diesen Prozess in den Vordergrund zu bringen, verwenden Sie den Befehl:

   ```bash
   fg
   ```

   Dies bringt den zuletzt gestarteten Hintergrundprozess in den Vordergrund.

2. **Einen spezifischen Hintergrundprozess auswählen**:
   Wenn Sie mehrere Hintergrundprozesse haben, können Sie die Job-Nummer verwenden, um einen bestimmten Prozess auszuwählen. Zuerst können Sie die Liste der Jobs mit dem Befehl `jobs` anzeigen:

   ```bash
   jobs
   ```

   Angenommen, die Ausgabe zeigt, dass Job 1 und Job 2 im Hintergrund laufen. Um Job 1 in den Vordergrund zu bringen, verwenden Sie:

   ```bash
   fg %1
   ```

## Tipps
- Verwenden Sie den Befehl `jobs`, um eine Übersicht über alle laufenden Hintergrundprozesse zu erhalten, bevor Sie `fg` verwenden.
- Wenn Sie einen Prozess im Hintergrund starten möchten, verwenden Sie das `&`-Zeichen am Ende des Befehls, z.B. `command &`.
- Seien Sie vorsichtig, wenn Sie einen Prozess in den Vordergrund bringen, da dies die Eingabeaufforderung blockiert, bis der Prozess abgeschlossen ist oder Sie ihn erneut in den Hintergrund verschieben.