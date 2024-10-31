# Decoding "Shot Marilyns" - Warhol's Color Language

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

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GitData-GA/shot-marilyns-analysis/blob/main/main.ipynb)
