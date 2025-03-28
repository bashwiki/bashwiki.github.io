# [लिनक्स] Bash exit उपयोग: प्रक्रिया समाप्त करना

## Overview
`exit` कमांड का उपयोग Bash स्क्रिप्ट या टर्मिनल सत्र को समाप्त करने के लिए किया जाता है। यह कमांड एक स्थिति कोड लौटाता है, जो यह दर्शाता है कि प्रक्रिया सफलतापूर्वक समाप्त हुई या नहीं।

## Usage
बुनियादी सिंटैक्स इस प्रकार है:
```
exit [options] [arguments]
```

## Common Options
- `n`: यह विकल्प एक स्थिति कोड निर्दिष्ट करता है, जहाँ `n` एक संख्या है। यदि कोई संख्या नहीं दी गई है, तो अंतिम कमांड का स्थिति कोड लौटाया जाता है।

## Common Examples
1. **बिना स्थिति कोड के बाहर निकलना:**
   ```bash
   exit
   ```

2. **स्थिति कोड 0 के साथ बाहर निकलना (सफलता):**
   ```bash
   exit 0
   ```

3. **स्थिति कोड 1 के साथ बाहर निकलना (त्रुटि):**
   ```bash
   exit 1
   ```

4. **स्क्रिप्ट के अंत में बाहर निकलना:**
   ```bash
   #!/bin/bash
   echo "स्क्रिप्ट चल रही है..."
   exit 0
   ```

## Tips
- हमेशा स्थिति कोड का उपयोग करें ताकि यह स्पष्ट हो सके कि स्क्रिप्ट सफलतापूर्वक समाप्त हुई या नहीं।
- यदि आप स्क्रिप्ट में कई स्थानों पर `exit` का उपयोग कर रहे हैं, तो सुनिश्चित करें कि कोड का प्रबंधन सही तरीके से किया गया है। 
- `exit` का उपयोग करते समय ध्यान रखें कि यह स्क्रिप्ट को तुरंत समाप्त कर देता है, इसलिए इसे सावधानी से उपयोग करें।