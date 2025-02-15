# [리눅스] Bash builtin 사용법

## Genel Bakış
`builtin` komutu, Bash kabuğunda yerleşik (builtin) komutları çağırmak için kullanılır. Bu komut, bir yerleşik komutun, kabuğun kendi sürümünü çağırarak, dış bir komutun çalıştırılmasını engeller. Özellikle, aynı isimde hem yerleşik hem de dış komut bulunan durumlarda, hangi komutun çalıştırılacağını belirlemek için kullanılır.

## Kullanım
Temel sözdizimi şu şekildedir:

```bash
builtin [komut]
```

Burada `[komut]`, çağırmak istediğiniz yerleşik komuttur. `builtin` komutu, belirli bir yerleşik komutu çalıştırmak için kullanılır. Örneğin, `echo` komutu hem yerleşik hem de dış bir komut olarak mevcut olabilir. `builtin echo` yazarak, yerleşik `echo` komutunu çağırabilirsiniz.

### Yaygın Seçenekler
- `-p`: Yerleşik komutun, dış bir komutun yerine kullanılmasını sağlar.
- `-f`: Yerleşik bir komutun, dış bir komutla değiştirilmesini sağlar.

## Örnekler

### Örnek 1: Yerleşik `echo` Komutunu Kullanma
Aşağıdaki komut, `builtin` kullanarak yerleşik `echo` komutunu çağırır:

```bash
builtin echo "Bu, yerleşik echo komutudur."
```

### Örnek 2: `type` Komutunu Kullanma
`type` komutu ile bir komutun yerleşik mi yoksa dış mı olduğunu kontrol edebilirsiniz:

```bash
type -a echo
```

Bu komut, `echo` komutunun hem yerleşik hem de dış sürümünü gösterir. Eğer sadece yerleşik sürümü çağırmak isterseniz:

```bash
builtin type -a echo
```

## İpuçları
- `builtin` komutunu kullanarak, yerleşik komutların dış sürümlerinin etkisini önleyebilirsiniz. Bu, özellikle betiklerinizde tutarlılığı sağlamak için faydalıdır.
- Yerleşik komutların hangi seçenekleri desteklediğini öğrenmek için `help [komut]` komutunu kullanabilirsiniz. Örneğin, `help echo` yazarak `echo` komutunun yerleşik sürümünün seçeneklerini görebilirsiniz.
- `builtin` komutunu kullanırken, dikkatli olun; çünkü yanlış bir komut çağrısı, beklenmedik sonuçlar doğurabilir.