# [macOS] Bash brew cách sử dụng: Quản lý gói phần mềm

## Tổng quan
Lệnh `brew` là một công cụ quản lý gói phần mềm cho macOS, cho phép người dùng cài đặt, cập nhật và quản lý các ứng dụng và thư viện một cách dễ dàng thông qua dòng lệnh.

## Cách sử dụng
Cú pháp cơ bản của lệnh `brew` như sau:
```
brew [tùy chọn] [tham số]
```

## Các tùy chọn phổ biến
- `install`: Cài đặt một gói phần mềm.
- `update`: Cập nhật danh sách gói phần mềm.
- `upgrade`: Nâng cấp các gói phần mềm đã cài đặt.
- `remove` hoặc `uninstall`: Gỡ bỏ một gói phần mềm.
- `list`: Hiển thị danh sách các gói phần mềm đã cài đặt.

## Ví dụ phổ biến
- Cài đặt một gói phần mềm:
  ```bash
  brew install wget
  ```
  
- Cập nhật danh sách gói phần mềm:
  ```bash
  brew update
  ```

- Nâng cấp tất cả các gói phần mềm đã cài đặt:
  ```bash
  brew upgrade
  ```

- Gỡ bỏ một gói phần mềm:
  ```bash
  brew uninstall wget
  ```

- Hiển thị danh sách các gói phần mềm đã cài đặt:
  ```bash
  brew list
  ```

## Mẹo
- Luôn chạy `brew update` trước khi cài đặt hoặc nâng cấp để đảm bảo bạn có danh sách gói mới nhất.
- Sử dụng `brew doctor` để kiểm tra xem có vấn đề gì với cài đặt Homebrew của bạn hay không.
- Tham khảo tài liệu chính thức của Homebrew để tìm hiểu thêm về các gói phần mềm và tùy chọn nâng cao.