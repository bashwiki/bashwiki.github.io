# [Linux] Bash cat उपयोग: फ़ाइलों की सामग्री प्रदर्शित करना

## Overview
`cat` कमांड का उपयोग फ़ाइलों की सामग्री को प्रदर्शित करने, जोड़ने और नई फ़ाइलें बनाने के लिए किया जाता है। यह एक सरल और प्रभावी टूल है जो टेक्स्ट फ़ाइलों को पढ़ने में मदद करता है।

## Usage
`cat` कमांड का बुनियादी सिंटैक्स निम्नलिखित है:

```bash
cat [options] [arguments]
```

## Common Options
- `-n`: फ़ाइल की हर पंक्ति को नंबर करता है।
- `-b`: केवल गैर-खाली पंक्तियों को नंबर करता है।
- `-E`: प्रत्येक पंक्ति के अंत में `$` प्रतीक जोड़ता है।
- `-s`: लगातार खाली पंक्तियों को एक में समाहित करता है।

## Common Examples
यहाँ कुछ सामान्य उदाहरण दिए गए हैं:

1. एक फ़ाइल की सामग्री प्रदर्शित करना:
   ```bash
   cat filename.txt
   ```

2. दो फ़ाइलों को जोड़कर एक नई फ़ाइल बनाना:
   ```bash
   cat file1.txt file2.txt > combined.txt
   ```

3. एक फ़ाइल की सामग्री को नंबर के साथ प्रदर्शित करना:
   ```bash
   cat -n filename.txt
   ```

4. एक फ़ाइल की सामग्री को स्क्रीन पर प्रदर्शित करते हुए एक नई फ़ाइल में सहेजना:
   ```bash
   cat filename.txt | tee newfile.txt
   ```

## Tips
- यदि आप बड़ी फ़ाइलों के साथ काम कर रहे हैं, तो `less` या `more` कमांड का उपयोग करना बेहतर हो सकता है, क्योंकि वे पृष्ठ दर पृष्ठ नेविगेशन की अनुमति देते हैं।
- फ़ाइलों को जोड़ते समय, सुनिश्चित करें कि आप सही फ़ाइलों का चयन कर रहे हैं, क्योंकि `cat` कमांड मौजूदा फ़ाइलों को ओवरराइट कर सकता है।
- `cat` का उपयोग करते समय, ध्यान रखें कि यह बाइनरी फ़ाइलों के लिए उपयुक्त नहीं है, क्योंकि यह बाइनरी डेटा को प्रदर्शित करते समय समस्याएँ उत्पन्न कर सकता है।