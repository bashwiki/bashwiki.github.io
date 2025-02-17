# [Linux] Bash getopts Kullanımı: Komut satırı seçeneklerini işleme

## Overview
`getopts`, Bash betiklerinde komut satırı seçeneklerini işlemek için kullanılan bir yerleşik komuttur. Kullanıcıdan gelen seçenekleri ve argümanları kolayca analiz etmeye yardımcı olur, böylece betiklerinizde esneklik ve kontrol sağlar.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
getopts [seçenekler] [argümanlar]
```

## Common Options
- `-a`: Seçeneklerin birden fazla kez kullanılmasına izin verir.
- `-l`: Uzun seçenek adlarını destekler.
- `-n`: Hata mesajlarında betik adını belirtir.
- `-o`: Seçeneklerin sırasını belirler.

## Common Examples

### Basit Kullanım
Aşağıdaki örnekte, `-f` seçeneği ile bir dosya adı alınıyor:

```bash
#!/bin/bash
while getopts "f:" opt; do
  case $opt in
    f) echo "Dosya adı: $OPTARG" ;;
    *) echo "Geçersiz seçenek" ;;
  esac
done
```

### Birden Fazla Seçenek
Birden fazla seçeneği işlemek için aşağıdaki gibi bir yapı kullanabilirsiniz:

```bash
#!/bin/bash
while getopts "a:b:c:" opt; do
  case $opt in
    a) echo "A seçeneği: $OPTARG" ;;
    b) echo "B seçeneği: $OPTARG" ;;
    c) echo "C seçeneği: $OPTARG" ;;
    *) echo "Geçersiz seçenek" ;;
  esac
done
```

### Varsayılan Değerler
Varsayılan değerler belirlemek için aşağıdaki örneği inceleyebilirsiniz:

```bash
#!/bin/bash
value="varsayılan"
while getopts "v:" opt; do
  case $opt in
    v) value="$OPTARG" ;;
    *) echo "Geçersiz seçenek" ;;
  esac
done
echo "Değer: $value"
```

## Tips
- Seçeneklerinizi tanımlarken, her bir seçeneğin ardından iki nokta (:) koyarak argüman gerektirdiğini belirtin.
- Hatalı seçenekler için kullanıcı dostu hata mesajları sağlamaya özen gösterin.
- Betiğinizin sonunda, işlenen seçenekleri ve argümanları özetleyen bir çıktı vermek, kullanıcı deneyimini artırabilir.