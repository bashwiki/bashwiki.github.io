# [Linux] Bash logout <Sử dụng tương đương>: Đăng xuất khỏi phiên làm việc

## Overview
Lệnh `logout` trong Bash được sử dụng để kết thúc một phiên làm việc của người dùng trong terminal. Khi bạn thực hiện lệnh này, nó sẽ đóng cửa sổ terminal hoặc đăng xuất khỏi phiên SSH, giúp giải phóng tài nguyên hệ thống.

## Usage
Cú pháp cơ bản của lệnh `logout` như sau:
```
logout [options]
```

## Common Options
Lệnh `logout` không có nhiều tùy chọn, nhưng dưới đây là một số thông tin hữu ích:
- Không có tùy chọn: Lệnh `logout` thường được sử dụng mà không cần thêm tùy chọn nào.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `logout`:

1. **Đăng xuất khỏi phiên terminal:**
   ```bash
   logout
   ```

2. **Đăng xuất khỏi phiên SSH:**
   ```bash
   ssh user@hostname
   # Sau khi hoàn tất công việc, bạn có thể đăng xuất bằng cách:
   logout
   ```

3. **Khi bạn đang trong một shell con:**
   ```bash
   bash
   # Thực hiện một số lệnh
   logout
   ```

## Tips
- Hãy chắc chắn rằng bạn đã lưu tất cả công việc của mình trước khi thực hiện lệnh `logout`, vì lệnh này sẽ đóng phiên làm việc và không thể hoàn tác.
- Nếu bạn đang sử dụng nhiều tab hoặc cửa sổ terminal, hãy kiểm tra xem bạn có muốn đăng xuất tất cả hay chỉ một phiên làm việc cụ thể.
- Sử dụng lệnh `exit` cũng có thể đạt được hiệu ứng tương tự trong nhiều trường hợp.