import glob
import os
import xml.dom.minidom as xml
from tqdm import tqdm

filelist = glob.glob('./bbox_val_v3/val/*.xml')
# print(filelist)

for f in tqdm(filelist[0:50000]):
    item = f.split("val/")[1]
    # print(item)
    doc = xml.parse(f)
    root = doc.documentElement
    # print(root.tagName) # annatation
    filename = root.getElementsByTagName("filename")[0].firstChild.data # ILSVRC2012_val_00000156
    # print(filename) # ILSVRC2012_val_00000156
    object_name = root.getElementsByTagName("name")[0].firstChild.data # n02114855
    # print(object_name)

    os.makedirs("/Lun2/great99/HRank-master/data/ILSVRC2012/" + object_name, exist_ok = True, mode=0o755)
    os.system("cp ./val/" + filename + ".JPEG ./val2/" + object_name + "/" )


