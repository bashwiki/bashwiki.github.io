# [লিনাক্স] Bash cd ব্যবহার: ডিরেক্টরি পরিবর্তন করা

## Overview
`cd` কমান্ডটি ব্যবহারকারীদের বর্তমান কার্যকরী ডিরেক্টরি পরিবর্তন করতে সহায়তা করে। এটি একটি গুরুত্বপূর্ণ কমান্ড যা ফাইল সিস্টেমের মধ্যে নেভিগেট করার জন্য ব্যবহৃত হয়।

## Usage
`cd` কমান্ডের মৌলিক সিনট্যাক্স হল:

```bash
cd [options] [arguments]
```

## Common Options
- `-`: পূর্ববর্তী ডিরেক্টরিতে ফিরে যাওয়ার জন্য ব্যবহৃত হয়।
- `..`: এক স্তর উপরে উঠতে ব্যবহৃত হয়।
- `~`: ব্যবহারকারীর হোম ডিরেক্টরিতে যাওয়ার জন্য ব্যবহৃত হয়।

## Common Examples
1. হোম ডিরেক্টরিতে যাওয়া:
    ```bash
    cd ~
    ```

2. এক স্তর উপরে যাওয়া:
    ```bash
    cd ..
    ```

3. একটি নির্দিষ্ট ডিরেক্টরিতে যাওয়া:
    ```bash
    cd /path/to/directory
    ```

4. পূর্ববর্তী ডিরেক্টরিতে ফিরে যাওয়া:
    ```bash
    cd -
    ```

## Tips
- `cd` কমান্ডটি ব্যবহার করার সময়, নিশ্চিত করুন যে আপনি সঠিক পাথ ব্যবহার করছেন।
- `pwd` কমান্ড ব্যবহার করে আপনার বর্তমান ডিরেক্টরি চেক করতে পারেন।
- ডিরেক্টরি নামের ক্ষেত্রে বড়-ছোট অক্ষরের প্রতি মনোযোগ দিন, কারণ লিনাক্সে এটি সংবেদনশীল।