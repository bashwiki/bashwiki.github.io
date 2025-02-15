# [리눅스] Bash csvtool 사용법

## Overview
`csvtool`, CSV (Comma-Separated Values) dosyalarını işlemek için kullanılan bir komut satırı aracıdır. Bu araç, CSV dosyalarındaki verileri kolayca okuma, yazma ve dönüştürme işlemleri yapmanıza olanak tanır. Geliştiriciler ve mühendisler için, veri analizi ve manipülasyonu süreçlerini hızlandırmak için oldukça faydalıdır.

## Usage
`csvtool` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
csvtool [seçenekler] [işlem] [girdi_dosyası] [çıktı_dosyası]
```

### Yaygın Seçenekler
- `-c`: Belirtilen sütunları seçer. Örneğin, `-c 1,3` ifadesi 1. ve 3. sütunları alır.
- `-r`: Satırları filtrelemek için kullanılır. Belirli bir koşula uyan satırları seçmek için kullanılabilir.
- `-t`: CSV dosyasındaki ayırıcıyı belirtir. Varsayılan ayırıcı virgüldür, ancak `-t ;` ile noktalı virgül gibi farklı bir ayırıcı da kullanılabilir.

## Examples
### Örnek 1: Belirli Sütunları Seçme
Aşağıdaki komut, `data.csv` dosyasından 1. ve 3. sütunları alır ve `output.csv` dosyasına yazar:

```bash
csvtool -c 1,3 data.csv output.csv
```

### Örnek 2: Satır Filtreleme
Aşağıdaki komut, `data.csv` dosyasındaki belirli bir koşula uyan satırları filtreler. Örneğin, 2. sütundaki değeri "aktif" olan satırları alır:

```bash
csvtool -r '2 == "aktif"' data.csv output.csv
```

## Tips
- CSV dosyalarınızı işlerken, dosya ayırıcılarının doğru ayarlandığından emin olun. Yanlış ayırıcı kullanımı, verilerin yanlış şekilde işlenmesine neden olabilir.
- Büyük CSV dosyaları ile çalışıyorsanız, işlemlerinizi optimize etmek için `csvtool` komutunu `grep` veya `awk` gibi diğer araçlarla birleştirebilirsiniz.
- CSV dosyalarınızı yedeklemeyi unutmayın; işlem öncesinde orijinal dosyaların kaybolmasını önlemek için her zaman bir kopyasını saklayın.