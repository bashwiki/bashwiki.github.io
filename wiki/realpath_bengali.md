# [লিনাক্স] Bash realpath ব্যবহার: ফাইলের পূর্ণ পাথ নির্ধারণ করা

## Overview
`realpath` কমান্ডটি একটি ফাইল বা ডিরেক্টরির পূর্ণ পাথ নির্ধারণ করতে ব্যবহৃত হয়। এটি একটি আপেক্ষিক পাথকে তার সম্পূর্ণ পাথে রূপান্তর করে, যা ফাইল সিস্টেমে সঠিক অবস্থান নির্দেশ করে।

## Usage
`realpath` কমান্ডের মৌলিক সিনট্যাক্স হলো:

```bash
realpath [options] [arguments]
```

## Common Options
- `-m`, `--canonicalize-missing`: যদি পাথটি বিদ্যমান না হয় তবে এটি একটি ক্যানোনিক্যাল পাথ প্রদান করে।
- `-q`, `--quiet`: ত্রুটি বার্তা প্রদর্শন করে না।
- `-s`, `--strip`: শেষের `/` চিহ্নগুলি সরিয়ে দেয়।

## Common Examples
নিচে কিছু সাধারণ উদাহরণ দেওয়া হলো:

### উদাহরণ 1: একটি আপেক্ষিক পাথের পূর্ণ পাথ নির্ধারণ করা
```bash
realpath ./myfile.txt
```

### উদাহরণ 2: একটি ডিরেক্টরির পূর্ণ পাথ নির্ধারণ করা
```bash
realpath /home/user/documents/
```

### উদাহরণ 3: একটি বিদ্যমান না থাকা ফাইলের ক্যানোনিক্যাল পাথ নির্ধারণ করা
```bash
realpath -m ./nonexistentfile.txt
```

## Tips
- `realpath` ব্যবহার করার সময় নিশ্চিত করুন যে আপনি সঠিক পাথ প্রদান করছেন, কারণ এটি আপেক্ষিক পাথগুলিকে পূর্ণ পাথে রূপান্তর করে।
- ত্রুটি বার্তা এড়াতে `-q` অপশন ব্যবহার করতে পারেন।
- যদি আপনি একটি ডিরেক্টরি পাথের শেষের `/` চিহ্নগুলি সরাতে চান, তবে `-s` অপশন ব্যবহার করুন।