# [리눅스] Bash bc 사용법

## Tổng quan
`bc` là một công cụ tính toán trong Bash, cho phép người dùng thực hiện các phép toán số học phức tạp với độ chính xác cao. Nó hỗ trợ các phép toán cơ bản như cộng, trừ, nhân, chia, cũng như các phép toán nâng cao hơn như lũy thừa và tính toán số thập phân. `bc` thường được sử dụng trong các script shell để thực hiện các phép toán mà `expr` không thể xử lý hoặc khi cần độ chính xác cao hơn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `bc` như sau:

```bash
bc [options]
```

### Các tùy chọn phổ biến:
- `-l`: Kích hoạt thư viện toán học, cho phép sử dụng các hàm toán học như `sine`, `cosine`, `square root`, v.v.
- `-q`: Chạy `bc` ở chế độ im lặng, không hiển thị thông điệp khởi động.
- `-e`: Chạy lệnh `bc` từ dòng lệnh mà không cần vào chế độ tương tác.

## Ví dụ
### Ví dụ 1: Tính toán đơn giản
Bạn có thể sử dụng `bc` để thực hiện các phép toán cơ bản. Ví dụ, để tính tổng của 5 và 10:

```bash
echo "5 + 10" | bc
```
Kết quả sẽ là:
```
15
```

### Ví dụ 2: Sử dụng thư viện toán học
Nếu bạn muốn tính căn bậc hai của một số, bạn có thể sử dụng tùy chọn `-l`:

```bash
echo "scale=2; sqrt(16)" | bc -l
```
Kết quả sẽ là:
```
4.00
```

## Mẹo
- Sử dụng `scale` để xác định số chữ số thập phân trong kết quả. Ví dụ, `scale=3; 1/3` sẽ cho kết quả là `0.333`.
- Để thực hiện các phép toán phức tạp, bạn có thể viết các biểu thức trong một tệp tin và sau đó sử dụng `bc` để thực thi nó. Ví dụ:

```bash
cat > calculations.bc << EOF
scale=2
a = 5
b = 10
a + b
EOF

bc calculations.bc
```

Hy vọng bài viết này giúp bạn hiểu rõ hơn về cách sử dụng lệnh `bc` trong Bash!