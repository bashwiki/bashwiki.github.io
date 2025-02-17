# [Linux] Bash egrep cách sử dụng: Tìm kiếm mẫu trong văn bản

## Tổng quan
Lệnh `egrep` là một phiên bản mở rộng của lệnh `grep`, cho phép tìm kiếm các mẫu trong văn bản bằng cách sử dụng biểu thức chính quy. `egrep` hỗ trợ các biểu thức chính quy mở rộng, giúp người dùng có thể thực hiện các tìm kiếm phức tạp hơn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `egrep` như sau:

```bash
egrep [tùy chọn] [tham số]
```

## Các tùy chọn phổ biến
- `-i`: Bỏ qua phân biệt chữ hoa chữ thường.
- `-v`: In ra các dòng không khớp với mẫu.
- `-c`: Đếm số dòng khớp với mẫu.
- `-n`: Hiển thị số dòng cùng với kết quả khớp.
- `-r`: Tìm kiếm đệ quy trong thư mục.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng `egrep`:

1. Tìm kiếm một từ trong tệp:
   ```bash
   egrep "từ_cần_tìm" ten_tap.txt
   ```

2. Tìm kiếm không phân biệt chữ hoa chữ thường:
   ```bash
   egrep -i "từ_cần_tìm" ten_tap.txt
   ```

3. Tìm kiếm và hiển thị số dòng:
   ```bash
   egrep -n "từ_cần_tìm" ten_tap.txt
   ```

4. Tìm kiếm trong tất cả các tệp trong thư mục:
   ```bash
   egrep -r "từ_cần_tìm" /duong_dan/thu_muc/
   ```

5. Đếm số dòng khớp với mẫu:
   ```bash
   egrep -c "từ_cần_tìm" ten_tap.txt
   ```

## Mẹo
- Sử dụng tùy chọn `-v` để lọc ra những dòng không chứa mẫu, giúp bạn dễ dàng tìm kiếm các dòng không mong muốn.
- Kết hợp `egrep` với các lệnh khác như `sort` hoặc `uniq` để xử lý kết quả tìm kiếm một cách hiệu quả hơn.
- Thực hành với các biểu thức chính quy để nâng cao khả năng tìm kiếm của bạn, vì `egrep` hỗ trợ nhiều loại mẫu phức tạp.