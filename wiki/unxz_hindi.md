# [लिनक्स] Bash unxz उपयोग: फ़ाइलों को अनज़िप करना

## Overview
`unxz` कमांड का उपयोग `.xz` फ़ाइलों को अनज़िप करने के लिए किया जाता है। यह एक सरल और प्रभावी तरीका है जिससे आप संकुचित फ़ाइलों को आसानी से निकाल सकते हैं।

## Usage
`unxz` कमांड का मूल सिंटैक्स इस प्रकार है:

```
unxz [options] [arguments]
```

## Common Options
- `-k` या `--keep`: यह विकल्प मूल `.xz` फ़ाइल को बनाए रखता है, जबकि अनज़िप की गई फ़ाइल को बनाता है।
- `-f` या `--force`: यदि अनज़िप की गई फ़ाइल पहले से मौजूद है, तो इसे ओवरराइट करने के लिए इस विकल्प का उपयोग करें।
- `-v` या `--verbose`: यह विकल्प अनज़िपिंग प्रक्रिया के दौरान विस्तृत जानकारी प्रदर्शित करता है।

## Common Examples
यहाँ कुछ सामान्य उदाहरण दिए गए हैं:

1. एक साधारण `.xz` फ़ाइल को अनज़िप करना:
   ```bash
   unxz file.xz
   ```

2. मूल फ़ाइल को बनाए रखते हुए अनज़िप करना:
   ```bash
   unxz -k file.xz
   ```

3. पहले से मौजूद फ़ाइल को ओवरराइट करते हुए अनज़िप करना:
   ```bash
   unxz -f file.xz
   ```

4. विस्तृत जानकारी के साथ अनज़िप करना:
   ```bash
   unxz -v file.xz
   ```

## Tips
- यदि आप सुनिश्चित नहीं हैं कि फ़ाइल पहले से मौजूद है, तो `-k` विकल्प का उपयोग करना एक अच्छा विचार है ताकि आपकी मूल फ़ाइल सुरक्षित रहे।
- बड़े फ़ाइलों को अनज़िप करते समय, यह सुनिश्चित करें कि आपके पास पर्याप्त डिस्क स्पेस हो।
- `unxz` का उपयोग करते समय, आप हमेशा `-v` विकल्प का उपयोग कर सकते हैं ताकि आपको प्रक्रिया के बारे में जानकारी मिलती रहे।