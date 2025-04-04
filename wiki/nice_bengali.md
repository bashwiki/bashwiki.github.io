# [লিনাক্স] Bash nice ব্যবহার: প্রক্রিয়ার অগ্রাধিকার নির্ধারণ করা

## Overview
`nice` কমান্ডটি লিনাক্স এবং ইউনিক্স ভিত্তিক সিস্টেমে ব্যবহৃত হয়, যা একটি প্রক্রিয়ার অগ্রাধিকার নির্ধারণ করতে সহায়তা করে। এটি একটি প্রক্রিয়াকে কম বা বেশি CPU সময় দেওয়ার জন্য ব্যবহার করা হয়, যাতে সিস্টেমের অন্যান্য প্রক্রিয়াগুলোর উপর প্রভাব কমানো যায়।

## Usage
`nice` কমান্ডের মৌলিক সিনট্যাক্স হল:

```bash
nice [options] [command]
```

## Common Options
- `-n, --adjustment=N`: প্রক্রিয়ার অগ্রাধিকার মান নির্ধারণ করে। এখানে N একটি সংখ্যা যা -20 থেকে 19 এর মধ্যে হতে পারে। -20 সর্বাধিক অগ্রাধিকার এবং 19 সর্বনিম্ন।
- `-h, --help`: সাহায্য তথ্য প্রদর্শন করে।
- `--version`: কমান্ডের সংস্করণ তথ্য প্রদর্শন করে।

## Common Examples
1. একটি প্রক্রিয়াকে স্বাভাবিক অগ্রাধিকার দিয়ে চালানো:
   ```bash
   nice echo "Hello, World!"
   ```

2. একটি প্রক্রিয়াকে কম অগ্রাধিকার দিয়ে চালানো (অগ্রাধিকার 10):
   ```bash
   nice -n 10 ./my_script.sh
   ```

3. একটি প্রক্রিয়াকে উচ্চ অগ্রাধিকার দিয়ে চালানো (অগ্রাধিকার -5):
   ```bash
   nice -n -5 ./my_heavy_task.sh
   ```

4. একটি প্রক্রিয়াকে স্বাভাবিক অগ্রাধিকার দিয়ে চালানোর সময়, তার অগ্রাধিকার পরিবর্তন করা:
   ```bash
   nice -n 0 ./my_program
   ```

## Tips
- `nice` কমান্ডটি ব্যবহার করার সময়, মনে রাখবেন যে কম অগ্রাধিকার দিয়ে চলমান প্রক্রিয়াগুলি সিস্টেমের অন্যান্য প্রক্রিয়ার তুলনায় কম CPU সময় পাবে।
- যদি আপনি একটি প্রক্রিয়ার অগ্রাধিকার পরিবর্তন করতে চান যা ইতিমধ্যে চলছে, `renice` কমান্ড ব্যবহার করতে পারেন।
- সিস্টেমের পারফরম্যান্স উন্নত করার জন্য, গুরুত্বপূর্ণ প্রক্রিয়াগুলিকে উচ্চ অগ্রাধিকার দিন এবং কম গুরুত্বপূর্ণ প্রক্রিয়াগুলিকে কম অগ্রাধিকার দিন।