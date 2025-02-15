# [리눅스] Bash mv 사용법

## Tổng quan
Lệnh `mv` trong Bash được sử dụng để di chuyển hoặc đổi tên các tệp và thư mục. Đây là một trong những lệnh cơ bản và quan trọng trong quản lý tệp trên hệ thống Unix/Linux. Khi bạn muốn tổ chức lại các tệp hoặc thay đổi tên của chúng, lệnh `mv` sẽ giúp bạn thực hiện điều đó một cách nhanh chóng và hiệu quả.

## Cú pháp
Cú pháp cơ bản của lệnh `mv` như sau:

```
mv [tùy chọn] nguồn đích
```

Trong đó:
- `nguồn`: là tệp hoặc thư mục mà bạn muốn di chuyển hoặc đổi tên.
- `đích`: là vị trí mới hoặc tên mới cho tệp hoặc thư mục.

### Các tùy chọn phổ biến
- `-i`: Hiển thị cảnh báo trước khi ghi đè lên tệp đích nếu nó đã tồn tại.
- `-u`: Chỉ di chuyển tệp nếu tệp nguồn mới hơn tệp đích hoặc nếu tệp đích không tồn tại.
- `-v`: Hiển thị thông tin chi tiết về các tệp được di chuyển.

## Ví dụ
### Ví dụ 1: Di chuyển tệp
Giả sử bạn có một tệp tên là `file.txt` trong thư mục hiện tại và bạn muốn di chuyển nó vào thư mục `documents`:

```bash
mv file.txt documents/
```

### Ví dụ 2: Đổi tên tệp
Nếu bạn muốn đổi tên tệp `file.txt` thành `newfile.txt`, bạn có thể sử dụng lệnh sau:

```bash
mv file.txt newfile.txt
```

## Mẹo
- Luôn sử dụng tùy chọn `-i` khi di chuyển hoặc đổi tên tệp để tránh ghi đè lên các tệp quan trọng mà bạn không muốn mất.
- Kiểm tra vị trí đích trước khi di chuyển tệp để đảm bảo rằng bạn đang di chuyển đến đúng thư mục.
- Sử dụng tùy chọn `-v` để theo dõi quá trình di chuyển tệp, đặc biệt là khi bạn làm việc với nhiều tệp cùng một lúc. 

Lệnh `mv` là một công cụ mạnh mẽ trong việc quản lý tệp, và việc hiểu rõ cách sử dụng nó sẽ giúp bạn làm việc hiệu quả hơn trên hệ thống Unix/Linux.