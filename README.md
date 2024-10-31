# Decoding "Shot Marilyns" - Warhol's Color Language

![](https://shotmarilyns.gd.edu.kg/assets/images/background.jpg)

*© 2024 The Andy Warhol Foundation for the Visual Arts, Inc.*

## Overview

Andy Warhol's *Shot Marilyns* showcases how color serves as a powerful language, evoking emotions and responses from viewers. Our research delves into how Warhol transformed a single iconic image into five distinct masterpieces. By analyzing color composition and distribution, particularly through methods like relative conditional entropy, we reveal intricate relationships among colors in key areas such as backgrounds, hair, eyeshadow, and face.

## How to Reproduce the Analysis

### Option 1: Using Docker (Recommended)

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

#### Step 3: Prepare for Analysis

Run the following commands to create a directory for the analysis plots, build the Docker image, start the Docker container, and execute the analysis script:

```bash
mkdir img
docker build -t shot-marilyns-analysis .
docker run -it --rm -v "$(pwd)/img:/img" shot-marilyns-analysis
```

#### Step 4: Review the Results

The analysis log will be displayed in the terminal, and all output plots will be saved in the `img` folder within `shot-marilyns-analysis-main`.

### Option 2: Using Google Colaboratory

For an easier setup, you can run the analysis in Google Colaboratory. Click the button below to open the Jupyter notebook in Google Colaboratory.

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GitData-GA/shot-marilyns-analysis/blob/main/main.ipynb)

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
