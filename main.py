import os
import shutil
import sys
import numpy as np
sys.path.insert(0, './src')
import sma
os.makedirs(r'img', exist_ok=True)


# Improt images and prepare data
# Source code of used functions in this section:
# - sma.utils.save_img: https://github.com/GitData-GA/shot-marilyns-analysis/blob/main/src/sma/utils/save_img.py
# - sma.utils.np_convert: https://github.com/GitData-GA/shot-marilyns-analysis/blob/main/src/sma/utils/np_convert.py
# - sma.utils.pd_convert: https://github.com/GitData-GA/shot-marilyns-analysis/blob/main/src/sma/utils/pd_convert.py
img_links = {
    "orange_marilyn": "data/1_1_orange_marilyn.jpg",
    "red_marilyn": "data/1_2_red_marilyn.jpg",
    "turq_marilyn": "data/1_3_turq_marilyn.jpg",
    "blue_marilyn": "data/1_4_blue_marilyn.jpg",
    "sageblue_marilyn": "data/1_5_sageblue_marilyn.jpg"
}

# Save images to local directory
sma.utils.save_img(img_links=img_links, img_idx=1, verbose=True)

# Store the images as a dictionary of 5 NumPy arraies
np_img = sma.utils.np_convert(img_links=img_links)
     
# Store the images as a dictionary of 5 Pandas dataframes with HEX codes
pd_img = sma.utils.pd_convert(np_img=np_img)

# Visualization
# Source code of used functions in this section:
# - sma.plot.distribution: https://github.com/GitData-GA/shot-marilyns-analysis/blob/main/src/sma/plot/distribution.py
# - sma.plot.entropy_heatmap: https://github.com/GitData-GA/shot-marilyns-analysis/blob/main/src/sma/plot/entropy_heatmap.py
# - sma.plot.scatter: https://github.com/GitData-GA/shot-marilyns-analysis/blob/main/src/sma/plot/scatter.py
# - sma.cluster.kmeans: https://github.com/GitData-GA/shot-marilyns-analysis/blob/main/src/sma/cluster/kmeans.py
# - sma.plot.bar: https://github.com/GitData-GA/shot-marilyns-analysis/blob/main/src/sma/plot/bar.py
# - sma.plot.ribbon: https://github.com/GitData-GA/shot-marilyns-analysis/blob/main/src/sma/plot/ribbon.py

# Distribution plots
sma.plot.distribution(np_img=np_img, img_idx=2, verbose=True)
     
# Relative conditional entropy plots
sma.plot.entropy_heatmap(np_img=np_img, img_idx=3, output_format="jpg", verbose=True)
     
# RGB space scatterplots
sma.plot.scatter(pd_img=pd_img, img_idx=4, verbose=True)
     
# KMeans clustering
kmean_result = sma.cluster.kmeans(pd_img=pd_img, n_clusters=15)
     
# Bar chart by clusters
sma.plot.bar(pd_img=pd_img, img_idx=5, kmeans=kmean_result, verbose=True)
     
# Color ribbon by clusters
sma.plot.ribbon(pd_img=pd_img, img_idx=6, kmeans=kmean_result, verbose=True)

# Region of interest
# Source code of used functions in this section:
# sma.roi.extract: https://github.com/GitData-GA/shot-marilyns-analysis/blob/main/src/sma/roi/extract.py

# Extraction
roi = {}
param = {
    "orange_marilyn": [
        ("7_1", "background", "sampling", [(0, 100, 0, 100)], None),
        ("7_2", "hair", "sampling", [(100, 150, 300, 400)], None),
        ("7_3", "eyeshadow", "sampling", [(460, 490, 450, 550)], None),
        ("7_4", "face", "sampling", [(300, 418, 300, 610)], None)
    ],
    "red_marilyn": [
        ("8_1", "background", "sampling", [(0, 960, 0, 30), (0, 960, 930, 960)], (690, 800, 275, 475)),
        ("8_2", "hair", "sampling", [(10, 200, 300, 380), (10, 200, 440, 520)], None),
        ("8_3", "eyeshadow", "sampling", [(455, 480, 455, 520)], None),
        ("8_4", "face", "sampling", [(280, 460, 310, 435)], None)
    ],
    "turq_marilyn": [
        ("9_1", "background", "sampling", [(0, 960, 0, 40), (0, 960, 930, 970)], None),
        ("9_2", "hair", "exact", [(19, 101, 70), (28, 255, 255)], None),
        ("9_3", "eyeshadow", "sampling", [(470, 490, 300, 320), (470, 490, 500, 550)], None),
        ("9_4", "face", "exact", [(0, 0, 0), (17, 100, 255)], None)
    ],
    "blue_marilyn": [
        ("10_1", "background", "sampling", [(0, 145, 0, 145)], None),
        ("10_2", "hair", "sampling", [(45, 200, 485, 590)], None),
        ("10_3", "eyeshadow", "sampling", [(470, 490, 300, 320)], (600, 960, 600, 800)),
        ("10_4", "face", "exact", [(110, 40, 0), (255, 255, 255)], None),
    ],
    "sageblue_marilyn": [
        ("11_1", "background", "exact", [(76, 31, 178), (88, 61, 210)], None),
        ("11_2", "hair", "exact", [(12, 60, 60), (27, 181, 232)], None),
        ("11_3", "eyeshadow", "sampling", [(460, 480, 470, 500)], (600, 960, 600, 800)),
        ("11_4", "face", "exact", [(110, 40, 0), (255, 255, 255)], None),
    ]
}

for key, value in param.items():
    single_roi = {}
    for param in value:
        single_roi[f"{key}_{param[1]}"] = sma.roi.extract(
            np_img=np_img,
            key=key,
            img_idx=param[0],
            extraction_name=param[1],
            param={"method": param[2], "value": param[3]},
            fix=param[4],
            verbose=True
        )
    roi[key] = single_roi

# Plots
img_idx = 11
for key, value in roi.items():
    pd_img_roi = {k: v[v['hex'] != '#000000'] for k, v in sma.utils.pd_convert(value).items()}
    kmeans_roi = sma.cluster.kmeans(pd_img_roi, n_clusters=15)
    sma.plot.bar(pd_img=pd_img_roi, img_idx=img_idx + 1, kmeans=kmeans_roi, verbose=True)
    sma.plot.ribbon(pd_img=pd_img_roi, img_idx=img_idx + 1, kmeans=kmeans_roi, verbose=True)
    img_idx += 1

# Gun shot repair for Blue Marilyn
# Source code of used functions in this section:
# - sma.roi.knn_repair: https://github.com/GitData-GA/shot-marilyns-analysis/blob/main/src/sma/roi/knn_repair.py
# - sma.plot.inset: https://github.com/GitData-GA/shot-marilyns-analysis/blob/main/src/sma/plot/inset.py
# - sma.plot.knn_demo: https://github.com/GitData-GA/shot-marilyns-analysis/blob/main/src/sma/plot/knn_demo.py
blue_marilyn_repair = sma.roi.knn_repair(
    np_img = np_img,
    key="blue_marilyn",
    img_idx="17_1",
    n_neighbors=8,
    start_col=410,
    end_col=450,
    start_row=375,
    end_row=430,
    damaged_pixel=[415, 425],
    verbose=True
)

# KNN Demo of pixel at [415, 425]
sma.plot.knn_demo(
    img_idx=18,
    neighbor_colors=np.array([
        [226, 158, 179],
        [226, 158, 179],
        [222, 154, 177],
        [224, 156, 177],
        [222, 154, 177],
        [223, 155, 178],
        [221, 153, 174],
        [224, 156, 177],
    ]),
    damaged_color=np_img["blue_marilyn"].reshape(960, 960, 3)[415, 425],
    fixed_color=blue_marilyn_repair.reshape(960, 960, 3)[415, 425],
    distances=np.array([5.0, 5.099, 5.099, 5.385, 5.385, 5.831, 5.831, 6.0]),
    width=15,
    height=4,
    output_format="pdf",
    verbose=True,
)

# Blue Marilyn Zoom In (Original)
sma.plot.inset(
    img_path="img/1_4_blue_marilyn.jpg",
    img_idx=19,
    start_col=410,
    end_col=450,
    start_row=375,
    end_row=430,
    position=[0.88, 0.5, 1, 0.5],
    hide_axes=True,
    verbose=True,
)

# Save all images in a zip file
shutil.make_archive("img.zip".replace('.zip', ''), 'zip', 'img')
