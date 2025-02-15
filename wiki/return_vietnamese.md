# [리눅스] Bash return 사용법

## Tổng quan
Lệnh `return` trong Bash được sử dụng để kết thúc một hàm và trả về một giá trị mã lỗi cho shell. Mã lỗi này có thể được sử dụng để xác định xem hàm đã thực hiện thành công hay không. Mặc định, một hàm trả về mã lỗi 0 nếu không có lỗi xảy ra, và các mã lỗi khác có thể được chỉ định bằng cách sử dụng lệnh `return`.

## Cách sử dụng
Cú pháp cơ bản của lệnh `return` như sau:

```bash
return [n]
```

Trong đó `n` là một số nguyên từ 0 đến 255, đại diện cho mã lỗi mà bạn muốn trả về. Nếu không chỉ định `n`, lệnh `return` sẽ trả về mã lỗi của lệnh cuối cùng được thực thi trong hàm.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `return` trong Bash:

### Ví dụ 1: Trả về mã lỗi thành công
```bash
my_function() {
    echo "Hàm đang thực thi..."
    return 0
}

my_function
echo "Mã lỗi trả về: $?"
```
Trong ví dụ này, hàm `my_function` sẽ in ra một thông báo và trả về mã lỗi 0, cho biết rằng hàm đã thực hiện thành công.

### Ví dụ 2: Trả về mã lỗi không thành công
```bash
my_function() {
    echo "Đã xảy ra lỗi!"
    return 1
}

my_function
echo "Mã lỗi trả về: $?"
```
Ở ví dụ này, hàm `my_function` sẽ in ra một thông báo lỗi và trả về mã lỗi 1, cho biết rằng đã có lỗi xảy ra.

## Mẹo
- Sử dụng lệnh `return` trong các hàm để kiểm soát luồng thực thi của script. Điều này giúp bạn dễ dàng xử lý các tình huống lỗi và thực hiện các hành động thích hợp.
- Luôn kiểm tra mã lỗi trả về bằng cách sử dụng biến `$?` ngay sau khi gọi hàm để đảm bảo rằng bạn biết được trạng thái thực thi của hàm.
- Đặt mã lỗi rõ ràng và có ý nghĩa để dễ dàng xác định nguyên nhân lỗi khi cần thiết.