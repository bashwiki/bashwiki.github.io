# [Linux] Bash pwd Cách sử dụng: Hiển thị thư mục làm việc hiện tại

## Tổng quan
Lệnh `pwd` (print working directory) trong Bash được sử dụng để hiển thị đường dẫn tuyệt đối của thư mục làm việc hiện tại. Đây là một công cụ hữu ích để biết bạn đang ở đâu trong hệ thống tệp.

## Cách sử dụng
Cú pháp cơ bản của lệnh `pwd` như sau:
```
pwd [options] [arguments]
```

## Tùy chọn thông dụng
- `-L`: Hiển thị đường dẫn logic (theo liên kết tượng trưng).
- `-P`: Hiển thị đường dẫn vật lý (theo đường dẫn thực tế, không theo liên kết tượng trưng).

## Ví dụ thông dụng
Dưới đây là một số ví dụ về cách sử dụng lệnh `pwd`:

1. Hiển thị thư mục làm việc hiện tại:
   ```bash
   pwd
   ```

2. Hiển thị đường dẫn vật lý:
   ```bash
   pwd -P
   ```

3. Hiển thị đường dẫn logic:
   ```bash
   pwd -L
   ```

## Mẹo
- Sử dụng `pwd` trước khi thực hiện các lệnh khác để xác định vị trí hiện tại của bạn trong hệ thống tệp.
- Kết hợp `pwd` với các lệnh khác như `cd` để dễ dàng điều hướng trong hệ thống tệp.
- Nếu bạn đang làm việc với các liên kết tượng trưng, hãy chú ý đến sự khác biệt giữa tùy chọn `-L` và `-P` để tránh nhầm lẫn.