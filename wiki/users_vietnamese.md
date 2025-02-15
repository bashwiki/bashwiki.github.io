# [리눅스] Bash users 사용법

## Tổng quan
Lệnh `users` trong Bash được sử dụng để hiển thị danh sách các tên người dùng đang đăng nhập vào hệ thống. Lệnh này giúp người quản trị hệ thống và các lập trình viên theo dõi ai đang sử dụng máy chủ hoặc máy tính tại một thời điểm cụ thể. Thông tin này có thể hữu ích trong việc quản lý tài nguyên và bảo mật hệ thống.

## Cách sử dụng
Cú pháp cơ bản của lệnh `users` như sau:

```bash
users [tùy chọn]
```

### Tùy chọn phổ biến
- Không có tùy chọn nào cần thiết cho lệnh này. Khi bạn chạy lệnh `users`, nó sẽ tự động hiển thị danh sách người dùng đang đăng nhập.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `users`.

### Ví dụ 1: Hiển thị danh sách người dùng đang đăng nhập
Chỉ cần gõ lệnh sau trong terminal:

```bash
users
```

Kết quả sẽ là một danh sách các tên người dùng hiện đang đăng nhập, ví dụ:

```
user1 user2 user3
```

### Ví dụ 2: Sử dụng lệnh trong một kịch bản
Bạn có thể sử dụng lệnh `users` trong một kịch bản Bash để kiểm tra xem có người dùng nào đang đăng nhập hay không:

```bash
if [ -z "$(users)" ]; then
    echo "Không có người dùng nào đang đăng nhập."
else
    echo "Người dùng đang đăng nhập: $(users)"
fi
```

## Mẹo
- Lệnh `users` rất hữu ích khi bạn cần nhanh chóng kiểm tra trạng thái người dùng trên hệ thống mà không cần phải xem chi tiết hơn như lệnh `who` hay `w`.
- Bạn có thể kết hợp lệnh `users` với các lệnh khác trong Bash để thực hiện các tác vụ tự động, như gửi thông báo hoặc ghi log khi có người dùng đăng nhập.
- Hãy nhớ rằng lệnh này chỉ hiển thị tên người dùng mà không cung cấp thông tin chi tiết như thời gian đăng nhập hay địa chỉ IP. Nếu bạn cần thông tin chi tiết hơn, hãy xem xét sử dụng lệnh `who` hoặc `w`.