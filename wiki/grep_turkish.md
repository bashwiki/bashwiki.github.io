# [리눅스] Bash grep 사용법

## Genel Bakış
`grep`, metin dosyalarında belirli bir deseni aramak için kullanılan güçlü bir komuttur. "Global Regular Expression Print" ifadesinin kısaltmasıdır. Genellikle log dosyalarını incelemek, belirli bir kelime veya ifade içeren satırları bulmak ve metin dosyalarını filtrelemek için kullanılır. `grep`, düzenli ifadeleri destekleyerek karmaşık arama işlemlerini gerçekleştirmeye olanak tanır.

## Kullanım
Temel `grep` komutunun sözdizimi aşağıdaki gibidir:

```bash
grep [seçenekler] 'desen' dosya_adı
```

### Yaygın Seçenekler
- `-i`: Büyük/küçük harf duyarsız arama yapar.
- `-v`: Deseni içermeyen satırları gösterir.
- `-r` veya `-R`: Alt dizinler dahil olmak üzere dizinlerde arama yapar.
- `-n`: Eşleşen satırların numaralarını gösterir.
- `-c`: Eşleşen satırların sayısını gösterir.
- `-l`: Eşleşen dosya adlarını listeler.

## Örnekler
### Örnek 1: Basit Arama
Aşağıdaki komut, `example.txt` dosyasında "hata" kelimesini arar ve eşleşen satırları gösterir:

```bash
grep 'hata' example.txt
```

### Örnek 2: Büyük/Küçük Harf Duyarsız Arama
Aşağıdaki komut, `example.txt` dosyasında "HATA" veya "hata" kelimesini bulmak için büyük/küçük harf duyarsız arama yapar:

```bash
grep -i 'hata' example.txt
```

## İpuçları
- `grep` komutunu diğer komutlarla birleştirerek daha karmaşık işlemler gerçekleştirebilirsiniz. Örneğin, `cat` komutunu kullanarak bir dosyanın içeriğini `grep` ile filtreleyebilirsiniz:

```bash
cat example.txt | grep 'hata'
```

- Düzenli ifadeleri kullanarak daha karmaşık desenler arayabilirsiniz. Örneğin, birden fazla kelimeyi aramak için `|` operatörünü kullanabilirsiniz:

```bash
grep 'hata|uyarı' example.txt
```

- Arama sonuçlarını daha iyi analiz etmek için `-n` seçeneğini kullanarak satır numaralarını görüntüleyin. Bu, hangi satırların eşleştiğini hızlıca bulmanıza yardımcı olur.

Bu bilgilerle `grep` komutunu etkili bir şekilde kullanarak metin dosyalarındaki verileri hızlıca filtreleyebilir ve analiz edebilirsiniz.