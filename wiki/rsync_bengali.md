# [লিনাক্স] Bash rsync ব্যবহার: ফাইল সিঙ্ক্রোনাইজেশন

## Overview
`rsync` একটি শক্তিশালী কমান্ড যা ফাইল এবং ডিরেক্টরি সিঙ্ক্রোনাইজেশন এবং স্থানান্তরের জন্য ব্যবহৃত হয়। এটি স্থানীয় এবং দূরবর্তী উভয় অবস্থানে ফাইল কপি করতে পারে এবং শুধুমাত্র পরিবর্তিত অংশগুলি স্থানান্তর করে, যা সময় এবং ব্যান্ডউইথ সাশ্রয় করে।

## Usage
`rsync` কমান্ডের মৌলিক সিনট্যাক্স হল:

```bash
rsync [options] [source] [destination]
```

## Common Options
- `-a`: আর্কাইভ মোড, যা ফাইলের সমস্ত বৈশিষ্ট্য (যেমন মালিকানা, অনুমতি, টাইমস্ট্যাম্প) সুরক্ষিত রাখে।
- `-v`: বিস্তারিত আউটপুট, যা প্রক্রিয়াকরণের সময় কনসোলে আরও তথ্য দেখায়।
- `-z`: ডেটা সংকোচন, যা স্থানান্তরের সময় ডেটা সংকুচিত করে।
- `-r`: রিকার্সিভ মোড, যা ডিরেক্টরিগুলির মধ্যে ফাইল এবং সাবডিরেক্টরিগুলি কপি করে।
- `--delete`: গন্তব্যে অতিরিক্ত ফাইল মুছে ফেলার জন্য ব্যবহৃত হয়, যাতে উভয় অবস্থানে ফাইল সিঙ্ক্রোনাইজড থাকে।

## Common Examples
1. স্থানীয় ফাইল সিঙ্ক্রোনাইজেশন:
   ```bash
   rsync -av /path/to/source/ /path/to/destination/
   ```

2. দূরবর্তী সার্ভারে ফাইল কপি করা:
   ```bash
   rsync -av /path/to/local/file user@remote_host:/path/to/remote/directory/
   ```

3. ডিরেক্টরি সিঙ্ক্রোনাইজেশন এবং অতিরিক্ত ফাইল মুছে ফেলা:
   ```bash
   rsync -av --delete /path/to/source/ /path/to/destination/
   ```

4. সংকোচন সহ ফাইল স্থানান্তর:
   ```bash
   rsync -avz /path/to/source/ user@remote_host:/path/to/remote/directory/
   ```

## Tips
- `-n` বা `--dry-run` অপশন ব্যবহার করুন, যাতে আপনি দেখতে পারেন কোন ফাইলগুলি স্থানান্তরিত হবে, কিন্তু আসলে কিছুই স্থানান্তরিত হবে না।
- স্থানীয় ব্যাকআপের জন্য `rsync` ব্যবহার করা নিরাপদ, কারণ এটি দ্রুত এবং কার্যকরী।
- নিয়মিত ব্যাকআপের জন্য ক্রন জব সেট আপ করুন যাতে আপনার ডেটা সর্বদা সুরক্ষিত থাকে।