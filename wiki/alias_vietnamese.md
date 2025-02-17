# [Linux] Bash alias sử dụng: Tạo bí danh cho các lệnh

## Overview
Lệnh `alias` trong Bash cho phép người dùng tạo bí danh cho các lệnh dài hoặc phức tạp, giúp tiết kiệm thời gian và công sức khi gõ lệnh. Khi bạn tạo một bí danh, bạn có thể sử dụng tên ngắn hơn để thực thi lệnh mà không cần phải gõ toàn bộ.

## Usage
Cú pháp cơ bản của lệnh `alias` như sau:

```bash
alias [tên_bí_danh]='[lệnh]'
```

## Common Options
- `-p`: Hiển thị tất cả các bí danh hiện có.
- `-d`: Xóa một bí danh đã được định nghĩa.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `alias`:

1. Tạo bí danh cho lệnh `ls -la`:
   ```bash
   alias ll='ls -la'
   ```

2. Tạo bí danh cho lệnh `git status`:
   ```bash
   alias gs='git status'
   ```

3. Tạo bí danh cho lệnh `rm -rf` với xác nhận:
   ```bash
   alias rmd='rm -rf'
   ```

4. Hiển thị tất cả các bí danh đã định nghĩa:
   ```bash
   alias -p
   ```

5. Xóa một bí danh:
   ```bash
   unalias ll
   ```

## Tips
- Nên thêm các bí danh vào tệp cấu hình như `~/.bashrc` hoặc `~/.bash_profile` để chúng có hiệu lực mỗi khi bạn mở terminal.
- Sử dụng tên bí danh ngắn gọn và dễ nhớ để tăng hiệu quả làm việc.
- Tránh tạo bí danh trùng với tên lệnh có sẵn để tránh nhầm lẫn.