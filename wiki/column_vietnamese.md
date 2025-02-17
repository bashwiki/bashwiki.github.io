# [Linux] Bash column sử dụng: Định dạng dữ liệu theo cột

## Overview
Lệnh `column` trong Bash được sử dụng để định dạng dữ liệu đầu vào thành các cột, giúp cho việc đọc và phân tích dữ liệu trở nên dễ dàng hơn. Nó thường được sử dụng để trình bày thông tin từ các tệp văn bản hoặc đầu ra của các lệnh khác theo cách có tổ chức.

## Usage
Cú pháp cơ bản của lệnh `column` như sau:
```bash
column [options] [arguments]
```

## Common Options
- `-t`: Tạo bảng với các cột được căn chỉnh tự động.
- `-s`: Chỉ định ký tự phân cách giữa các cột (mặc định là khoảng trắng).
- `-n`: Không căn chỉnh cột, giữ nguyên định dạng ban đầu.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `column`:

1. **Căn chỉnh dữ liệu theo khoảng trắng**:
   ```bash
   cat data.txt | column
   ```

2. **Sử dụng ký tự phân cách là dấu phẩy**:
   ```bash
   cat data.csv | column -s, -t
   ```

3. **Hiển thị dữ liệu mà không căn chỉnh cột**:
   ```bash
   cat data.txt | column -n
   ```

4. **Định dạng đầu ra của lệnh `ps`**:
   ```bash
   ps aux | column -t
   ```

## Tips
- Khi làm việc với tệp CSV, hãy luôn sử dụng tùy chọn `-s` để chỉ định ký tự phân cách chính xác.
- Sử dụng tùy chọn `-t` để tự động căn chỉnh cột, giúp cho dữ liệu dễ đọc hơn.
- Kiểm tra đầu ra của lệnh trước khi sử dụng `column` để đảm bảo rằng dữ liệu được định dạng đúng cách.