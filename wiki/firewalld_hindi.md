# [Linux] Bash firewalld उपयोग: फ़ायरवॉल प्रबंधन के लिए

## Overview
firewalld एक डायनामिक फ़ायरवॉल प्रबंधन उपकरण है जो Linux सिस्टम पर नेटवर्क सुरक्षा को नियंत्रित करने के लिए उपयोग किया जाता है। यह उपयोगकर्ताओं को विभिन्न नेटवर्क ज़ोन और सेवाओं के माध्यम से ट्रैफ़िक को नियंत्रित करने की अनुमति देता है।

## Usage
firewalld कमांड का मूल सिंटैक्स इस प्रकार है:

```bash
firewalld [options] [arguments]
```

## Common Options
- `--zone=<zone>`: निर्दिष्ट ज़ोन के लिए नियम लागू करता है।
- `--add-service=<service>`: निर्दिष्ट सेवा को सक्रिय करता है।
- `--remove-service=<service>`: निर्दिष्ट सेवा को निष्क्रिय करता है।
- `--add-port=<port>/<protocol>`: निर्दिष्ट पोर्ट को सक्रिय करता है।
- `--remove-port=<port>/<protocol>`: निर्दिष्ट पोर्ट को निष्क्रिय करता है。
- `--list-all`: सभी सक्रिय ज़ोन और उनके नियमों की सूची दिखाता है।

## Common Examples
1. **एक सेवा को सक्रिय करना:**
   ```bash
   firewall-cmd --zone=public --add-service=http --permanent
   ```

2. **एक सेवा को निष्क्रिय करना:**
   ```bash
   firewall-cmd --zone=public --remove-service=http --permanent
   ```

3. **एक पोर्ट को सक्रिय करना:**
   ```bash
   firewall-cmd --zone=public --add-port=8080/tcp --permanent
   ```

4. **सभी सक्रिय ज़ोन और नियमों की सूची दिखाना:**
   ```bash
   firewall-cmd --list-all
   ```

5. **परिवर्तनों को लागू करना:**
   ```bash
   firewall-cmd --reload
   ```

## Tips
- हमेशा `--permanent` विकल्प का उपयोग करें यदि आप चाहते हैं कि परिवर्तन सिस्टम रीबूट के बाद भी बने रहें।
- `firewall-cmd --list-all` का उपयोग करके अपने फ़ायरवॉल की स्थिति की नियमित रूप से जांच करें।
- ज़ोन का सही चयन करें, क्योंकि यह आपके नेटवर्क ट्रैफ़िक को प्रभावित कर सकता है।