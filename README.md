[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6629874&assignment_repo_type=AssignmentRepo)
# 基于图像拼接技术实现A Look Into the Past
* 刘俞伶（PB18061301）
## 问题描述
* 我们试图将同一地点不同时期的两张照片匹配拼接，下面是我们使用到的两组示例图片。 
* 森林的早晨
[![day.jpg](https://i.postimg.cc/JhskHgk4/day.jpg)] 
* 森林的夜晚
[![night.jpg](https://i.postimg.cc/cHYtXnhp/night.jpg)]


 
## 原理分析
通过计算平方误差来对两图片进行位置配准。  
#### NMSE算法原理简介：
* 模板匹配的是一种非常实用的方法。Opencv中集成了一个模板匹配算法，调用cv2.matchtemplate函数就可以实现该功能。但是只能匹配到与目标一样大小的区域，即适用的条件为：被匹配对象与模板大小相同，角度一致。其中“归一化相关系数匹配法”效果相对更好。
* 评估图像的归一化均方误差 (NMSE) 作为滤波过程中去噪有效性和图像结构/细节保留的度量。 归一化均方误差是一种基于能量归一化的测量方法，它相对均方误差是将分母的大小变成了原始图像的各个像素的平方和。值越小表示图像质量越好。（在这种情况下，NMSE = 0）。


## 代码实现
代码实现主要分为两部分，一部分是显示图片，把前景图和背景图显示在屏幕上，并能根据鼠标位置动态调整。  
```python
X, Y = (1920,965)#图片长宽比

pygame.init()
screen = pygame.display.set_mode((X,Y)) 
pygame.display.set_caption('lookintopast')
day_img = pygame.image.load("..\\images\\day.jpg").convert()
night_img = pygame.image.load("..\\images\\night.jpg").convert_alpha()
day = cv2.imread("..\\images\\day.jpg")
night = cv2.imread("..\\images\\night.jpg")
screen.blit(day_img, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            
            x, y = event.pos
            x=max(x,200)
            y=max(y,200)
            x=min(X-1-200,x)
            y=min(Y-1-200,y)
            
            target = day[:]
            temp = night[y-200:y+200, x-200:x+200]
```  
另一部分则是匹配，即找出当前鼠标选中区域在另一张图中对应的范围。
```python
           result = cv2.matchTemplate(target , temp, cv2.TM_SQDIFF_NORMED,-1)
            cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            screen.blit(day_img, (0, 0)) 
            screen.blit(night_img, (x-200, y-200), pygame.Rect(min_loc[0], min_loc[1], 400, 400))
    
            pygame.display.flip()

```
## 效果展示
如下所示：
* [![1.jpg](https://i.postimg.cc/rwxSf7pn/1.png)] 
* [![2.jpg](https://i.postimg.cc/vH69mC5Y/2.png)] 
* [![3.jpg](https://i.postimg.cc/0jhwfC11/3.png)] 
* [![4.jpg](https://i.postimg.cc/ZYQp4JBs/4.png)] 
* [![5.jpg](https://i.postimg.cc/j5gNWb85/5.png)]
* [![6.jpg](https://i.postimg.cc/rF6sfstT/6.png)]

## 工程结构  
    ├─code
    │   └─main.py
    ├─images
    │   ├─bg.jpg(before image)
    │   └─fg.jpg(after image)
    └─result   

## 运行说明
* version  
    python3.9.7  
    pygame2.1.2  
    opencv4.5.3  
* install  
    conda config --add channels conda-forge  
    conda install pygame  
    conda install opencv  
    python cv.py  ##运行
