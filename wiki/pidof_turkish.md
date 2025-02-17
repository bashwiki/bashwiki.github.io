# [Linux] Bash pidof Kullanımı: Bir işlemin PID'sini bulma

## Overview
`pidof` komutu, belirli bir programın veya işlemin Process ID (PID) numarasını bulmak için kullanılır. Bu, bir işlemi yönetmek veya izlemek için önemlidir.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
pidof [options] [arguments]
```

## Common Options
- `-o, --exclude`: Belirtilen PID'leri hariç tutar.
- `-s, --silent`: Çıktıyı sessiz modda verir; yalnızca PID varsa çıktı verir.
- `-c, --help`: Yardım bilgilerini gösterir.

## Common Examples
1. Belirli bir programın PID'sini bulmak:
   ```bash
   pidof firefox
   ```

2. Birden fazla PID'yi almak:
   ```bash
   pidof bash
   ```

3. Hariç tutma seçeneği ile PID'leri bulmak:
   ```bash
   pidof -o 1234 firefox
   ```

4. Sessiz modda PID almak:
   ```bash
   pidof -s firefox
   ```

## Tips
- `pidof` komutunu, bir işlemin çalışıp çalışmadığını kontrol etmek için kullanabilirsiniz.
- Birden fazla PID döndüğünde, çıktıyı bir dosyaya yönlendirmek faydalı olabilir.
- PID'leri kullanarak işlemleri sonlandırmak için `kill` komutuyla birlikte kullanabilirsiniz.