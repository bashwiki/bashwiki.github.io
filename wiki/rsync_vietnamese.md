# [Linux] Bash rsync cách sử dụng: Đồng bộ hóa tệp và thư mục

## Tổng quan
Lệnh `rsync` là một công cụ mạnh mẽ dùng để đồng bộ hóa và sao chép tệp và thư mục giữa hai vị trí, có thể là trên cùng một máy tính hoặc giữa các máy tính khác nhau qua mạng. Nó chỉ sao chép những thay đổi, giúp tiết kiệm băng thông và thời gian.

## Cách sử dụng
Cú pháp cơ bản của lệnh `rsync` như sau:

```bash
rsync [options] [arguments]
```

## Các tùy chọn phổ biến
- `-a`: Chế độ lưu trữ, bao gồm các thuộc tính như quyền truy cập và thời gian sửa đổi.
- `-v`: Hiển thị thông tin chi tiết về quá trình sao chép.
- `-z`: Nén dữ liệu trong quá trình truyền tải để tiết kiệm băng thông.
- `-r`: Sao chép thư mục một cách đệ quy.
- `--delete`: Xóa các tệp trong thư mục đích mà không còn tồn tại trong thư mục nguồn.

## Ví dụ thường gặp
1. **Sao chép tệp từ thư mục này sang thư mục khác:**
   ```bash
   rsync -av /path/to/source/file.txt /path/to/destination/
   ```

2. **Đồng bộ hóa thư mục giữa hai máy tính qua SSH:**
   ```bash
   rsync -avz -e ssh /path/to/local/dir/ user@remote:/path/to/remote/dir/
   ```

3. **Sao chép và xóa các tệp không còn tồn tại trong thư mục nguồn:**
   ```bash
   rsync -av --delete /path/to/source/ /path/to/destination/
   ```

4. **Sao chép tệp và nén dữ liệu:**
   ```bash
   rsync -avz /path/to/source/file.txt user@remote:/path/to/destination/
   ```

## Mẹo
- Luôn kiểm tra lệnh với tùy chọn `-n` (dry run) trước khi thực hiện để xem những gì sẽ xảy ra mà không thực sự sao chép tệp.
- Sử dụng `--progress` để theo dõi tiến trình sao chép, đặc biệt là khi làm việc với các tệp lớn.
- Đảm bảo rằng bạn có quyền truy cập cần thiết vào cả thư mục nguồn và thư mục đích để tránh lỗi trong quá trình sao chép.