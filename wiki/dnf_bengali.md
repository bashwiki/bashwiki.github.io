# [লিনাক্স] Bash dnf ব্যবহার: প্যাকেজ ম্যানেজমেন্টের জন্য একটি শক্তিশালী টুল

## Overview
`dnf` (Dandified YUM) হল একটি প্যাকেজ ম্যানেজার যা RPM ভিত্তিক ডিস্ট্রিবিউশনের জন্য ব্যবহৃত হয়। এটি সফটওয়্যার ইনস্টল, আপডেট এবং মুছে ফেলার জন্য একটি সহজ এবং কার্যকরী উপায় প্রদান করে।

## Usage
`dnf` কমান্ডের মৌলিক সিনট্যাক্স হল:
```bash
dnf [options] [arguments]
```

## Common Options
- `install`: একটি বা একাধিক প্যাকেজ ইনস্টল করতে ব্যবহৃত হয়।
- `remove`: একটি বা একাধিক প্যাকেজ মুছে ফেলতে ব্যবহৃত হয়।
- `update`: ইনস্টল করা প্যাকেজগুলির সর্বশেষ সংস্করণ আপডেট করতে ব্যবহৃত হয়।
- `search`: প্যাকেজ নাম বা বর্ণনা অনুসারে অনুসন্ধান করতে ব্যবহৃত হয়।
- `list`: ইনস্টল করা এবং উপলব্ধ প্যাকেজের তালিকা প্রদর্শন করতে ব্যবহৃত হয়।

## Common Examples
- একটি প্যাকেজ ইনস্টল করা:
```bash
dnf install package_name
```

- একটি প্যাকেজ মুছে ফেলা:
```bash
dnf remove package_name
```

- সমস্ত প্যাকেজ আপডেট করা:
```bash
dnf update
```

- একটি প্যাকেজের জন্য অনুসন্ধান করা:
```bash
dnf search package_name
```

- ইনস্টল করা প্যাকেজের তালিকা দেখা:
```bash
dnf list installed
```

## Tips
- `-y` অপশন ব্যবহার করুন যাতে ইনস্টলেশন প্রক্রিয়ায় স্বয়ংক্রিয়ভাবে "হ্যাঁ" নির্বাচন করা হয়:
```bash
dnf install -y package_name
```
- প্যাকেজের নির্ভরতা সমস্যা সমাধানের জন্য `dnf history` কমান্ড ব্যবহার করুন।
- নিয়মিত আপডেট করতে `dnf update` চালানো নিশ্চিত করুন যাতে আপনার সিস্টেম সর্বদা সুরক্ষিত এবং আপডেট থাকে।