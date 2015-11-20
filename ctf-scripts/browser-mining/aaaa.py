__author__ = 'HuyNA'


import os
import re
'''

'''

folder_contain = 'C:\\Users\\HuyNA\\Desktop\\Research\\browser\\SVG\\'

def write_file(file_name, content):
    f = open(file_name,'wb')
    f.write(content)
    f.close()

def read_file(file_name):
    f = open(file_name, 'rb')
    content = ''
    byte = f.read(1)
    while byte != b"":
        content += byte
        byte = f.read(1)
    f.close()
    return content

file_svg_element_list = folder_contain + 'svg-elements-list-fix.csv'
file_svg_attributes_list = folder_contain + 'svg-attributes-list-fix.csv'
file_svg_properties_list = folder_contain + 'svg-properties-list.csv'


svg_element_list = read_file(file_svg_element_list)
svg_attributes_list = read_file(file_svg_attributes_list)
svg_properties_list = read_file(file_svg_properties_list)

#print svg_properties_list
#print svg_element_list
#print svg_attributes_list

SVGAttributeList = []
def print_attribute(svg_attributes_list):
    svg_attributes_list1 = svg_attributes_list.split('\r\n')
    count = 0
    for i in svg_attributes_list1:
        temp = ''

        i = i.split(',')
        #print type(i)
        if len(i) < 3:
            print 'THE END ...'
            break
        SVGProperty = {}
        temp += 'AttributeName:"'+i[0]+'",\r\n'
        SVGProperty['AttributeName'] = i[0]

        element_contain = i[1].split(';')
        aa = ''
        for iii in element_contain:
            aa += '"'+iii.replace(' ','')+'",'
        aa = "["+aa+"]"
        temp += 'ElementContain:'+aa+',\r\n'
        SVGProperty['ElementContain'] = aa

        if i[2] == '':
            t = 'false'
        else:
            t = 'true'
        temp += 'IsAnimate:"'+t+'"\r\n'
        SVGProperty['IsAnimate'] = t

        #SVGPropertyList[SVGProperty['AttributeName']]=SVGProperty
        SVGAttributeList.append(SVGProperty)
        print SVGProperty
    print len(SVGAttributeList)

print_attribute(svg_attributes_list)

SVGElement = []
def print_element(svg_element_list):
    count = 0
    regex = r'\"(.+)\"'
    svg_element_list1 = svg_element_list.split('\x0d')
    for i in svg_element_list1:
        count += 1
        match = re.findall(regex,i)
        #print '%d %s' % (count, i)
        if len(match) != 0:
            match1 = match[0]
        SVGElement.append(match1)
    print SVGElement
    print len(SVGElement)
print_element(svg_element_list)

def print_properties(svg_properties_list):
    svg_attributes_list1 = svg_attributes_list.split('\r\n')
    return 1

print svg_properties_list