# [Linux] Bash svn cách sử dụng: Quản lý phiên bản mã nguồn

## Overview
Lệnh `svn` (Subversion) là một hệ thống quản lý phiên bản mã nguồn, cho phép người dùng theo dõi các thay đổi trong mã nguồn và hợp tác với nhau trong các dự án phát triển phần mềm. Nó giúp quản lý các phiên bản khác nhau của tệp tin và thư mục, cho phép khôi phục lại phiên bản trước đó khi cần thiết.

## Usage
Cú pháp cơ bản của lệnh `svn` như sau:

```bash
svn [options] [arguments]
```

## Common Options
- `checkout`: Tải xuống một bản sao của kho lưu trữ từ máy chủ.
- `commit`: Gửi các thay đổi từ bản sao cục bộ lên kho lưu trữ.
- `update`: Cập nhật bản sao cục bộ với các thay đổi mới nhất từ kho lưu trữ.
- `add`: Thêm tệp tin hoặc thư mục mới vào kho lưu trữ.
- `delete`: Xóa tệp tin hoặc thư mục khỏi kho lưu trữ.
- `status`: Hiển thị trạng thái của các tệp tin trong bản sao cục bộ.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `svn`:

1. **Tải xuống kho lưu trữ**:
   ```bash
   svn checkout https://example.com/svn/myproject
   ```

2. **Gửi thay đổi lên kho lưu trữ**:
   ```bash
   svn commit -m "Cập nhật tài liệu"
   ```

3. **Cập nhật bản sao cục bộ**:
   ```bash
   svn update
   ```

4. **Thêm tệp tin mới**:
   ```bash
   svn add newfile.txt
   ```

5. **Xóa tệp tin**:
   ```bash
   svn delete oldfile.txt
   ```

6. **Kiểm tra trạng thái**:
   ```bash
   svn status
   ```

## Tips
- Luôn ghi chú rõ ràng khi sử dụng lệnh `commit` để giúp người khác hiểu rõ về những thay đổi bạn đã thực hiện.
- Thường xuyên cập nhật bản sao cục bộ của bạn để tránh xung đột khi gửi thay đổi.
- Sử dụng lệnh `status` để kiểm tra trạng thái của các tệp tin trước khi thực hiện các thao tác khác.