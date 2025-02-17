# [Linux] Bash chmod cách sử dụng: Thay đổi quyền truy cập tệp

## Tổng quan
Lệnh `chmod` được sử dụng để thay đổi quyền truy cập cho các tệp và thư mục trong hệ điều hành Unix và Linux. Quyền truy cập có thể được thiết lập cho người sở hữu tệp, nhóm và người dùng khác.

## Cách sử dụng
Cú pháp cơ bản của lệnh `chmod` như sau:
```bash
chmod [options] [arguments]
```

## Các tùy chọn phổ biến
- `-R`: Thay đổi quyền truy cập cho tất cả các tệp và thư mục con bên trong thư mục.
- `u`: Đại diện cho người sở hữu tệp (user).
- `g`: Đại diện cho nhóm (group).
- `o`: Đại diện cho người dùng khác (others).
- `a`: Đại diện cho tất cả (all).
- `+`: Thêm quyền.
- `-`: Xóa quyền.
- `=`: Thiết lập quyền cụ thể.

## Ví dụ thường gặp
- **Thêm quyền đọc cho người dùng khác:**
```bash
chmod o+r filename.txt
```

- **Xóa quyền ghi cho nhóm:**
```bash
chmod g-w filename.txt
```

- **Thiết lập quyền truy cập cho người sở hữu, nhóm và người khác:**
```bash
chmod u=rwx,g=rx,o=r filename.txt
```

- **Thay đổi quyền cho tất cả tệp trong thư mục:**
```bash
chmod -R 755 /path/to/directory
```

## Mẹo
- Sử dụng `ls -l` để kiểm tra quyền truy cập hiện tại của tệp trước khi thay đổi.
- Hãy cẩn thận khi sử dụng tùy chọn `-R`, vì nó sẽ áp dụng thay đổi cho tất cả các tệp và thư mục con.
- Nên sử dụng quyền tối thiểu cần thiết để bảo mật tốt hơn cho hệ thống của bạn.