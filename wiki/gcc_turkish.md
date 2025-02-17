# [Linux] Bash gcc Kullanımı: C ve C++ programlarını derleme

## Genel Bakış
`gcc`, GNU Compiler Collection'ın bir parçası olan bir derleyicidir. C ve C++ gibi dillerde yazılmış programları derlemek için kullanılır. `gcc`, kaynak kodunu makine diline çevirerek çalıştırılabilir dosyalar oluşturur.

## Kullanım
`gcc` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
gcc [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-o [dosya_adı]`: Çıktı dosyasının adını belirler.
- `-Wall`: Tüm uyarıları etkinleştirir.
- `-g`: Hata ayıklama bilgilerini ekler.
- `-O2`: Optimizasyon seviyesini ayarlar (daha hızlı çalışması için).
- `-I[klasör_adı]`: Başlık dosyalarının bulunduğu klasörü belirtir.

## Yaygın Örnekler
Aşağıda `gcc` komutunun bazı pratik kullanım örnekleri bulunmaktadır:

### Basit Bir Program Derleme
Bir C dosyasını derlemek için:

```bash
gcc program.c -o program
```

### Hata Ayıklama Bilgileri ile Derleme
Hata ayıklama bilgileri ekleyerek derlemek için:

```bash
gcc -g program.c -o program
```

### Uyarıları Etkinleştirerek Derleme
Tüm uyarıları görmek için:

```bash
gcc -Wall program.c -o program
```

### Optimizasyon ile Derleme
Optimizasyon yaparak derlemek için:

```bash
gcc -O2 program.c -o program
```

## İpuçları
- Derleme sırasında oluşan hataları anlamak için `-Wall` seçeneğini kullanın.
- Hata ayıklama sürecinde `-g` seçeneğini kullanarak daha fazla bilgi edinin.
- Derleme işlemlerini daha hızlı hale getirmek için optimizasyon seçeneklerini kullanmayı düşünün.
- Projelerinizde başlık dosyalarını yönetmek için `-I` seçeneğini kullanarak dosya yollarını belirtin.