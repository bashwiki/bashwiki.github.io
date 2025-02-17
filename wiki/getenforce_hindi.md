# [Linux] Bash getenforce उपयोग: SELinux की स्थिति जानें

## Overview
getenforce कमांड का उपयोग SELinux (Security-Enhanced Linux) की वर्तमान स्थिति को देखने के लिए किया जाता है। यह कमांड आपको बताता है कि SELinux वर्तमान में एनेबल्ड है, डिसेबल्ड है, या केवल कुछ विशेष मोड में चल रहा है।

## Usage
getentforce कमांड का मूल सिंटैक्स निम्नलिखित है:

```
getenforce [options]
```

## Common Options
getenforce कमांड के लिए कोई विशेष विकल्प नहीं होते हैं। यह केवल SELinux की स्थिति को प्रदर्शित करता है। 

## Common Examples
यहाँ कुछ सामान्य उदाहरण दिए गए हैं:

1. **SELinux की स्थिति देखें:**
   ```
   getenforce
   ```
   यह कमांड SELinux की वर्तमान स्थिति को प्रदर्शित करेगा, जैसे "Enforcing", "Permissive", या "Disabled"।

2. **SELinux की स्थिति को एक स्क्रिप्ट में उपयोग करना:**
   ```bash
   if [ "$(getenforce)" == "Enforcing" ]; then
       echo "SELinux is enforcing."
   else
       echo "SELinux is not enforcing."
   fi
   ```
   इस स्क्रिप्ट का उपयोग करके आप SELinux की स्थिति के आधार पर विभिन्न क्रियाएँ कर सकते हैं।

## Tips
- सुनिश्चित करें कि आप कमांड को सुपरयूजर के रूप में चला रहे हैं यदि आप SELinux की सेटिंग्स को बदलना चाहते हैं।
- नियमित रूप से SELinux की स्थिति की जांच करें, खासकर जब आप सुरक्षा सेटिंग्स में बदलाव कर रहे हों।
- यदि आप SELinux को डिसेबल करना चाहते हैं, तो ध्यान दें कि यह सुरक्षा को प्रभावित कर सकता है, इसलिए इसे सावधानी से करें।