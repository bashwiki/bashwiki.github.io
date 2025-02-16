# [Linux] Bash kubectl การใช้งาน: คำสั่งสำหรับจัดการ Kubernetes

## Overview
คำสั่ง `kubectl` เป็นเครื่องมือที่ใช้ในการจัดการและควบคุมคลัสเตอร์ Kubernetes โดยช่วยให้ผู้ใช้สามารถสร้าง ดู แก้ไข และลบทรัพยากรในคลัสเตอร์ได้อย่างง่ายดาย

## Usage
รูปแบบพื้นฐานของคำสั่ง `kubectl` คือ:

```bash
kubectl [options] [arguments]
```

## Common Options
- `get`: ใช้เพื่อดึงข้อมูลทรัพยากรในคลัสเตอร์
- `create`: ใช้เพื่อสร้างทรัพยากรใหม่
- `apply`: ใช้เพื่อปรับปรุงหรือสร้างทรัพยากรจากไฟล์
- `delete`: ใช้เพื่อลบทรัพยากร
- `describe`: ใช้เพื่อแสดงรายละเอียดของทรัพยากร

## Common Examples
- ดึงข้อมูล Pods ทั้งหมดในคลัสเตอร์:
  ```bash
  kubectl get pods
  ```

- สร้าง Deployment ใหม่จากไฟล์ YAML:
  ```bash
  kubectl create -f deployment.yaml
  ```

- ปรับปรุง Deployment ที่มีอยู่:
  ```bash
  kubectl apply -f deployment.yaml
  ```

- ลบ Service ที่ชื่อว่า `my-service`:
  ```bash
  kubectl delete service my-service
  ```

- แสดงรายละเอียดของ Pod ที่ชื่อว่า `my-pod`:
  ```bash
  kubectl describe pod my-pod
  ```

## Tips
- ใช้ `kubectl get all` เพื่อดูทรัพยากรทั้งหมดในคลัสเตอร์
- ใช้ `--namespace` เพื่อระบุ namespace ที่ต้องการทำงานด้วย
- ใช้ `-o wide` เพื่อแสดงข้อมูลเพิ่มเติมเกี่ยวกับทรัพยากร
- แนะนำให้ใช้ไฟล์ YAML ในการจัดการทรัพยากรเพื่อให้สามารถติดตามและปรับปรุงได้ง่ายขึ้น