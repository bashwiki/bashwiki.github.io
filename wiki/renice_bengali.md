# [লিনাক্স] Bash renice ব্যবহার: প্রক্রিয়ার অগ্রাধিকার পরিবর্তন করা

## Overview
`renice` কমান্ডটি চলমান প্রক্রিয়ার অগ্রাধিকার পরিবর্তন করতে ব্যবহৃত হয়। এটি সিস্টেমের সম্পদ ব্যবস্থাপনায় সহায়তা করে, বিশেষ করে যখন কিছু প্রক্রিয়া বেশি CPU সময় ব্যবহার করছে।

## Usage
`renice` কমান্ডের মৌলিক সিনট্যাক্স হলো:

```bash
renice [options] [arguments]
```

## Common Options
- `-n, --priority`: নতুন অগ্রাধিকার মান নির্ধারণ করে।
- `-p, --pid`: নির্দিষ্ট প্রক্রিয়ার আইডি (PID) উল্লেখ করে।
- `-g, --pgroup`: প্রক্রিয়া গ্রুপের জন্য অগ্রাধিকার পরিবর্তন করে।
- `-u, --user`: নির্দিষ্ট ব্যবহারকারীর সমস্ত প্রক্রিয়ার জন্য অগ্রাধিকার পরিবর্তন করে।

## Common Examples
1. একটি নির্দিষ্ট PID এর জন্য অগ্রাধিকার পরিবর্তন করা:
   ```bash
   renice -n 10 -p 1234
   ```

2. একটি প্রক্রিয়া গ্রুপের জন্য অগ্রাধিকার পরিবর্তন করা:
   ```bash
   renice -n 5 -g 5678
   ```

3. একটি ব্যবহারকারীর সমস্ত প্রক্রিয়ার জন্য অগ্রাধিকার পরিবর্তন করা:
   ```bash
   renice -n 15 -u username
   ```

4. একাধিক PID এর জন্য একই অগ্রাধিকার সেট করা:
   ```bash
   renice -n 0 -p 1234 -p 5678
   ```

## Tips
- `renice` কমান্ড ব্যবহার করার আগে নিশ্চিত করুন যে আপনি যথাযথ অনুমতি পেয়েছেন, কারণ কিছু প্রক্রিয়ার অগ্রাধিকার পরিবর্তন করতে প্রশাসক অধিকার প্রয়োজন হতে পারে।
- অগ্রাধিকার মান -20 থেকে 19 এর মধ্যে হতে পারে, যেখানে -20 সর্বাধিক অগ্রাধিকার এবং 19 সর্বনিম্ন।
- প্রক্রিয়ার অগ্রাধিকার পরিবর্তন করার সময় সিস্টেমের স্থিতিশীলতা এবং কর্মক্ষমতা বিবেচনা করুন।