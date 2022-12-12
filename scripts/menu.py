import pygame
from objeto import Obj
import os
import json
import sys


path = f"parameters/requeriments.json"

param=open(path)
data = param.read()
content = json.loads(data)

bg = content["bg"]
aranha = content["aranha"]
flor = content["flor"]
abelha = content["abelha"]
assets = content["assets"]



class Menu:
    def __init__(self, image):
        self.bg = Obj(image, 0, 0)
        self.change_scene = False

    def draw(self, window):
        self.bg.group.draw(window)

    def events(self, event):
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RETURN:
               self.change_scene = True


class FimdeJogo(Menu):
    def __init__(self, image):
        super().__init__(image)

class Vitoria(Menu):
    def __init__(self, image) :
        super().__init__(image)
