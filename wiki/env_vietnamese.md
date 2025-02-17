# [Linux] Bash env cách sử dụng: [quản lý biến môi trường]

## Tổng quan
Lệnh `env` trong Bash được sử dụng để hiển thị hoặc thiết lập các biến môi trường. Nó cho phép người dùng chạy một chương trình trong một môi trường mới, với các biến môi trường được chỉ định.

## Cách sử dụng
Cú pháp cơ bản của lệnh `env` như sau:

```bash
env [tùy chọn] [tham số]
```

## Tùy chọn phổ biến
- `-i`: Khởi tạo một môi trường trống, không có biến môi trường nào.
- `-u VAR`: Xóa biến môi trường có tên là `VAR`.
- `VAR=value`: Thiết lập một biến môi trường mới với tên `VAR` và giá trị `value`.

## Ví dụ phổ biến
1. **Hiển thị tất cả các biến môi trường:**
   ```bash
   env
   ```

2. **Chạy một lệnh với biến môi trường mới:**
   ```bash
   env MY_VAR=hello bash -c 'echo $MY_VAR'
   ```

3. **Xóa một biến môi trường:**
   ```bash
   env -u MY_VAR bash -c 'echo $MY_VAR'
   ```

4. **Khởi tạo một môi trường trống:**
   ```bash
   env -i bash -c 'echo $HOME'
   ```

## Mẹo
- Sử dụng `env` để kiểm tra các biến môi trường hiện tại trước khi chạy một lệnh quan trọng.
- Khi cần chạy một chương trình trong một môi trường sạch sẽ, hãy sử dụng tùy chọn `-i` để tránh ảnh hưởng từ các biến môi trường hiện có.
- Kết hợp `env` với các lệnh khác để tạo ra các kịch bản tự động hóa hiệu quả hơn.