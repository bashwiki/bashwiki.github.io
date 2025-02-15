# [리눅스] Bash svn 사용법

## Genel Bakış
`svn` (Subversion), sürüm kontrol sistemi olarak kullanılan bir komuttur. Yazılım geliştirme projelerinde dosyaların ve dizinlerin sürümlerini yönetmek için kullanılır. `svn`, kullanıcıların dosyaları takip etmesine, değişiklikleri kaydetmesine ve projelerin farklı sürümleri arasında geçiş yapmasına olanak tanır. Bu sayede ekipler, projeler üzerinde işbirliği yaparken daha düzenli ve verimli bir şekilde çalışabilirler.

## Kullanım
`svn` komutunun temel sözdizimi aşağıdaki gibidir:

```
svn [komut] [seçenekler] [hedef]
```

### Yaygın Seçenekler
- `checkout`: Bir depo içeriğini yerel bir dizine kopyalar.
- `commit`: Yerel değişiklikleri depoya kaydeder.
- `update`: Yerel kopyayı depodaki en son sürümle günceller.
- `add`: Yeni dosyaları veya dizinleri depoya ekler.
- `delete`: Depodan dosyaları veya dizinleri siler.
- `status`: Yerel çalışma kopyasındaki değişikliklerin durumunu gösterir.

## Örnekler

### Örnek 1: Depodan Çekme
Bir Subversion deposundan dosyaları yerel bir dizine çekmek için `checkout` komutunu kullanabilirsiniz:

```bash
svn checkout https://example.com/svn/repo/trunk my_project
```

Bu komut, belirtilen depo URL'sinden `my_project` adlı bir dizine dosyaları kopyalar.

### Örnek 2: Değişiklikleri Kaydetme
Yerel değişikliklerinizi depoya kaydetmek için `commit` komutunu kullanabilirsiniz:

```bash
svn commit -m "Bu değişiklikler projeye eklendi."
```

Bu komut, yerel kopyanızdaki değişiklikleri depoya kaydeder ve "Bu değişiklikler projeye eklendi." mesajını ekler.

## İpuçları
- Değişikliklerinizi sık sık kaydedin ve açıklayıcı mesajlar ekleyin. Bu, ileride değişikliklerinizi anlamanızı kolaylaştırır.
- `svn status` komutunu kullanarak yerel kopyanızdaki değişikliklerin durumunu kontrol edin. Bu, hangi dosyaların değiştiğini veya eklenip silindiğini görmenizi sağlar.
- Projelerinizde birden fazla dal (branch) kullanıyorsanız, her dalda çalışırken dikkatli olun ve hangi dalda olduğunuzu kontrol edin.

Bu bilgilerle `svn` komutunu etkili bir şekilde kullanarak projelerinizin sürüm kontrolünü yönetebilirsiniz.