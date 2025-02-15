# [리눅스] Bash cron 사용법

## Tổng quan
`cron` là một dịch vụ trên hệ điều hành Unix và Linux cho phép người dùng lên lịch thực hiện các tác vụ tự động tại các thời điểm cụ thể. Mục đích chính của `cron` là tự động hóa các công việc định kỳ, chẳng hạn như sao lưu dữ liệu, gửi email hoặc thực hiện các lệnh hệ thống mà không cần sự can thiệp của người dùng.

## Cách sử dụng
Cú pháp cơ bản để sử dụng `cron` không phải là một lệnh trực tiếp mà là cấu hình trong tệp `crontab`. Để chỉnh sửa tệp `crontab`, bạn có thể sử dụng lệnh sau:

```bash
crontab -e
```

Mỗi dòng trong tệp `crontab` sẽ có định dạng như sau:

```
* * * * * command_to_execute
```

Trong đó:

- `* * * * *` là các trường thời gian, bao gồm:
  - Phút (0-59)
  - Giờ (0-23)
  - Ngày trong tháng (1-31)
  - Tháng (1-12)
  - Ngày trong tuần (0-7) (0 và 7 đều là Chủ nhật)

- `command_to_execute` là lệnh hoặc script mà bạn muốn thực hiện.

## Ví dụ
### Ví dụ 1: Chạy một script mỗi ngày lúc 2 giờ sáng
Để chạy một script có tên `backup.sh` mỗi ngày lúc 2 giờ sáng, bạn có thể thêm dòng sau vào tệp `crontab`:

```bash
0 2 * * * /path/to/backup.sh
```

### Ví dụ 2: Chạy một lệnh mỗi giờ
Nếu bạn muốn chạy lệnh `echo "Hello World"` mỗi giờ, bạn có thể thêm dòng sau:

```bash
0 * * * * echo "Hello World"
```

## Mẹo
- **Kiểm tra log**: Để theo dõi các tác vụ đã chạy, bạn có thể kiểm tra log của `cron` thường nằm trong `/var/log/syslog` hoặc `/var/log/cron`.
- **Đường dẫn đầy đủ**: Khi sử dụng `cron`, hãy đảm bảo sử dụng đường dẫn đầy đủ cho các lệnh hoặc script, vì môi trường của `cron` có thể khác với môi trường của shell tương tác.
- **Thử nghiệm trước**: Trước khi lên lịch cho một tác vụ, hãy thử chạy lệnh trong terminal để đảm bảo rằng nó hoạt động như mong muốn.
- **Sử dụng `MAILTO`**: Bạn có thể sử dụng biến `MAILTO` trong tệp `crontab` để nhận thông báo qua email về các tác vụ đã chạy hoặc lỗi xảy ra.

Với những thông tin trên, bạn đã có thể bắt đầu sử dụng `cron` để tự động hóa các tác vụ trên hệ thống của mình.