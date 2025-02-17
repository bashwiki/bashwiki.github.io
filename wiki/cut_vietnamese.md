# [Linux] Bash cut cách sử dụng: Trích xuất các phần của dòng văn bản

## Overview
Lệnh `cut` trong Bash được sử dụng để trích xuất các phần cụ thể từ mỗi dòng của một tệp hoặc đầu vào. Nó rất hữu ích khi bạn cần lấy thông tin từ các tệp văn bản có cấu trúc, chẳng hạn như tệp CSV hoặc tệp log.

## Usage
Cú pháp cơ bản của lệnh `cut` như sau:
```bash
cut [options] [arguments]
```

## Common Options
- `-f`: Chỉ định các trường cần trích xuất, sử dụng dấu phẩy để phân tách.
- `-d`: Đặt ký tự phân cách (mặc định là tab).
- `-c`: Chỉ định các ký tự cần trích xuất.
- `--complement`: Trích xuất tất cả các trường ngoại trừ những trường đã chỉ định.

## Common Examples
- Trích xuất trường thứ hai từ một tệp CSV:
```bash
cut -d ',' -f 2 file.csv
```

- Trích xuất các ký tự từ vị trí 1 đến 5 trong một tệp:
```bash
cut -c 1-5 file.txt
```

- Trích xuất các trường từ đầu vào chuẩn:
```bash
echo "apple,banana,cherry" | cut -d ',' -f 2
```

- Trích xuất tất cả các trường ngoại trừ trường thứ nhất:
```bash
cut --complement -f 1 -d ',' file.csv
```

## Tips
- Luôn kiểm tra định dạng của tệp đầu vào để chọn ký tự phân cách chính xác.
- Sử dụng `-n` để tránh in ra các dòng trống khi sử dụng với tệp có định dạng không đồng nhất.
- Kết hợp `cut` với các lệnh khác như `grep` hoặc `sort` để xử lý dữ liệu hiệu quả hơn.