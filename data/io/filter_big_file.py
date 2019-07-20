import os
import glob


big_file_list = []
xml_list = glob.glob('D:/competition/crop_dataset/without_big_train/train/labeltxt/*.xml')
print(len(xml_list))
for i, xml in enumerate(xml_list):
    if os.path.getsize(xml) > 103000:
        big_file_list.append(xml.split('\\')[-1])
        # print(i, ':', xml)
print('out of range files have :', len(big_file_list))

delete_path = 'D:/competition/crop_dataset/without_big_train/train'
print(big_file_list)
for j, xm in enumerate(big_file_list):
    img_name = xm.split('.')[0]+'.png'
    # print(xm)
    # print(img_name)
    img_path = os.path.join(delete_path, 'images', img_name)
    xml_path = os.path.join(delete_path, 'labeltxt', xm)
    if os.path.exists(img_path) and os.path.exists(xml_path):
        os.remove(img_path)
        os.remove(xml_path)
        print(j, ' ', img_name, 'have deleted!')
    else:
        print(j, ' ', img_name, 'didnot found!')
        break


# 尝试删除文件
# src_path = 'D:/competition/crop_dataset/without_big_train/*.xml'
# img_path_list = glob.glob(src_path)
# print(len(img_path_list))
# for i, im in enumerate(img_path_list):
#     if os.path.getsize(im) < 588311:
#         os.remove(im)
# img_path_list = glob.glob(src_path)
# print(len(img_path_list))