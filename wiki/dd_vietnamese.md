# [Linux] Bash dd Cách sử dụng: Sao chép và chuyển đổi dữ liệu

## Overview
Lệnh `dd` trong Bash được sử dụng để sao chép và chuyển đổi dữ liệu giữa các tệp hoặc thiết bị. Nó có thể được sử dụng để tạo bản sao của ổ đĩa, chuyển đổi định dạng tệp, hoặc sao chép dữ liệu từ một nguồn này sang một nguồn khác.

## Usage
Cú pháp cơ bản của lệnh `dd` như sau:

```bash
dd [options] [arguments]
```

## Common Options
- `if=`: Chỉ định tệp đầu vào (input file).
- `of=`: Chỉ định tệp đầu ra (output file).
- `bs=`: Đặt kích thước khối (block size) cho việc sao chép.
- `count=`: Chỉ định số lượng khối sẽ được sao chép.
- `status=`: Hiển thị thông tin trạng thái trong quá trình thực hiện.

## Common Examples

### 1. Sao chép một tệp
Sao chép tệp `input.txt` thành `output.txt`:

```bash
dd if=input.txt of=output.txt
```

### 2. Sao chép ổ đĩa
Sao chép ổ đĩa `/dev/sda` thành tệp ảnh `disk.img`:

```bash
dd if=/dev/sda of=disk.img bs=4M
```

### 3. Tạo ổ đĩa USB khởi động
Ghi tệp ISO vào ổ đĩa USB `/dev/sdb`:

```bash
dd if=ubuntu.iso of=/dev/sdb bs=4M status=progress
```

### 4. Chuyển đổi định dạng
Chuyển đổi tệp từ định dạng nhị phân sang định dạng văn bản:

```bash
dd if=input.bin of=output.txt conv=ucase
```

## Tips
- Luôn kiểm tra lại tệp đầu vào và đầu ra để tránh mất dữ liệu.
- Sử dụng tùy chọn `status=progress` để theo dõi tiến trình sao chép.
- Khi sao chép ổ đĩa, hãy chắc chắn rằng ổ đĩa đầu ra không chứa dữ liệu quan trọng, vì nó sẽ bị ghi đè.