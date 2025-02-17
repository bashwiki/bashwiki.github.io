# [Linux] Bash seq Cách sử dụng: Tạo dãy số

## Overview
Lệnh `seq` trong Bash được sử dụng để tạo ra một dãy số. Nó cho phép người dùng dễ dàng tạo ra các số liên tiếp, có thể được sử dụng trong các kịch bản khác nhau, chẳng hạn như lặp qua các số trong một vòng lặp hoặc tạo danh sách số.

## Usage
Cú pháp cơ bản của lệnh `seq` như sau:
```
seq [options] [arguments]
```

## Common Options
- `-s STRING`: Chỉ định chuỗi phân cách giữa các số (mặc định là khoảng trắng).
- `-f FORMAT`: Định dạng số theo định dạng đã chỉ định.
- `-w`: Đảm bảo tất cả các số có cùng độ dài bằng cách thêm số 0 vào đầu.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `seq`:

1. Tạo dãy số từ 1 đến 10:
   ```bash
   seq 1 10
   ```

2. Tạo dãy số từ 5 đến 15:
   ```bash
   seq 5 15
   ```

3. Tạo dãy số từ 1 đến 10 với bước nhảy là 2:
   ```bash
   seq 1 2 10
   ```

4. Tạo dãy số từ 1 đến 5 và phân cách bằng dấu phẩy:
   ```bash
   seq -s "," 1 5
   ```

5. Tạo dãy số với định dạng số thập phân:
   ```bash
   seq -f "%.2f" 1 0.5 5
   ```

## Tips
- Sử dụng `seq` trong vòng lặp `for` để thực hiện các tác vụ lặp lại dễ dàng.
- Khi cần tạo dãy số có định dạng đặc biệt, hãy tận dụng tùy chọn `-f` để định dạng.
- Nếu bạn cần dãy số có độ dài cố định, hãy sử dụng tùy chọn `-w` để đảm bảo các số có cùng độ dài.