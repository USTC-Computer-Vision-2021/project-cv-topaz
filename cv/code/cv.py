import cv2, pygame, sys

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
            
            result = cv2.matchTemplate(target , temp, cv2.TM_SQDIFF_NORMED,-1)
            cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            screen.blit(day_img, (0, 0)) 
            screen.blit(night_img, (x-200, y-200), pygame.Rect(min_loc[0], min_loc[1], 400, 400))
    
            pygame.display.flip()
