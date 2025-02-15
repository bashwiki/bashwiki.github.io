# [리눅스] Bash xmlstarlet 사용법

## Genel Bakış
`xmlstarlet`, XML belgeleri üzerinde işlem yapmayı sağlayan bir komut satırı aracıdır. Bu araç, XML verilerini sorgulama, dönüştürme, doğrulama ve düzenleme gibi işlemleri gerçekleştirmek için kullanılır. `xmlstarlet`, XML ile çalışırken geliştiricilere ve mühendislere büyük kolaylık sağlar, çünkü karmaşık XML yapılarını basit ve etkili bir şekilde yönetmelerine olanak tanır.

## Kullanım
`xmlstarlet` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
xmlstarlet [seçenekler] [işlem] [belge]
```

### Yaygın Seçenekler
- `xmlstarlet sel`: XML belgesinden veri seçmek için kullanılır.
- `xmlstarlet ed`: XML belgesini düzenlemek için kullanılır.
- `xmlstarlet val`: XML belgesinin geçerliliğini kontrol etmek için kullanılır.
- `xmlstarlet tr`: XML belgesini dönüştürmek için kullanılır.

## Örnekler

### Örnek 1: XML Belgesinden Veri Seçme
Aşağıdaki komut, `example.xml` dosyasındaki tüm `<title>` etiketlerini seçer ve çıktısını verir:

```bash
xmlstarlet sel -t -m "//title" -v "." -n example.xml
```

### Örnek 2: XML Belgesini Düzenleme
Aşağıdaki komut, `example.xml` dosyasındaki `<author>` etiketinin içeriğini "Yeni Yazar" olarak değiştirir:

```bash
xmlstarlet ed -u "//author" -v "Yeni Yazar" example.xml
```

## İpuçları
- XML belgeleri üzerinde işlem yapmadan önce, belgenin yedeğini almak iyi bir uygulamadır. Bu, istenmeyen değişikliklerden kaçınmanıza yardımcı olur.
- `xmlstarlet` ile çalışırken, belgenizin yapısını anlamak için `xmlstarlet fo` komutunu kullanarak XML belgenizi biçimlendirebilirsiniz. Bu, okunabilirliği artırır.
- Komutları test etmeden önce, `--dry-run` seçeneğini kullanarak değişikliklerinizi önizleyebilirsiniz. Bu, hatalı işlemlerden kaçınmanıza yardımcı olur.

`xmlstarlet`, XML ile çalışırken güçlü bir araçtır ve yukarıdaki bilgilerle, bu komutun temel işlevlerini etkili bir şekilde kullanabilirsiniz.