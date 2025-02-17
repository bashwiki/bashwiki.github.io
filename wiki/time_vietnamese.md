# [Linux] Bash time sử dụng: Đo thời gian thực thi lệnh

## Overview
Lệnh `time` trong Bash được sử dụng để đo thời gian thực thi của một lệnh hoặc một tập hợp các lệnh. Nó cung cấp thông tin về thời gian thực tế, thời gian CPU và thời gian hệ thống mà lệnh đã sử dụng.

## Usage
Cú pháp cơ bản của lệnh `time` như sau:
```
time [options] [arguments]
```

## Common Options
- `-p`: Định dạng đầu ra theo cách POSIX.
- `-o filename`: Ghi kết quả vào tệp tin thay vì hiển thị trên màn hình.
- `-v`: Hiển thị thông tin chi tiết về thời gian thực thi.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `time`:

1. Đo thời gian thực thi của một lệnh đơn giản:
   ```bash
   time ls
   ```

2. Ghi kết quả vào tệp tin:
   ```bash
   time -o result.txt sleep 2
   ```

3. Sử dụng tùy chọn chi tiết:
   ```bash
   time -v find / -name "*.txt"
   ```

4. Đo thời gian thực thi của một tập hợp lệnh:
   ```bash
   time { echo "Start"; sleep 3; echo "End"; }
   ```

## Tips
- Sử dụng tùy chọn `-p` để có định dạng đầu ra dễ đọc hơn, đặc biệt khi bạn cần tích hợp với các công cụ khác.
- Ghi kết quả vào tệp tin nếu bạn cần lưu trữ hoặc phân tích sau này.
- Thử nghiệm với các lệnh khác nhau để hiểu rõ hơn về thời gian thực thi trong các tình huống khác nhau.