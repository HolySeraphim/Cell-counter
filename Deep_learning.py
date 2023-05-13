def build_annot(file):
    from xml.etree import ElementTree
    tree = ElementTree.parse(file)
    root = tree.getroot()
    x_min = list()
    x_max = list()
    y_min = list()
    y_max = list()
    for box in root.findall('.//bndbox'):
        x_min.append(int(box.find('xmin').text))
        y_min.append(int(box.find('ymin').text))
        x_max.append(int(box.find('xmax').text))
        y_max.append(int(box.find('ymax').text))
    my_classes = list()
    my_images = list()
    for name in root.findall('.//object'):
        my_classes.append(name.find('name').text)
        my_images.append('train/' + root.findall('.//filename')[0].text)

    annot_df = pd.DataFrame({'Image': my_images,'xmin': x_min, 'xmax': x_max,
                             'ymin': y_min, 'ymax': y_max,
                             'Class': my_classes})
    return annot_df


import os
import pandas as pd

annot_df = pd.DataFrame()
for i in os.listdir('C:/Users/palpa/Desktop/Death/MIPT/ICT/Algorithms_bioinformatics/Cell_counter/tryphoto/Fluorescent-E/annot/'):
    annot_df = pd.concat([annot_df, build_annot('C:/Users/palpa/Desktop/Death/MIPT/ICT/Algorithms_bioinformatics/Cell_counter/tryphoto/Fluorescent-E/annot/'
                                                + str(i))], ignore_index=True)
annot_df.to_csv('C:/Users/palpa/Desktop/Death/MIPT/ICT/Algorithms_bioinformatics/Cell_counter/tryphoto/Fluorescent-E/annot/annot.txt', header=False, index=False, sep=',')