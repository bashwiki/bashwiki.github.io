# [리눅스] Bash vmstat 사용법

## Overview
`vmstat` (Virtual Memory Statistics) komutu, sistemin bellek, işlemci ve I/O (giriş/çıkış) aktiviteleri hakkında bilgi sağlar. Bu komut, sistem performansını izlemek ve analiz etmek için kullanılır. `vmstat`, sistem kaynaklarının nasıl kullanıldığını anlamak için yararlı bir araçtır ve özellikle bellek yönetimi ve işlemci yükü hakkında bilgi edinmek isteyen mühendisler ve geliştiriciler için faydalıdır.

## Usage
`vmstat` komutunun temel sözdizimi şu şekildedir:

```bash
vmstat [options] [delay [count]]
```

- **options**: Komutun çalışma şeklini değiştiren çeşitli seçeneklerdir.
- **delay**: İstatistiklerin güncellenme süresini (saniye cinsinden) belirtir.
- **count**: İstatistiklerin kaç kez gösterileceğini belirtir.

### Yaygın Seçenekler
- `-s`: Bellek ve diğer sistem kaynakları hakkında detaylı bir özet gösterir.
- `-m`: Bellek sayfaları hakkında bilgi verir.
- `-d`: Disk istatistiklerini gösterir.

## Examples
### Örnek 1: Temel Kullanım
Aşağıdaki komut, her 2 saniyede bir sistem istatistiklerini gösterir:

```bash
vmstat 2
```

Bu komut, işlemci, bellek, swap alanı ve I/O istatistiklerini sürekli olarak güncelleyerek görüntüler.

### Örnek 2: Detaylı Bellek Bilgisi
Aşağıdaki komut, sistemin bellek ve diğer kaynakları hakkında detaylı bir özet sunar:

```bash
vmstat -s
```

Bu komut, toplam bellek, kullanılabilir bellek, swap alanı ve diğer önemli bilgileri listeler.

## Tips
- `vmstat` çıktısını analiz ederken, sistemin genel performansını değerlendirmek için işlemci ve bellek kullanımı arasındaki ilişkiye dikkat edin.
- Uzun süreli izleme için `vmstat` komutunu bir dosyaya yönlendirebilirsiniz. Örneğin:

```bash
vmstat 2 10 > vmstat_output.txt
```

Bu komut, 2 saniyede bir 10 kez istatistikleri alır ve çıktıyı `vmstat_output.txt` dosyasına kaydeder.
- `vmstat` çıktısını diğer sistem izleme araçlarıyla birlikte kullanarak daha kapsamlı bir analiz yapabilirsiniz.