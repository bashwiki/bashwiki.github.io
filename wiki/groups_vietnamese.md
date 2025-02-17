# [Linux] Bash groups: Nhóm người dùng

## Overview
Lệnh `groups` trong Bash được sử dụng để hiển thị các nhóm mà một người dùng thuộc về. Nó cho phép người dùng kiểm tra các quyền và vai trò của mình trong hệ thống thông qua các nhóm.

## Usage
Cú pháp cơ bản của lệnh `groups` như sau:

```bash
groups [options] [arguments]
```

## Common Options
- `-h`, `--help`: Hiển thị thông tin trợ giúp về lệnh `groups`.
- `-v`, `--version`: Hiển thị phiên bản của lệnh `groups`.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `groups`:

1. **Hiển thị các nhóm của người dùng hiện tại:**
   ```bash
   groups
   ```

2. **Hiển thị các nhóm của một người dùng cụ thể:**
   ```bash
   groups username
   ```

3. **Sử dụng tùy chọn để hiển thị thông tin trợ giúp:**
   ```bash
   groups --help
   ```

## Tips
- Sử dụng lệnh `groups` để kiểm tra quyền truy cập của bạn trước khi thực hiện các thao tác yêu cầu quyền hạn cao hơn.
- Kết hợp lệnh `groups` với các lệnh khác như `id` để có thêm thông tin chi tiết về người dùng và nhóm.