# [লিনাক্স] Bash mv ব্যবহার: ফাইল স্থানান্তর বা নাম পরিবর্তন করা

## Overview
`mv` কমান্ডটি লিনাক্স এবং ইউনিক্স ভিত্তিক সিস্টেমে ফাইল এবং ডিরেক্টরি স্থানান্তর বা নাম পরিবর্তন করার জন্য ব্যবহৃত হয়। এটি একটি মৌলিক এবং গুরুত্বপূর্ণ কমান্ড, যা ব্যবহারকারীদের ফাইল ব্যবস্থাপনায় সহায়তা করে।

## Usage
`mv` কমান্ডের মৌলিক সিনট্যাক্স হল:

```bash
mv [options] [source] [destination]
```

## Common Options
- `-i`: যদি গন্তব্যে একই নামের ফাইল থাকে, তবে ব্যবহারকারীকে নিশ্চিতকরণের জন্য জিজ্ঞাসা করে।
- `-u`: শুধুমাত্র তখনই স্থানান্তর করে যখন উৎস ফাইলটি গন্তব্য ফাইলের চেয়ে নতুন হয়।
- `-v`: স্থানান্তরের সময় বিস্তারিত তথ্য প্রদর্শন করে।
- `-f`: গন্তব্যে একই নামের ফাইল থাকলে তা অটোমেটিকভাবে মুছে ফেলে এবং স্থানান্তর সম্পন্ন করে।

## Common Examples
- একটি ফাইলের নাম পরিবর্তন করা:

```bash
mv old_filename.txt new_filename.txt
```

- একটি ফাইল অন্য ডিরেক্টরিতে স্থানান্তর করা:

```bash
mv filename.txt /path/to/destination/
```

- একই নামের ফাইল থাকলে নিশ্চিতকরণ সহ স্থানান্তর করা:

```bash
mv -i filename.txt /path/to/destination/
```

- একটি ডিরেক্টরি এবং এর সব ফাইল স্থানান্তর করা:

```bash
mv /path/to/source_directory/ /path/to/destination_directory/
```

## Tips
- ফাইল স্থানান্তরের আগে সবসময় নিশ্চিত করুন যে গন্তব্য সঠিক। 
- `-i` অপশন ব্যবহার করে নিশ্চিতকরণ পেতে পারেন, যা ভুল স্থানান্তরের সম্ভাবনা কমায়।
- ফাইল স্থানান্তরের পরে, গন্তব্যে ফাইলটি সঠিকভাবে স্থানান্তরিত হয়েছে কিনা তা পরীক্ষা করুন।