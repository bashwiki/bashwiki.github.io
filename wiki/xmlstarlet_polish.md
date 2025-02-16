# [Linux] Bash xmlstarlet użycie: Narzędzie do przetwarzania XML

## Overview
`xmlstarlet` to potężne narzędzie wiersza poleceń do przetwarzania i manipulacji dokumentami XML. Umożliwia użytkownikom wykonywanie różnych operacji, takich jak walidacja, transformacja, czy ekstrakcja danych z plików XML.

## Usage
Podstawowa składnia polecenia `xmlstarlet` wygląda następująco:

```bash
xmlstarlet [options] [arguments]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `xmlstarlet`:

- `xmlstarlet sel`: Wybiera dane z dokumentu XML.
- `xmlstarlet ed`: Edytuje dokument XML.
- `xmlstarlet val`: Waliduje dokument XML względem schematu.
- `xmlstarlet tr`: Przeprowadza transformację dokumentu XML przy użyciu XSLT.
- `xmlstarlet fo`: Formatuje dokument XML, aby był bardziej czytelny.

## Common Examples

### Wybieranie elementów XML
Aby wybrać elementy z dokumentu XML, można użyć polecenia `sel`:

```bash
xmlstarlet sel -t -m "//book" -v "title" -n books.xml
```

### Edytowanie dokumentu XML
Aby dodać nowy element do dokumentu XML, użyj polecenia `ed`:

```bash
xmlstarlet ed -s /library -t -n newbook -v "Nowa Książka" library.xml
```

### Walidacja dokumentu XML
Aby zweryfikować, czy dokument XML jest zgodny z określonym schematem, użyj polecenia `val`:

```bash
xmlstarlet val -e schema.xsd document.xml
```

### Transformacja dokumentu XML
Aby przekształcić dokument XML przy użyciu XSLT, użyj polecenia `tr`:

```bash
xmlstarlet tr transform.xsl input.xml > output.xml
```

### Formatowanie dokumentu XML
Aby sformatować dokument XML dla lepszej czytelności, użyj polecenia `fo`:

```bash
xmlstarlet fo input.xml > formatted.xml
```

## Tips
- Zawsze twórz kopie zapasowe swoich plików XML przed ich edytowaniem, aby uniknąć utraty danych.
- Używaj opcji `-v` w poleceniach, aby uzyskać bardziej szczegółowe informacje o błędach.
- Eksperymentuj z różnymi opcjami `xmlstarlet`, aby odkryć pełen potencjał narzędzia w przetwarzaniu XML.