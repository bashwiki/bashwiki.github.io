# [리눅스] Bash fc 사용법

## Genel Bakış
`fc` komutu, Bash kabuğunda daha önce çalıştırılmış komutları düzenlemek ve tekrar çalıştırmak için kullanılan bir araçtır. Bu komut, kullanıcıların geçmişteki komutlarını kolayca bulmalarını, düzenlemelerini ve yeniden çalıştırmalarını sağlar. `fc`, "fix command" (komutu düzelt) ifadesinin kısaltmasıdır ve genellikle hata yapıldığında veya bir komutun tekrar çalıştırılması gerektiğinde kullanılır.

## Kullanım
`fc` komutunun temel sözdizimi şu şekildedir:

```bash
fc [seçenekler] [ilk] [son]
```

### Yaygın Seçenekler
- `-l`: Geçmişteki komutların listesini gösterir.
- `-r`: Komutları ters sırada listeler.
- `-s`: Belirtilen komutu çalıştırmadan önce düzenlemeden doğrudan çalıştırır.
- `[ilk]` ve `[son]`: Geçmişteki komutların hangi aralıkta gösterileceğini belirtir. Eğer belirtilmezse, en son komutlar kullanılır.

## Örnekler

### Örnek 1: Geçmiş Komutlarını Listeleme
Geçmişteki komutlarınızı listelemek için aşağıdaki komutu kullanabilirsiniz:

```bash
fc -l
```
Bu komut, geçmişteki komutlarınızı numaralarıyla birlikte listeleyecektir.

### Örnek 2: Belirli Bir Komutu Düzenleme
Son çalıştırdığınız komutu düzenlemek için:

```bash
fc
```
Bu komut, son komutu varsayılan metin düzenleyicinizde açar. Düzenledikten sonra kaydedip çıkarsanız, komut otomatik olarak çalıştırılacaktır.

## İpuçları
- `fc` komutunu kullanırken, geçmişteki komutlarınızı düzenlemek için tercih ettiğiniz bir metin düzenleyici ayarlamak iyi bir uygulamadır. Bunu yapmak için `EDITOR` ortam değişkenini ayarlayabilirsiniz:
  ```bash
  export EDITOR=nano
  ```
- Komut geçmişinizi daha iyi yönetmek için `HISTSIZE` ve `HISTFILESIZE` değişkenlerini ayarlayarak geçmişte saklanan komut sayısını artırabilirsiniz.
- `fc` komutunu kullanarak sık kullandığınız komutları hızlıca düzenleyip çalıştırmak, zaman kazandırabilir ve hata yapma olasılığını azaltabilir.