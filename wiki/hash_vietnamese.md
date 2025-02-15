# [리눅스] Bash hash 사용법

## Tổng quan
Lệnh `hash` trong Bash được sử dụng để quản lý và theo dõi các đường dẫn của các lệnh đã được thực thi. Khi bạn chạy một lệnh, Bash sẽ ghi nhớ vị trí của lệnh đó trong bộ nhớ cache, giúp tăng tốc độ thực thi cho các lần gọi lệnh tiếp theo. Lệnh này rất hữu ích trong việc tối ưu hóa hiệu suất khi làm việc với các lệnh thường xuyên.

## Cách sử dụng
Cú pháp cơ bản của lệnh `hash` như sau:

```bash
hash [options] [command]
```

### Tùy chọn phổ biến:
- `-r`: Xóa bộ nhớ cache của tất cả các lệnh đã được ghi nhớ.
- `-l`: Hiển thị danh sách các lệnh đã được ghi nhớ cùng với đường dẫn của chúng.
- `command`: Tên của lệnh mà bạn muốn kiểm tra hoặc cập nhật trong bộ nhớ cache.

## Ví dụ
### Ví dụ 1: Kiểm tra các lệnh đã được ghi nhớ
Bạn có thể sử dụng lệnh `hash` mà không có tùy chọn nào để xem danh sách các lệnh đã được ghi nhớ:

```bash
hash
```

Kết quả sẽ hiển thị danh sách các lệnh cùng với đường dẫn của chúng.

### Ví dụ 2: Xóa bộ nhớ cache
Nếu bạn muốn xóa tất cả các lệnh đã được ghi nhớ, bạn có thể sử dụng tùy chọn `-r`:

```bash
hash -r
```

Điều này sẽ làm mới bộ nhớ cache, giúp Bash quên đi tất cả các đường dẫn đã lưu trước đó.

## Mẹo
- Sử dụng lệnh `hash` để kiểm tra xem một lệnh cụ thể có được ghi nhớ hay không, giúp bạn xác định xem có cần cập nhật đường dẫn cho lệnh đó hay không.
- Hãy nhớ rằng việc xóa bộ nhớ cache có thể làm giảm hiệu suất tạm thời cho các lệnh thường xuyên, vì Bash sẽ phải tìm kiếm lại đường dẫn cho các lệnh đó. Do đó, chỉ nên sử dụng tùy chọn `-r` khi thực sự cần thiết.