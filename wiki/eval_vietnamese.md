# [Linux] Bash eval cách sử dụng: Thực thi chuỗi lệnh

## Tổng quan
Lệnh `eval` trong Bash được sử dụng để thực thi một chuỗi lệnh được lưu trữ trong một biến hoặc một chuỗi. Nó giúp mở rộng các biến và thực thi lệnh như thể chúng được nhập trực tiếp vào dòng lệnh.

## Cách sử dụng
Cú pháp cơ bản của lệnh `eval` như sau:
```
eval [options] [arguments]
```

## Tùy chọn phổ biến
- Không có tùy chọn đặc biệt nào cho lệnh `eval`, nhưng bạn có thể sử dụng nó với các biến và chuỗi lệnh khác nhau.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `eval`:

1. **Thực thi lệnh từ biến**
   ```bash
   command="ls -l"
   eval $command
   ```

2. **Mở rộng biến và thực thi**
   ```bash
   filename="file.txt"
   command="cat $filename"
   eval $command
   ```

3. **Sử dụng với nhiều lệnh**
   ```bash
   commands="echo 'Hello, World!' && ls"
   eval $commands
   ```

4. **Kết hợp với các biến khác**
   ```bash
   var1="Hello"
   var2="World"
   eval "echo \$var1, \$var2!"
   ```

## Mẹo
- Hãy cẩn thận khi sử dụng `eval`, vì nó có thể thực thi bất kỳ lệnh nào, bao gồm cả lệnh không an toàn nếu chuỗi lệnh được tạo từ đầu vào không đáng tin cậy.
- Sử dụng `eval` khi bạn cần mở rộng biến trong một chuỗi lệnh phức tạp.
- Kiểm tra kỹ lưỡng các biến trước khi truyền vào `eval` để tránh các lỗi không mong muốn.