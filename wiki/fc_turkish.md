# [Linux] Bash fc Kullanımı: Geçmişteki Komutları Düzenleme

## Overview
`fc` komutu, Bash kabuğunda daha önce çalıştırılmış komutları düzenlemek ve yeniden çalıştırmak için kullanılır. Bu komut, kullanıcıların geçmişteki komutları kolayca bulup düzenlemesine ve tekrar çalıştırmasına olanak tanır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
fc [options] [arguments]
```

## Common Options
- `-l`: Geçmişteki komutların listesini gösterir.
- `-r`: Komutları ters sırada listeler.
- `-s`: Belirtilen komutu çalıştırmadan önce düzenler.
- `-n`: Komut numaralarını göstermeden listeleme yapar.

## Common Examples
Aşağıda `fc` komutunun bazı yaygın kullanım örnekleri verilmiştir:

1. **Son Komutu Düzenleme:**
   ```bash
   fc
   ```
   Bu komut, en son çalıştırılan komutu varsayılan metin düzenleyici ile açar.

2. **Belirli Bir Komutu Düzenleme:**
   ```bash
   fc 10
   ```
   Bu komut, geçmişteki 10 numaralı komutu düzenler.

3. **Geçmişteki Komutları Listeleme:**
   ```bash
   fc -l
   ```
   Bu komut, geçmişteki tüm komutları listeler.

4. **Ters Sırada Listeleme:**
   ```bash
   fc -lr
   ```
   Bu komut, geçmişteki komutları ters sırada listeler.

5. **Komutu Düzenleyip Çalıştırma:**
   ```bash
   fc -s 10
   ```
   Bu komut, geçmişteki 10 numaralı komutu düzenler ve hemen çalıştırır.

## Tips
- `fc` komutunu kullanmadan önce, hangi komutları düzenlemek istediğinizi belirlemek için `history` komutunu kullanabilirsiniz.
- Düzenleme işlemi için varsayılan metin düzenleyicinizi ayarlamak isterseniz, `EDITOR` ortam değişkenini kullanabilirsiniz.
- `fc` komutunu kullanarak sık kullandığınız komutları daha verimli hale getirebilirsiniz; bu, zaman kazandırır ve hata yapma olasılığını azaltır.