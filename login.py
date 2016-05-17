import yaml
from autopy import key, screen, mouse
import os
import time

class Login:
    def __init__(self):
        self.config = yaml.load(open('settings.yaml'))
        self.screen_size = screen.get_size()

    def open_qq(self):
        qq_path = self.config['qq_path']
        os.startfile(qq_path)

    def double_click_qq_input_text_box(self):
        mouse.move(self.screen_size[0] / 2, self.screen_size[1] / 2 + 49)
        mouse.click()


    def double_click_passwd_input_text_box(self):
        mouse.move(self.screen_size[0] / 2, self.screen_size[1] / 2 + 76)
        mouse.click()

    def login(self):
        for k, v in self.config.items():
            if k == 'qq_path':
                continue
            self.open_qq()
            time.sleep(7)
            self.double_click_qq_input_text_box()
            time.sleep(1)
            key.tap(key.K_SHIFT)
            key.type_string(k)
            key.type_string('\t')

            self.double_click_passwd_input_text_box()
            key.tap(key.K_SHIFT)
            time.sleep(1)
            key.type_string(v)
            key.tap(key.K_RETURN)

            time.sleep(7)
        
if __name__ == '__main__':
    l = Login()
    l.login()
