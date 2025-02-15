# [리눅스] Bash disown 사용법

## Tổng quan
Lệnh `disown` trong Bash được sử dụng để loại bỏ một hoặc nhiều tiến trình khỏi danh sách tiến trình hiện tại của shell. Khi một tiến trình bị disown, nó sẽ không còn bị quản lý bởi shell, nghĩa là nó sẽ không nhận tín hiệu SIGHUP (tín hiệu khi shell thoát) và sẽ tiếp tục chạy ngay cả khi người dùng thoát khỏi phiên làm việc. Lệnh này rất hữu ích khi bạn muốn giữ cho một tiến trình chạy trong nền mà không bị ảnh hưởng bởi việc đóng shell.

## Cách sử dụng
Cú pháp cơ bản của lệnh `disown` như sau:

```bash
disown [options] [job_spec]
```

Trong đó:
- `job_spec`: Chỉ định tiến trình mà bạn muốn disown. Nếu không chỉ định, lệnh sẽ áp dụng cho tiến trình gần nhất trong danh sách tiến trình.
- `options`: Một số tùy chọn phổ biến bao gồm:
  - `-a`: Disown tất cả các tiến trình.
  - `-r`: Chỉ disown các tiến trình đang chạy (running jobs).
  - `-h`: Đánh dấu tiến trình để không nhận tín hiệu SIGHUP khi shell thoát.

## Ví dụ
### Ví dụ 1: Disown một tiến trình cụ thể
Giả sử bạn đã khởi động một tiến trình trong nền với lệnh:

```bash
sleep 100 &
```

Bạn có thể sử dụng lệnh `jobs` để xem danh sách các tiến trình đang chạy:

```bash
jobs
```

Kết quả có thể là:

```
[1]+  12345 Running                 sleep 100 &
```

Để disown tiến trình này, bạn có thể sử dụng:

```bash
disown %1
```

### Ví dụ 2: Disown tất cả các tiến trình
Nếu bạn muốn disown tất cả các tiến trình đang chạy trong nền, bạn có thể sử dụng:

```bash
disown -a
```

Điều này sẽ loại bỏ tất cả các tiến trình khỏi quản lý của shell.

## Mẹo
- Trước khi sử dụng `disown`, hãy chắc chắn rằng bạn đã khởi động tiến trình trong nền bằng cách sử dụng dấu `&` ở cuối lệnh.
- Sử dụng lệnh `jobs` để kiểm tra các tiến trình đang chạy trước khi disown để tránh nhầm lẫn.
- Nếu bạn muốn giữ một tiến trình chạy mà không bị ảnh hưởng bởi việc thoát shell, hãy luôn sử dụng `disown` sau khi đưa tiến trình vào nền.

Hy vọng bài viết này giúp bạn hiểu rõ hơn về lệnh `disown` trong Bash và cách sử dụng nó hiệu quả!