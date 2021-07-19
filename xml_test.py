import xml.etree.ElementTree as ET

tree = ET.parse('ss.xml')
root = tree.getroot()
for node in list(root):
    print(node.tag, node.get('Index'), node.get('Name'), node.text)
    if node.get('Name') == "姓名":
        node.text = "某某人不在家"


print('\n')
print('修改后：')
for node in list(root):
    print(node.tag, node.get('Index'), node.get('Name'), node.text)
