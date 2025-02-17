# [Linux] Bash bc Cách sử dụng: Thực hiện các phép toán số học

## Overview
Lệnh `bc` là một trình tính toán số học trong Bash, cho phép người dùng thực hiện các phép toán số học phức tạp. Nó hỗ trợ các phép toán cơ bản như cộng, trừ, nhân, chia, và còn có thể xử lý các phép toán với số thập phân và số lớn.

## Usage
Cú pháp cơ bản của lệnh `bc` như sau:
```
bc [options] [arguments]
```

## Common Options
- `-l`: Kích hoạt thư viện toán học, cho phép sử dụng các hàm toán học như sin, cos, sqrt.
- `-q`: Chạy `bc` trong chế độ im lặng, không hiển thị thông điệp khởi động.
- `-e`: Chạy một lệnh cụ thể và sau đó thoát.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `bc`:

1. **Thực hiện phép cộng đơn giản:**
   ```bash
   echo "5 + 3" | bc
   ```

2. **Thực hiện phép chia với số thập phân:**
   ```bash
   echo "scale=2; 10 / 3" | bc
   ```

3. **Sử dụng thư viện toán học để tính căn bậc hai:**
   ```bash
   echo "scale=4; sqrt(16)" | bc -l
   ```

4. **Tính toán phức tạp hơn:**
   ```bash
   echo "scale=3; (2 + 3) * (4 - 1)" | bc
   ```

5. **Chạy lệnh trực tiếp trong `bc`:**
   ```bash
   bc <<< "10 + 20"
   ```

## Tips
- Luôn đặt `scale` trước khi thực hiện phép toán với số thập phân để xác định số chữ số thập phân muốn hiển thị.
- Sử dụng `-l` nếu bạn cần thực hiện các phép toán phức tạp hơn với các hàm toán học.
- Bạn có thể lưu các phép toán vào một tệp và sau đó chạy tệp đó bằng lệnh `bc` để tiết kiệm thời gian.