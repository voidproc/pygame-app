import pygame

def draw_text_center(surface_dest: pygame.Surface, text: str, font: pygame.font.Font, color: pygame.Color | None = None):
  text_surface = font.render(text, False, color)
  text_width, text_height = text_surface.get_size()
  draw_pos = (surface_dest.get_width() / 2 - text_width / 2, surface_dest.get_height() / 2 - text_height / 2)
  surface_dest.blit(text_surface, draw_pos)
