# [Linux] Bash env उपयोग: पर्यावरण चर दिखाना और सेट करना

## Overview
`env` कमांड का उपयोग वर्तमान पर्यावरण चर को देखने और नए पर्यावरण चर सेट करने के लिए किया जाता है। यह कमांड शेल में एक नया वातावरण बनाने में मदद करता है, जो विशेष रूप से स्क्रिप्टिंग और प्रोग्राम चलाने के लिए उपयोगी है।

## Usage
कमांड की मूल संरचना इस प्रकार है:
```bash
env [options] [arguments]
```

## Common Options
- `-i` : एक खाली पर्यावरण के साथ कमांड चलाता है।
- `-u` : निर्दिष्ट पर्यावरण चर को हटा देता है।
- `-0` : शून्य-समाप्ति वाले इनपुट का उपयोग करता है।

## Common Examples
1. **सभी पर्यावरण चर दिखाना:**
   ```bash
   env
   ```

2. **विशिष्ट पर्यावरण चर दिखाना:**
   ```bash
   env | grep PATH
   ```

3. **नया पर्यावरण चर सेट करना और कमांड चलाना:**
   ```bash
   env MY_VAR=value command_name
   ```

4. **एक खाली पर्यावरण के साथ कमांड चलाना:**
   ```bash
   env -i command_name
   ```

5. **एक पर्यावरण चर को हटाना:**
   ```bash
   env -u MY_VAR command_name
   ```

## Tips
- `env` का उपयोग करते समय, सुनिश्चित करें कि आप सही पर्यावरण चर सेट कर रहे हैं, ताकि आपके प्रोग्राम सही तरीके से काम करें।
- स्क्रिप्ट में `env` का उपयोग करना एक अच्छा अभ्यास है, क्योंकि यह सुनिश्चित करता है कि स्क्रिप्ट में आवश्यक पर्यावरण चर उपलब्ध हैं।
- जब आप `-i` विकल्प का उपयोग करते हैं, तो ध्यान रखें कि यह सभी मौजूदा पर्यावरण चर को हटा देता है, इसलिए केवल आवश्यक चर ही सेट करें।