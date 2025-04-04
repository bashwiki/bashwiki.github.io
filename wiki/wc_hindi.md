# [Linux] Bash wc उपयोग: फ़ाइलों में शब्द, पंक्तियाँ और वर्ण गिनें

## Overview
`wc` (word count) एक Bash कमांड है जिसका उपयोग फ़ाइलों में शब्दों, पंक्तियों और वर्णों की संख्या गिनने के लिए किया जाता है। यह कमांड टेक्स्ट फ़ाइलों के विश्लेषण में सहायक होता है और विभिन्न प्रकार की जानकारी प्रदान करता है।

## Usage
`wc` कमांड का बुनियादी सिंटैक्स इस प्रकार है:

```bash
wc [options] [arguments]
```

## Common Options
- `-l`: केवल पंक्तियों की संख्या दिखाता है।
- `-w`: केवल शब्दों की संख्या दिखाता है।
- `-c`: केवल वर्णों की संख्या दिखाता है।
- `-m`: केवल अक्षरों की संख्या दिखाता है (UTF-8 में)।
- `-L`: सबसे लंबी पंक्ति की लंबाई दिखाता है।

## Common Examples
1. **पंक्तियों की संख्या गिनना:**
   ```bash
   wc -l filename.txt
   ```

2. **शब्दों की संख्या गिनना:**
   ```bash
   wc -w filename.txt
   ```

3. **वर्णों की संख्या गिनना:**
   ```bash
   wc -c filename.txt
   ```

4. **एकाधिक फ़ाइलों के लिए गिनती:**
   ```bash
   wc file1.txt file2.txt
   ```

5. **सबसे लंबी पंक्ति की लंबाई दिखाना:**
   ```bash
   wc -L filename.txt
   ```

## Tips
- यदि आप एक ही समय में पंक्तियों, शब्दों और वर्णों की संख्या देखना चाहते हैं, तो बस `wc filename.txt` का उपयोग करें।
- कई फ़ाइलों के लिए गिनती करते समय, आउटपुट में प्रत्येक फ़ाइल के लिए अलग-अलग गिनती दिखाई देगी, और अंतिम पंक्ति में कुल गिनती दी जाएगी।
- `wc` कमांड को अन्य कमांड के साथ पाइप करके भी उपयोग किया जा सकता है, जैसे कि `cat` के साथ। उदाहरण:
  ```bash
  cat filename.txt | wc -l
  ```

`wc` कमांड एक सरल लेकिन शक्तिशाली उपकरण है जो टेक्स्ट फ़ाइलों के साथ काम करने में बहुत सहायक होता है।