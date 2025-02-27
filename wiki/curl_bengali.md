# [লিনাক্স] Bash curl ব্যবহার: URL থেকে ডেটা ডাউনলোড করা

## Overview
`curl` একটি কমান্ড লাইন টুল যা URL থেকে ডেটা স্থানান্তর করতে ব্যবহৃত হয়। এটি HTTP, HTTPS, FTP এবং অন্যান্য প্রোটোকল সমর্থন করে, যা ব্যবহারকারীদের বিভিন্ন ধরনের সার্ভার থেকে তথ্য আহরণ করতে সক্ষম করে।

## Usage
`curl` কমান্ডের মৌলিক সিনট্যাক্স হল:

```bash
curl [options] [arguments]
```

## Common Options
- `-O`: ফাইলটি ডাউনলোড করে এবং উৎসের নাম অনুযায়ী সংরক্ষণ করে।
- `-o [filename]`: ডাউনলোড করা ফাইলটি নির্দিষ্ট নাম দিয়ে সংরক্ষণ করে।
- `-I`: শুধুমাত্র HTTP হেডারগুলি দেখায়, ডেটা নয়।
- `-L`: যদি URL-এ রিডাইরেকশন থাকে তবে সেটি অনুসরণ করে।
- `-u [user:password]`: প্রমাণীকরণের জন্য ব্যবহারকারীর নাম এবং পাসওয়ার্ড প্রদান করে।

## Common Examples
- একটি URL থেকে একটি ফাইল ডাউনলোড করা:

```bash
curl -O http://example.com/file.txt
```

- একটি ফাইল নির্দিষ্ট নাম দিয়ে ডাউনলোড করা:

```bash
curl -o myfile.txt http://example.com/file.txt
```

- শুধুমাত্র HTTP হেডারগুলি দেখা:

```bash
curl -I http://example.com
```

- রিডাইরেকশন অনুসরণ করা:

```bash
curl -L http://example.com/redirect
```

- প্রমাণীকরণের সাথে ডেটা আহরণ করা:

```bash
curl -u username:password http://example.com/protected
```

## Tips
- `-v` অপশন ব্যবহার করে ডিবাগিং তথ্য দেখতে পারেন, যা সমস্যা সমাধানে সহায়ক হতে পারে।
- নিরাপত্তার জন্য, পাসওয়ার্ড সরাসরি কমান্ড লাইনে না লিখে, একটি `.netrc` ফাইল ব্যবহার করা ভাল।
- ডাউনলোডের অগ্রগতি দেখতে `-#` অপশন ব্যবহার করুন, যা একটি প্রগ্রেস বার প্রদর্শন করে।