# [리눅스] Bash tr 사용법

## Genel Bakış
`tr` (translate) komutu, bir karakter dizisini başka bir karakter dizisi ile değiştirmek için kullanılan bir Unix/Linux komutudur. Genellikle metin dosyalarında belirli karakterleri değiştirmek, silmek veya dönüştürmek için kullanılır. `tr`, standart girdi (stdin) ile çalışır ve çıktıyı standart çıkışa (stdout) yönlendirir.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
tr [seçenekler] [arama_karakterleri] [değiştirme_karakterleri]
```

### Yaygın Seçenekler
- `-d`: Belirtilen karakterleri siler.
- `-s`: Ardışık aynı karakterleri birleştirir (sıkıştırır).
- `-c`: Belirtilen karakterler dışındaki tüm karakterleri işler.

## Örnekler

### Örnek 1: Karakter Değiştirme
Aşağıdaki komut, "hello" kelimesindeki 'e' harfini 'a' harfi ile değiştirir:

```bash
echo "hello" | tr 'e' 'a'
```
Çıktı:
```
hallo
```

### Örnek 2: Karakter Silme
Aşağıdaki komut, "hello world" ifadesinden 'l' harflerini siler:

```bash
echo "hello world" | tr -d 'l'
```
Çıktı:
```
heo word
```

## İpuçları
- `tr` komutunu kullanırken, girdi verisinin bir dosyadan okunması gerekiyorsa, `cat` komutuyla birlikte kullanabilirsiniz:
  ```bash
  cat dosya.txt | tr 'a-z' 'A-Z'
  ```
- `tr` komutunun çıktısını bir dosyaya yönlendirmek için `>` operatörünü kullanabilirsiniz:
  ```bash
  echo "hello" | tr 'e' 'a' > yeni_dosya.txt
  ```
- Karakter setlerini belirtirken, birden fazla karakteri aynı anda değiştirmek için eşit sayıda karakter belirtmeyi unutmayın. Örneğin, `tr 'abc' 'xyz'` komutu 'a' harfini 'x', 'b' harfini 'y' ve 'c' harfini 'z' ile değiştirir.