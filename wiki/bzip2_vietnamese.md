# [Linux] Bash bzip2 Cách sử dụng: Nén và giải nén tệp tin

## Tổng quan
Lệnh `bzip2` được sử dụng để nén và giải nén các tệp tin. Nó sử dụng thuật toán nén bzip2, giúp giảm kích thước tệp tin một cách hiệu quả hơn so với một số phương pháp nén khác.

## Cách sử dụng
Cú pháp cơ bản của lệnh `bzip2` như sau:
```
bzip2 [options] [arguments]
```

## Các tùy chọn phổ biến
- `-d`, `--decompress`: Giải nén tệp tin.
- `-k`, `--keep`: Giữ lại tệp tin gốc sau khi nén.
- `-f`, `--force`: Buộc ghi đè lên tệp tin đã tồn tại.
- `-v`, `--verbose`: Hiển thị thông tin chi tiết trong quá trình nén hoặc giải nén.
- `-z`, `--compress`: Nén tệp tin (mặc định).

## Ví dụ phổ biến
- Nén một tệp tin:
```bash
bzip2 file.txt
```

- Giải nén một tệp tin đã nén:
```bash
bzip2 -d file.txt.bz2
```

- Nén và giữ lại tệp gốc:
```bash
bzip2 -k file.txt
```

- Nén một thư mục (sử dụng tar trước):
```bash
tar -cvf - folder/ | bzip2 > folder.tar.bz2
```

- Giải nén tệp tin tar.bz2:
```bash
tar -xvjf folder.tar.bz2
```

## Mẹo
- Luôn kiểm tra dung lượng tệp tin sau khi nén để đảm bảo rằng quá trình nén đã thành công.
- Sử dụng tùy chọn `-v` để theo dõi tiến trình nén, đặc biệt khi làm việc với các tệp lớn.
- Kết hợp `bzip2` với `tar` để nén nhiều tệp tin hoặc thư mục thành một tệp duy nhất, giúp quản lý dễ dàng hơn.