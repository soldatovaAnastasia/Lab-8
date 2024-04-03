import numpy as np
import cv2 

def add_noise():  # Определяем вместе с пользователем коэффициент шума
    noise_multiplier = int(input('Введите коэффициент для желаемого шума (1-99): '))
    if noise_multiplier > 99: 
        noise_multiplier = 0.99  
    elif noise_multiplier < 1: 
        noise_multiplier = 0.01 
    else: 
        noise_multiplier /= 100 

    img = cv2.imread(r'variant-5.jpg', cv2.IMREAD_COLOR)
    image_arr = np.array(img/255, dtype=float)
    noise_arr = np.random.normal(0, noise_multiplier, img.shape)  # Генерируем случайный шум

    image_final = image_arr + noise_arr  # Добавляем сгенерированный шум к изображению

    cv2.imshow(f'Noise {noise_multiplier}', image_final)  # Изображение с добавленным шумом
    cv2.waitKey(0)

#Модификация кода из п2
def circle_tracking():  
    video = cv2.VideoCapture(r'sample.mp4')
    detector = cv2.createBackgroundSubtractorMOG2(history=100)

    # Ищем контуры
    while True:
        rat, frame = video.read() 
        mask = detector.apply(frame)
        _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        object_contour, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #Проверяем контур и рисуем круги
        for countur in object_contour: 
            area = cv2.contourArea(countur) 
            if area > 450: 
                (x, y), r = cv2.minEnclosingCircle(countur) 
                center = (int(x), int(y))  
                r = int(r) 
                if center[0] < 250 and center[1] < 210: 
                    cv2.circle(frame, center, r, (255, 0, 0), 3) 
                elif center[0] > 340 and center[1] > 300:  
                    cv2.circle(frame, center, r, (0, 0, 255), 3) 
                else: 
                    cv2.circle(frame, center, r, (0, 0, 0), 3) 
         
        # Отображаем кадр с обнаруженными кругами
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(30)  
        if key == 27:  
            break  

    video.release() 
    cv2.destroyAllWindows() 

add_noise() 
circle_tracking()