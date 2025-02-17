# [Linux] Bash kubectl Sử dụng: Quản lý Kubernetes

## Tổng quan
Lệnh `kubectl` là công cụ dòng lệnh chính để tương tác với Kubernetes, cho phép người dùng quản lý các tài nguyên trong cụm Kubernetes. Với `kubectl`, bạn có thể triển khai ứng dụng, kiểm tra trạng thái của các pod, và thực hiện nhiều tác vụ quản lý khác.

## Cách sử dụng
Cú pháp cơ bản của lệnh `kubectl` như sau:
```
kubectl [options] [arguments]
```

## Tùy chọn phổ biến
- `get`: Lấy thông tin về các tài nguyên trong cụm.
- `apply`: Áp dụng các thay đổi từ tệp cấu hình.
- `delete`: Xóa tài nguyên khỏi cụm.
- `describe`: Hiển thị thông tin chi tiết về một tài nguyên cụ thể.
- `logs`: Xem nhật ký của một pod.

## Ví dụ phổ biến
1. **Lấy danh sách các pod trong namespace mặc định:**
   ```bash
   kubectl get pods
   ```

2. **Áp dụng cấu hình từ tệp YAML:**
   ```bash
   kubectl apply -f deployment.yaml
   ```

3. **Xóa một pod cụ thể:**
   ```bash
   kubectl delete pod my-pod
   ```

4. **Hiển thị thông tin chi tiết về một dịch vụ:**
   ```bash
   kubectl describe service my-service
   ```

5. **Xem nhật ký của một pod:**
   ```bash
   kubectl logs my-pod
   ```

## Mẹo
- Luôn kiểm tra trạng thái của các tài nguyên bằng lệnh `kubectl get` để đảm bảo mọi thứ hoạt động như mong đợi.
- Sử dụng tệp cấu hình YAML để quản lý các tài nguyên phức tạp, giúp dễ dàng áp dụng và thay đổi.
- Thực hành sử dụng các lệnh trong môi trường thử nghiệm trước khi áp dụng vào môi trường sản xuất để tránh rủi ro.