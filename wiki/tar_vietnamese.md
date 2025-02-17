# [Linux] Bash tar Cách sử dụng: Nén và giải nén tệp

## Overview
Lệnh `tar` là một công cụ mạnh mẽ trong Bash được sử dụng để nén và giải nén các tệp và thư mục. Nó giúp bạn tạo ra các tệp lưu trữ (archive files) để dễ dàng quản lý và truyền tải dữ liệu.

## Usage
Cú pháp cơ bản của lệnh tar như sau:
```bash
tar [options] [arguments]
```

## Common Options
- `-c`: Tạo một tệp lưu trữ mới.
- `-x`: Giải nén tệp lưu trữ.
- `-f`: Chỉ định tên tệp lưu trữ.
- `-v`: Hiển thị tiến trình thực hiện (verbose).
- `-z`: Nén hoặc giải nén tệp với gzip.
- `-j`: Nén hoặc giải nén tệp với bzip2.

## Common Examples
- Tạo tệp lưu trữ từ một thư mục:
```bash
tar -cvf archive.tar /path/to/directory
```

- Giải nén tệp lưu trữ:
```bash
tar -xvf archive.tar
```

- Tạo tệp lưu trữ nén với gzip:
```bash
tar -czvf archive.tar.gz /path/to/directory
```

- Giải nén tệp lưu trữ nén với gzip:
```bash
tar -xzvf archive.tar.gz
```

- Tạo tệp lưu trữ nén với bzip2:
```bash
tar -cjvf archive.tar.bz2 /path/to/directory
```

- Giải nén tệp lưu trữ nén với bzip2:
```bash
tar -xjvf archive.tar.bz2
```

## Tips
- Luôn kiểm tra nội dung của tệp lưu trữ trước khi giải nén bằng lệnh `tar -tvf archive.tar`.
- Sử dụng tùy chọn `-C` để chỉ định thư mục đích khi giải nén.
- Đặt tên tệp lưu trữ có phần mở rộng phù hợp (như .tar, .tar.gz, .tar.bz2) để dễ dàng nhận biết.