from MTM import matchTemplates, drawBoxesOnRGB
import os
import cv2
import matplotlib.pyplot as plt

threshold=0.975
proj_path = "c:/Users/igors/source/repos/xmas_ctf_ancient_text"

max_article_columns = 2
max_rows = 18
max_character_columns = 9

def get_templates(ids, path_prefix):
    listTemplate = list()
    for id in ids:
        try:
            small = cv2.imread(path_prefix + os.sep + id + ".png")
            listTemplate.append((id, small.copy()))
        except:
            print("file with the given ID not found, skipping...")
    return listTemplate


def search_and_draw_templates(templates, image, threshold):
    Hits = matchTemplates(templates, image, score_threshold=threshold, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0)

    print("Found {} hits".format(len(Hits.index)))
    print(Hits)

    Overlay = drawBoxesOnRGB(image, Hits, showLabel=True, labelColor=(255,0,0), boxColor=(255,0,0))
    plt.imshow(Overlay)
    plt.show()


if __name__ == '__main__':
    image = cv2.imread(proj_path + os.sep + "ancient_text.png")
    path_prefix = proj_path + os.sep + "small"

    ids = [str(i) + "." + str(j) + "." + str(k) for i in range(max_article_columns) for j in range(max_rows) for k in range(max_character_columns)]

    search_and_draw_templates(get_templates(ids, path_prefix), image, threshold)