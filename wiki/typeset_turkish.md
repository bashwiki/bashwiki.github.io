# [Linux] Bash typeset Kullanımı: Değişkenlerin özelliklerini ayarlama

## Genel Bakış
`typeset` komutu, Bash kabuğunda değişkenlerin özelliklerini ayarlamak için kullanılır. Bu komut, değişkenlerin türünü, kapsamını ve diğer özelliklerini belirleyerek, programlama sırasında daha iyi kontrol sağlar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```bash
typeset [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-i`: Değişkeni tamsayı olarak tanımlar.
- `-r`: Değişkeni salt okunur yapar.
- `-x`: Değişkeni ortam değişkeni olarak ayarlar.
- `-a`: Değişkeni dizi olarak tanımlar.
- `-A`: Değişkeni ilişkilendirilmiş dizi (associative array) olarak tanımlar.

## Yaygın Örnekler
Aşağıda `typeset` komutunun bazı pratik örnekleri bulunmaktadır:

### Tamsayı Değişken Tanımlama
```bash
typeset -i sayi=10
echo $sayi  # Çıktı: 10
```

### Salt Okunur Değişken
```bash
typeset -r sabit=100
echo $sabit  # Çıktı: 100
sabit=200    # Hata: sabit değişken salt okunur
```

### Ortam Değişkeni Tanımlama
```bash
typeset -x ortam_degiskeni="değer"
echo $ortam_degiskeni  # Çıktı: değer
```

### Dizi Değişkeni Tanımlama
```bash
typeset -a dizi
dizi[0]="bir"
dizi[1]="iki"
echo ${dizi[@]}  # Çıktı: bir iki
```

### İlişkilendirilmiş Dizi Tanımlama
```bash
typeset -A sozluk
sozluk["anahtar"]="değer"
echo ${sozluk["anahtar"]}  # Çıktı: değer
```

## İpuçları
- `typeset` komutunu kullanırken, değişkenlerin kapsamını iyi belirlemek önemlidir. Özellikle büyük projelerde, değişkenlerin yanlışlıkla değiştirilmesini önlemek için `-r` seçeneğini kullanmayı düşünebilirsiniz.
- Dizi ve ilişkilendirilmiş dizilerle çalışırken, değişkenlerin içeriğini kontrol etmek için `declare -p` komutunu kullanabilirsiniz.
- Ortam değişkenleri tanımlarken, `-x` seçeneği ile değişkenlerin diğer süreçler tarafından erişilebilir olmasını sağlayabilirsiniz.