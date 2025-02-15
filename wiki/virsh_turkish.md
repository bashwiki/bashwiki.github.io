# [리눅스] Bash virsh 사용법

## Overview
`virsh`, sanal makine yönetimi için kullanılan bir komut satırı aracıdır. Bu komut, KVM (Kernel-based Virtual Machine), Xen ve diğer sanal makine yöneticileri ile etkileşimde bulunarak sanal makineleri oluşturma, silme, başlatma, durdurma ve yönetme gibi işlemleri gerçekleştirmeye olanak tanır. `virsh`, sanal makineler üzerinde detaylı kontrol sağlamak için geniş bir komut seti sunar.

## Usage
`virsh` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
virsh [komut] [seçenekler]
```

### Yaygın Seçenekler
- `list`: Aktif sanal makinelerin listesini gösterir.
- `start <VM_adı>`: Belirtilen sanal makineyi başlatır.
- `shutdown <VM_adı>`: Belirtilen sanal makineyi kapatır.
- `destroy <VM_adı>`: Belirtilen sanal makineyi aniden durdurur.
- `create <dosya>`: Belirtilen XML dosyasına göre yeni bir sanal makine oluşturur.
- `define <dosya>`: Belirtilen XML dosyasını kullanarak sanal makine tanımını yapar.

## Examples
### Örnek 1: Aktif Sanal Makineleri Listeleme
Aşağıdaki komut, mevcut aktif sanal makinelerin listesini gösterir:

```bash
virsh list
```

### Örnek 2: Bir Sanal Makineyi Başlatma
`my_vm` adlı sanal makineyi başlatmak için şu komutu kullanabilirsiniz:

```bash
virsh start my_vm
```

## Tips
- `virsh` komutunu kullanmadan önce, sanal makine yöneticinizin (örneğin, libvirt) düzgün bir şekilde kurulu ve çalışır durumda olduğundan emin olun.
- Komutları çalıştırmadan önce `virsh help` komutunu kullanarak mevcut komutlar ve seçenekler hakkında bilgi alabilirsiniz.
- Sanal makineleri yönetirken dikkatli olun; `destroy` komutu, sanal makineyi aniden kapatır ve veri kaybına neden olabilir. Bunun yerine `shutdown` komutunu kullanmak genellikle daha güvenlidir.