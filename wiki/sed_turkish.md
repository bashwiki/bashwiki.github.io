# [Linux] Bash sed Kullanımı: Metin düzenleme aracı

## Genel Bakış
`sed`, akış metin düzenleyici olarak bilinen bir komuttur. Metin dosyalarında düzenlemeler yapmak için kullanılır ve genellikle otomatikleştirilmiş işlemler için tercih edilir. `sed`, metin akışını alır, belirli kurallara göre işler ve sonuçları çıktı olarak verir.

## Kullanım
`sed` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
sed [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-e`: Birden fazla komut belirtmek için kullanılır.
- `-i`: Dosyayı yerinde düzenler, yani değişiklikleri dosyaya kaydeder.
- `-n`: Varsayılan çıktıyı bastırır, yalnızca belirtilen komutlarla sonuçları gösterir.
- `s/pattern/replacement/`: Belirli bir deseni bulur ve yerine başka bir metin koyar.

## Yaygın Örnekler
- Bir dosyadaki "eski" kelimesini "yeni" ile değiştirmek:

```bash
sed 's/eski/yeni/' dosya.txt
```

- Tüm "eski" kelimelerini "yeni" ile değiştirmek için:

```bash
sed 's/eski/yeni/g' dosya.txt
```

- Bir dosyayı yerinde düzenleyerek "eski" kelimesini "yeni" ile değiştirmek:

```bash
sed -i 's/eski/yeni/g' dosya.txt
```

- Sadece belirli bir satırda değişiklik yapmak (örneğin, 2. satır):

```bash
sed '2s/eski/yeni/' dosya.txt
```

- Belirli bir deseni içeren satırları bastırmak:

```bash
sed -n '/desen/p' dosya.txt
```

## İpuçları
- `sed` komutunu test etmek için `-n` seçeneğini kullanarak çıktıyı kontrol edin.
- Değişikliklerinizi kaydetmeden önce dosyanın yedeğini almak iyi bir uygulamadır.
- Karmaşık düzenlemeler için birden fazla `-e` seçeneği ile birden fazla komut verebilirsiniz.