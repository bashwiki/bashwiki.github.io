# [Linux] Bash groupmod cách sử dụng: Thay đổi thông tin nhóm

## Tổng quan
Lệnh `groupmod` được sử dụng để thay đổi các thuộc tính của một nhóm người dùng trong hệ thống Linux. Bạn có thể thay đổi tên nhóm hoặc ID nhóm của một nhóm đã tồn tại.

## Cách sử dụng
Cú pháp cơ bản của lệnh `groupmod` như sau:

```bash
groupmod [options] [arguments]
```

## Các tùy chọn phổ biến
- `-n, --new-name NEW_GROUP`: Đặt tên mới cho nhóm.
- `-g, --gid NEW_GID`: Đặt ID mới cho nhóm.
- `-o, --non-unique`: Cho phép ID nhóm không duy nhất (nếu có nhiều nhóm với cùng ID).

## Ví dụ phổ biến
1. Đổi tên nhóm từ `oldgroup` thành `newgroup`:
   ```bash
   groupmod -n newgroup oldgroup
   ```

2. Thay đổi ID nhóm của nhóm `mygroup` thành `1001`:
   ```bash
   groupmod -g 1001 mygroup
   ```

3. Đổi tên nhóm và ID nhóm cùng lúc:
   ```bash
   groupmod -n newgroup -g 1002 oldgroup
   ```

## Mẹo
- Trước khi thay đổi tên hoặc ID của nhóm, hãy đảm bảo rằng không có người dùng nào đang sử dụng nhóm đó để tránh gây ra sự cố.
- Sử dụng lệnh `getent group` để kiểm tra thông tin nhóm hiện tại trước khi thực hiện thay đổi.
- Luôn sao lưu cấu hình nhóm trước khi thực hiện các thay đổi lớn để có thể khôi phục lại nếu cần.