# [리눅스] Bash svn 사용법

## Tổng quan
`svn` (Subversion) là một hệ thống quản lý phiên bản mã nguồn mở, cho phép các nhà phát triển theo dõi và quản lý các thay đổi trong mã nguồn của họ. Command `svn` được sử dụng để thực hiện các thao tác như kiểm tra mã nguồn, cập nhật, và cam kết các thay đổi lên kho lưu trữ.

## Cách sử dụng
Cú pháp cơ bản của command `svn` như sau:

```
svn [tùy chọn] [lệnh] [đối tượng]
```

### Các tùy chọn phổ biến:
- `checkout`: Tải mã nguồn từ kho lưu trữ về máy cục bộ.
- `commit`: Gửi các thay đổi từ máy cục bộ lên kho lưu trữ.
- `update`: Cập nhật mã nguồn cục bộ với các thay đổi mới nhất từ kho lưu trữ.
- `add`: Thêm tệp hoặc thư mục mới vào kho lưu trữ.
- `delete`: Xóa tệp hoặc thư mục khỏi kho lưu trữ.

## Ví dụ
### Ví dụ 1: Kiểm tra mã nguồn
Để tải mã nguồn từ kho lưu trữ, bạn có thể sử dụng lệnh sau:

```bash
svn checkout https://example.com/svn/myproject/trunk
```

Lệnh này sẽ tải mã nguồn từ đường dẫn đã chỉ định về thư mục cục bộ.

### Ví dụ 2: Cam kết thay đổi
Sau khi thực hiện các thay đổi trong mã nguồn, bạn có thể cam kết chúng bằng lệnh:

```bash
svn commit -m "Cập nhật tài liệu hướng dẫn"
```

Thay thế `"Cập nhật tài liệu hướng dẫn"` bằng thông điệp mô tả các thay đổi của bạn.

## Mẹo
- **Thường xuyên cập nhật**: Hãy sử dụng lệnh `svn update` thường xuyên để đảm bảo rằng bạn luôn làm việc với phiên bản mới nhất của mã nguồn.
- **Sử dụng thông điệp cam kết rõ ràng**: Khi cam kết thay đổi, hãy viết thông điệp rõ ràng và cụ thể để giúp người khác hiểu được mục đích của các thay đổi.
- **Kiểm tra trạng thái**: Sử dụng lệnh `svn status` để xem trạng thái của các tệp trong thư mục làm việc của bạn, giúp bạn theo dõi các thay đổi chưa được cam kết.

Hy vọng bài viết này sẽ giúp bạn hiểu rõ hơn về cách sử dụng command `svn` trong quản lý mã nguồn!