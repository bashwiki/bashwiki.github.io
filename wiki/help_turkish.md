# [리눅스] Bash help 사용법

## Genel Bakış
`help` komutu, Bash kabuğunda yerleşik olan ve kullanıcıların komutlar hakkında bilgi almasını sağlayan bir araçtır. Bu komut, kullanıcıların belirli bir komutun nasıl kullanılacağını öğrenmelerine yardımcı olur ve genellikle komutun sözdizimi, seçenekleri ve işlevleri hakkında bilgi sağlar. `help`, özellikle yeni başlayanlar için faydalıdır ve komutların hızlı bir şekilde anlaşılmasına olanak tanır.

## Kullanım
`help` komutunun temel sözdizimi şu şekildedir:

```bash
help [komut]
```

- `komut`: Yardım almak istediğiniz Bash yerleşik komutunun adıdır. Eğer bu parametre verilmezse, `help` komutu genel bir yardım mesajı gösterir.

### Yaygın Seçenekler
- `-s`: Komutun kısa bir açıklamasını gösterir.
- `-m`: Komutun kullanımını daha ayrıntılı bir şekilde açıklayan bir metin gösterir.

## Örnekler
1. Belirli bir komut hakkında bilgi almak için:

```bash
help cd
```
Bu komut, `cd` (değiştir) komutunun nasıl kullanılacağına dair bilgi sağlar.

2. Tüm yerleşik komutlar hakkında genel bir yardım almak için:

```bash
help
```
Bu komut, Bash'ta mevcut olan tüm yerleşik komutlar hakkında kısa bir bilgi listesi gösterir.

## İpuçları
- `help` komutunu kullanarak, sık kullandığınız komutların işlevlerini ve seçeneklerini hızlı bir şekilde öğrenebilirsiniz.
- Yeni bir komut denemeden önce `help` ile o komutun ne yaptığını kontrol etmek, hataları önlemek için iyi bir uygulamadır.
- `help` komutunu sık sık kullanarak, Bash kabuğundaki yerleşik komutları daha iyi öğrenebilir ve verimliliğinizi artırabilirsiniz.