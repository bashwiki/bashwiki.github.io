# [리눅스] Bash docker 사용법

## Genel Bakış
`docker` komutu, konteyner tabanlı uygulamaları oluşturmak, dağıtmak ve çalıştırmak için kullanılan bir platformdur. Docker, geliştiricilerin uygulamalarını ve bağımlılıklarını izole bir ortamda paketlemelerine olanak tanır. Bu sayede, uygulamalar farklı ortamlarda tutarlı bir şekilde çalışabilir. Docker, mikro hizmet mimarisi ve DevOps süreçleri için yaygın olarak kullanılmaktadır.

## Kullanım
`docker` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
docker [OPTIONS] COMMAND [ARG...]
```

### Yaygın Seçenekler
- `-v`, `--version`: Docker sürümünü gösterir.
- `-h`, `--help`: Docker komutları hakkında yardım almanızı sağlar.
- `--config`: Docker yapılandırma dosyasının yolunu belirtir.

## Örnekler
### Örnek 1: Docker Sürümünü Kontrol Etme
Docker'ın yüklü sürümünü kontrol etmek için aşağıdaki komutu kullanabilirsiniz:

```bash
docker --version
```

Bu komut, yüklü olan Docker sürümünü terminalde gösterecektir.

### Örnek 2: Bir Konteyner Çalıştırma
Docker ile bir konteyner çalıştırmak için aşağıdaki komutu kullanabilirsiniz:

```bash
docker run hello-world
```

Bu komut, "hello-world" adlı bir konteyneri çalıştırır ve Docker'ın düzgün bir şekilde kurulduğunu doğrulamak için basit bir mesaj gösterir.

## İpuçları
- Docker'ı kullanmadan önce, Docker daemon'unun çalıştığından emin olun. Aksi takdirde, komutlarınız çalışmayabilir.
- Konteynerlerinizi yönetmek için `docker ps` komutunu kullanarak aktif konteynerlerinizi listeleyebilirsiniz.
- Docker görüntülerinizi güncel tutmak için `docker pull` komutunu kullanarak en son sürümleri çekebilirsiniz.
- Geliştirme sürecinde, konteynerlerinizi hızlı bir şekilde başlatmak ve durdurmak için `docker start` ve `docker stop` komutlarını kullanabilirsiniz.

Bu bilgiler, `docker` komutunu etkili bir şekilde kullanmanıza yardımcı olacaktır. Docker ile uygulama geliştirme sürecinizi hızlandırabilir ve daha verimli hale getirebilirsiniz.