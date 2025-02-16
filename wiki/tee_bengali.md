# [লিনাক্স] Bash tee ব্যবহার: আউটপুট ফাইল ও প্রদর্শন করা

## Overview
`tee` কমান্ডটি একটি বিশেষ ধরনের কমান্ড যা স্ট্যান্ডার্ড ইনপুট থেকে ডেটা গ্রহণ করে এবং সেই ডেটাকে একাধিক আউটপুটে পাঠায়। এটি সাধারণত একটি ফাইলের মধ্যে লেখা এবং একই সাথে টার্মিনালে প্রদর্শন করার জন্য ব্যবহৃত হয়।

## Usage
`tee` কমান্ডের মৌলিক সিনট্যাক্স হল:

```
tee [options] [arguments]
```

## Common Options
- `-a`, `--append`: ফাইলের শেষে ডেটা যোগ করতে ব্যবহৃত হয়, নতুন করে লেখার পরিবর্তে।
- `-i`, `--ignore-interrupts`: ইন্টারাপ্ট সিগন্যাল উপেক্ষা করে।
- `-p`, `--output-error`: আউটপুট ত্রুটি পরিচালনা করতে ব্যবহৃত হয়।

## Common Examples
নিচে কিছু সাধারণ উদাহরণ দেওয়া হল:

1. **একটি ফাইলে লেখা এবং টার্মিনালে প্রদর্শন করা:**
   ```bash
   echo "Hello, World!" | tee output.txt
   ```

2. **একাধিক ফাইলে লেখা:**
   ```bash
   echo "Hello, again!" | tee file1.txt file2.txt
   ```

3. **ফাইলে ডেটা যোগ করা:**
   ```bash
   echo "Appending this line." | tee -a output.txt
   ```

4. **ইন্টারাপ্ট সিগন্যাল উপেক্ষা করা:**
   ```bash
   echo "This will ignore interrupts." | tee -i output.txt
   ```

## Tips
- `tee` ব্যবহার করার সময়, নিশ্চিত করুন যে আপনি সঠিক ফাইলের নাম উল্লেখ করছেন যাতে ভুল ফাইলে লেখা না হয়।
- `-a` অপশন ব্যবহার করে ডেটা যোগ করার সময় সাবধান থাকুন, কারণ এটি পূর্বের ডেটা মুছে ফেলবে না।
- যখন আপনি একটি পাইপলাইন ব্যবহার করছেন, তখন `tee` কমান্ডটি ডেটা প্রবাহের মধ্যে একটি পয়েন্টে আউটপুট দেখতে সাহায্য করে।