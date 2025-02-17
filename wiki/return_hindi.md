# [Linux] Bash return उपयोग: फ़ंक्शन का परिणाम लौटाना

## Overview
`return` कमांड Bash स्क्रिप्टिंग में एक फ़ंक्शन के निष्पादन के बाद एक स्थिति कोड लौटाने के लिए उपयोग किया जाता है। यह मुख्य रूप से फ़ंक्शन के अंत में उपयोग किया जाता है ताकि यह संकेत दिया जा सके कि फ़ंक्शन सफलतापूर्वक समाप्त हुआ या नहीं।

## Usage
`return` कमांड का मूल सिंटैक्स इस प्रकार है:

```bash
return [options] [status_code]
```

## Common Options
- `status_code`: यह एक संख्यात्मक मान है जो फ़ंक्शन की स्थिति को दर्शाता है। 0 का अर्थ है सफल निष्पादन, जबकि 1 या उससे अधिक का अर्थ है कोई त्रुटि।

## Common Examples

### उदाहरण 1: सफल निष्पादन के लिए 0 लौटाना
```bash
my_function() {
    echo "Function executed successfully."
    return 0
}
my_function
```

### उदाहरण 2: त्रुटि के लिए 1 लौटाना
```bash
my_function() {
    echo "An error occurred."
    return 1
}
my_function
```

### उदाहरण 3: स्थिति कोड का उपयोग करना
```bash
my_function() {
    if [ -f "myfile.txt" ]; then
        echo "File exists."
        return 0
    else
        echo "File does not exist."
        return 1
    fi
}
my_function
```

## Tips
- हमेशा `return 0` का उपयोग करें जब आपका फ़ंक्शन सफलतापूर्वक समाप्त हो जाए।
- त्रुटियों की पहचान करने के लिए विभिन्न स्थिति कोड का उपयोग करें, जैसे `return 1`, `return 2`, आदि।
- फ़ंक्शन के बाहर `echo $?` का उपयोग करके अंतिम स्थिति कोड की जांच करें।