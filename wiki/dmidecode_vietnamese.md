# [Linux] Bash dmidecode cách sử dụng: Truy xuất thông tin phần cứng hệ thống

## Tổng quan
Lệnh `dmidecode` được sử dụng để truy xuất thông tin về phần cứng của hệ thống từ bảng DMI (Desktop Management Interface). Thông tin này bao gồm các chi tiết về bộ vi xử lý, bộ nhớ, bo mạch chủ và các thành phần khác của máy tính.

## Cách sử dụng
Cú pháp cơ bản của lệnh `dmidecode` như sau:
```
dmidecode [options] [arguments]
```

## Các tùy chọn phổ biến
- `-t, --type TYPE`: Chỉ định loại thông tin cần hiển thị (ví dụ: BIOS, hệ thống, bộ vi xử lý).
- `-q, --quiet`: Giảm thiểu thông tin đầu ra.
- `-s, --string STRING`: Hiển thị thông tin cụ thể theo chuỗi (ví dụ: BIOS-version, system-uuid).
- `-h, --help`: Hiển thị hướng dẫn sử dụng.

## Ví dụ phổ biến
1. **Hiển thị toàn bộ thông tin phần cứng:**
   ```bash
   dmidecode
   ```

2. **Chỉ hiển thị thông tin về bộ vi xử lý:**
   ```bash
   dmidecode -t processor
   ```

3. **Hiển thị phiên bản BIOS:**
   ```bash
   dmidecode -s bios-version
   ```

4. **Hiển thị UUID của hệ thống:**
   ```bash
   dmidecode -s system-uuid
   ```

## Mẹo
- Sử dụng `sudo` để đảm bảo bạn có quyền truy cập đầy đủ vào thông tin phần cứng:
  ```bash
  sudo dmidecode
  ```
- Lưu thông tin đầu ra vào tệp để phân tích sau này:
  ```bash
  sudo dmidecode > hardware_info.txt
  ```
- Tham khảo tài liệu chính thức hoặc sử dụng `dmidecode --help` để tìm hiểu thêm về các tùy chọn và cách sử dụng.