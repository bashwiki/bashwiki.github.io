# [Linux] Bash times Kullanımı: Çalışma süresi istatistiklerini gösterir

## Overview
`times` komutu, bir shell oturumu sırasında geçen süreyi ve bu oturumda çalıştırılan komutların toplam CPU zamanını gösterir. Bu komut, özellikle performans analizi ve sistem izleme için faydalıdır.

## Usage
Temel sözdizimi aşağıdaki gibidir:
```
times [options] [arguments]
```

## Common Options
- `-p`: Zamanı POSIX formatında gösterir.
- `-h`: İnsan tarafından okunabilir bir formatta çıktı verir.

## Common Examples
Aşağıda `times` komutunun bazı pratik örnekleri bulunmaktadır:

### Örnek 1: Basit Kullanım
Sadece `times` komutunu yazarak, mevcut shell oturumundaki toplam CPU sürelerini görebilirsiniz.
```bash
times
```

### Örnek 2: POSIX Formatında Çıktı
Zamanı POSIX formatında görmek için `-p` seçeneğini kullanabilirsiniz.
```bash
times -p
```

### Örnek 3: İnsan Okunabilir Format
İnsan tarafından okunabilir bir formatta çıktı almak için `-h` seçeneğini kullanabilirsiniz.
```bash
times -h
```

## Tips
- `times` komutunu, uzun süreli çalışan komutların ardından kullanarak, bu komutların ne kadar CPU süresi harcadığını analiz edebilirsiniz.
- Performans sorunlarını tespit etmek için, farklı komutların çalışma sürelerini karşılaştırmak amacıyla `times` komutunu sık sık kullanın.
- Shell oturumunuzun sonunda `times` komutunu çalıştırarak, o oturumda ne kadar süre harcadığınızı gözlemleyebilirsiniz.