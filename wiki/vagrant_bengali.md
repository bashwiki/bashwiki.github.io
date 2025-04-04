# [লিনাক্স] Bash vagrant ব্যবহার: ভার্চুয়াল পরিবেশ তৈরি করা

## Overview
`vagrant` একটি শক্তিশালী টুল যা ডেভেলপারদের জন্য ভার্চুয়াল পরিবেশ তৈরি এবং পরিচালনা করতে সহায়ক। এটি বিভিন্ন প্ল্যাটফর্মে কাজ করে এবং সহজেই ভার্চুয়াল মেশিন তৈরি, কনফিগার এবং পরিচালনা করার সুবিধা প্রদান করে।

## Usage
`vagrant` কমান্ডের মৌলিক সিনট্যাক্স হল:

```
vagrant [options] [arguments]
```

## Common Options
- `init`: একটি নতুন Vagrant প্রকল্প শুরু করে।
- `up`: ভার্চুয়াল মেশিন চালু করে।
- `halt`: ভার্চুয়াল মেশিন বন্ধ করে।
- `destroy`: ভার্চুয়াল মেশিন মুছে ফেলে।
- `ssh`: ভার্চুয়াল মেশিনে SSH এর মাধ্যমে সংযোগ স্থাপন করে।

## Common Examples
- একটি নতুন Vagrant প্রকল্প তৈরি করতে:
  ```bash
  vagrant init ubuntu/bionic64
  ```

- ভার্চুয়াল মেশিন চালু করতে:
  ```bash
  vagrant up
  ```

- ভার্চুয়াল মেশিন বন্ধ করতে:
  ```bash
  vagrant halt
  ```

- ভার্চুয়াল মেশিন মুছে ফেলতে:
  ```bash
  vagrant destroy
  ```

- ভার্চুয়াল মেশিনে SSH এর মাধ্যমে সংযোগ করতে:
  ```bash
  vagrant ssh
  ```

## Tips
- Vagrantfile কনফিগারেশন ফাইলটি সম্পাদনা করে আপনার ভার্চুয়াল মেশিনের সেটিংস কাস্টমাইজ করুন।
- Vagrant প্লাগইন ব্যবহার করে নতুন ফিচার যোগ করুন।
- ভার্চুয়াল মেশিনের অবস্থা নিয়মিত চেক করতে `vagrant status` কমান্ড ব্যবহার করুন।