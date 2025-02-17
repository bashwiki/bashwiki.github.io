# [Linux] Bash xmlstarlet cách sử dụng: Xử lý và truy vấn XML

## Tổng quan
`xmlstarlet` là một công cụ dòng lệnh mạnh mẽ dùng để xử lý và truy vấn tài liệu XML. Nó cho phép người dùng thực hiện các thao tác như truy vấn, chuyển đổi, và định dạng XML một cách dễ dàng và hiệu quả.

## Cách sử dụng
Cú pháp cơ bản của lệnh `xmlstarlet` như sau:
```
xmlstarlet [options] [arguments]
```

## Các tùy chọn phổ biến
- `sel`: Chọn các nút từ tài liệu XML.
- `val`: Kiểm tra tính hợp lệ của tài liệu XML.
- `ed`: Chỉnh sửa tài liệu XML.
- `tr`: Chuyển đổi tài liệu XML sang định dạng khác.
- `fo`: Định dạng tài liệu XML để dễ đọc hơn.

## Ví dụ phổ biến
1. **Chọn nút từ tài liệu XML**:
   ```bash
   xmlstarlet sel -t -m "/root/element" -v "text()" file.xml
   ```

2. **Kiểm tra tính hợp lệ của tài liệu XML**:
   ```bash
   xmlstarlet val -e file.xml
   ```

3. **Chỉnh sửa tài liệu XML**:
   ```bash
   xmlstarlet ed -u "/root/element" -v "new_value" file.xml
   ```

4. **Chuyển đổi XML sang định dạng JSON**:
   ```bash
   xmlstarlet tr xml-to-json.xsl file.xml
   ```

5. **Định dạng tài liệu XML**:
   ```bash
   xmlstarlet fo file.xml
   ```

## Mẹo
- Sử dụng `xmlstarlet` kết hợp với các lệnh khác trong Bash để tự động hóa quy trình xử lý XML.
- Thử nghiệm với các tùy chọn khác nhau để tìm ra cách sử dụng phù hợp nhất cho nhu cầu của bạn.
- Đọc tài liệu hướng dẫn của `xmlstarlet` để hiểu rõ hơn về các tính năng nâng cao mà nó cung cấp.