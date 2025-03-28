# [লিনাক্স] Bash reboot ব্যবহার: সিস্টেম পুনরায় চালু করা

## Overview
`reboot` কমান্ডটি লিনাক্স সিস্টেমে সিস্টেমটি পুনরায় চালু করার জন্য ব্যবহৃত হয়। এটি সিস্টেমের সমস্ত কার্যক্রম বন্ধ করে এবং কম্পিউটারকে পুনরায় চালু করে।

## Usage
বেসিক সিনট্যাক্স হলো:
```
reboot [options] [arguments]
```

## Common Options
- `-f`: ফোর্সড রিবুট, যা সিস্টেমের সমস্ত কার্যক্রমকে জোরপূর্বক বন্ধ করে।
- `-p`: সিস্টেম বন্ধ করার পর পাওয়ার অফ করে।
- `-w`: শুধুমাত্র লগ ফাইল আপডেট করে, সিস্টেম পুনরায় চালু করে না।

## Common Examples
1. সাধারণভাবে সিস্টেম পুনরায় চালু করতে:
   ```bash
   reboot
   ```

2. ফোর্সড রিবুট করার জন্য:
   ```bash
   reboot -f
   ```

3. সিস্টেম বন্ধ করার পর পাওয়ার অফ করতে:
   ```bash
   reboot -p
   ```

4. লগ ফাইল আপডেট করতে (কিন্তু সিস্টেম পুনরায় চালু না করে):
   ```bash
   reboot -w
   ```

## Tips
- সিস্টেম পুনরায় চালু করার আগে নিশ্চিত করুন যে সমস্ত গুরুত্বপূর্ণ কাজ সংরক্ষিত হয়েছে।
- `reboot` কমান্ডটি ব্যবহার করার জন্য প্রশাসক (root) অধিকার প্রয়োজন হতে পারে।
- সিস্টেমের পুনরায় চালু করার সময়, কিছু সময় অপেক্ষা করুন যাতে সমস্ত পরিষেবা সঠিকভাবে বন্ধ হয়।