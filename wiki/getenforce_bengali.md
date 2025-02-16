# [লিনাক্স] Bash getenforce ব্যবহার: SELinux-এর বর্তমান অবস্থা দেখুন

## Overview
`getenforce` কমান্ডটি SELinux (Security-Enhanced Linux) এর বর্তমান কার্যকরী অবস্থা প্রদর্শন করে। এটি আপনাকে জানায় যে SELinux বর্তমানে "Enforcing", "Permissive", অথবা "Disabled" মোডে চলছে কিনা।

## Usage
নিচে `getenforce` কমান্ডের মৌলিক সিনট্যাক্স দেওয়া হলো:

```bash
getenforce [options]
```

## Common Options
`getenforce` কমান্ডের জন্য সাধারণ অপশনগুলি হল:
- `-h`, `--help`: সাহায্য তথ্য প্রদর্শন করে।
- `-V`, `--version`: সংস্করণ তথ্য প্রদর্শন করে।

## Common Examples
নিচে কিছু সাধারণ উদাহরণ দেওয়া হলো:

1. **SELinux-এর বর্তমান অবস্থা দেখুন:**
   ```bash
   getenforce
   ```

2. **সাহায্য তথ্য দেখুন:**
   ```bash
   getenforce --help
   ```

3. **সংস্করণ তথ্য দেখুন:**
   ```bash
   getenforce --version
   ```

## Tips
- SELinux-এর অবস্থা পরিবর্তন করতে চাইলে `setenforce` কমান্ড ব্যবহার করুন।
- নিরাপত্তা নীতি পরিবর্তনের আগে `getenforce` ব্যবহার করে নিশ্চিত করুন যে SELinux সঠিকভাবে কনফিগার করা আছে। 
- যদি আপনি SELinux-এর কার্যকরী অবস্থা সম্পর্কে আরও বিস্তারিত জানতে চান, তাহলে `/etc/selinux/config` ফাইলটি পরীক্ষা করুন।