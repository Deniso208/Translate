from module.module1 import *

def main():
    # text = input("Введіть текст перекладу: ")
    # src = input("Введіть код оригінального тексту: ") 
    # dest = input("Введіть код мови на яку потрібно перекласти: ")  
    # set = input("Введіть що хочете дізнатися: \nlang – функція повертає тільки мову тексту\nconfidence – функція повертає тільки коефіцієнт довіри \nall (по замовченню) – функція повертає мову і коефіцієнт довіри ") 

    text = "Hi bro"
    src = "en"
    dest = "uk"
    set = "all"


    detection_result = LangDetect(text, set=set)
    print(Fore.RED, detection_result)

    translated_text = TransLate(text, src=src, dest=dest)
    print(Fore.GREEN, translated_text)

    code = CodeLang(src)
    print(Fore.BLUE,code)

    # out = input("Виберіть метод виведення мови 'screen'  або 'txt' "  )
    out = "txt"
    LanguageList(out, text)

    print(Style.RESET_ALL)

if __name__ == '__main__':
    main()