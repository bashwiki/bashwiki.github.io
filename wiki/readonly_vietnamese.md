# [Linux] Bash readonly: Thiết lập biến không thể thay đổi

## Overview
Lệnh `readonly` trong Bash được sử dụng để đánh dấu một biến là không thể thay đổi. Khi một biến được thiết lập là readonly, bạn không thể gán giá trị mới cho nó trong phiên làm việc hiện tại. Điều này rất hữu ích khi bạn muốn bảo vệ các giá trị quan trọng khỏi việc bị thay đổi.

## Usage
Cú pháp cơ bản của lệnh `readonly` như sau:
```bash
readonly [options] [arguments]
```

## Common Options
- `-p`: Hiển thị tất cả các biến readonly hiện có cùng với giá trị của chúng.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `readonly`:

1. **Thiết lập một biến readonly:**
   ```bash
   readonly MY_VAR="Giá trị không thay đổi"
   ```

2. **Cố gắng thay đổi giá trị của biến readonly (sẽ báo lỗi):**
   ```bash
   MY_VAR="Giá trị mới"  # Lỗi: không thể thay đổi giá trị của MY_VAR
   ```

3. **Hiển thị các biến readonly hiện có:**
   ```bash
   readonly -p
   ```

4. **Thiết lập nhiều biến readonly cùng lúc:**
   ```bash
   readonly VAR1="Giá trị 1" VAR2="Giá trị 2"
   ```

## Tips
- Sử dụng `readonly` cho các biến quan trọng mà bạn không muốn bị thay đổi trong quá trình thực thi script.
- Kiểm tra các biến readonly bằng cách sử dụng `readonly -p` để đảm bảo rằng các giá trị quan trọng vẫn được bảo vệ.
- Hãy nhớ rằng việc thiết lập một biến là readonly chỉ có hiệu lực trong phiên làm việc hiện tại và không ảnh hưởng đến các phiên khác.