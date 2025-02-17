# [Linux] Bash cmake Cách sử dụng: Tạo và quản lý dự án phần mềm

## Tổng quan
Câu lệnh `cmake` được sử dụng để tạo và quản lý dự án phần mềm. Nó giúp người dùng cấu hình các tệp dự án, tạo Makefile hoặc tệp dự án cho các IDE khác nhau, từ đó dễ dàng biên dịch và xây dựng ứng dụng.

## Cách sử dụng
Cú pháp cơ bản của câu lệnh `cmake` như sau:
```
cmake [options] [arguments]
```

## Tùy chọn phổ biến
- `-S <path>`: Chỉ định thư mục nguồn chứa mã nguồn.
- `-B <path>`: Chỉ định thư mục xây dựng nơi các tệp được tạo ra.
- `-D <var>=<value>`: Đặt giá trị cho biến CMake.
- `--build <path>`: Xây dựng dự án từ thư mục đã chỉ định.
- `--install <path>`: Cài đặt dự án đã xây dựng vào thư mục chỉ định.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng `cmake`:

1. **Tạo một thư mục xây dựng và cấu hình dự án**:
   ```bash
   mkdir build
   cd build
   cmake ..
   ```

2. **Cấu hình dự án với biến**:
   ```bash
   cmake -D CMAKE_BUILD_TYPE=Release ..
   ```

3. **Xây dựng dự án**:
   ```bash
   cmake --build .
   ```

4. **Cài đặt dự án đã xây dựng**:
   ```bash
   cmake --install .
   ```

## Mẹo
- Luôn tạo một thư mục xây dựng riêng để giữ cho thư mục mã nguồn sạch sẽ.
- Sử dụng tùy chọn `-D` để tùy chỉnh các biến cấu hình mà không cần chỉnh sửa tệp CMakeLists.txt.
- Kiểm tra tài liệu CMake để biết thêm thông tin về các tùy chọn và biến có sẵn để tối ưu hóa quá trình xây dựng của bạn.