from MTM import matchTemplates, drawBoxesOnRGB
import os
import cv2
import matplotlib.pyplot as plt

threshold=0.975
proj_path = "c:/Users/igors/Downloads/ancient"

def get_templates(ids, path_prefix):
    listTemplate = list()
    for id in ids:
        try:
            small = cv2.imread(path_prefix + os.sep + id + ".png")
            listTemplate.append((id, small.copy()))
        except:
            pass
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

    ids = list()
    for i in range(2):
        for j in range(19):
            for k in range(9):
                ids.append(str(i) + "." + str(j) + "." + str(k))

    search_and_draw_templates(get_templates(ids, path_prefix), image, threshold)