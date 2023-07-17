import re

def harverd_to_rsc_order (harverd):
    strip_comma = harverd.replace(',', '')
    split_list = strip_comma.split(" ")
    contain_period = []
    for i in range(len(split_list)):
        if "." in split_list[i]:
            contain_period.append(i)
    year = str(int(float(split_list[(contain_period[-3])])))
    last_author = split_list[(contain_period[-3])-3]+" "+ split_list[(contain_period[-3])-1]+split_list[(contain_period[-3])-2]
    name_list = []
    except_last_author = split_list[:(contain_period[-3])-3]
    for j in range(0, len(except_last_author), 2):
        if j+2 < len(except_last_author): 
            name_list.append(except_last_author[j+1]+except_last_author[j]+", ")
        elif j+1 < len(except_last_author): 
            name_list.append(except_last_author[j+1]+except_last_author[j]+" ")
    name_list.append(last_author)
    names = "".join(name_list)
    journal = "".join([string + ' ' for string in split_list[(contain_period[-2])+1:-2]]).strip(" ")
    page = split_list[-1].strip("pp.")
    vol = re.findall(r'^(.*?)\(', split_list[-2])[0]
    order = names +", "+ journal +", "+year +", "+ vol+", " + page
    return order