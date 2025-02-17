# [Linux] Bash fdisk cách sử dụng: Quản lý phân vùng ổ đĩa

## Tổng quan
Lệnh `fdisk` là một công cụ dòng lệnh dùng để quản lý các phân vùng trên ổ đĩa cứng. Nó cho phép người dùng tạo, xóa, sửa đổi và xem thông tin phân vùng của các ổ đĩa.

## Cách sử dụng
Cú pháp cơ bản của lệnh `fdisk` như sau:

```bash
fdisk [options] [arguments]
```

## Các tùy chọn phổ biến
- `-l`: Liệt kê tất cả các phân vùng trên các ổ đĩa.
- `-u`: Sử dụng đơn vị là sector thay vì cylinder.
- `-n`: Tạo một phân vùng mới.
- `-d`: Xóa một phân vùng.
- `-p`: In ra bảng phân vùng hiện tại.

## Ví dụ thường gặp
1. **Liệt kê các phân vùng trên ổ đĩa**:
   ```bash
   fdisk -l
   ```

2. **Mở một ổ đĩa cụ thể để quản lý phân vùng**:
   ```bash
   fdisk /dev/sda
   ```

3. **Tạo một phân vùng mới**:
   Trong chế độ tương tác của `fdisk`, bạn có thể sử dụng lệnh `n` để tạo phân vùng mới.

4. **Xóa một phân vùng**:
   Trong chế độ tương tác của `fdisk`, bạn có thể sử dụng lệnh `d` để xóa phân vùng.

5. **In ra bảng phân vùng hiện tại**:
   ```bash
   fdisk -p /dev/sda
   ```

## Mẹo
- Trước khi thực hiện bất kỳ thay đổi nào với `fdisk`, hãy sao lưu dữ liệu quan trọng để tránh mất mát.
- Sử dụng `man fdisk` để xem hướng dẫn chi tiết và các tùy chọn khác của lệnh.
- Hãy cẩn thận khi xóa hoặc thay đổi phân vùng, vì điều này có thể ảnh hưởng đến hệ điều hành và dữ liệu của bạn.