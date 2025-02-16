# [लिनक्स] Bash nohup उपयोग: बैकग्राउंड में प्रक्रिया चलाना

## Overview
`nohup` एक Bash कमांड है जो आपको किसी प्रक्रिया को लॉगआउट करने के बाद भी चलाने की अनुमति देती है। इसका उपयोग तब किया जाता है जब आप चाहते हैं कि प्रक्रिया बैकग्राउंड में चलती रहे, भले ही आप टर्मिनल को बंद कर दें।

## Usage
`nohup` कमांड का मूल सिंटैक्स इस प्रकार है:

```
nohup [options] [arguments]
```

## Common Options
- `&` : प्रक्रिया को बैकग्राउंड में चलाने के लिए।
- `-h` : हेल्प मेन्यू दिखाने के लिए।
- `-v` : वर्ज़न जानकारी दिखाने के लिए।

## Common Examples
1. एक साधारण प्रक्रिया को बैकग्राउंड में चलाना:
   ```bash
   nohup python script.py &
   ```

2. लॉग फाइल में आउटपुट को स्टोर करना:
   ```bash
   nohup my_command > output.log &
   ```

3. किसी प्रक्रिया को बिना किसी आउटपुट के चलाना:
   ```bash
   nohup my_command > /dev/null 2>&1 &
   ```

4. एक लंबे समय तक चलने वाले कमांड को चलाना:
   ```bash
   nohup long_running_task &
   ```

## Tips
- हमेशा `&` का उपयोग करें ताकि प्रक्रिया बैकग्राउंड में चले।
- आउटपुट को एक फ़ाइल में रीडायरेक्ट करना न भूलें, ताकि आप बाद में परिणाम देख सकें।
- यदि आप कई प्रक्रियाएँ चला रहे हैं, तो उन्हें अलग-अलग लॉग फ़ाइलों में रीडायरेक्ट करें ताकि ट्रैक करना आसान हो।