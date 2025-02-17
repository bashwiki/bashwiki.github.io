# [Linux] Bash test cách sử dụng: Kiểm tra điều kiện

## Overview
Lệnh `test` trong Bash được sử dụng để kiểm tra các điều kiện khác nhau, chẳng hạn như kiểm tra sự tồn tại của tệp, so sánh số, hoặc kiểm tra chuỗi. Kết quả của lệnh này sẽ trả về giá trị đúng (0) hoặc sai (1), giúp bạn thực hiện các quyết định trong các kịch bản lập trình shell.

## Usage
Cú pháp cơ bản của lệnh `test` như sau:
```bash
test [options] [arguments]
```

## Common Options
Dưới đây là một số tùy chọn phổ biến của lệnh `test`:
- `-e FILE`: Kiểm tra xem tệp có tồn tại hay không.
- `-f FILE`: Kiểm tra xem tệp có phải là tệp thông thường hay không.
- `-d DIRECTORY`: Kiểm tra xem thư mục có tồn tại hay không.
- `-z STRING`: Kiểm tra xem chuỗi có rỗng hay không.
- `-eq`, `-ne`, `-lt`, `-le`, `-gt`, `-ge`: So sánh các số.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `test`:

1. Kiểm tra sự tồn tại của một tệp:
   ```bash
   test -e myfile.txt && echo "Tệp tồn tại"
   ```

2. Kiểm tra xem một thư mục có tồn tại hay không:
   ```bash
   test -d /home/user && echo "Thư mục tồn tại"
   ```

3. So sánh hai số:
   ```bash
   a=5
   b=10
   test $a -lt $b && echo "$a nhỏ hơn $b"
   ```

4. Kiểm tra xem một chuỗi có rỗng hay không:
   ```bash
   str=""
   test -z "$str" && echo "Chuỗi rỗng"
   ```

## Tips
- Sử dụng `[` thay cho `test` để viết mã ngắn gọn hơn, ví dụ: `[ -e myfile.txt ]`.
- Kết hợp lệnh `test` với các cấu trúc điều kiện như `if` để thực hiện các hành động dựa trên kết quả kiểm tra.
- Luôn sử dụng dấu ngoặc kép cho các biến chứa chuỗi để tránh lỗi khi chuỗi rỗng hoặc chứa khoảng trắng.