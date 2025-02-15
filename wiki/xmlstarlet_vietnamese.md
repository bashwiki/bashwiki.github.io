# [리눅스] Bash xmlstarlet 사용법

## Tổng quan
`xmlstarlet` là một công cụ dòng lệnh mạnh mẽ dùng để xử lý và thao tác với các tài liệu XML. Nó cho phép người dùng thực hiện nhiều thao tác khác nhau như truy vấn, chuyển đổi, và sửa đổi nội dung XML một cách dễ dàng. `xmlstarlet` rất hữu ích cho các kỹ sư và nhà phát triển khi làm việc với dữ liệu XML trong các ứng dụng hoặc khi cần xử lý dữ liệu từ các API.

## Cách sử dụng
Cú pháp cơ bản của `xmlstarlet` như sau:

```
xmlstarlet [lựa chọn] [tệp XML]
```

Một số tùy chọn phổ biến của `xmlstarlet` bao gồm:

- `xmlstarlet sel`: Chọn và truy vấn các nút trong tài liệu XML.
- `xmlstarlet ed`: Chỉnh sửa tài liệu XML, cho phép thêm, sửa hoặc xóa các nút.
- `xmlstarlet tr`: Chuyển đổi tài liệu XML sang định dạng khác bằng cách sử dụng XSLT.
- `xmlstarlet val`: Xác thực tài liệu XML với một lược đồ (schema) nhất định.

## Ví dụ
### Ví dụ 1: Truy vấn dữ liệu XML
Giả sử bạn có một tệp XML tên là `data.xml` với nội dung sau:

```xml
<root>
    <item>
        <name>Item 1</name>
        <value>10</value>
    </item>
    <item>
        <name>Item 2</name>
        <value>20</value>
    </item>
</root>
```

Bạn có thể sử dụng `xmlstarlet` để truy vấn tất cả các tên của các mục như sau:

```bash
xmlstarlet sel -t -m "//item" -v "name" -n data.xml
```

Kết quả sẽ là:

```
Item 1
Item 2
```

### Ví dụ 2: Chỉnh sửa tệp XML
Nếu bạn muốn thêm một mục mới vào tệp XML trên, bạn có thể sử dụng lệnh sau:

```bash
xmlstarlet ed -s /root -t -n "item" -v "" \
    -s /root/item[last()] -t -n "name" -v "Item 3" \
    -s /root/item[last()] -t -n "value" -v "30" data.xml
```

Lệnh này sẽ thêm một mục mới với tên "Item 3" và giá trị "30".

## Mẹo
- Khi làm việc với `xmlstarlet`, hãy đảm bảo rằng tệp XML của bạn được định dạng chính xác để tránh lỗi trong quá trình xử lý.
- Sử dụng tùy chọn `-o` để xuất kết quả ra tệp mới nếu bạn không muốn ghi đè lên tệp XML gốc.
- Tham khảo tài liệu chính thức của `xmlstarlet` để tìm hiểu thêm về các tùy chọn và chức năng nâng cao.