# [리눅스] Bash vagrant 사용법

## Overview
Vagrant, sanal makineler oluşturmak ve yönetmek için kullanılan bir araçtır. Geliştiricilere, projeleri için tutarlı bir geliştirme ortamı sağlamayı amaçlar. Vagrant, sanal makineleri kolayca oluşturma, yapılandırma ve dağıtma imkanı sunarak, farklı platformlarda çalışmayı kolaylaştırır. Bu sayede, projelerin taşınabilirliği ve tekrarlanabilirliği artırılır.

## Usage
Vagrant komutunun temel sözdizimi şu şekildedir:

```bash
vagrant [komut] [seçenekler]
```

En yaygın kullanılan Vagrant komutları şunlardır:

- `vagrant init`: Yeni bir Vagrant projesi başlatır ve bir Vagrantfile oluşturur.
- `vagrant up`: Tanımlı sanal makineyi başlatır.
- `vagrant halt`: Çalışan sanal makineyi durdurur.
- `vagrant destroy`: Sanal makineyi siler.
- `vagrant ssh`: Sanal makineye SSH ile bağlanır.

## Examples
### Örnek 1: Yeni bir Vagrant projesi oluşturma
Aşağıdaki komut, yeni bir Vagrant projesi başlatır ve varsayılan bir Vagrantfile oluşturur:

```bash
vagrant init hashicorp/bionic64
```

Bu komut, Ubuntu 18.04 (Bionic Beaver) tabanlı bir sanal makine için bir Vagrantfile oluşturur.

### Örnek 2: Sanal makineyi başlatma
Oluşturduğunuz Vagrant projesini başlatmak için şu komutu kullanabilirsiniz:

```bash
vagrant up
```

Bu komut, Vagrantfile'da tanımlı olan sanal makineyi başlatır ve gerekli yapılandırmaları otomatik olarak yapar.

## Tips
- Vagrant ile çalışırken, her zaman güncel bir Vagrant ve sanal makine sağlayıcısı (örneğin VirtualBox) kullanmaya özen gösterin.
- Projelerinizde Vagrantfile'ı versiyon kontrol sistemine ekleyerek, ekip üyeleri arasında tutarlılığı sağlayabilirsiniz.
- `vagrant destroy` komutunu kullanmadan önce, sanal makinenizdeki verilerin yedeğini aldığınızdan emin olun, çünkü bu komut tüm verileri siler.
- Vagrant ile birlikte kullanılan provisioner'lar (örneğin, shell, Ansible, Puppet) ile sanal makinelerinizi otomatik olarak yapılandırabilirsiniz.