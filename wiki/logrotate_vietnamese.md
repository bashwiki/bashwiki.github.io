# [Linux] Bash logrotate: Quản lý và xoay vòng file log

## Overview
Lệnh `logrotate` được sử dụng để quản lý và xoay vòng các file log trên hệ thống Linux. Nó giúp tự động nén, xóa hoặc gửi file log cũ để tiết kiệm không gian lưu trữ và giữ cho hệ thống hoạt động hiệu quả.

## Usage
Cú pháp cơ bản của lệnh `logrotate` như sau:

```bash
logrotate [options] [arguments]
```

## Common Options
- `-f`: Buộc thực hiện xoay vòng log ngay cả khi không cần thiết.
- `-s`: Chỉ định file trạng thái để lưu thông tin về các log đã được xử lý.
- `-d`: Chạy trong chế độ gỡ lỗi, hiển thị những gì sẽ xảy ra mà không thực hiện thay đổi.
- `-v`: Hiển thị thông tin chi tiết về quá trình xoay vòng log.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng `logrotate`:

### Ví dụ 1: Xoay vòng log theo cấu hình mặc định
```bash
logrotate /etc/logrotate.conf
```

### Ví dụ 2: Buộc xoay vòng log
```bash
logrotate -f /etc/logrotate.conf
```

### Ví dụ 3: Chạy logrotate trong chế độ gỡ lỗi
```bash
logrotate -d /etc/logrotate.conf
```

### Ví dụ 4: Sử dụng file trạng thái tùy chỉnh
```bash
logrotate -s /var/lib/logrotate/status /etc/logrotate.conf
```

## Tips
- Đảm bảo cấu hình file logrotate được thiết lập đúng để tránh mất dữ liệu log quan trọng.
- Kiểm tra thường xuyên các file log để đảm bảo chúng không vượt quá kích thước tối đa đã định.
- Sử dụng chế độ gỡ lỗi để kiểm tra cấu hình trước khi thực hiện xoay vòng thực tế.