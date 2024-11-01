# Decoding "Shot Marilyns" - Warhol's Color Language

*Last update: 11/01/2024*

![](https://shotmarilyns.gd.edu.kg/assets/images/background.jpg)

*Image source: [The Interior Review](https://www.theinteriorreview.com/story/2022/5/10/critically-assessing-warhols-shot-sage-blue-marilyn?srsltid=AfmBOorNDV0MYlOhOPaHxqHTWfbINkbTNX-h4POd1SvoCzc569K7Swau)*

## Overview

Andy Warhol's *Shot Marilyns* showcases how color serves as a powerful language, evoking emotions and responses from viewers. Our research delves into how Warhol transformed a single iconic image into five distinct masterpieces. By analyzing color composition and distribution, particularly through methods like relative conditional entropy, we reveal intricate relationships among colors in key areas such as backgrounds, hair, eyeshadow, and face.

Detail about this research: https://shotmarilyns.gd.edu.kg/

### Authors

| Name           | Institution                                  | Email                           |
|----------------|----------------------------------------------|---------------------------------|
| Hengyuan Liu   | University of California, Los Angeles        | `hengyuanliu[at]ucla[dot]edu`     |
| Li Yuan       | Swiss Federal Institute of Technology, Zurich | `liyuan1[at]ethz[dot]ch`          |
| Kathy Mo      | University of California, Los Angeles         | `kathymo24[at]ucla[dot]edu`       |
| Xinhui Luo    | Tufts University                              | `xinhui.luo[at]tufts[dot]edu`     |
| Weilin Cheng  | University of California, Davis               | `wncheng[at]ucdavis[dot]edu` |
| Erick Arenas  | University of California, Davis               | `esarenas[at]ucdavis[dot]edu` |


## How to Reproduce the Analysis

### Option 1: Using Google Colaboratory (the easist way)

For an easier setup, you can run the analysis in Google Colaboratory. Click the button below to open the Jupyter notebook in Google Colaboratory.

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GitData-GA/shot-marilyns-analysis/blob/main/main.ipynb)

### Option 2: Using Docker (the most stable way)

#### Step 1: Download the Repository

You can download the repository in two ways:

- **Using Git Command:**

  ```bash
  git clone https://github.com/GitData-GA/shot-marilyns-analysis.git shot-marilyns-analysis-main
  ```

- **Direct Download:**

  Download the ZIP file from GitHub and unzip it:

  [Download](https://github.com/GitData-GA/shot-marilyns-analysis/archive/refs/heads/main.zip)

#### Step 2: Navigate to the Directory

Open your Docker terminal and change to the shot-marilyns-analysis-main directory:

```bash
cd shot-marilyns-analysis-main
```

Your path might be different.

#### Step 3: Prepare for Analysis

Run the following commands to create a directory for the analysis plots, build the Docker image, start the Docker container, and execute the analysis script:

```bash
mkdir img; docker build -t shot-marilyns-analysis .; docker run -it --rm -v "$(pwd)/img:/img" shot-marilyns-analysis
```

#### Step 4: Review the Results

The analysis log will be displayed in the terminal, and all output plots will be saved in the `img` folder within `shot-marilyns-analysis-main`.

## Computational Detail

**Operating System**: Ubuntu 22.04.3 LTS.

**CPU Information**: Intel(R) Xeon(R) CPU @ 2.20GHz, 2 cores

**Memory**: Recommended at least 4GB.

**Python Version**: Python 3.10.12.

**Python packages and versions**:

- `matplotlib==3.7.1`
- `networkx==3.4.2`
- `numpy==1.26.4`
- `opencv-python==4.10.0.84`
- `pandas==2.2.2`
- `pytz==2024.2`
- `requests==2.32.3`
- `scikit-image==0.24.0`
- `scikit-learn==1.5.2`
