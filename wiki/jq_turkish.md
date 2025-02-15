# [리눅스] Bash jq 사용법

## Genel Bakış
`jq`, JSON (JavaScript Object Notation) verilerini işlemek için kullanılan bir komut satırı aracıdır. JSON formatındaki verileri okumak, yazmak ve dönüştürmek için güçlü bir dil sunar. Geliştiriciler ve mühendisler için, API'lerden gelen JSON yanıtlarını analiz etmek ve düzenlemek için yaygın olarak kullanılır.

## Kullanım
`jq` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
jq [seçenekler] 'filtre' dosya.json
```

### Yaygın Seçenekler
- `-r`: JSON çıktısını ham (raw) formatta döndürür. Bu, metin çıktısı almak için faydalıdır.
- `-c`: Çıktıyı tek satırda döndürür, bu da daha okunabilir hale getirir.
- `-f`: Dışarıdan bir filtre dosyası belirtmek için kullanılır.

## Örnekler
### Örnek 1: Basit JSON Verisini Okuma
Aşağıdaki JSON dosyası `data.json` içeriğine sahip olsun:

```json
{
  "isim": "Ahmet",
  "yaş": 30,
  "şehir": "İstanbul"
}
```

Bu dosyadaki "isim" alanını okumak için şu komutu kullanabilirsiniz:

```bash
jq '.isim' data.json
```

Çıktı:
```
"Ahmet"
```

### Örnek 2: JSON Verisini Filtreleme
Aynı JSON dosyasını kullanarak, "yaş" alanını ham formatta almak için:

```bash
jq -r '.yaş' data.json
```

Çıktı:
```
30
```

## İpuçları
- JSON verilerini işlerken, `jq`'nun filtreleme yeteneklerini kullanarak karmaşık sorgular oluşturabilirsiniz. Örneğin, bir dizi içindeki belirli nesneleri seçmek için `select()` fonksiyonunu kullanabilirsiniz.
- `jq` ile çalışırken, JSON verinizin yapısını anlamak için `jq '.' dosya.json` komutunu kullanarak tüm veriyi görüntüleyebilirsiniz.
- Filtrelerinizi daha okunabilir hale getirmek için `|` (pipe) operatörünü kullanarak birden fazla filtreyi birleştirebilirsiniz.

`jq`, JSON verileriyle çalışırken güçlü ve esnek bir araçtır. Bu temel bilgilerle, `jq`'yu etkili bir şekilde kullanmaya başlayabilirsiniz.