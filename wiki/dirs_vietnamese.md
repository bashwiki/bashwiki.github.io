# [Linux] Bash dirs cách sử dụng: Hiển thị danh sách thư mục

## Tổng quan
Lệnh `dirs` trong Bash được sử dụng để hiển thị danh sách các thư mục trong ngăn xếp thư mục hiện tại. Ngăn xếp này cho phép người dùng điều hướng nhanh chóng giữa các thư mục mà họ đã truy cập.

## Cách sử dụng
Cú pháp cơ bản của lệnh `dirs` như sau:
```
dirs [options] [arguments]
```

## Tùy chọn phổ biến
- `-l`: Hiển thị danh sách các thư mục trong định dạng dài.
- `-p`: Hiển thị danh sách thư mục mà không có các ký tự đặc biệt.
- `+n`: Hiển thị thư mục tại vị trí n trong ngăn xếp.
- `-n`: Hiển thị thư mục tại vị trí -n tính từ cuối ngăn xếp.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `dirs`:

1. Hiển thị danh sách thư mục hiện tại:
   ```bash
   dirs
   ```

2. Hiển thị danh sách thư mục với định dạng dài:
   ```bash
   dirs -l
   ```

3. Hiển thị thư mục tại vị trí thứ hai trong ngăn xếp:
   ```bash
   dirs +2
   ```

4. Hiển thị thư mục tính từ cuối ngăn xếp:
   ```bash
   dirs -1
   ```

## Mẹo
- Sử dụng lệnh `pushd` và `popd` để thêm hoặc xóa thư mục khỏi ngăn xếp, giúp quản lý các thư mục dễ dàng hơn.
- Kết hợp `dirs` với các lệnh khác như `echo` để hiển thị thông tin về thư mục hiện tại một cách rõ ràng hơn.
- Thường xuyên kiểm tra ngăn xếp thư mục của bạn để giữ cho nó gọn gàng và dễ quản lý.