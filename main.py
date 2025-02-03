#Django text to speach
import pygame
import random
from tkinter import Tk, simpledialog
from playsound import playsound
import os

# تنظیمات اولیه pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("AI Art Creator")
clock = pygame.time.Clock()
# رنگ‌های تصادفی
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# رسم اشکال هندسی
def draw_shape(shape_type, x, y):
    color = random_color()
    size = random.randint(20, 100)
    if shape_type == "circle":
        pygame.draw.circle(screen, color, (x, y), size)
    elif shape_type == "square":
        pygame.draw.rect(screen, color, (x, y, size, size))
    elif shape_type == "line":
        pygame.draw.line(screen, color, (x, y), (x + size, y + size), 5)
# حلقه اصلی
def main():
    running = True
    shapes = ["circle", "square", "line"]
    # رابط برای دریافت متن از کاربر
    root = Tk()
    root.withdraw()
    user_input = simpledialog.askstring("AI Art", "What pattern do you want? (e.g., star, rain, wave)")
    # پخش صدای ورود
   # playsound("start.mp3")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                shape_type = random.choice(shapes)
                draw_shape(shape_type, x, y)

        pygame.display.flip()
        clock.tick(60)

    # ذخیره نقاشی
    pygame.image.save(screen, "ai_art.png")
    print("Your art has been saved as 'ai_art.png'!")
    pygame.quit()


if __name__ == "__main__":
    main()
