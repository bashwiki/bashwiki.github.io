# [Linux] Bash htop Kullanımı: Sistem kaynaklarını izleme aracı

## Genel Bakış
htop, Linux ve Unix benzeri işletim sistemlerinde çalışan bir etkileşimli süreç görüntüleyicisidir. Kullanıcılara sistemdeki işlemleri, bellek ve CPU kullanımını gerçek zamanlı olarak izleme imkanı sunar. htop, top komutuna benzer, ancak daha kullanıcı dostu bir arayüze sahiptir ve daha fazla bilgi sunar.

## Kullanım
htop komutunun temel sözdizimi aşağıdaki gibidir:

```bash
htop [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-h`, `--help`: Yardım bilgilerini gösterir.
- `-s`, `--sort`: Görüntüleme sırasını belirler (örneğin, CPU veya bellek kullanımı).
- `-p`, `--pid`: Belirli bir işlem kimliğini (PID) izlemek için kullanılır.
- `-u`, `--user`: Belirli bir kullanıcıya ait işlemleri görüntüler.

## Yaygın Örnekler
Aşağıda htop komutunun bazı pratik kullanım örnekleri bulunmaktadır:

1. **htop'u başlatmak:**
   ```bash
   htop
   ```

2. **Belirli bir kullanıcıya ait işlemleri görüntülemek:**
   ```bash
   htop -u kullanıcı_adı
   ```

3. **İşlemleri CPU kullanımına göre sıralamak:**
   ```bash
   htop -s PERCENT_CPU
   ```

4. **Belirli bir PID'yi izlemek:**
   ```bash
   htop -p 1234
   ```

## İpuçları
- htop arayüzünde ok tuşları ile gezinerek işlemler arasında geçiş yapabilirsiniz.
- `F9` tuşuna basarak bir işlemi sonlandırabilir ve `F10` ile htop'tan çıkabilirsiniz.
- Htop'u çalıştırmadan önce terminalinizin boyutunu artırarak daha fazla bilgi görüntüleyebilirsiniz. 

htop, sistem yöneticileri ve kullanıcılar için güçlü bir araçtır ve sistem kaynaklarını izlemek için sıklıkla tercih edilir.