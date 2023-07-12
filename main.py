import pygame
import math
import config
import draw_text


class App:
  def __init__(self):
    pygame.init()

    self.screen = pygame.display.set_mode(config.SCREEN_SIZE)
    self.clock = pygame.time.Clock()
    self.running = True
    self.frame = 0

    self._load_assets()


  def run(self):
    while self.running:
      # イベント処理
      self._dispatch_events()

      # ゲームの描画処理
      self._draw()

      # 描画内容を画面に転送
      pygame.display.flip()

      # FPS制御
      self.clock.tick(60)

      self.frame += 1


  def _load_assets(self):
    self.fonts = { 'message': pygame.font.Font('fonts/JF-Dot-MPlus10.ttf', 20) }


  def _dispatch_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False


  def _draw(self):
    # スクリーンをクリア
    self.screen.fill((32, 32, 32))

    # 画面の中央にメッセージを表示する
    color = (255, 255 - 32 * (math.floor(self.frame / 2) % 2), 255)
    message = 'これはpygameでフォント描画をするサンプルです.'
    draw_text.draw_text_center(self.screen, message, self.fonts['message'], color)


def main():
  app = App()
  app.run()


if __name__ == '__main__':
  main()
