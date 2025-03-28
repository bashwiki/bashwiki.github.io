# [Linux] Bash alias उपयोग: कमांड को संक्षिप्त नाम देना

## Overview
`alias` कमांड का उपयोग शेल में एक संक्षिप्त नाम बनाने के लिए किया जाता है, जिससे आप लंबे और जटिल कमांड को आसानी से चला सकते हैं। यह आपके कार्य को सरल बनाता है और समय की बचत करता है।

## Usage
`alias` कमांड का मूल सिंटैक्स इस प्रकार है:

```bash
alias [options] [arguments]
```

## Common Options
- `-p`: सभी मौजूदा अलियास को प्रदर्शित करता है।
- `-d`: एक अलियास को हटाने के लिए उपयोग किया जाता है।

## Common Examples
यहाँ कुछ सामान्य उदाहरण दिए गए हैं:

1. एक सरल अलियास बनाना:
   ```bash
   alias ll='ls -la'
   ```
   यह कमांड `ll` टाइप करने पर `ls -la` चलाएगा।

2. एक अलियास को हटाना:
   ```bash
   unalias ll
   ```
   यह `ll` अलियास को हटा देगा।

3. एक अलियास के साथ एक विशेष विकल्प जोड़ना:
   ```bash
   alias gs='git status'
   ```
   अब `gs` टाइप करने पर `git status` चलाया जाएगा।

4. एक अलियास को स्थायी बनाना (बश प्रोफाइल में जोड़ना):
   ```bash
   echo "alias ll='ls -la'" >> ~/.bashrc
   ```
   इस कमांड से `~/.bashrc` फ़ाइल में अलियास जोड़ा जाएगा, जो हर बार शेल शुरू होने पर लोड होगा।

## Tips
- अलियास का नाम छोटा और याद रखने में आसान रखें।
- अलियास को स्थायी बनाने के लिए उन्हें अपने बश प्रोफाइल में जोड़ें।
- अलियास के नाम में ऐसे शब्दों का उपयोग न करें जो पहले से ही किसी अन्य कमांड के लिए उपयोग में हैं, ताकि भ्रम से बचा जा सके।