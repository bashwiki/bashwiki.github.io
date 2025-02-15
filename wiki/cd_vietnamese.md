# [리눅스] Bash cd 사용법

## Tổng quan
Lệnh `cd` (change directory) trong Bash được sử dụng để thay đổi thư mục làm việc hiện tại trong hệ thống tệp. Đây là một trong những lệnh cơ bản và quan trọng nhất mà người dùng cần biết khi làm việc với dòng lệnh, giúp điều hướng giữa các thư mục một cách dễ dàng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `cd` như sau:

```bash
cd [tùy chọn] [thư mục]
```

### Tùy chọn phổ biến:
- `..`: Quay lại thư mục cha của thư mục hiện tại.
- `-`: Quay lại thư mục trước đó mà bạn đã truy cập.
- `~`: Chuyển đến thư mục chính của người dùng hiện tại.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `cd`:

1. Chuyển đến thư mục con có tên "documents":
   ```bash
   cd documents
   ```

2. Quay lại thư mục cha:
   ```bash
   cd ..
   ```

3. Quay lại thư mục trước đó:
   ```bash
   cd -
   ```

4. Chuyển đến thư mục chính của người dùng:
   ```bash
   cd ~
   ```

## Mẹo
- Sử dụng phím Tab để tự động hoàn thành tên thư mục khi bạn gõ lệnh `cd`. Điều này giúp tiết kiệm thời gian và giảm lỗi chính tả.
- Bạn có thể sử dụng đường dẫn tuyệt đối hoặc đường dẫn tương đối khi sử dụng lệnh `cd`. Đường dẫn tuyệt đối bắt đầu từ thư mục gốc (`/`), trong khi đường dẫn tương đối bắt đầu từ thư mục hiện tại.
- Hãy chắc chắn rằng bạn có quyền truy cập vào thư mục mà bạn đang cố gắng chuyển đến, nếu không, bạn sẽ nhận được thông báo lỗi.