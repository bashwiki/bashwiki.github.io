# [Linux] Bash xmlstarlet Kullanımı: XML verilerini işlemek için bir araç

## Genel Bakış
xmlstarlet, XML belgelerini işlemek için kullanılan güçlü bir komut satırı aracıdır. XML verilerini sorgulamak, dönüştürmek ve düzenlemek için çeşitli işlevler sunar. Bu, özellikle otomatikleştirilmiş görevlerde ve veri işleme senaryolarında oldukça faydalıdır.

## Kullanım
xmlstarlet komutunun temel sözdizimi aşağıdaki gibidir:

```bash
xmlstarlet [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `sel`: XML belgesinden belirli düğümleri seçmek için kullanılır.
- `val`: XML belgesinin geçerliliğini kontrol eder.
- `ed`: XML belgesini düzenlemek için kullanılır.
- `tr`: XML belgesini dönüştürmek için kullanılır.
- `format`: XML belgesini biçimlendirmek için kullanılır.

## Yaygın Örnekler

### 1. XML Belgesinden Düğüm Seçme
Belirli bir düğümü seçmek için `sel` seçeneğini kullanabilirsiniz:

```bash
xmlstarlet sel -t -m "/kitaplar/kitap" -v "başlık" -n kitaplar.xml
```

### 2. XML Belgesinin Geçerliliğini Kontrol Etme
Bir XML belgesinin geçerliliğini kontrol etmek için `val` seçeneğini kullanın:

```bash
xmlstarlet val -e kitaplar.xml
```

### 3. XML Belgesini Düzenleme
Belirli bir düğümün değerini değiştirmek için `ed` seçeneğini kullanabilirsiniz:

```bash
xmlstarlet ed -u "/kitaplar/kitap[1]/başlık" -v "Yeni Başlık" kitaplar.xml
```

### 4. XML Belgesini Dönüştürme
XML belgesini başka bir formatta dönüştürmek için `tr` seçeneğini kullanabilirsiniz:

```bash
xmlstarlet tr dönüşüm.xsl kitaplar.xml
```

### 5. XML Belgesini Biçimlendirme
XML belgesini daha okunabilir hale getirmek için `format` seçeneğini kullanın:

```bash
xmlstarlet fo kitaplar.xml
```

## İpuçları
- XML belgeleriyle çalışırken, her zaman yedeklerinizi alın; düzenlemeler geri alınamaz.
- XML belgelerinizin yapısını anlamak için `sel` seçeneğini kullanarak düğümleri inceleyin.
- Dönüşüm işlemleri için XSLT dosyalarını kullanarak daha karmaşık işlemler gerçekleştirebilirsiniz.
- Komutları test etmek için küçük örnek XML dosyaları oluşturun ve üzerinde denemeler yapın.