# [리눅스] Bash rsync 사용법

## Tổng quan
`rsync` là một công cụ mạnh mẽ trong Bash được sử dụng để sao chép và đồng bộ hóa tệp và thư mục giữa hai vị trí. Nó có khả năng làm việc trên cùng một máy tính hoặc qua mạng, giúp tiết kiệm băng thông bằng cách chỉ sao chép các phần đã thay đổi của tệp. `rsync` thường được sử dụng để sao lưu dữ liệu, đồng bộ hóa tệp giữa các máy chủ và quản lý các bản sao lưu.

## Cách sử dụng
Cú pháp cơ bản của lệnh `rsync` như sau:

```bash
rsync [OPTIONS] SOURCE DESTINATION
```

Trong đó:
- `SOURCE`: Đường dẫn đến tệp hoặc thư mục nguồn mà bạn muốn sao chép.
- `DESTINATION`: Đường dẫn đến tệp hoặc thư mục đích nơi bạn muốn sao chép dữ liệu.

Một số tùy chọn phổ biến của `rsync` bao gồm:
- `-a`: Chế độ lưu trữ, sao chép tệp và thư mục cùng với các thuộc tính của chúng.
- `-v`: Chế độ chi tiết, hiển thị thông tin chi tiết về quá trình sao chép.
- `-z`: Nén dữ liệu trong quá trình truyền tải, giúp tiết kiệm băng thông.
- `-r`: Sao chép thư mục và tất cả các tệp con bên trong.
- `--delete`: Xóa các tệp trong thư mục đích mà không còn tồn tại trong thư mục nguồn.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `rsync`.

### Ví dụ 1: Sao chép thư mục
Sao chép thư mục `my_folder` từ máy tính cục bộ đến một máy chủ từ xa:

```bash
rsync -avz my_folder/ user@remote_host:/path/to/destination/
```

### Ví dụ 2: Đồng bộ hóa thư mục
Đồng bộ hóa thư mục giữa hai vị trí, xóa các tệp không còn tồn tại trong thư mục nguồn:

```bash
rsync -av --delete /local/folder/ user@remote_host:/remote/folder/
```

## Mẹo
- Sử dụng tùy chọn `-n` (hoặc `--dry-run`) để kiểm tra những gì sẽ xảy ra mà không thực sự thực hiện sao chép. Điều này rất hữu ích để đảm bảo rằng bạn không xóa nhầm tệp.
- Thêm tùy chọn `-e ssh` để sử dụng SSH cho việc truyền tải an toàn khi sao chép tệp qua mạng.
- Thường xuyên kiểm tra các tệp sao lưu của bạn để đảm bảo rằng chúng được đồng bộ hóa chính xác và không có tệp nào bị thiếu.

Với những thông tin trên, bạn có thể bắt đầu sử dụng `rsync` để quản lý và đồng bộ hóa tệp một cách hiệu quả.