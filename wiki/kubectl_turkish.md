# [리눅스] Bash kubectl 사용법

## Genel Bakış
`kubectl`, Kubernetes ile etkileşimde bulunmak için kullanılan bir komut satırı aracıdır. Kubernetes, konteynerleştirilmiş uygulamaların otomatik dağıtımı, ölçeklenmesi ve yönetimi için açık kaynaklı bir platformdur. `kubectl`, Kubernetes kümesine komutlar göndermek ve kaynakları yönetmek için kullanılır. Bu araç, kullanıcıların pod'lar, servisler, dağıtımlar ve diğer Kubernetes kaynakları üzerinde işlem yapmalarını sağlar.

## Kullanım
`kubectl` komutunun temel sözdizimi şu şekildedir:

```bash
kubectl [OPTIONS] COMMAND [SUBCOMMAND] [FLAGS]
```

### Yaygın Seçenekler
- `--kubeconfig`: Belirli bir kubeconfig dosyasını kullanarak Kubernetes kümesine bağlanır.
- `--context`: Belirli bir bağlamı kullanarak komutları çalıştırır.
- `-n`, `--namespace`: Belirli bir ad alanında işlem yapar.
- `-o`, `--output`: Çıktı formatını belirler (örneğin, `json`, `yaml`, `wide`).

## Örnekler
### Örnek 1: Pod'ları Listeleme
Aşağıdaki komut, mevcut Kubernetes kümesindeki tüm pod'ları listeleyecektir:

```bash
kubectl get pods
```

### Örnek 2: Belirli Bir Pod Hakkında Bilgi Alma
Aşağıdaki komut, "my-pod" adlı pod hakkında ayrıntılı bilgi alır:

```bash
kubectl describe pod my-pod
```

## İpuçları
- `kubectl` komutunu daha verimli kullanmak için, sık kullandığınız komutları bir alias olarak tanımlayabilirsiniz. Örneğin, pod'ları hızlıca listelemek için `alias kgetp='kubectl get pods'` komutunu kullanabilirsiniz.
- Komutları çalıştırmadan önce `--dry-run` seçeneğini kullanarak, komutların ne yapacağını görebilirsiniz. Bu, yanlışlıkla istenmeyen değişiklikler yapmanızı önler.
- Kubernetes kaynaklarını yönetirken, `-o yaml` veya `-o json` seçeneklerini kullanarak çıktıyı yapılandırılmış bir formatta alabilirsiniz. Bu, kaynakları daha iyi anlamanıza yardımcı olur.