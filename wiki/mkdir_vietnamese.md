# [리눅스] Bash mkdir 사용법

## Tổng quan
Lệnh `mkdir` (make directory) trong Bash được sử dụng để tạo thư mục mới trong hệ thống tệp. Đây là một trong những lệnh cơ bản và quan trọng nhất trong quản lý tệp và thư mục trên các hệ điều hành dựa trên Unix, bao gồm Linux và macOS. Mục đích chính của lệnh này là giúp người dùng tổ chức và quản lý dữ liệu của họ một cách hiệu quả hơn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `mkdir` như sau:

```bash
mkdir [tùy chọn] tên_thư_mục
```

### Các tùy chọn phổ biến:
- `-p`: Tạo các thư mục cha cần thiết nếu chúng chưa tồn tại. Nếu thư mục đã tồn tại, lệnh sẽ không báo lỗi.
- `-v`: Hiển thị thông báo chi tiết về các thư mục đã được tạo.
- `-m`: Đặt quyền truy cập cho thư mục mới. Ví dụ: `-m 755` sẽ tạo thư mục với quyền truy cập 755.

## Ví dụ
### Ví dụ 1: Tạo một thư mục đơn giản
Để tạo một thư mục mới có tên là `thumuc_moi`, bạn có thể sử dụng lệnh sau:

```bash
mkdir thumuc_moi
```

### Ví dụ 2: Tạo thư mục với cấu trúc cha
Nếu bạn muốn tạo một thư mục con bên trong một thư mục cha mà chưa tồn tại, bạn có thể sử dụng tùy chọn `-p`:

```bash
mkdir -p thu_muc_cha/thu_muc_con
```

Lệnh này sẽ tạo `thu_muc_cha` nếu nó chưa tồn tại và sau đó tạo `thu_muc_con` bên trong.

## Mẹo
- Sử dụng tùy chọn `-v` để xác nhận rằng thư mục đã được tạo thành công, đặc biệt khi bạn đang tạo nhiều thư mục cùng một lúc.
- Nếu bạn không chắc chắn về quyền truy cập của thư mục mới, hãy sử dụng tùy chọn `-m` để chỉ định quyền truy cập ngay khi tạo thư mục.
- Hãy cẩn thận khi sử dụng lệnh `mkdir` trong các thư mục quan trọng để tránh tạo ra các thư mục không cần thiết.