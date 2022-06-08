import pygame
class button:
    def __init__(self, text, font_size, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font_size = font_size
        while 1:
            font =  pygame.font.Font("PokemonGB.ttf", self.font_size)
            x, y = pygame.font.Font.size(font, self.text)
            if x > self.width:
                self.font_size -= 1
            if x <= self.width:
                break

    def draw_button(self, display, text_color):
        font = pygame.font.Font("PokemonGB.ttf", self.font_size)
        draw = font.render(self.text, False, text_color)
        pygame.draw.rect(display, self.color, self.rect)
        display.blit(draw, (self.x + 3, self.y + self.heigth/2.7))        

    def update(self, event, display, active):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                pygame.draw.rect(display, active, self.rect)
                pygame.display.flip()
                pygame.time.wait(200)
                return True