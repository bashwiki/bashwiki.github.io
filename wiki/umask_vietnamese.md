# [리눅스] Bash umask 사용법

## Tổng quan
Lệnh `umask` trong Bash được sử dụng để thiết lập quyền truy cập mặc định cho các tệp và thư mục mới được tạo. Nó xác định các quyền mà người dùng không muốn cấp cho các tệp và thư mục mới. Mặc định, khi một tệp hoặc thư mục mới được tạo, quyền truy cập sẽ được tính toán dựa trên giá trị `umask` đã được thiết lập.

## Cú pháp
Cú pháp cơ bản của lệnh `umask` như sau:

```bash
umask [options] [mask]
```

### Các tùy chọn phổ biến:
- `-S`: Hiển thị giá trị `umask` hiện tại dưới dạng ký hiệu quyền (ví dụ: `u=rwx,g=rx,o=rx`).
- `-p`: Hiển thị giá trị `umask` hiện tại mà không thay đổi nó.

## Ví dụ
### Ví dụ 1: Kiểm tra giá trị umask hiện tại
Để xem giá trị `umask` hiện tại, bạn có thể sử dụng lệnh sau:

```bash
umask
```

Kết quả có thể là một giá trị như `0022`, điều này có nghĩa là quyền truy cập cho nhóm và người khác sẽ bị hạn chế.

### Ví dụ 2: Thiết lập umask mới
Để thiết lập giá trị `umask` mới, bạn có thể sử dụng lệnh sau:

```bash
umask 007
```

Giá trị này có nghĩa là quyền truy cập cho nhóm và người khác sẽ bị từ chối hoàn toàn cho các tệp mới được tạo.

## Mẹo
- Hãy nhớ rằng giá trị `umask` là một giá trị bit, vì vậy bạn có thể tính toán các quyền truy cập bằng cách sử dụng các số nhị phân.
- Để đảm bảo rằng các quyền truy cập được thiết lập đúng, hãy kiểm tra giá trị `umask` trước khi tạo tệp hoặc thư mục mới.
- Nếu bạn muốn thiết lập `umask` cho một phiên làm việc cụ thể, hãy thêm lệnh `umask` vào tệp cấu hình shell của bạn (như `.bashrc` hoặc `.bash_profile`) để tự động áp dụng mỗi khi bạn mở một phiên làm việc mới.