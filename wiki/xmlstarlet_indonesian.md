# [Linux] Bash xmlstarlet Penggunaan: Mengelola dan Memanipulasi XML

## Overview
`xmlstarlet` adalah alat baris perintah yang digunakan untuk memanipulasi dan mengelola file XML. Dengan `xmlstarlet`, pengguna dapat melakukan berbagai operasi seperti mengubah, mengekstrak, dan memvalidasi data XML dengan cara yang efisien.

## Usage
Berikut adalah sintaks dasar dari perintah `xmlstarlet`:

```bash
xmlstarlet [options] [arguments]
```

## Common Options
- `sel`: Memilih elemen atau atribut dari dokumen XML.
- `ed`: Mengedit elemen atau atribut dalam dokumen XML.
- `val`: Memvalidasi dokumen XML terhadap skema.
- `fo`: Mengubah format dokumen XML.
- `xml`: Menampilkan dokumen XML dalam format yang lebih mudah dibaca.

## Common Examples

### 1. Memilih Elemen
Untuk memilih elemen tertentu dari file XML, gunakan perintah berikut:

```bash
xmlstarlet sel -t -m "//namaElemen" -v "." -n file.xml
```

### 2. Mengedit Elemen
Untuk mengedit elemen dalam file XML, Anda bisa menggunakan perintah ini:

```bash
xmlstarlet ed -u "//namaElemen" -v "nilaiBaru" file.xml
```

### 3. Memvalidasi XML
Untuk memvalidasi file XML terhadap skema, gunakan perintah berikut:

```bash
xmlstarlet val -e -s skema.xsd file.xml
```

### 4. Mengubah Format XML
Untuk mengubah format dokumen XML agar lebih mudah dibaca, gunakan:

```bash
xmlstarlet fo file.xml
```

## Tips
- Selalu buat salinan cadangan dari file XML sebelum melakukan pengeditan untuk menghindari kehilangan data.
- Gunakan opsi `-d` untuk menghapus elemen yang tidak diinginkan dengan aman.
- Manfaatkan opsi `-o` untuk menyimpan hasil keluaran ke file baru agar tidak mengubah file asli secara langsung.