# [Linux] Bash rmdir: Xóa thư mục rỗng

## Overview
Lệnh `rmdir` được sử dụng để xóa các thư mục rỗng trong hệ thống tệp. Nếu thư mục không rỗng, lệnh này sẽ không thực hiện được và sẽ thông báo lỗi.

## Usage
Cú pháp cơ bản của lệnh `rmdir` như sau:
```
rmdir [options] [arguments]
```

## Common Options
- `-p`: Xóa thư mục rỗng và tất cả các thư mục cha của nó nếu chúng cũng rỗng.
- `--ignore-fail-on-non-empty`: Bỏ qua lỗi nếu thư mục không rỗng.

## Common Examples
- **Xóa một thư mục rỗng:**
  ```bash
  rmdir my_empty_directory
  ```

- **Xóa nhiều thư mục rỗng cùng một lúc:**
  ```bash
  rmdir dir1 dir2 dir3
  ```

- **Xóa thư mục rỗng và các thư mục cha của nó:**
  ```bash
  rmdir -p parent_dir/child_dir
  ```

- **Bỏ qua lỗi khi thư mục không rỗng:**
  ```bash
  rmdir --ignore-fail-on-non-empty my_non_empty_directory
  ```

## Tips
- Trước khi sử dụng `rmdir`, hãy chắc chắn rằng thư mục bạn muốn xóa là rỗng để tránh thông báo lỗi.
- Sử dụng tùy chọn `-p` để tiết kiệm thời gian khi bạn cần xóa nhiều thư mục rỗng lồng nhau.
- Kiểm tra nội dung của thư mục bằng lệnh `ls` trước khi xóa để đảm bảo rằng bạn không xóa nhầm dữ liệu quan trọng.