import xml.etree.ElementTree as ET
data = """
<student>
   <name>Ada</name>
   <department>cybersecurity</department>
   </student>
"""
root = ET.fromstring(data)
print(root.find('name').text)
print(root.find('department').text)