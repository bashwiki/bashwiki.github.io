# [Linux] Bash true cách sử dụng: Trả về giá trị đúng

## Overview
Lệnh `true` trong Bash là một lệnh đơn giản, nó luôn trả về giá trị thành công (0). Lệnh này thường được sử dụng trong các kịch bản để đảm bảo rằng một phần của mã chạy mà không gặp lỗi.

## Usage
Cú pháp cơ bản của lệnh `true` như sau:

```bash
true [options] [arguments]
```

## Common Options
Lệnh `true` không có tùy chọn nào đặc biệt, nhưng bạn có thể sử dụng nó trong các kịch bản với các lệnh khác. 

## Common Examples
Dưới đây là một số ví dụ thực tiễn về cách sử dụng lệnh `true`:

1. **Sử dụng trong một kịch bản điều kiện:**
   ```bash
   if true; then
       echo "Điều kiện đúng!"
   fi
   ```

2. **Kết hợp với lệnh `&&`:**
   ```bash
   true && echo "Lệnh trước thành công!"
   ```

3. **Sử dụng trong vòng lặp:**
   ```bash
   while true; do
       echo "Vòng lặp này sẽ chạy mãi mãi cho đến khi bị dừng."
       sleep 1
   done
   ```

4. **Sử dụng trong lệnh `||`:**
   ```bash
   false || true && echo "Lệnh đầu tiên thất bại, nhưng lệnh true thành công!"
   ```

## Tips
- Lệnh `true` rất hữu ích khi bạn cần một lệnh không làm gì nhưng vẫn cần một giá trị trả về thành công.
- Bạn có thể sử dụng `true` trong các kịch bản phức tạp để kiểm soát luồng thực thi mà không cần phải viết mã phức tạp.
- Kết hợp `true` với các lệnh khác có thể giúp bạn kiểm soát tốt hơn các tình huống trong kịch bản của mình.