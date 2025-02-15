# [리눅스] Bash uname 사용법

## Tổng quan
Lệnh `uname` trong Bash được sử dụng để hiển thị thông tin về hệ thống đang chạy. Lệnh này cung cấp các thông tin cơ bản như tên hệ điều hành, tên máy chủ, phiên bản kernel và nhiều thông tin khác. Mục đích chính của `uname` là giúp người dùng và các nhà phát triển hiểu rõ hơn về môi trường hệ thống mà họ đang làm việc.

## Cú pháp
Cú pháp cơ bản của lệnh `uname` là:

```bash
uname [tùy chọn]
```

Một số tùy chọn phổ biến của lệnh `uname` bao gồm:

- `-a`: Hiển thị tất cả thông tin hệ thống.
- `-s`: Hiển thị tên hệ điều hành.
- `-n`: Hiển thị tên máy chủ.
- `-r`: Hiển thị phiên bản kernel.
- `-v`: Hiển thị thông tin phiên bản kernel.
- `-m`: Hiển thị kiến trúc máy tính.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `uname`:

1. Hiển thị tất cả thông tin hệ thống:

```bash
uname -a
```
Kết quả có thể trông như sau:
```
Linux myhostname 5.4.0-42-generic #46-Ubuntu SMP Fri Aug 14 11:00:00 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

2. Hiển thị chỉ tên hệ điều hành:

```bash
uname -s
```
Kết quả sẽ là:
```
Linux
```

## Mẹo
- Sử dụng tùy chọn `-a` để có cái nhìn tổng quát về hệ thống của bạn, điều này rất hữu ích khi bạn cần thông tin chi tiết nhanh chóng.
- Kết hợp lệnh `uname` với các lệnh khác trong Bash để tự động hóa các tác vụ liên quan đến hệ thống, chẳng hạn như ghi lại thông tin hệ thống vào một tệp log.
- Lưu ý rằng một số tùy chọn có thể không khả dụng trên tất cả các hệ thống, vì vậy hãy kiểm tra tài liệu của hệ điều hành cụ thể của bạn nếu bạn gặp vấn đề.