# [리눅스] Bash export 사용법

## Overview
`export` komutu, bir shell değişkenini ortam değişkeni olarak ayarlamak için kullanılır. Ortam değişkenleri, alt süreçler tarafından erişilebilen ve kullanılan değişkenlerdir. Bu komut, bir değişkenin değerini dışa aktararak, o değişkenin alt süreçlerde de kullanılabilmesini sağlar. Genellikle, uygulama yapılandırmaları veya kullanıcı ayarları gibi bilgileri paylaşmak için kullanılır.

## Usage
Temel `export` komutunun sözdizimi aşağıdaki gibidir:

```bash
export VARIABLE_NAME=value
```

Burada `VARIABLE_NAME`, oluşturmak istediğiniz değişkenin adıdır ve `value`, bu değişkene atamak istediğiniz değerdir. Eğer sadece bir değişkeni dışa aktarmak istiyorsanız, aşağıdaki gibi de kullanabilirsiniz:

```bash
export VARIABLE_NAME
```

Bu durumda, `VARIABLE_NAME` değişkeninin mevcut değeri dışa aktarılacaktır.

## Examples
### Örnek 1: Değişken Oluşturma ve Dışa Aktarma
Aşağıdaki komut, `MY_VAR` adında bir değişken oluşturur ve ona "Hello, World!" değerini atar. Ardından bu değişkeni dışa aktarır.

```bash
MY_VAR="Hello, World!"
export MY_VAR
```

Bu işlemden sonra, `MY_VAR` değişkenine alt süreçlerden erişilebilir.

### Örnek 2: Dışa Aktarılan Değişkeni Kullanma
Aşağıdaki örnekte, `MY_VAR` değişkeni dışa aktarıldıktan sonra, bir alt süreçte (örneğin, bir `bash` oturumu) bu değişkenin nasıl kullanılabileceği gösterilmektedir.

```bash
export MY_VAR="Hello, World!"
bash -c 'echo $MY_VAR'
```

Bu komut, "Hello, World!" çıktısını verecektir.

## Tips
- Değişken adları büyük harfle başlamalıdır ve genellikle büyük harflerle yazılır. Bu, ortam değişkenlerini ve yerel değişkenleri ayırt etmeye yardımcı olur.
- `export` komutunu kullanmadan önce değişkenin değerini kontrol etmek için `echo $VARIABLE_NAME` komutunu kullanabilirsiniz.
- Birden fazla değişkeni aynı anda dışa aktarmak için, her birini ayrı bir `export` komutuyla veya tek bir komut içinde virgülle ayırarak belirtebilirsiniz:

```bash
export VAR1=value1 VAR2=value2
```

Bu ipuçları, `export` komutunu etkili bir şekilde kullanmanıza yardımcı olacaktır.