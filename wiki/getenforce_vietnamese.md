# [리눅스] Bash getenforce 사용법

## Tổng quan
Lệnh `getenforce` được sử dụng trong hệ điều hành Linux để kiểm tra trạng thái hiện tại của SELinux (Security-Enhanced Linux). SELinux là một tính năng bảo mật mạnh mẽ giúp quản lý quyền truy cập và bảo vệ hệ thống khỏi các mối đe dọa. Lệnh này cho phép người dùng xem liệu SELinux đang hoạt động ở chế độ "Enforcing", "Permissive" hay "Disabled".

## Cách sử dụng
Cú pháp cơ bản của lệnh `getenforce` rất đơn giản:

```bash
getenforce
```

Lệnh này không yêu cầu bất kỳ tùy chọn nào và sẽ trả về một trong ba trạng thái:

- **Enforcing**: SELinux đang hoạt động và áp dụng các quy tắc bảo mật.
- **Permissive**: SELinux đang hoạt động nhưng không áp dụng các quy tắc, chỉ ghi lại các vi phạm.
- **Disabled**: SELinux không được kích hoạt.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `getenforce`.

### Ví dụ 1: Kiểm tra trạng thái SELinux
Để kiểm tra trạng thái hiện tại của SELinux, bạn chỉ cần chạy lệnh sau:

```bash
getenforce
```

Kết quả có thể là một trong ba trạng thái: `Enforcing`, `Permissive`, hoặc `Disabled`.

### Ví dụ 2: Sử dụng trong kịch bản
Bạn có thể sử dụng lệnh `getenforce` trong các kịch bản Bash để thực hiện các hành động dựa trên trạng thái của SELinux. Ví dụ:

```bash
if [ "$(getenforce)" == "Enforcing" ]; then
    echo "SELinux is enforcing."
else
    echo "SELinux is not enforcing."
fi
```

## Mẹo
- **Kiểm tra thường xuyên**: Để đảm bảo rằng hệ thống của bạn luôn được bảo vệ, hãy kiểm tra trạng thái của SELinux thường xuyên, đặc biệt là sau khi thực hiện các thay đổi cấu hình.
- **Kết hợp với các lệnh khác**: Bạn có thể kết hợp `getenforce` với các lệnh khác như `setenforce` để thay đổi chế độ SELinux một cách linh hoạt trong các kịch bản tự động hóa.
- **Đọc tài liệu**: Để hiểu rõ hơn về SELinux và cách cấu hình nó, hãy tham khảo tài liệu chính thức của SELinux hoặc các nguồn tài liệu đáng tin cậy khác.

Hy vọng bài viết này giúp bạn hiểu rõ hơn về lệnh `getenforce` và cách sử dụng nó trong môi trường Linux!