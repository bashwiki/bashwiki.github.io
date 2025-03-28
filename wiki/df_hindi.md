# [लिनक्स] Bash df उपयोग: डिस्क स्थान की जानकारी प्राप्त करें

## Overview
`df` कमांड का उपयोग डिस्क स्थान की जानकारी प्राप्त करने के लिए किया जाता है। यह दिखाता है कि आपके सिस्टम में कितनी डिस्क स्पेस उपलब्ध है और कितनी स्पेस उपयोग में है।

## Usage
`df` कमांड का बेसिक सिंटैक्स इस प्रकार है:

```
df [options] [arguments]
```

## Common Options
- `-h`: मानव-पठनीय फॉर्मेट में आउटपुट दिखाता है (जैसे कि KB, MB, GB)।
- `-T`: फाइल सिस्टम के प्रकार को दिखाता है।
- `-a`: सभी फाइल सिस्टम को दिखाता है, जिसमें शून्य-आकार वाले भी शामिल हैं।
- `-i`: इनोड्स की जानकारी दिखाता है।

## Common Examples
1. **सभी फाइल सिस्टम की जानकारी प्राप्त करें:**
   ```bash
   df
   ```

2. **मानव-पठनीय फॉर्मेट में जानकारी प्राप्त करें:**
   ```bash
   df -h
   ```

3. **फाइल सिस्टम के प्रकार के साथ जानकारी प्राप्त करें:**
   ```bash
   df -T
   ```

4. **शून्य-आकार वाले फाइल सिस्टम को भी दिखाएं:**
   ```bash
   df -a
   ```

5. **इनोड्स की जानकारी प्राप्त करें:**
   ```bash
   df -i
   ```

## Tips
- `df -h` का उपयोग करना हमेशा बेहतर होता है ताकि आप आसानी से समझ सकें कि कितनी स्पेस उपलब्ध है।
- नियमित रूप से `df` कमांड का उपयोग करें ताकि आप अपने सिस्टम की डिस्क स्पेस का ध्यान रख सकें।
- जब आप किसी सर्वर पर काम कर रहे हों, तो सुनिश्चित करें कि आप फाइल सिस्टम के प्रकार को जानने के लिए `-T` विकल्प का उपयोग करें।