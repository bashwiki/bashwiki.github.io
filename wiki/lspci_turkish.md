# [Linux] Bash lspci Kullanımı: Donanım aygıtlarını listeleme

## Genel Bakış
`lspci` komutu, Linux tabanlı sistemlerde PCI (Peripheral Component Interconnect) aygıtlarını listelemek için kullanılır. Bu komut, sistemdeki tüm PCI aygıtlarının bilgilerini gösterir, böylece donanım bileşenlerini tanımlamak ve sorun gidermek daha kolay hale gelir.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```
lspci [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-v`: Ayrıntılı bilgi gösterir.
- `-vv`: Daha fazla ayrıntı gösterir.
- `-k`: Aygıt sürücülerini gösterir.
- `-n`: Aygıtları sayısal kimlikleriyle gösterir.
- `-s <bölüm>`: Belirtilen bölüm için bilgileri gösterir.

## Yaygın Örnekler
Aşağıda `lspci` komutunun bazı pratik örnekleri bulunmaktadır:

1. Tüm PCI aygıtlarını listeleme:
   ```bash
   lspci
   ```

2. Ayrıntılı bilgi ile listeleme:
   ```bash
   lspci -v
   ```

3. Aygıt sürücülerini gösterme:
   ```bash
   lspci -k
   ```

4. Belirli bir aygıtın bilgilerini gösterme (örneğin, 00:1f.0):
   ```bash
   lspci -s 00:1f.0
   ```

5. Aygıtları sayısal kimlikleriyle listeleme:
   ```bash
   lspci -n
   ```

## İpuçları
- `lspci` çıktısını daha okunabilir hale getirmek için `less` komutuyla birleştirebilirsiniz:
  ```bash
  lspci | less
  ```
- Çıktıyı bir dosyaya kaydetmek için yönlendirme kullanabilirsiniz:
  ```bash
  lspci > aygıtlar.txt
  ```
- `lspci` komutunu sık sık kullanıyorsanız, belirli seçenekleri varsayılan olarak ayarlamak için bir alias oluşturabilirsiniz:
  ```bash
  alias lspci='lspci -v'
  ``` 

Bu bilgilerle `lspci` komutunu etkili bir şekilde kullanarak sisteminizdeki donanım aygıtlarını kolayca yönetebilirsiniz.