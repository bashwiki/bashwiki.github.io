# [লিনাক্স] Bash free ব্যবহার: মেমোরি ব্যবহারের তথ্য দেখান

## Overview
`free` কমান্ডটি লিনাক্স সিস্টেমে মেমোরি ব্যবহারের তথ্য প্রদর্শন করে। এটি RAM এবং সোয়াপ মেমোরির পরিমাণ, ব্যবহৃত এবং ফ্রি মেমোরির পরিসংখ্যান দেখায়, যা সিস্টেমের মেমোরি ব্যবস্থাপনা সম্পর্কে ধারণা দেয়।

## Usage
`free` কমান্ডের মৌলিক সিনট্যাক্স হলো:

```
free [options] [arguments]
```

## Common Options
- `-h`: মানব-পঠনযোগ্য ফরম্যাটে আউটপুট দেখায় (যেমন KB, MB, GB)।
- `-m`: মেমোরি পরিমাণ মেগাবাইটে দেখায়।
- `-g`: মেমোরি পরিমাণ গিগাবাইটে দেখায়।
- `-s [seconds]`: নির্দিষ্ট সময় অন্তর তথ্য আপডেট করে।
- `-t`: মোট মেমোরি ব্যবহারের তথ্য দেখায়।

## Common Examples
1. সাধারণ মেমোরি তথ্য দেখানোর জন্য:
   ```bash
   free
   ```

2. মানব-পঠনযোগ্য আউটপুটে মেমোরি তথ্য দেখানোর জন্য:
   ```bash
   free -h
   ```

3. মেমোরি তথ্য মেগাবাইটে দেখানোর জন্য:
   ```bash
   free -m
   ```

4. প্রতি 5 সেকেন্ডে আপডেট হওয়া মেমোরি তথ্য দেখানোর জন্য:
   ```bash
   free -s 5
   ```

5. মোট মেমোরি ব্যবহারের তথ্য দেখানোর জন্য:
   ```bash
   free -t
   ```

## Tips
- `free -h` ব্যবহার করা সর্বদা ভালো, কারণ এটি মেমোরি পরিমাণকে সহজে বোঝার জন্য উপযোগী করে।
- মেমোরি ব্যবহারের ট্রেন্ড বুঝতে `free -s [seconds]` ব্যবহার করে সময়ের সাথে সাথে পরিবর্তনগুলি পর্যবেক্ষণ করতে পারেন।
- `free` কমান্ডের আউটপুটের সাথে `grep` বা `awk` ব্যবহার করে নির্দিষ্ট তথ্য বের করা যেতে পারে।