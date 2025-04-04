# [লিনাক্স] Bash mknod ব্যবহার: ডিভাইস ফাইল তৈরি করা

## Overview
`mknod` কমান্ডটি লিনাক্সে ডিভাইস ফাইল তৈরি করার জন্য ব্যবহৃত হয়। এটি বিশেষ ধরনের ফাইল তৈরি করে যা হার্ডওয়্যার ডিভাইসের সাথে যোগাযোগ করতে ব্যবহৃত হয়।

## Usage
`mknod` কমান্ডের মৌলিক সিনট্যাক্স হল:

```
mknod [options] [arguments]
```

## Common Options
- `-m` : নতুন ফাইলটির অনুমতি সেট করতে ব্যবহৃত হয়।
- `-t` : টাইপ নির্ধারণ করতে ব্যবহৃত হয় (যেমন, পিপ, ব্লক ইত্যাদি)।

## Common Examples
1. একটি ব্লক ডিভাইস ফাইল তৈরি করা:
   ```bash
   mknod /dev/myblock b 8 0
   ```

2. একটি ক্যারেক্টার ডিভাইস ফাইল তৈরি করা:
   ```bash
   mknod /dev/mychar c 1 3
   ```

3. অনুমতি সেট করা:
   ```bash
   mknod -m 666 /dev/mydevice c 1 4
   ```

## Tips
- `mknod` ব্যবহার করার সময় সঠিক ডিভাইস নম্বর এবং টাইপ নিশ্চিত করুন।
- ডিভাইস ফাইল তৈরি করার আগে আপনার কাছে যথাযথ অনুমতি থাকা উচিত।
- `mknod` কমান্ডটি সাধারণত রুট ব্যবহারকারীর দ্বারা চালানো হয়, তাই সতর্কতা অবলম্বন করুন।