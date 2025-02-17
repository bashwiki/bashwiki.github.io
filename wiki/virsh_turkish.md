# [Linux] Bash virsh Kullanımı: Sanal makineleri yönetmek için bir araç

## Genel Bakış
`virsh`, sanal makineleri yönetmek için kullanılan bir komut satırı aracıdır. KVM, Xen ve diğer sanallaştırma teknolojileri ile çalışan sanal makineleri oluşturma, başlatma, durdurma ve yönetme işlemlerini kolaylaştırır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```bash
virsh [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `list`: Aktif sanal makinelerin listesini gösterir.
- `start <VM_adı>`: Belirtilen sanal makineyi başlatır.
- `shutdown <VM_adı>`: Belirtilen sanal makineyi kapatır.
- `destroy <VM_adı>`: Belirtilen sanal makineyi durdurur ve siler.
- `create <dosya>`: Belirtilen XML dosyasından yeni bir sanal makine oluşturur.

## Yaygın Örnekler
Sanal makineleri yönetmek için `virsh` komutunun nasıl kullanılacağını gösteren bazı örnekler:

### 1. Aktif Sanal Makineleri Listeleme
```bash
virsh list
```

### 2. Sanal Makine Başlatma
```bash
virsh start my_vm
```

### 3. Sanal Makineyi Kapatma
```bash
virsh shutdown my_vm
```

### 4. Sanal Makineyi Silme
```bash
virsh destroy my_vm
```

### 5. Yeni Bir Sanal Makine Oluşturma
```bash
virsh create my_vm.xml
```

## İpuçları
- Sanal makinelerin durumunu kontrol etmek için `virsh list --all` komutunu kullanabilirsiniz.
- XML dosyalarını düzenleyerek sanal makinelerin yapılandırmasını özelleştirebilirsiniz.
- `virsh` komutunu kullanmadan önce gerekli izinlere sahip olduğunuzdan emin olun.