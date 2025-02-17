# [Linux] Bash mv Cách sử dụng: Di chuyển hoặc đổi tên tệp

## Overview
Lệnh `mv` trong Bash được sử dụng để di chuyển hoặc đổi tên các tệp và thư mục. Khi bạn sử dụng lệnh này, bạn có thể chuyển tệp từ vị trí này sang vị trí khác hoặc thay đổi tên của tệp mà không cần tạo một bản sao mới.

## Usage
Cú pháp cơ bản của lệnh `mv` như sau:
```
mv [options] [arguments]
```

## Common Options
- `-i`: Yêu cầu xác nhận trước khi ghi đè lên tệp đích nếu nó đã tồn tại.
- `-u`: Chỉ di chuyển tệp nếu tệp nguồn mới hơn tệp đích hoặc nếu tệp đích không tồn tại.
- `-v`: Hiển thị thông tin chi tiết về các tệp đang được di chuyển.

## Common Examples
1. **Di chuyển một tệp đến thư mục khác:**
   ```bash
   mv file.txt /path/to/destination/
   ```

2. **Đổi tên một tệp:**
   ```bash
   mv oldname.txt newname.txt
   ```

3. **Di chuyển nhiều tệp cùng lúc:**
   ```bash
   mv file1.txt file2.txt /path/to/destination/
   ```

4. **Sử dụng tùy chọn xác nhận khi ghi đè:**
   ```bash
   mv -i file.txt /path/to/destination/
   ```

5. **Di chuyển tệp chỉ khi tệp nguồn mới hơn tệp đích:**
   ```bash
   mv -u file.txt /path/to/destination/
   ```

## Tips
- Luôn kiểm tra tệp đích trước khi di chuyển để tránh ghi đè mất dữ liệu quan trọng.
- Sử dụng tùy chọn `-v` để theo dõi quá trình di chuyển tệp, đặc biệt khi làm việc với nhiều tệp.
- Nếu bạn không chắc chắn về lệnh, hãy thử với tùy chọn `-i` để đảm bảo an toàn cho dữ liệu của bạn.