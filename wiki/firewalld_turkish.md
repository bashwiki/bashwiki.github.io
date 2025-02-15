# [리눅스] Bash firewalld 사용법

## Genel Bakış
`firewalld`, Linux sistemlerinde güvenlik duvarı yönetimi için kullanılan bir komut ve hizmettir. Dinamik bir güvenlik duvarı çözümü sunarak, ağ trafiğini kontrol etmenizi sağlar. `firewalld`, farklı ağ bölgeleri ve hizmetler için kural setleri oluşturmanıza olanak tanır ve bu sayede sisteminize gelen ve giden trafiği yönetebilirsiniz.

## Kullanım
`firewalld` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
firewalld [seçenekler]
```

### Yaygın Seçenekler
- `--zone`: Belirli bir bölgeyi belirtir. Örneğin, `--zone=public`.
- `--add-service`: Belirli bir hizmeti ekler. Örneğin, `--add-service=http`.
- `--remove-service`: Belirli bir hizmeti kaldırır. Örneğin, `--remove-service=ftp`.
- `--list-all`: Mevcut bölgenin tüm ayarlarını listeler.
- `--reload`: Yapılandırmayı yeniden yükler.

## Örnekler
### Örnek 1: HTTP Hizmetini Ekleme
Aşağıdaki komut, `public` bölgesine HTTP hizmetini ekler:

```bash
firewall-cmd --zone=public --add-service=http --permanent
```

Bu komut, HTTP trafiğine izin verir ve değişikliklerin kalıcı olmasını sağlar.

### Örnek 2: Tüm Ayarları Listeleme
Mevcut `public` bölgesinin tüm ayarlarını görüntülemek için şu komutu kullanabilirsiniz:

```bash
firewall-cmd --zone=public --list-all
```

Bu komut, `public` bölgesindeki tüm hizmetleri ve kural setlerini gösterir.

## İpuçları
- `--permanent` seçeneğini kullanarak yaptığınız değişikliklerin kalıcı olmasını sağlayabilirsiniz. Aksi takdirde, sistem yeniden başlatıldığında değişiklikler kaybolur.
- Değişikliklerinizi uyguladıktan sonra `--reload` komutunu kullanarak yapılandırmayı yeniden yüklemeyi unutmayın.
- `firewalld` ile çalışırken, hangi bölgelerin ve hizmetlerin aktif olduğunu kontrol etmek için `firewall-cmd --get-active-zones` komutunu kullanabilirsiniz.

Bu bilgilerle, `firewalld` komutunu etkili bir şekilde kullanarak sisteminizin güvenliğini artırabilirsiniz.