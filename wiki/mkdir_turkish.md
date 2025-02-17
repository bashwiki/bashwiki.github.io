# [Linux] Bash mkdir Kullanımı: Klasör oluşturma komutu

## Overview
`mkdir` komutu, Linux ve diğer Unix benzeri işletim sistemlerinde yeni dizinler (klasörler) oluşturmak için kullanılır. Bu komut, kullanıcıların dosya sisteminde düzenli bir yapı kurmasına yardımcı olur.

## Usage
Temel sözdizimi şu şekildedir:
```bash
mkdir [options] [arguments]
```

## Common Options
- `-p`: Ara dizinleri de oluşturur. Yani, belirtilen yolun tamamını oluşturur.
- `-v`: Oluşturulan dizinlerin adlarını ekrana yazdırır.
- `-m`: Oluşturulan dizin için belirli bir izin ayarı yapar.

## Common Examples
Aşağıda `mkdir` komutunun bazı yaygın kullanım örnekleri bulunmaktadır:

1. Basit bir dizin oluşturma:
   ```bash
   mkdir yeni_klasor
   ```

2. Birden fazla dizin oluşturma:
   ```bash
   mkdir klasor1 klasor2 klasor3
   ```

3. Ara dizinlerle birlikte dizin oluşturma:
   ```bash
   mkdir -p ana_klasor/alt_klasor
   ```

4. Oluşturulan dizinlerin adlarını görüntüleme:
   ```bash
   mkdir -v yeni_klasor
   ```

5. Belirli izinlerle dizin oluşturma:
   ```bash
   mkdir -m 755 yeni_klasor
   ```

## Tips
- Dizin oluştururken `-p` seçeneğini kullanarak, birden fazla katmanlı dizin yapısını tek seferde oluşturabilirsiniz.
- Dizin adlarında boşluk kullanıyorsanız, çift tırnak içinde yazmayı unutmayın: `mkdir "yeni klasör"`.
- İzin ayarlarını dikkatli yapın; yanlış izinler, dizine erişimi kısıtlayabilir.