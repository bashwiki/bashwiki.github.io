# [Linux] Bash cd cách sử dụng: Chuyển đổi thư mục làm việc

## Overview
Lệnh `cd` (change directory) trong Bash được sử dụng để thay đổi thư mục làm việc hiện tại. Khi bạn sử dụng lệnh này, bạn có thể di chuyển giữa các thư mục trong hệ thống tệp của bạn.

## Usage
Cú pháp cơ bản của lệnh `cd` như sau:
```
cd [options] [arguments]
```

## Common Options
- `..`: Quay lại thư mục cha.
- `-`: Quay lại thư mục trước đó.
- `~`: Chuyển đến thư mục chính của người dùng hiện tại.

## Common Examples
- Chuyển đến thư mục con có tên "Documents":
  ```bash
  cd Documents
  ```
  
- Quay lại thư mục cha:
  ```bash
  cd ..
  ```

- Chuyển đến thư mục chính của người dùng:
  ```bash
  cd ~
  ```

- Quay lại thư mục trước đó:
  ```bash
  cd -
  ```

## Tips
- Sử dụng `cd` kèm theo `tab` để tự động hoàn thành tên thư mục.
- Kiểm tra thư mục hiện tại bằng lệnh `pwd` trước khi sử dụng `cd` để đảm bảo bạn đang ở đúng vị trí.
- Nếu bạn cần di chuyển đến một đường dẫn dài, hãy sử dụng dấu nháy đơn hoặc nháy kép để bao quanh đường dẫn đó.