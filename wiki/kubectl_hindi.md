# [리눅스] Bash kubectl 사용법

## Overview
`kubectl` एक कमांड-लाइन टूल है जिसका उपयोग Kubernetes क्लस्टर के साथ बातचीत करने के लिए किया जाता है। यह डेवलपर्स और सिस्टम एडमिनिस्ट्रेटर्स को Kubernetes संसाधनों को प्रबंधित करने, निगरानी करने और तैनात करने की अनुमति देता है। `kubectl` का मुख्य उद्देश्य Kubernetes API के साथ संवाद करना और क्लस्टर में विभिन्न कार्यों को निष्पादित करना है।

## Usage
`kubectl` का मूल सिंटैक्स इस प्रकार है:

```bash
kubectl [command] [TYPE] [NAME] [flags]
```

यहाँ, `[command]` वह क्रिया है जो आप करना चाहते हैं (जैसे `get`, `create`, `delete`), `[TYPE]` वह संसाधन प्रकार है (जैसे `pod`, `service`, `deployment`), और `[NAME]` उस संसाधन का नाम है जिस पर आप क्रिया करना चाहते हैं। 

कुछ सामान्य विकल्प (options) हैं:
- `--namespace`: विशेष namespace में कमांड चलाने के लिए।
- `-o`: आउटपुट फॉर्मेट (जैसे `json`, `yaml`) निर्दिष्ट करने के लिए।
- `--kubeconfig`: वैकल्पिक kubeconfig फ़ाइल का पथ।

## Examples
### उदाहरण 1: Pods की सूची प्राप्त करना
```bash
kubectl get pods
```
यह कमांड वर्तमान namespace में सभी Pods की सूची दिखाएगा।

### उदाहरण 2: एक नया Deployment बनाना
```bash
kubectl create deployment my-deployment --image=my-image:latest
```
यह कमांड `my-image:latest` इमेज का उपयोग करके `my-deployment` नाम का एक नया Deployment बनाएगा।

## Tips
- `kubectl` के साथ `--help` विकल्प का उपयोग करें ताकि आप किसी भी कमांड के लिए मदद प्राप्त कर सकें। उदाहरण: `kubectl get --help`
- नियमित रूप से `kubectl` के वर्शन को अपडेट करें ताकि आप नई सुविधाओं और सुधारों का लाभ उठा सकें।
- YAML फ़ाइलों का उपयोग करके संसाधनों को प्रबंधित करने के लिए `kubectl apply -f <file.yaml>` का उपयोग करें, जिससे आप संसाधनों को आसानी से तैनात और अपडेट कर सकें।