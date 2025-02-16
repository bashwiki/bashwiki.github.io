# [لینوکس] Bash kubectl استفاده: مدیریت منابع کلاستر Kubernetes

## Overview
دستور `kubectl` ابزاری است که برای مدیریت و تعامل با کلاسترهای Kubernetes استفاده می‌شود. این ابزار به کاربران اجازه می‌دهد تا منابع مختلفی مانند پادها، سرویس‌ها و دیپلویمنت‌ها را ایجاد، به‌روزرسانی و حذف کنند.

## Usage
سینتکس پایه دستور `kubectl` به صورت زیر است:

```bash
kubectl [options] [arguments]
```

## Common Options
- `get`: برای دریافت اطلاعات در مورد منابع موجود.
- `create`: برای ایجاد منابع جدید.
- `delete`: برای حذف منابع.
- `apply`: برای به‌روزرسانی منابع با استفاده از فایل‌های پیکربندی.
- `describe`: برای نمایش جزئیات یک منبع خاص.

## Common Examples
### دریافت لیست پادها
```bash
kubectl get pods
```

### ایجاد یک پاد جدید
```bash
kubectl create deployment my-deployment --image=my-image
```

### حذف یک سرویس
```bash
kubectl delete service my-service
```

### به‌روزرسانی یک دیپلویمنت
```bash
kubectl apply -f deployment.yaml
```

### نمایش جزئیات یک پاد خاص
```bash
kubectl describe pod my-pod
```

## Tips
- همیشه قبل از اعمال تغییرات بزرگ، از منابع خود پشتیبان بگیرید.
- از گزینه `--dry-run` برای تست دستورات بدون اعمال تغییرات واقعی استفاده کنید.
- برای مدیریت بهتر، از فایل‌های YAML برای تعریف منابع استفاده کنید.