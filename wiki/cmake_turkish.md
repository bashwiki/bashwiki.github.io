# [Linux] Bash cmake Kullanımı: Proje yapılandırma aracı

## Genel Bakış
`cmake`, yazılım projelerini yapılandırmak için kullanılan bir araçtır. Proje dosyalarını oluşturmak ve derleme süreçlerini yönetmek için platformdan bağımsız bir çözüm sunar. CMake, farklı derleyicilere ve platformlara uygun yapı dosyaları oluşturmayı kolaylaştırır.

## Kullanım
Temel sözdizimi aşağıdaki gibidir:
```bash
cmake [seçenekler] [argümanlar]
```

## Yaygın Seçenekler
- `-S <dizin>`: Kaynak dizinini belirtir.
- `-B <dizin>`: Yapı dizinini belirtir.
- `-D <değişken>=<değer>`: Değişkenleri tanımlamak için kullanılır.
- `--build <dizin>`: Belirtilen dizinde projeyi derler.
- `--target <hedef>`: Belirtilen hedefi derler.

## Yaygın Örnekler
Aşağıda `cmake` komutunun bazı pratik kullanım örnekleri verilmiştir:

### Proje Yapılandırma
Bir proje dizininde yapılandırma yapmak için:
```bash
cmake -S . -B build
```

### Belirli Bir Değişken Tanımlama
Bir değişken tanımlayarak yapılandırma yapmak için:
```bash
cmake -S . -B build -D CMAKE_BUILD_TYPE=Release
```

### Projeyi Derleme
Yapı dizininde projeyi derlemek için:
```bash
cmake --build build
```

### Belirli Bir Hedefi Derleme
Belirli bir hedefi derlemek için:
```bash
cmake --build build --target my_target
```

## İpuçları
- Projelerinizi temiz bir şekilde yapılandırmak için her zaman ayrı bir yapı dizini kullanın.
- `CMakeLists.txt` dosyanızda değişiklik yaptıktan sonra yapı dizinini yeniden yapılandırmayı unutmayın.
- Hata ayıklama için `-D CMAKE_VERBOSE_MAKEFILE:BOOL=ON` seçeneğini ekleyerek daha fazla bilgi alabilirsiniz.