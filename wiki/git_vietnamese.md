# [리눅스] Bash git 사용법

## Tổng quan
`git` là một hệ thống quản lý phiên bản phân tán, cho phép nhiều người cùng làm việc trên một dự án mà không làm mất dữ liệu của nhau. Nó giúp theo dõi thay đổi trong mã nguồn, cho phép phục hồi các phiên bản trước đó và hỗ trợ làm việc nhóm hiệu quả. Git được sử dụng rộng rãi trong phát triển phần mềm và là công cụ chính cho nhiều dự án mã nguồn mở.

## Cách sử dụng
Cú pháp cơ bản của lệnh `git` là:

```
git [tùy chọn] [lệnh] [tham số]
```

Một số tùy chọn và lệnh phổ biến của `git` bao gồm:

- `git init`: Khởi tạo một kho lưu trữ git mới.
- `git clone [url]`: Sao chép một kho lưu trữ từ một địa chỉ URL.
- `git add [tập tin]`: Thêm tập tin vào khu vực chuẩn bị (staging area).
- `git commit -m "[thông điệp]"`: Lưu các thay đổi đã thêm vào kho lưu trữ với một thông điệp mô tả.
- `git push`: Đẩy các thay đổi lên kho lưu trữ từ xa.
- `git pull`: Tải về và hợp nhất các thay đổi từ kho lưu trữ từ xa.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `git`:

1. **Khởi tạo một kho lưu trữ mới**:
   ```bash
   git init my_project
   cd my_project
   ```

2. **Sao chép một kho lưu trữ từ xa**:
   ```bash
   git clone https://github.com/username/repository.git
   ```

3. **Thêm và cam kết thay đổi**:
   ```bash
   git add file.txt
   git commit -m "Thêm file.txt vào kho lưu trữ"
   ```

4. **Đẩy thay đổi lên kho lưu trữ từ xa**:
   ```bash
   git push origin main
   ```

## Mẹo
- **Thường xuyên cam kết**: Hãy cam kết các thay đổi thường xuyên với thông điệp rõ ràng để dễ dàng theo dõi lịch sử thay đổi.
- **Sử dụng nhánh**: Tạo và làm việc trên các nhánh để thử nghiệm tính năng mới mà không làm ảnh hưởng đến mã chính.
- **Kiểm tra trạng thái**: Sử dụng lệnh `git status` để kiểm tra trạng thái của kho lưu trữ và các thay đổi chưa được cam kết.
- **Học cách sử dụng `.gitignore`**: Tạo tệp `.gitignore` để chỉ định các tệp hoặc thư mục mà bạn không muốn theo dõi trong kho lưu trữ.

Hy vọng bài viết này giúp bạn hiểu rõ hơn về cách sử dụng lệnh `git` trong phát triển phần mềm!