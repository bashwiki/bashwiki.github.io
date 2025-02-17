# [Linux] Bash cat cách sử dụng: Hiển thị nội dung tệp

## Overview
Lệnh `cat` trong Bash được sử dụng để hiển thị nội dung của một hoặc nhiều tệp trên màn hình. Nó cũng có thể được sử dụng để kết hợp các tệp và tạo ra tệp mới.

## Usage
Cú pháp cơ bản của lệnh `cat` như sau:

```bash
cat [options] [arguments]
```

## Common Options
- `-n`: Đánh số các dòng trong đầu ra.
- `-b`: Đánh số các dòng không trống trong đầu ra.
- `-E`: Hiển thị ký tự kết thúc dòng `$`.
- `-s`: Giảm thiểu các dòng trống liên tiếp thành một dòng.

## Common Examples
- Hiển thị nội dung của một tệp:
    ```bash
    cat filename.txt
    ```

- Kết hợp nội dung của hai tệp và hiển thị:
    ```bash
    cat file1.txt file2.txt
    ```

- Tạo một tệp mới từ nội dung của tệp khác:
    ```bash
    cat source.txt > newfile.txt
    ```

- Hiển thị nội dung của tệp với số dòng:
    ```bash
    cat -n filename.txt
    ```

- Giảm thiểu các dòng trống trong tệp:
    ```bash
    cat -s filename.txt
    ```

## Tips
- Sử dụng `cat` để nhanh chóng kiểm tra nội dung của tệp mà không cần mở trình soạn thảo.
- Kết hợp với các lệnh khác như `grep` để tìm kiếm nội dung trong tệp.
- Cẩn thận khi sử dụng `>` để ghi đè tệp, vì điều này sẽ xóa nội dung tệp gốc.