# [리눅스] Bash df 사용법

## Genel Bakış
`df` komutu, Linux ve Unix benzeri işletim sistemlerinde disk alanı kullanımını görüntülemek için kullanılır. Bu komut, dosya sistemlerinin ne kadar alan kullandığını ve ne kadar boş alan kaldığını gösterir. Sistem yöneticileri ve geliştiriciler için, sistemin depolama durumu hakkında hızlı bir genel bakış sağlamak açısından oldukça faydalıdır.

## Kullanım
`df` komutunun temel sözdizimi şu şekildedir:

```bash
df [seçenekler] [dosya_sistemi]
```

### Yaygın Seçenekler
- `-h`: İnsan tarafından okunabilir formatta çıktı verir (örneğin, KB, MB, GB).
- `-T`: Dosya sisteminin türünü gösterir.
- `-a`: Tüm dosya sistemlerini, boş olanlar dahil, gösterir.
- `-i`: İnode kullanımını gösterir, bu da dosya sistemindeki dosya sayısını temsil eder.

## Örnekler
### Örnek 1: Temel Kullanım
Aşağıdaki komut, mevcut dosya sistemlerinin disk alanı kullanımını gösterir:

```bash
df
```

### Örnek 2: İnsan Okunabilir Format
Aşağıdaki komut, disk alanı kullanımını insan tarafından okunabilir formatta gösterir:

```bash
df -h
```

## İpuçları
- `df` komutunu düzenli olarak çalıştırarak sisteminizin disk alanı kullanımını izlemek, gereksiz dosyaların silinmesi veya depolama alanının genişletilmesi gerektiğinde proaktif olmanıza yardımcı olabilir.
- `df -T` seçeneği ile dosya sisteminin türünü de görebilir, bu sayede hangi dosya sisteminin hangi alanı kullandığını daha iyi anlayabilirsiniz.
- Disk alanı sorunlarıyla karşılaşmamak için, kritik sistem dosyalarının bulunduğu dosya sistemlerinin kullanımını düzenli olarak kontrol edin.