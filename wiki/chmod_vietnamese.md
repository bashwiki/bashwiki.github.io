# [리눅스] Bash chmod 사용법

## Tổng quan
Lệnh `chmod` (viết tắt của "change mode") trong Bash được sử dụng để thay đổi quyền truy cập của các tệp và thư mục trong hệ thống Unix và Linux. Quyền truy cập này xác định ai có thể đọc, ghi hoặc thực thi một tệp hoặc thư mục. Lệnh này là một phần quan trọng trong việc quản lý bảo mật và quyền truy cập trong môi trường phát triển và sản xuất.

## Cú pháp
Cú pháp cơ bản của lệnh `chmod` như sau:

```bash
chmod [tùy chọn] [quyền] [tệp hoặc thư mục]
```

### Các tùy chọn phổ biến:
- `u`: đại diện cho người sở hữu tệp (user).
- `g`: đại diện cho nhóm tệp (group).
- `o`: đại diện cho những người khác (others).
- `a`: đại diện cho tất cả (all).
- `+`: thêm quyền.
- `-`: xóa quyền.
- `=`: thiết lập quyền cụ thể.

### Ví dụ về quyền:
- `r`: quyền đọc (read).
- `w`: quyền ghi (write).
- `x`: quyền thực thi (execute).

## Ví dụ
### Ví dụ 1: Thêm quyền thực thi cho người sở hữu
Để thêm quyền thực thi cho người sở hữu tệp `script.sh`, bạn có thể sử dụng lệnh sau:

```bash
chmod u+x script.sh
```

### Ví dụ 2: Thiết lập quyền đọc và ghi cho nhóm và quyền đọc cho những người khác
Để thiết lập quyền đọc và ghi cho nhóm và quyền đọc cho những người khác trên tệp `data.txt`, bạn có thể sử dụng lệnh sau:

```bash
chmod g+rw,o+r data.txt
```

## Mẹo
- Luôn kiểm tra quyền truy cập của tệp sau khi sử dụng lệnh `chmod` bằng cách sử dụng lệnh `ls -l`. Điều này giúp bạn xác nhận rằng các quyền đã được thiết lập đúng cách.
- Khi làm việc với các tệp nhạy cảm, hãy cẩn thận khi cấp quyền cho nhóm và những người khác để đảm bảo rằng không ai có thể truy cập vào thông tin quan trọng.
- Sử dụng quyền tối thiểu cần thiết cho các tệp và thư mục để giảm thiểu rủi ro bảo mật.