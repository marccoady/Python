
#!/usr/bin/env python3.7

def count_substring(string, sub_string):
    firstl=len(string)
    secondl=len(sub_string)
    counter=0
    
    for i in range(firstl-secondl+1):
        if(string[i:(i+secondl)]== sub_string):
            counter=counter+1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)



