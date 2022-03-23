import os
dir_path = '/Lun2/great99/HRank-master/data/ILSVRC2012'
for root, dir, files in os.walk(dir_path):
    for file in files:
        t = file.split('.')
        target_dir = os.path.join(root, t[0])
        # os.makedirs(target_dir)
        os.system("tar -xf " + './train/' + file + " -C ./train/" + file.split('.')[0])
        # print("tar -xf " + './train/' + file + " -C ./train/" + file.split('.')[0])
        # print(target_dir)
