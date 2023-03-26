import pygame.font


class Button:

    def __init__(self, ai_game, msg):
        """Initialization of button attributes"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect_x = self.screen.get_rect()
        self.screen_rect_y = self.screen.get_rect()
        self.width, self.height = 200, 50
        self.screen_rect_x.x = (self.settings.screen_width - self.width) / 2
        self.screen_rect_y.y = (self.settings.screen_height - self.height + 210) / 2

        # Set the dimensions and properties of the button
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create rect  button object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = self.screen_rect_x.x
        self.rect.y = self.screen_rect_y.y

        # Message on button show once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Transform the text on image place it in the center of button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw empty button, and then -- message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


