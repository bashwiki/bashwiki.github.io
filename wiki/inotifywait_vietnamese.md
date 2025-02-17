# [Linux] Bash inotifywait Cách sử dụng: Theo dõi thay đổi tệp tin

## Tổng quan
Lệnh `inotifywait` là một công cụ mạnh mẽ trong Bash cho phép bạn theo dõi các thay đổi trong hệ thống tệp tin. Nó sử dụng hệ thống inotify của Linux để thông báo cho người dùng về các sự kiện như tạo, xóa, hoặc sửa đổi tệp tin và thư mục.

## Cách sử dụng
Cú pháp cơ bản của lệnh `inotifywait` như sau:

```bash
inotifywait [options] [arguments]
```

## Tùy chọn phổ biến
- `-m`: Chế độ theo dõi liên tục, cho phép lệnh tiếp tục chạy và báo cáo các sự kiện mới.
- `-r`: Theo dõi các thư mục một cách đệ quy, bao gồm cả các thư mục con.
- `-e`: Chỉ định loại sự kiện cần theo dõi (ví dụ: `create`, `delete`, `modify`).
- `-q`: Chạy trong chế độ yên lặng, không hiển thị thông tin không cần thiết.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng `inotifywait`:

1. Theo dõi thay đổi trong một thư mục cụ thể:
   ```bash
   inotifywait -m /path/to/directory
   ```

2. Theo dõi sự kiện tạo và xóa tệp tin trong một thư mục:
   ```bash
   inotifywait -m -e create -e delete /path/to/directory
   ```

3. Theo dõi thay đổi trong một thư mục và tất cả các thư mục con:
   ```bash
   inotifywait -mr /path/to/directory
   ```

4. Ghi lại sự kiện vào một tệp tin:
   ```bash
   inotifywait -m /path/to/directory >> changes.log
   ```

## Mẹo
- Sử dụng tùy chọn `-q` để giảm thiểu thông tin hiển thị khi bạn chỉ muốn theo dõi các sự kiện quan trọng.
- Kết hợp `inotifywait` với các lệnh khác trong Bash để tự động hóa các tác vụ, chẳng hạn như sao lưu hoặc thông báo khi có thay đổi.
- Hãy chắc chắn rằng bạn có quyền truy cập vào thư mục mà bạn muốn theo dõi để tránh lỗi không cần thiết.