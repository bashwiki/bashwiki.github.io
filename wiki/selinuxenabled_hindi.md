# [Linux] Bash selinuxenabled उपयोग: SELinux की स्थिति की जांच करें

## Overview
`selinuxenabled` कमांड यह जांचने के लिए उपयोग किया जाता है कि क्या SELinux (Security-Enhanced Linux) सक्षम है या नहीं। यह एक साधारण कमांड है जो केवल 0 (यदि SELinux सक्षम है) या 1 (यदि SELinux अक्षम है) लौटाता है।

## Usage
कमांड का मूल सिंटैक्स इस प्रकार है:

```bash
selinuxenabled [options] [arguments]
```

## Common Options
`selinuxenabled` कमांड के लिए कोई विशेष विकल्प नहीं होते हैं। यह केवल एक साधारण जांच है।

## Common Examples
यहाँ कुछ सामान्य उदाहरण दिए गए हैं:

### उदाहरण 1: SELinux स्थिति की जांच करना
SELinux की स्थिति की जांच करने के लिए, आप बस कमांड चला सकते हैं:

```bash
selinuxenabled
```

यदि SELinux सक्षम है, तो यह कोई आउटपुट नहीं देगा (शून्य लौटाएगा), और यदि यह अक्षम है, तो यह 1 लौटाएगा।

### उदाहरण 2: SELinux स्थिति का उपयोग करना
आप इस कमांड का उपयोग स्क्रिप्ट में कर सकते हैं, जैसे:

```bash
if selinuxenabled; then
    echo "SELinux is enabled."
else
    echo "SELinux is disabled."
fi
```

यह स्क्रिप्ट SELinux की स्थिति के आधार पर एक संदेश प्रदर्शित करेगी।

## Tips
- SELinux की स्थिति की जांच करने के लिए `selinuxenabled` एक तेज़ और प्रभावी तरीका है।
- इसे स्क्रिप्टिंग में शामिल करें ताकि आप अपने सिस्टम की सुरक्षा सेटिंग्स के बारे में जानकारी प्राप्त कर सकें।
- SELinux को सक्षम या अक्षम करने के लिए, `setenforce` और `setsebool` जैसे अन्य कमांड का उपयोग करें।