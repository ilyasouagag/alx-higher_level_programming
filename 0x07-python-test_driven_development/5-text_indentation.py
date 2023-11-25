def text_indentation(text):
    if  not isinstance(text, str):
        raise TypeError("text must be a string")
    string = ""
    for i in text:
        alert = 0
        string += i
        if i == '\n':
            string = string.rstrip()
            print(string)
            string=""
        if i in ".?:":
            string = string.strip()
            print(string)
            print()
            string = ""
            alert = 1
    if alert == 0 and not all(n == ' ' for n in string):
        string = string.strip() 
        print(string)
