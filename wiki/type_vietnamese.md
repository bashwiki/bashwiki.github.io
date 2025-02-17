# [Linux] Bash type: Xác định loại của lệnh

## Overview
Lệnh `type` trong Bash được sử dụng để xác định loại của một lệnh hoặc một biến. Nó cho phép người dùng biết lệnh đó là một lệnh nội bộ, lệnh bên ngoài, hoặc một alias.

## Usage
Cú pháp cơ bản của lệnh `type` như sau:

```bash
type [options] [arguments]
```

## Common Options
- `-t`: Chỉ hiển thị loại của lệnh mà không có thông tin bổ sung.
- `-a`: Hiển thị tất cả các vị trí mà lệnh có thể được tìm thấy.
- `-p`: Chỉ hiển thị đường dẫn của lệnh nếu nó là một lệnh bên ngoài.

## Common Examples
- Kiểm tra loại của một lệnh:

```bash
type ls
```

- Kiểm tra loại của một alias:

```bash
alias ll='ls -l'
type ll
```

- Hiển thị tất cả các vị trí của một lệnh:

```bash
type -a echo
```

- Kiểm tra đường dẫn của một lệnh bên ngoài:

```bash
type -p grep
```

## Tips
- Sử dụng `type` để xác định xem một lệnh có phải là lệnh nội bộ hay không, điều này có thể giúp bạn hiểu rõ hơn về cách hoạt động của shell.
- Khi làm việc với nhiều alias, `type -a` rất hữu ích để tìm hiểu tất cả các phiên bản của lệnh mà bạn có thể sử dụng.
- Kết hợp `type` với các lệnh khác để kiểm tra tính khả dụng của các lệnh trong script của bạn.