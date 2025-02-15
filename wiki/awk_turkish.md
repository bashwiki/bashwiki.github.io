# [리눅스] Bash awk 사용법

## Overview
`awk`, metin işleme ve veri analizi için kullanılan güçlü bir programlama dilidir. Genellikle dosyalardaki verileri işlemek, filtrelemek ve biçimlendirmek için kullanılır. `awk`, satır bazında çalışarak, her bir satırı belirli bir biçimde analiz eder ve belirli alanlar üzerinde işlemler yapar. Bu özellikleri sayesinde, verileri düzenlemek ve raporlamak için oldukça etkili bir araçtır.

## Usage
`awk` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
awk 'pattern { action }' dosya_adı
```

- **pattern**: İşlenecek satırları belirlemek için kullanılan bir koşuldur. Eğer belirtilen koşul sağlanıyorsa, `action` kısmı çalıştırılır.
- **action**: Koşul sağlandığında gerçekleştirilecek işlemleri tanımlar. Genellikle, belirli alanları yazdırmak veya hesaplamalar yapmak için kullanılır.

### Yaygın Seçenekler
- `-F`: Girdi dosyasındaki alan ayırıcıyı belirtir. Örneğin, `-F,` virgül ile ayrılmış dosyalar için kullanılır.
- `-v`: Değişken tanımlamak için kullanılır. Örneğin, `-v var=değer` şeklinde.

## Examples
### Örnek 1: Belirli Bir Alanı Yazdırma
Aşağıdaki komut, `data.txt` dosyasındaki ikinci alanı yazdırır:

```bash
awk '{ print $2 }' data.txt
```

### Örnek 2: Alan Ayırıcı Kullanma
Eğer `data.csv` dosyası virgülle ayrılmışsa ve yalnızca birinci ve üçüncü alanları yazdırmak istiyorsanız:

```bash
awk -F, '{ print $1, $3 }' data.csv
```

## Tips
- `awk` kullanırken, dosyanızın yapısını iyi anlamak önemlidir. Alan ayırıcıları ve satır yapısı hakkında bilgi sahibi olmak, daha etkili komutlar yazmanıza yardımcı olur.
- Karmaşık işlemler için `awk` içinde döngüler ve koşullu ifadeler kullanarak daha gelişmiş veri işleme senaryoları oluşturabilirsiniz.
- `awk` komutunu diğer komutlarla birleştirerek (örneğin, `grep` ile) daha güçlü veri filtreleme ve analiz işlemleri gerçekleştirebilirsiniz.