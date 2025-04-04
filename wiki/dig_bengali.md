# [লিনাক্স] Bash dig ব্যবহার: DNS তথ্য অনুসন্ধান

## Overview
`dig` (Domain Information Groper) একটি শক্তিশালী কমান্ড-লাইন টুল যা DNS (Domain Name System) তথ্য অনুসন্ধানের জন্য ব্যবহৃত হয়। এটি ডোমেইন নামের সাথে সম্পর্কিত বিভিন্ন তথ্য যেমন IP ঠিকানা, MX রেকর্ড, এবং অন্যান্য DNS রেকর্ড পাওয়ার জন্য ব্যবহৃত হয়।

## Usage
`dig` কমান্ডের মৌলিক সিনট্যাক্স হলো:

```
dig [options] [arguments]
```

## Common Options
- `@server`: নির্দিষ্ট DNS সার্ভারের সাথে অনুসন্ধান করতে ব্যবহৃত হয়।
- `-t type`: অনুসন্ধানের জন্য DNS রেকর্ডের ধরন নির্ধারণ করে (যেমন A, AAAA, MX, TXT)।
- `+short`: সংক্ষিপ্ত আউটপুট প্রদর্শন করে, যা শুধুমাত্র প্রয়োজনীয় তথ্য দেখায়।
- `+trace`: DNS অনুসন্ধান প্রক্রিয়ার প্রতিটি ধাপ প্রদর্শন করে।

## Common Examples
1. একটি ডোমেইনের A রেকর্ড অনুসন্ধান:
   ```bash
   dig example.com
   ```

2. নির্দিষ্ট DNS সার্ভার ব্যবহার করে অনুসন্ধান:
   ```bash
   dig @8.8.8.8 example.com
   ```

3. MX রেকর্ড অনুসন্ধান:
   ```bash
   dig -t MX example.com
   ```

4. সংক্ষিপ্ত আউটপুট:
   ```bash
   dig +short example.com
   ```

5. DNS অনুসন্ধান প্রক্রিয়া ট্রেস করা:
   ```bash
   dig +trace example.com
   ```

## Tips
- `dig` কমান্ডের আউটপুট বিশ্লেষণ করতে সময় নিন, কারণ এটি বিভিন্ন তথ্য প্রদান করে যা DNS সমস্যা সমাধানে সহায়ক হতে পারে।
- DNS রেকর্ডের বিভিন্ন ধরনের জন্য আলাদা আলাদা অনুসন্ধান করুন, যেমন A, AAAA, MX, এবং TXT।
- DNS ক্যাশিং সমস্যা সমাধানের জন্য `+trace` অপশন ব্যবহার করুন, এটি আপনাকে DNS সার্ভারের সাথে যোগাযোগের প্রতিটি ধাপ দেখাবে।