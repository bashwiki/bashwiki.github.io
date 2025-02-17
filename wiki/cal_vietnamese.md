# [Linux] Bash cal <Sử dụng tương đương>: Hiển thị lịch

## Overview
Lệnh `cal` trong Bash được sử dụng để hiển thị lịch tháng hoặc năm. Nó cho phép người dùng xem lịch một cách nhanh chóng và dễ dàng từ dòng lệnh.

## Usage
Cú pháp cơ bản của lệnh `cal` là:

```bash
cal [options] [arguments]
```

## Common Options
- `-m`: Hiển thị tháng hiện tại.
- `-y`: Hiển thị toàn bộ lịch năm hiện tại.
- `-3`: Hiển thị lịch của tháng trước, tháng hiện tại và tháng sau.
- `-j`: Hiển thị số ngày trong năm (ngày Julian).
- `-A [n]`: Hiển thị n tháng sau tháng hiện tại.
- `-B [n]`: Hiển thị n tháng trước tháng hiện tại.

## Common Examples
- Hiển thị lịch tháng hiện tại:

```bash
cal
```

- Hiển thị lịch của tháng 12 năm 2023:

```bash
cal 12 2023
```

- Hiển thị lịch của năm 2023:

```bash
cal -y 2023
```

- Hiển thị lịch của tháng trước, tháng hiện tại và tháng sau:

```bash
cal -3
```

- Hiển thị lịch tháng hiện tại với số ngày trong năm:

```bash
cal -j
```

## Tips
- Sử dụng `cal -A 1` để xem lịch tháng sau tháng hiện tại, rất hữu ích để lập kế hoạch.
- Kết hợp với lệnh `grep` để tìm kiếm ngày cụ thể trong lịch.
- Bạn có thể tạo một alias trong file cấu hình của Bash để dễ dàng sử dụng lệnh `cal` với các tùy chọn yêu thích.