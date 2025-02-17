# [Linux] Bash jq Cách sử dụng: Trình phân tích và xử lý JSON

## Tổng quan
`jq` là một công cụ mạnh mẽ dùng để phân tích và xử lý dữ liệu JSON trong dòng lệnh. Nó cho phép người dùng truy vấn, lọc và biến đổi dữ liệu JSON một cách dễ dàng và hiệu quả.

## Cách sử dụng
Cú pháp cơ bản của lệnh `jq` như sau:

```bash
jq [options] [arguments]
```

## Các tùy chọn phổ biến
- `-c`: Xuất kết quả dưới dạng một dòng duy nhất.
- `-r`: Trả về kết quả dưới dạng chuỗi thô, không có dấu nháy.
- `-f <file>`: Đọc các biểu thức jq từ một tệp tin.
- `--arg <name> <value>`: Đặt một biến jq với tên và giá trị cụ thể.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng `jq`:

1. **Lọc một trường cụ thể từ JSON**:
   ```bash
   echo '{"name": "Alice", "age": 30}' | jq '.name'
   ```
   Kết quả: `"Alice"`

2. **Lọc nhiều trường từ JSON**:
   ```bash
   echo '{"name": "Alice", "age": 30}' | jq '{name, age}'
   ```
   Kết quả: `{"name": "Alice", "age": 30}`

3. **Sử dụng tùy chọn -r để xuất chuỗi thô**:
   ```bash
   echo '{"name": "Alice", "age": 30}' | jq -r '.name'
   ```
   Kết quả: `Alice`

4. **Đọc từ tệp JSON**:
   ```bash
   jq '.[] | .name' data.json
   ```
   Lệnh này sẽ in ra tên của từng đối tượng trong mảng JSON trong tệp `data.json`.

5. **Sử dụng biến**:
   ```bash
   echo '{"name": "Alice", "age": 30}' | jq --arg name "Bob" '.name = $name'
   ```
   Kết quả: `{"name": "Bob", "age": 30}`

## Mẹo
- Hãy sử dụng tùy chọn `-c` khi bạn cần xuất dữ liệu JSON gọn gàng hơn.
- Kiểm tra cú pháp của biểu thức jq bằng cách sử dụng `jq .` để đảm bảo rằng dữ liệu JSON của bạn được định dạng chính xác.
- Tham khảo tài liệu chính thức của jq để tìm hiểu thêm về các biểu thức phức tạp và tính năng nâng cao.