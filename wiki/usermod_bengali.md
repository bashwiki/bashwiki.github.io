# [লিনাক্স] Bash usermod ব্যবহার: ব্যবহারকারীর তথ্য পরিবর্তন করা

## Overview
`usermod` কমান্ডটি লিনাক্সে ব্যবহারকারীর তথ্য পরিবর্তন করার জন্য ব্যবহৃত হয়। এটি ব্যবহারকারীর নাম, গ্রুপ, হোম ডিরেক্টরি এবং অন্যান্য বৈশিষ্ট্য পরিবর্তন করতে সাহায্য করে।

## Usage
`usermod` কমান্ডের মৌলিক সিনট্যাক্স হল:

```bash
usermod [options] [arguments]
```

## Common Options
- `-l, --login NEW_LOGIN` : ব্যবহারকারীর নতুন লগইন নাম সেট করে।
- `-d, --home NEW_HOME` : ব্যবহারকারীর নতুন হোম ডিরেক্টরি সেট করে।
- `-m, --move-home` : পুরানো হোম ডিরেক্টরি থেকে নতুন হোম ডিরেক্টরিতে ফাইল স্থানান্তর করে।
- `-G, --groups GROUP1[,GROUP2,...]` : ব্যবহারকারীকে নতুন গ্রুপে যোগ করে।
- `-a, --append` : ব্যবহারকারীকে নতুন গ্রুপে যোগ করার সময় পূর্ববর্তী গ্রুপগুলিকে বজায় রাখে।

## Common Examples
- ব্যবহারকারীর নাম পরিবর্তন করা:

```bash
usermod -l newusername oldusername
```

- ব্যবহারকারীর হোম ডিরেক্টরি পরিবর্তন করা:

```bash
usermod -d /new/home/directory username
```

- ব্যবহারকারীর হোম ডিরেক্টরির ফাইল স্থানান্তর করা:

```bash
usermod -d /new/home/directory -m username
```

- ব্যবহারকারীকে নতুন গ্রুপে যোগ করা:

```bash
usermod -aG groupname username
```

## Tips
- `usermod` কমান্ডটি চালানোর আগে অবশ্যই রুট বা সুপারইউজার হিসেবে লগইন করুন।
- ব্যবহারকারী নাম বা হোম ডিরেক্টরি পরিবর্তন করার সময় সতর্ক থাকুন, কারণ এটি ব্যবহারকারীর লগইন এবং ফাইল অ্যাক্সেসকে প্রভাবিত করতে পারে।
- পরিবর্তনগুলি কার্যকর করার জন্য ব্যবহারকারীকে পুনরায় লগইন করতে হতে পারে।