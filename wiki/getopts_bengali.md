# [লিনাক্স] Bash getopts ব্যবহার: অপশন প্রক্রিয়াকরণ

## Overview
`getopts` কমান্ডটি Bash স্ক্রিপ্টে অপশন এবং আর্গুমেন্টগুলি প্রক্রিয়া করার জন্য ব্যবহৃত হয়। এটি স্ক্রিপ্টের জন্য ব্যবহারকারীর ইনপুট থেকে অপশনগুলি পড়তে এবং সেগুলি পরিচালনা করতে সহায়তা করে।

## Usage
`getopts` কমান্ডের মৌলিক সিনট্যাক্স নিম্নরূপ:

```bash
getopts [options] [arguments]
```

## Common Options
- `-a` : অপশনগুলির জন্য একটি অ্যালিয়াস তৈরি করে।
- `-n` : স্ক্রিপ্টের নাম নির্দিষ্ট করে।
- `-o` : অপশনগুলির জন্য সংক্ষিপ্ত ফর্ম তৈরি করে।

## Common Examples
নিচে কিছু সাধারণ উদাহরণ দেওয়া হলো:

### উদাহরণ ১: সাধারণ অপশন প্রক্রিয়াকরণ
```bash
#!/bin/bash

while getopts "a:b:c:" opt; do
  case $opt in
    a) echo "Option A: $OPTARG" ;;
    b) echo "Option B: $OPTARG" ;;
    c) echo "Option C: $OPTARG" ;;
    *) echo "Invalid option" ;;
  esac
done
```

### উদাহরণ ২: অপশন সহ স্ক্রিপ্ট চালানো
```bash
./myscript.sh -a value1 -b value2 -c value3
```

### উদাহরণ ৩: ডিফল্ট মান সেট করা
```bash
#!/bin/bash

while getopts "a:b:c:" opt; do
  case $opt in
    a) a_value=$OPTARG ;;
    b) b_value=$OPTARG ;;
    c) c_value=$OPTARG ;;
    *) echo "Invalid option" ;;
  esac
done

echo "A: ${a_value:-defaultA}, B: ${b_value:-defaultB}, C: ${c_value:-defaultC}"
```

## Tips
- `getopts` ব্যবহার করার সময়, অপশনগুলিকে একটি স্ট্রিং আকারে উল্লেখ করুন যাতে প্রতিটি অপশন একটি অক্ষর দ্বারা চিহ্নিত হয়।
- অপশনগুলির জন্য মানগুলি `:` দিয়ে পৃথক করুন, যেমন `a:` মানে `-a` অপশনের জন্য একটি আর্গুমেন্ট প্রয়োজন।
- `OPTIND` ভেরিয়েবলটি ব্যবহার করে পরবর্তী অপশনের অবস্থান ট্র্যাক করুন।