# [리눅스] Bash tput 사용법

## Tổng quan
Lệnh `tput` trong Bash được sử dụng để truy cập các thuộc tính của terminal, cho phép người dùng điều khiển cách hiển thị văn bản trên màn hình. Lệnh này chủ yếu được sử dụng để thay đổi màu sắc, định dạng văn bản (như in đậm hoặc gạch chân) và điều chỉnh vị trí con trỏ. `tput` giúp cải thiện trải nghiệm người dùng trong các ứng dụng dòng lệnh bằng cách cung cấp các tùy chọn định dạng linh hoạt.

## Cách sử dụng
Cú pháp cơ bản của lệnh `tput` như sau:

```bash
tput [tùy chọn] [tham số]
```

Một số tùy chọn phổ biến của lệnh `tput` bao gồm:

- `setaf`: Đặt màu văn bản (foreground color).
- `setab`: Đặt màu nền (background color).
- `bold`: Đặt văn bản ở định dạng in đậm.
- `smso`: Bật chế độ gạch chân (standout mode).
- `clear`: Xóa màn hình.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `tput`:

1. **Thay đổi màu sắc văn bản**:
   Để thay đổi màu sắc văn bản thành màu đỏ, bạn có thể sử dụng lệnh sau:

   ```bash
   tput setaf 1; echo "Đây là văn bản màu đỏ"; tput sgr0
   ```

   Trong đó, `setaf 1` đặt màu văn bản thành đỏ và `sgr0` sẽ đặt lại các thuộc tính về mặc định.

2. **In đậm và gạch chân**:
   Để in một dòng văn bản ở định dạng in đậm và gạch chân, bạn có thể sử dụng:

   ```bash
   tput bold; tput smso; echo "Văn bản này được in đậm và gạch chân"; tput rmso; tput sgr0
   ```

   Ở đây, `bold` bật chế độ in đậm và `smso` bật chế độ gạch chân. Sau khi in xong, `rmso` và `sgr0` sẽ đặt lại các thuộc tính.

## Mẹo
- Hãy luôn sử dụng `tput sgr0` sau khi thay đổi thuộc tính để đảm bảo rằng các thay đổi không ảnh hưởng đến các lệnh tiếp theo.
- Kiểm tra các mã màu của terminal của bạn, vì các mã màu có thể khác nhau giữa các hệ thống.
- Sử dụng `tput clear` để xóa màn hình trước khi hiển thị thông tin mới, giúp cải thiện tính dễ đọc của đầu ra.

Với lệnh `tput`, bạn có thể tạo ra các giao diện dòng lệnh hấp dẫn và dễ sử dụng hơn cho người dùng.