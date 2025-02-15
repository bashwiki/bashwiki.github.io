# [리눅스] Bash jq 사용법

## Tổng quan
`jq` là một công cụ dòng lệnh mạnh mẽ dùng để xử lý và phân tích dữ liệu JSON. Nó cho phép người dùng truy vấn, lọc, và chuyển đổi dữ liệu JSON một cách dễ dàng và hiệu quả. Với cú pháp đơn giản và khả năng mở rộng, `jq` trở thành một công cụ không thể thiếu cho các kỹ sư và nhà phát triển làm việc với dữ liệu JSON trong các ứng dụng và dịch vụ web.

## Cách sử dụng
Cú pháp cơ bản của lệnh `jq` như sau:

```bash
jq [options] 'filter' file.json
```

### Các tùy chọn phổ biến:
- `-c`: Xuất kết quả dưới dạng một dòng (compact output).
- `-r`: Xuất kết quả dưới dạng chuỗi thô (raw output), không bao gồm dấu nháy kép.
- `-f file.jq`: Sử dụng một tệp chứa các biểu thức jq.
- `--arg name value`: Đặt một biến có tên `name` với giá trị `value` để sử dụng trong biểu thức jq.

## Ví dụ
### Ví dụ 1: Truy vấn một trường cụ thể
Giả sử bạn có một tệp JSON có tên `data.json` như sau:

```json
{
  "employees": [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
  ]
}
```

Bạn có thể sử dụng `jq` để lấy tên của tất cả nhân viên:

```bash
jq '.employees[].name' data.json
```

Kết quả sẽ là:
```
"Alice"
"Bob"
```

### Ví dụ 2: Lọc dữ liệu theo điều kiện
Nếu bạn muốn lấy thông tin của những nhân viên trên 28 tuổi, bạn có thể sử dụng:

```bash
jq '.employees[] | select(.age > 28)' data.json
```

Kết quả sẽ là:
```json
{
  "name": "Alice",
  "age": 30
}
```

## Mẹo
- Sử dụng `jq` kết hợp với các lệnh khác trong Bash để xử lý dữ liệu một cách linh hoạt. Ví dụ, bạn có thể sử dụng `curl` để lấy dữ liệu JSON từ một API và sau đó truyền nó vào `jq` để phân tích.
- Đọc tài liệu chính thức của `jq` để tìm hiểu thêm về các biểu thức và cú pháp nâng cao, giúp bạn tối ưu hóa quy trình làm việc với dữ liệu JSON.
- Khi làm việc với các tệp JSON lớn, hãy sử dụng tùy chọn `-c` để giảm thiểu kích thước đầu ra và tăng tốc độ xử lý.