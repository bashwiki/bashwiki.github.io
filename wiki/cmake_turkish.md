# [리눅스] Bash cmake 사용법

## Overview
`cmake`, yazılım projelerini derlemek ve yapılandırmak için kullanılan bir araçtır. CMake, platformdan bağımsız bir yapı sistemi oluşturmanıza olanak tanır ve projelerinizi farklı derleyiciler ve işletim sistemleri üzerinde kolayca yapılandırmanıza yardımcı olur. Genellikle C ve C++ projeleri için kullanılsa da, diğer dillerle de uyumlu çalışabilir.

## Usage
CMake komutunun temel sözdizimi şu şekildedir:

```bash
cmake [OPTIONS] <path-to-source>
```

### Yaygın Seçenekler
- `-B <dir>`: Derleme dosyalarının oluşturulacağı dizini belirtir. Bu seçenek, genellikle derleme dizinini ayırmak için kullanılır.
- `-S <dir>`: Kaynak dosyalarının bulunduğu dizini belirtir.
- `-G <generator>`: Kullanılacak yapılandırma aracını belirtir. Örneğin, `Ninja`, `Unix Makefiles` gibi.
- `-D <var>=<value>`: CMake değişkenlerini ayarlamak için kullanılır. Örneğin, `-D CMAKE_BUILD_TYPE=Release` ile yapı türünü belirleyebilirsiniz.

## Examples
### Örnek 1: Basit bir proje yapılandırması
Aşağıdaki komut, mevcut dizindeki kaynak dosyalarından bir derleme dizini oluşturur:

```bash
cmake -B build -S .
```

Bu komut, `build` adlı bir dizin oluşturacak ve mevcut dizindeki kaynak dosyalarını kullanarak yapılandırma işlemini gerçekleştirecektir.

### Örnek 2: Özelleştirilmiş bir yapılandırma
Aşağıdaki komut, `Ninja` jeneratörünü kullanarak bir proje yapılandırması yapar ve yapı türünü `Release` olarak ayarlar:

```bash
cmake -B build -S . -G Ninja -D CMAKE_BUILD_TYPE=Release
```

Bu komut, `build` dizininde `Ninja` jeneratörü ile yapılandırılmış bir proje oluşturacaktır.

## Tips
- CMake ile çalışırken, derleme ve kaynak dizinlerini ayırmak iyi bir uygulamadır. Bu, projelerinizi daha düzenli tutmanıza yardımcı olur.
- CMakeLists.txt dosyanızı düzenlerken, her değişiklikten sonra yapılandırma komutunu yeniden çalıştırmayı unutmayın.
- CMake ile ilgili daha fazla bilgi için resmi belgeleri inceleyebilirsiniz. Bu belgeler, daha karmaşık projeler için faydalı bilgiler içermektedir.