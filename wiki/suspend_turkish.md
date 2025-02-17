# [Linux] Bash suspend Kullanımı: Arka planda işlemi duraklatma

## Overview
`suspend` komutu, bir terminal oturumundaki aktif işlemi geçici olarak duraklatmak için kullanılır. Bu komut, genellikle bir işlemi arka planda çalıştırmak ve daha sonra devam ettirmek amacıyla kullanılır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
suspend [options] [arguments]
```

## Common Options
- `-h`, `--help`: Komut hakkında yardım bilgisi gösterir.
- `-v`, `--version`: Komutun sürüm bilgisini gösterir.

## Common Examples
Aşağıda `suspend` komutunun bazı pratik örnekleri bulunmaktadır:

### Örnek 1: Geçici Olarak Durdurma
Bir terminalde çalışan bir işlemi duraklatmak için `Ctrl + Z` tuş kombinasyonunu kullanabilirsiniz. Bu, işlemi duraklatır ve arka plana alır.

```bash
# Bir işlem başlatın
sleep 100

# Ardından duraklatmak için Ctrl + Z tuşlarına basın
```

### Örnek 2: Durdurulan İşlemi Devam Ettirme
Durdurulan bir işlemi devam ettirmek için `fg` komutunu kullanabilirsiniz.

```bash
# Durdurulan işlemi devam ettirmek için
fg
```

### Örnek 3: Arka Planda Çalıştırma
Durdurulan bir işlemi arka planda çalıştırmak için `bg` komutunu kullanabilirsiniz.

```bash
# Durdurulan işlemi arka planda çalıştırmak için
bg
```

## Tips
- `Ctrl + Z` ile duraklatılan işlemleri takip etmek için `jobs` komutunu kullanabilirsiniz.
- Durdurulan işlemleri yönetmek için `fg` ve `bg` komutlarını etkili bir şekilde kullanın.
- İşlemleri duraklatmak, uzun süren görevlerde terminali serbest bırakmak için faydalıdır.