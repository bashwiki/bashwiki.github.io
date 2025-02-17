# [Linux] Bash chattr cách sử dụng: Quản lý thuộc tính tập tin

## Tổng quan
Lệnh `chattr` trong Bash được sử dụng để thay đổi các thuộc tính của tập tin trong hệ thống tệp Linux. Nó cho phép người dùng thiết lập các thuộc tính đặc biệt cho tập tin, giúp bảo vệ chúng khỏi các thay đổi không mong muốn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `chattr` như sau:

```bash
chattr [options] [arguments]
```

## Các tùy chọn phổ biến
- `+a`: Thêm thuộc tính "append only", cho phép chỉ thêm dữ liệu vào tập tin.
- `-a`: Xóa thuộc tính "append only".
- `+i`: Thêm thuộc tính "immutable", ngăn không cho tập tin bị xóa hoặc thay đổi.
- `-i`: Xóa thuộc tính "immutable".
- `+e`: Thêm thuộc tính "extent format", cho phép sử dụng định dạng mở rộng cho tập tin.
- `-e`: Xóa thuộc tính "extent format".

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `chattr`:

1. **Thêm thuộc tính immutable cho tập tin:**
   ```bash
   chattr +i ten_tap_tin.txt
   ```
   Lệnh này sẽ ngăn không cho bất kỳ ai thay đổi hoặc xóa tập tin `ten_tap_tin.txt`.

2. **Xóa thuộc tính immutable:**
   ```bash
   chattr -i ten_tap_tin.txt
   ```
   Lệnh này sẽ cho phép thay đổi và xóa tập tin `ten_tap_tin.txt` một lần nữa.

3. **Thêm thuộc tính append only cho tập tin:**
   ```bash
   chattr +a ten_tap_tin.txt
   ```
   Sau khi thực hiện lệnh này, chỉ có thể thêm dữ liệu vào `ten_tap_tin.txt`, không thể xóa hoặc thay thế nội dung.

4. **Kiểm tra thuộc tính của tập tin:**
   ```bash
   lsattr ten_tap_tin.txt
   ```
   Lệnh này sẽ hiển thị các thuộc tính hiện tại của tập tin `ten_tap_tin.txt`.

## Mẹo
- Hãy cẩn thận khi sử dụng thuộc tính `immutable`, vì nó có thể gây khó khăn trong việc quản lý tập tin nếu bạn quên xóa thuộc tính này.
- Sử dụng `lsattr` để kiểm tra thuộc tính của tập tin trước khi thực hiện bất kỳ thay đổi nào.
- Chỉ nên sử dụng `chattr` trên các tập tin mà bạn thực sự cần bảo vệ, để tránh gây rắc rối trong việc quản lý tập tin hàng ngày.