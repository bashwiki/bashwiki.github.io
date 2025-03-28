# [লিনাক্স] Bash scp ব্যবহার: ফাইল স্থানান্তর করা

## Overview
`scp` (Secure Copy Protocol) কমান্ডটি একটি নিরাপদ পদ্ধতিতে ফাইল স্থানান্তরের জন্য ব্যবহৃত হয়। এটি SSH প্রোটোকল ব্যবহার করে স্থানীয় এবং দূরবর্তী সিস্টেমের মধ্যে ফাইল কপি করতে সক্ষম।

## Usage
`scp` কমান্ডের মৌলিক সিনট্যাক্স হলো:

```bash
scp [options] [source] [destination]
```

## Common Options
- `-r`: ডিরেক্টরি এবং এর সমস্ত বিষয়বস্তু রিকার্সিভলি কপি করতে ব্যবহৃত হয়।
- `-P`: দূরবর্তী সার্ভারের পোর্ট নম্বর নির্ধারণ করতে ব্যবহৃত হয় (মনে রাখবেন, এটি বড় P)।
- `-i`: নির্দিষ্ট SSH কী ফাইল ব্যবহার করতে ব্যবহৃত হয়।
- `-v`: ডিবাগ তথ্য প্রদর্শনের জন্য ব্যবহৃত হয়, যা সমস্যা সমাধানে সহায়ক।

## Common Examples
1. স্থানীয় থেকে দূরবর্তী সার্ভারে একটি ফাইল কপি করা:
   ```bash
   scp localfile.txt user@remotehost:/path/to/destination/
   ```

2. দূরবর্তী সার্ভার থেকে স্থানীয় মেশিনে একটি ফাইল কপি করা:
   ```bash
   scp user@remotehost:/path/to/remotefile.txt /local/path/
   ```

3. একটি সম্পূর্ণ ডিরেক্টরি রিকার্সিভলি কপি করা:
   ```bash
   scp -r /local/directory user@remotehost:/path/to/destination/
   ```

4. নির্দিষ্ট পোর্ট ব্যবহার করে ফাইল কপি করা:
   ```bash
   scp -P 2222 localfile.txt user@remotehost:/path/to/destination/
   ```

## Tips
- নিশ্চিত করুন যে SSH সার্ভারটি দূরবর্তী মেশিনে চলছে।
- ফাইল স্থানান্তরের সময় নিরাপত্তার জন্য SSH কী ব্যবহার করা সর্বদা ভাল।
- বড় ফাইল স্থানান্তরের সময় `-v` অপশন ব্যবহার করে প্রক্রিয়াটি মনিটর করুন।