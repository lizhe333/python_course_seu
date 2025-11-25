def remove_samename(s):
    names = s.split()
    #利用字典的键不重复的特质,会默认强制将字典的键转换成列表当中的元素
    unique_words=list(dict.fromkeys(names))
    return ' '.join(unique_words)

def main():
    s = input("Enter a string of names: ")
    result = remove_samename(s)
    print("String after removing duplicate names:", result)
if __name__ == "__main__":
    main()