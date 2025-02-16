# [Linux] Bash head ব্যবহার: ফাইলের শীর্ষ লাইনগুলি দেখুন

## Overview
`head` কমান্ডটি একটি ফাইলের শীর্ষের কিছু লাইন প্রদর্শন করতে ব্যবহৃত হয়। এটি সাধারণত বড় ফাইলের প্রথম কয়েকটি লাইন দেখতে বা ডেটার একটি সংক্ষিপ্ত চিত্র পেতে ব্যবহৃত হয়।

## Usage
`head` কমান্ডের মৌলিক সিনট্যাক্স হল:

```bash
head [options] [arguments]
```

## Common Options
- `-n [number]`: নির্দিষ্ট সংখ্যক লাইন প্রদর্শন করে। ডিফল্টভাবে এটি প্রথম 10 লাইন দেখায়।
- `-c [number]`: নির্দিষ্ট সংখ্যক বাইট প্রদর্শন করে।
- `-q`: একাধিক ফাইলের জন্য হেডার তথ্য দেখায় না।
- `-v`: একাধিক ফাইলের জন্য হেডার তথ্য দেখায়।

## Common Examples
1. প্রথম 10 লাইন দেখানো:
   ```bash
   head filename.txt
   ```

2. প্রথম 5 লাইন দেখানো:
   ```bash
   head -n 5 filename.txt
   ```

3, প্রথম 20 বাইট দেখানো:
   ```bash
   head -c 20 filename.txt
   ```

4. একাধিক ফাইলের শীর্ষ 10 লাইন দেখানো:
   ```bash
   head file1.txt file2.txt
   ```

5. একটি ফাইলের শীর্ষ 15 লাইন দেখানো এবং হেডার তথ্য সহ:
   ```bash
   head -v -n 15 filename.txt
   ```

## Tips
- বড় ফাইলের ক্ষেত্রে, `head` ব্যবহার করে দ্রুত একটি ধারণা পেতে পারেন।
- `head` কমান্ডের সাথে পাইপ ব্যবহার করে অন্যান্য কমান্ডের সাথে সংযোগ করতে পারেন, যেমন `grep`।
- `head` এবং `tail` কমান্ডগুলি একসাথে ব্যবহার করে ফাইলের মাঝের অংশ দেখতে পারেন।