# Clothe Color Recognition

## Dataset Folder Structure
- Folder
  -  CLASS_1/
    [IMAGES]
  -  CLASS_2/
    [IMAGES]
  -  CLASS_3/
    [IMAGES]
  -  .../
    [IMAGES]
    
## TEST DATA
https://www.kaggle.com/dqmonn/zalando-store-crawl/download

## How To Run
1. Download COLORS.csv file for determining colors. Also you can use another colors csv file which has columns ["Name","Red (8 bit)","Green (8 bit)","Blue (8 bit)"]
- https://drive.google.com/file/d/1E4EZ-p4chwM4ASxASLgrJo8tLeiOa64U/view?usp=sharing
2. Install requirements with code below:
- ``` pip install -r requirements.txt ```
3. Run main.py. This script determines image's background color.
- ```python main.py -i/--image [IMAGE_PATH] -c/--colors [COLOR_CSV]```

## An Example

![Query Image](https://github.com/Burak-Tasci/Clothe-color-segmentation/blob/main/images/img_screenshot_17.11.2021.png)
