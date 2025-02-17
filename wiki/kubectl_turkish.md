# [Linux] Bash kubectl Kullanımı: Kubernetes kaynaklarını yönetmek için bir komut

## Genel Bakış
`kubectl`, Kubernetes kümesindeki kaynakları yönetmek için kullanılan bir komuttur. Bu komut, kullanıcıların pod'lar, hizmetler, dağıtımlar ve diğer Kubernetes kaynakları üzerinde işlem yapmalarını sağlar.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```
kubectl [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `get`: Belirtilen kaynak türlerini listelemek için kullanılır.
- `describe`: Belirli bir kaynağın detaylı bilgilerini görüntüler.
- `create`: Yeni bir kaynak oluşturur.
- `delete`: Belirtilen bir kaynağı siler.
- `apply`: Bir kaynak üzerinde değişiklik yapmak için kullanılır.

## Yaygın Örnekler
Aşağıda `kubectl` komutunun bazı yaygın kullanım örnekleri verilmiştir:

### Pod'ları Listeleme
```
kubectl get pods
```

### Belirli Bir Pod Hakkında Bilgi Alma
```
kubectl describe pod <pod_adı>
```

### Yeni Bir Dağıtım Oluşturma
```
kubectl create deployment <dağıtım_adı> --image=<görüntü_adı>
```

### Bir Kaynağı Silme
```
kubectl delete pod <pod_adı>
```

### Değişiklik Uygulama
```
kubectl apply -f <dosya_adı>.yaml
```

## İpuçları
- `kubectl` komutlarını daha verimli kullanmak için, sık kullandığınız komutları bir alias olarak tanımlayabilirsiniz.
- Komutların çıktısını daha okunabilir hale getirmek için `-o wide` veya `-o json` gibi seçenekler kullanabilirsiniz.
- Kubernetes kaynaklarını yönetirken, her zaman güncel dökümantasyonu kontrol etmek iyi bir uygulamadır.