# [Linux] Bash mknod: Tạo tệp đặc biệt

## Overview
Lệnh `mknod` được sử dụng để tạo các tệp đặc biệt trong hệ thống Unix/Linux. Các tệp này có thể là tệp thiết bị, cho phép người dùng tương tác với phần cứng như ổ đĩa, máy in hoặc các thiết bị khác.

## Usage
Cú pháp cơ bản của lệnh `mknod` như sau:
```
mknod [tùy chọn] [tên_tệp] [kiểu] [major] [minor]
```

## Common Options
- `-m, --mode`: Chỉ định quyền truy cập cho tệp được tạo.
- `-Z, --context`: Gán ngữ cảnh SELinux cho tệp.
- `-h, --help`: Hiển thị thông tin trợ giúp về lệnh `mknod`.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `mknod`:

1. Tạo một tệp thiết bị kiểu block:
   ```bash
   mknod /dev/myblock b 8 0
   ```

2. Tạo một tệp thiết bị kiểu character:
   ```bash
   mknod /dev/mychar c 1 3
   ```

3. Tạo một tệp thiết bị với quyền truy cập cụ thể:
   ```bash
   mknod -m 660 /dev/mydevice c 10 200
   ```

## Tips
- Đảm bảo rằng bạn có quyền root khi sử dụng lệnh `mknod`, vì việc tạo tệp thiết bị thường yêu cầu quyền cao.
- Kiểm tra các số major và minor để đảm bảo rằng bạn đang tạo đúng tệp thiết bị cho phần cứng mà bạn muốn tương tác.
- Sử dụng lệnh `ls -l /dev` để xác minh rằng tệp thiết bị đã được tạo thành công.