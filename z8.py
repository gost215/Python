import re

def main(text: str) -> dict [str,list[str]]:
    text = text.replace("\n", ' ')
    result = dict()
    data_list = re.findall(r"t\s*\(.*?\)", text)
    keys = re.findall(r"\".*?\"", text)
    for n in range(len(keys)):
        keys[n] = keys[n].replace('"', '')
        data_list[n] = data_list[n].replace(' ', '').replace('t(', '')
        data_list[n] = data_list[n].replace(')', '').replace('#', '')
        result[keys[n]] = list(map(int, data_list[n].split(";")))
    return result

text1='(( [data "usle_482" : list( #4165; #2075; #9273 ; #4483 ) ][ data\n\
"bion" : list( #6508 ;#5184 ; #4366; #7128 ) ] [ data"soin_168" :\n\
list(#-8268 ; #-4655 ; #3415) ] [ data "bemain_709": list(#-5191 ;\n\
#-2151; #6198 ; #2457) ] ))'
print(main(text1))
text2 = '(([data "biorso_598" : list( #4247; #2600 ) ] [ data "diedin": \n\
list(#-8352 ; #1547 ; #8934 ) ] [ data"tear" :list(#2400 ;#6828) ] [ \n\
data "zara" : list( #5031 ;#5582; #-538 )] ))'
print(main(text2))
