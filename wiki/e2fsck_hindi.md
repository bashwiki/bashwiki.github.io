# [लिनक्स] Bash e2fsck उपयोग: फ़ाइल सिस्टम की जांच करना

## Overview
e2fsck एक उपयोगिता है जो Linux और UNIX जैसे ऑपरेटिंग सिस्टम में ext2, ext3, और ext4 फ़ाइल सिस्टम की जांच और मरम्मत के लिए उपयोग की जाती है। यह कमांड फ़ाइल सिस्टम में किसी भी त्रुटियों का पता लगाता है और उन्हें ठीक करने का प्रयास करता है।

## Usage
e2fsck कमांड का बुनियादी सिंटैक्स निम्नलिखित है:

```
e2fsck [options] [arguments]
```

## Common Options
- `-p`: बिना किसी उपयोगकर्ता इनपुट के फ़ाइल सिस्टम की स्वचालित जांच करें।
- `-f`: फ़ाइल सिस्टम की मजबूर जांच करें, भले ही यह ठीक दिखे।
- `-n`: कोई भी परिवर्तन किए बिना केवल जांच करें (read-only मोड)।
- `-y`: सभी प्रश्नों का उत्तर "हाँ" दें, जिससे सभी त्रुटियों को स्वचालित रूप से ठीक किया जा सके।

## Common Examples
यहाँ कुछ सामान्य उदाहरण दिए गए हैं:

1. **बुनियादी जांच**:
   ```bash
   e2fsck /dev/sda1
   ```

2. **स्वचालित जांच**:
   ```bash
   e2fsck -p /dev/sda1
   ```

3. **मजबूर जांच**:
   ```bash
   e2fsck -f /dev/sda1
   ```

4. **केवल पढ़ने के लिए जांच**:
   ```bash
   e2fsck -n /dev/sda1
   ```

5. **सभी त्रुटियों को स्वचालित रूप से ठीक करना**:
   ```bash
   e2fsck -y /dev/sda1
   ```

## Tips
- हमेशा e2fsck का उपयोग करने से पहले फ़ाइल सिस्टम को अनमाउंट करें, ताकि डेटा हानि से बचा जा सके।
- यदि आप सुनिश्चित नहीं हैं कि क्या करना है, तो `-n` विकल्प का उपयोग करें ताकि आप बिना किसी परिवर्तन के केवल जांच कर सकें।
- नियमित रूप से फ़ाइल सिस्टम की जांच करना एक अच्छा अभ्यास है, खासकर जब आप किसी समस्या का सामना कर रहे हों।