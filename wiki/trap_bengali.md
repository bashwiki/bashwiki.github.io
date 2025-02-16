# [লিনাক্স] Bash trap ব্যবহার: সংকেত পরিচালনা করা

## Overview
`trap` কমান্ডটি Bash স্ক্রিপ্টে সংকেত (signals) এবং অন্যান্য ইভেন্টগুলির জন্য হ্যান্ডলার সেট করতে ব্যবহৃত হয়। এটি স্ক্রিপ্টের কার্যক্রম নিয়ন্ত্রণ করতে সাহায্য করে, বিশেষ করে যখন স্ক্রিপ্টটি বন্ধ হচ্ছে বা কোনো সংকেত পাচ্ছে।

## Usage
`trap` কমান্ডের মৌলিক সিনট্যাক্স হল:

```bash
trap [options] [arguments]
```

## Common Options
- `SIGINT`: ইন্টারাপ্ট সংকেত (যেমন Ctrl+C) গ্রহণ করার সময় একটি কমান্ড চালায়।
- `SIGTERM`: টার্মিনেট সংকেত গ্রহণ করার সময় একটি কমান্ড চালায়।
- `EXIT`: স্ক্রিপ্টটি শেষ হওয়ার সময় একটি কমান্ড চালায়।

## Common Examples
### 1. SIGINT সংকেতের জন্য হ্যান্ডলার সেট করা
```bash
trap 'echo "Script interrupted"; exit' SIGINT
```
এই উদাহরণে, যদি স্ক্রিপ্টটি Ctrl+C দ্বারা বন্ধ করা হয়, তাহলে "Script interrupted" বার্তা প্রদর্শিত হবে।

### 2. স্ক্রিপ্ট শেষ হলে একটি বার্তা প্রদর্শন করা
```bash
trap 'echo "Script finished!"' EXIT
```
এই উদাহরণে, স্ক্রিপ্টটি শেষ হলে "Script finished!" বার্তা প্রদর্শিত হবে।

### 3. একাধিক সংকেতের জন্য হ্যান্ডলার সেট করা
```bash
trap 'echo "Caught SIGTERM"; exit' SIGTERM
trap 'echo "Caught SIGINT"; exit' SIGINT
```
এখানে, SIGTERM এবং SIGINT উভয়ের জন্য আলাদা হ্যান্ডলার সেট করা হয়েছে।

## Tips
- সংকেত হ্যান্ডলিংয়ের সময় সতর্ক থাকুন, কারণ ভুলভাবে সংকেত পরিচালনা করলে স্ক্রিপ্টের কার্যক্রম ব্যাহত হতে পারে।
- সংকেত হ্যান্ডলারের মধ্যে যতটা সম্ভব কম কোড রাখুন, যাতে তা দ্রুত সম্পন্ন হয়।
- বিভিন্ন সংকেতের জন্য আলাদা হ্যান্ডলার ব্যবহার করুন যাতে আপনি নির্দিষ্ট সংকেতের জন্য নির্দিষ্ট কার্যক্রম পরিচালনা করতে পারেন।