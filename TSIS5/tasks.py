#1
import re

txt = "abba or abr or abbott mountain"
x = re.findall(r'ab*', txt)
print(x)


#2
import re

txt = "abba or abr or abbott mountain"
x = re.findall(r'ab{2,3}', txt)
print(x)


#3
import re

txt = "lowercase_letters or upper_case_Letter"
x = re.findall(r'[a-z]+_[a-z]+', txt)
print(x)


#4
import re

txt = "Lowercase_letters or upper_case_Letter"
x = re.findall(r'[A-Z][a-z]+', txt)
print(x)


#5
import re

txt = "abb or overabsorb or abbott mountain"
x = re.findall(r'a.*?b$', txt)
print(x)


#6
import re

txt = "A string. with spaces and, commas."
y = re.compile(r'[ ,.]')
x = re.sub(y, ":", txt)
print(x)


#7
txt = "Panda_is_the_best_animal"

def snake_to_camel(txt):
    temp = txt.split('_')
    return temp[0] + ''.join(ele.title() for ele in temp[1:])

print(snake_to_camel(txt))


txt = "Panda_is_the_best_animal"

def snake_to_camel(txt):
    import re
    return ''.join(x.capitalize() or '_' for x in txt.split('_'))

print(snake_to_camel(txt))


#8
import re

txt = "PandaIsTheBestAnimal"
x = re.findall("[A-Z][a-z]*", txt)
print(x)


#9
import re

def capital_ch_spaces(txt):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)

txt = "PandaIsTheBestAnimal"
print(capital_ch_spaces(txt))


#10
txt = "PandaIsTheBestAnimal"

def camel_to_snake(txt):
    import re
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

print(camel_to_snake(txt))