# [লিনাক্স] Bash kubectl ব্যবহার: Kubernetes ক্লাস্টার পরিচালনা করুন

## Overview
`kubectl` হলো একটি কমান্ড-লাইন টুল যা Kubernetes ক্লাস্টার পরিচালনার জন্য ব্যবহৃত হয়। এটি ব্যবহারকারীদের পড, সার্ভিস, ডিপ্লয়মেন্ট এবং অন্যান্য Kubernetes রিসোর্স তৈরি, আপডেট এবং মুছে ফেলার অনুমতি দেয়।

## Usage
`kubectl` কমান্ডের মৌলিক সিনট্যাক্স হলো:

```bash
kubectl [options] [arguments]
```

## Common Options
- `get`: রিসোর্সের তালিকা প্রদর্শন করে।
- `create`: নতুন রিসোর্স তৈরি করে।
- `delete`: বিদ্যমান রিসোর্স মুছে ফেলে।
- `apply`: YAML ফাইল থেকে রিসোর্স তৈরি বা আপডেট করে।
- `describe`: নির্দিষ্ট রিসোর্সের বিস্তারিত তথ্য দেখায়।

## Common Examples
- পডের তালিকা দেখতে:
    ```bash
    kubectl get pods
    ```

- একটি নতুন পড তৈরি করতে:
    ```bash
    kubectl create -f pod.yaml
    ```

- একটি পড মুছে ফেলতে:
    ```bash
    kubectl delete pod <pod-name>
    ```

- YAML ফাইল থেকে রিসোর্স আপডেট করতে:
    ```bash
    kubectl apply -f deployment.yaml
    ```

- একটি সার্ভিসের বিস্তারিত তথ্য দেখতে:
    ```bash
    kubectl describe service <service-name>
    ```

## Tips
- YAML ফাইল ব্যবহার করে রিসোর্স তৈরি এবং আপডেট করা সর্বদা একটি ভালো অভ্যাস।
- `kubectl` কমান্ডের সাথে `--help` অপশন ব্যবহার করে বিভিন্ন অপশন এবং তাদের ব্যাখ্যা দেখতে পারেন।
- ক্লাস্টারের বর্তমান কনটেক্সট চেক করতে `kubectl config current-context` কমান্ড ব্যবহার করুন।