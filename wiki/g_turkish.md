# [리눅스] Bash g++ 사용법

## Overview
`g++`, GNU Compiler Collection'ın (GCC) C++ derleyicisidir. C++ programlarını derlemek ve çalıştırmak için kullanılır. Geliştiriciler, `g++` komutunu kullanarak kaynak kod dosyalarını makine diline çevirerek çalıştırılabilir programlar oluştururlar. Bu komut, C++ dilinin standartlarına uygun olarak yazılmış kodları derlemek için yaygın olarak tercih edilmektedir.

## Usage
`g++` komutunun temel sözdizimi aşağıdaki gibidir:

```bash
g++ [seçenekler] [kaynak_dosyaları] -o [çıkış_dosyası]
```

### Yaygın Seçenekler:
- `-o [çıkış_dosyası]`: Derleme sonucunda oluşturulacak çalıştırılabilir dosyanın adını belirtir.
- `-Wall`: Tüm uyarıları etkinleştirir, bu sayede kodunuzda olası hataları daha kolay tespit edebilirsiniz.
- `-g`: Hata ayıklama bilgilerini derleme dosyasına ekler, bu da `gdb` gibi hata ayıklayıcılarla daha iyi çalışmanıza olanak tanır.
- `-std=c++11`: C++11 standardını kullanarak derleme yapar. Farklı C++ standartları için `c++14`, `c++17` gibi seçenekler de mevcuttur.

## Examples
### Örnek 1: Basit Bir C++ Programını Derlemek
Aşağıdaki örnekte, `hello.cpp` adlı bir dosyayı derleyerek `hello` adlı çalıştırılabilir bir dosya oluşturacağız.

```bash
g++ hello.cpp -o hello
```

Bu komut, `hello.cpp` dosyasını derler ve `hello` adlı çalıştırılabilir dosyayı oluşturur. Ardından, programı çalıştırmak için:

```bash
./hello
```

### Örnek 2: Uyarıları Etkinleştirerek Derlemek
Aşağıdaki komut, `program.cpp` dosyasını derlerken tüm uyarıları etkinleştirir ve hata ayıklama bilgilerini ekler:

```bash
g++ -Wall -g program.cpp -o program
```

Bu komut, `program.cpp` dosyasını derlerken olası hataları ve uyarıları gösterir, ayrıca hata ayıklama için gerekli bilgileri de ekler.

## Tips
- Derleme sırasında uyarıları görmek, kodunuzun kalitesini artırmak için önemlidir. Bu nedenle `-Wall` seçeneğini kullanmayı unutmayın.
- Hata ayıklama yapacaksanız, `-g` seçeneğini kullanarak derleyin. Bu, hata ayıklama sürecini kolaylaştırır.
- Farklı C++ standartlarını kullanmak için uygun `-std` seçeneğini eklemeyi unutmayın. Bu, kodunuzun uyumluluğunu artırır.
- Projelerinizde birden fazla kaynak dosyası varsa, tüm dosyaları tek bir komutla derlemek için dosya adlarını boşlukla ayırarak ekleyebilirsiniz.

Bu bilgilerle `g++` komutunu etkili bir şekilde kullanabilir ve C++ projelerinizi başarıyla derleyebilirsiniz.