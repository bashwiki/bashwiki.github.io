# [Linux] Bash timeout Kullanımı: Komutların belirli bir süre içinde çalışmasını sağlamak

## Overview
`timeout` komutu, bir komutun veya programın belirli bir süre içinde çalışmasını sağlar. Eğer belirtilen süre dolduğunda komut hala çalışıyorsa, `timeout` komutu onu durdurur. Bu, uzun süren işlemleri kontrol altında tutmak için oldukça yararlıdır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```bash
timeout [options] [duration] [command]
```

## Common Options
- `-k`, `--kill-after=DURATION`: Komut belirtilen süre içinde bitmezse, bu süre dolduktan sonra komutu öldürmek için ek bir süre belirler.
- `-s`, `--signal=SIGNAL`: Komuta gönderilecek sinyali belirtir. Varsayılan olarak `TERM` sinyali gönderilir.
- `--preserve-status`: Komutun çıkış durumunu korur. Bu, `timeout` komutunun çıkış durumunu değiştirmeden komutun çıkış durumunu döndürmesini sağlar.

## Common Examples
Aşağıda `timeout` komutunun bazı pratik örnekleri bulunmaktadır:

### Örnek 1: Basit bir komut için timeout kullanma
```bash
timeout 5s sleep 10
```
Bu komut, `sleep 10` komutunu başlatır, ancak sadece 5 saniye çalışmasına izin verir. 5 saniye sonra `sleep` komutu durdurulacaktır.

### Örnek 2: Belirli bir sinyal ile komutu durdurma
```bash
timeout -s SIGKILL 3m my_long_running_command
```
Bu komut, `my_long_running_command` komutunu 3 dakika çalıştırır. Eğer bu süre dolarsa, komut `SIGKILL` sinyali ile durdurulur.

### Örnek 3: Çıkış durumunu koruma
```bash
timeout --preserve-status 10s my_command
echo $?
```
Bu komut, `my_command`'ı 10 saniye içinde çalıştırır ve ardından çıkış durumunu korur. `echo $?` ile `my_command`'ın çıkış durumu görüntülenir.

## Tips
- `timeout` komutunu uzun süren işlemleri yönetmek için kullanarak sistem kaynaklarınızı daha verimli kullanabilirsiniz.
- Komutlarınızın beklenmedik bir şekilde uzun sürmesini önlemek için `timeout` ile birlikte uygun süreler belirleyin.
- Çalıştırdığınız komutların hangi sinyalleri desteklediğini kontrol ederek, `-s` seçeneği ile uygun sinyali seçin.