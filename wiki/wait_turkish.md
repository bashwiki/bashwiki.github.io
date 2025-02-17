# [Linux] Bash wait Kullanımı: İşlem bekletme komutu

## Overview
`wait` komutu, bir veya daha fazla arka plan işleminin tamamlanmasını beklemek için kullanılır. Bu komut, genellikle bir betik içinde arka planda çalışan işlemlerin sonuçlarını almak için kullanılır.

## Usage
Temel sözdizimi şu şekildedir:

```bash
wait [options] [arguments]
```

## Common Options
- `-n`: Beklemek için belirtilen işlemlerden herhangi birinin tamamlanmasını bekler.
- `PID`: Belirtilen işlem kimliğine (PID) sahip işlemi bekler. Eğer PID verilmezse, tüm arka plan işlemleri beklenir.

## Common Examples

### Örnek 1: Arka planda bir işlem başlatma ve bekleme
```bash
sleep 5 &
wait
echo "5 saniye bekledikten sonra devam edildi."
```
Bu örnekte, `sleep 5` komutu arka planda çalıştırılır ve `wait` komutu, bu işlemin tamamlanmasını bekler.

### Örnek 2: Belirli bir PID için bekleme
```bash
sleep 3 &
PID=$!
echo "PID: $PID"
wait $PID
echo "İşlem tamamlandı."
```
Burada, `sleep 3` komutunun PID'si alınır ve `wait` komutu bu PID için bekler.

### Örnek 3: Birden fazla arka plan işlemi için bekleme
```bash
sleep 2 &
sleep 4 &
wait
echo "Tüm işlemler tamamlandı."
```
Bu örnekte, iki arka plan işlemi başlatılır ve `wait` komutu, her iki işlemin de tamamlanmasını bekler.

## Tips
- Arka planda çalışan işlemlerinizin sonuçlarını almak için `wait` komutunu kullanmayı unutmayın.
- `wait` komutunu kullanırken, hangi işlemi beklediğinizi bilmek için PID'leri takip etmek iyi bir uygulamadır.
- Eğer birden fazla işlem başlattıysanız, `-n` seçeneği ile herhangi birinin tamamlanmasını beklemek, zaman kazandırabilir.