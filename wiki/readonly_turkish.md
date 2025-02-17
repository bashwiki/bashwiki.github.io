# [Linux] Bash readonly Kullanımı: Değiştirilemez Değişkenler Oluşturma

## Overview
`readonly` komutu, bir değişkenin değerini değiştirilmez hale getirir. Bu, bir değişkenin bir kez atandıktan sonra tekrar atanmasını veya değiştirilmesini engeller. Böylece, belirli bir değerin sabit kalmasını sağlamak için kullanılır.

## Usage
Temel sözdizimi aşağıdaki gibidir:

```bash
readonly [options] [arguments]
```

## Common Options
- `-p`: Mevcut readonly değişkenlerini ve değerlerini listelemek için kullanılır.

## Common Examples

### 1. Basit bir readonly değişken oluşturma
```bash
readonly MY_VAR="Sabit Değer"
```

### 2. Değişkenin değerini değiştirmeye çalışmak
```bash
MY_VAR="Yeni Değer"  # Bu, hata verecektir.
```

### 3. Mevcut readonly değişkenlerini listeleme
```bash
readonly -p
```

### 4. Bir değişkeni readonly hale getirmeden önce atama
```bash
MY_VAR="Başlangıç Değeri"
readonly MY_VAR
```

## Tips
- `readonly` kullanmadan önce değişkenin değerini doğru bir şekilde atadığınızdan emin olun.
- Değişkenleri `readonly` olarak tanımlamak, özellikle büyük projelerde hata yapma olasılığını azaltır.
- `readonly` değişkenleri, betiklerinizi daha güvenilir hale getirir ve beklenmeyen değişikliklerden korur.