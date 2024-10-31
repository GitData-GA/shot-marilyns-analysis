# Decoding "Shot Marilyns" - Warhol's Color Language

Shot Marilyns Analysis

## Description

The vibrant world of Andy Warhol's Shot Marilyns reveals how color becomes a powerful language that speaks to the viewer's emotions. Our research explores how Warhol transformed a single iconic image into five distinct masterpieces. By analyzing color composition and distribution using techniques like relative conditional entropy, we uncovered intricate relationships between colors in key regions, including backgrounds, hair, eyeshadow, and face.

## Reproduce the analysis

### Option 1: Docker (Recommended)

#### Step 1: Download the `main` branch of this repository.

- Method 1: Use Git command

  ```cmd
  git clone https://github.com/GitData-GA/shot-marilyns-analysis.git shot-marilyns-analysis-main
  ```

- Method 2: Download from GitHub and unzip the zip file

  https://github.com/GitData-GA/shot-marilyns-analysis/archive/refs/heads/main.zip

#### Step 2: In your terminal, switch driectory to `shot-marilyns-analysis-main`

#### Step 3: Make a directory for analysis plots, build Docker image, start Docker container, and run the script

```cmd
mkdir img; docker build -t shot-marilyns-analysis .; docker run -it --rm -v "$(pwd)/img:/img" shot-marilyns-analysis
```

#### Step 4: The analysis log will be shown in the terminal, and all the output plots are in the folder `shot-marilyns-analysis-main/img`

### Option 2: Google Colaboratory

Simply click on the following button to open the Jupyter notebook in Google Colaboratory.

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GitData-GA/shot-marilyns-analysis/blob/main/main.ipynb)
