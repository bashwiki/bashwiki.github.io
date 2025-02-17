# [Linux] Bash getenforce: Xem trạng thái SELinux

## Overview
Lệnh `getenforce` được sử dụng để kiểm tra trạng thái hiện tại của SELinux (Security-Enhanced Linux). Nó cho phép người dùng biết liệu SELinux đang hoạt động ở chế độ "Enforcing", "Permissive" hay "Disabled".

## Usage
Cú pháp cơ bản của lệnh `getenforce` như sau:
```
getenforce [options]
```

## Common Options
- Không có tùy chọn nào phổ biến cho lệnh `getenforce`, vì lệnh này chỉ đơn giản là trả về trạng thái SELinux mà không cần thêm tham số.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `getenforce`:

1. Kiểm tra trạng thái SELinux:
   ```bash
   getenforce
   ```

2. Sử dụng lệnh trong một script để xác định hành động tiếp theo:
   ```bash
   if [ "$(getenforce)" == "Enforcing" ]; then
       echo "SELinux đang ở chế độ Enforcing."
   else
       echo "SELinux không ở chế độ Enforcing."
   fi
   ```

## Tips
- Hãy nhớ rằng lệnh `getenforce` chỉ trả về trạng thái hiện tại mà không thay đổi nó. Nếu bạn muốn thay đổi trạng thái SELinux, bạn sẽ cần sử dụng lệnh `setenforce`.
- Thường xuyên kiểm tra trạng thái SELinux là một thói quen tốt để đảm bảo rằng hệ thống của bạn được bảo mật đúng cách.