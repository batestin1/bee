import pygame
from objeto import Obj
from menu import Menu, FimdeJogo, Vitoria
from jogo import Jogo
import asyncio
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
start = content["start"]
over = content["over"]
vitoria = content["vitoria"]





class Main :
    pygame.init()

    def __init__(self, sizex, sizey, title) :


        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)
        self.menu = Menu(start)
        self.jogo = Jogo()
        self.loop = True
        self.fps = pygame.time.Clock()
        self.gameover = FimdeJogo(over)
        self.vitoria = Vitoria(vitoria)

    def draw(self):

        if not self.menu.change_scene:
            self.menu.draw(self.window)

        elif not self.jogo.change_scene:
            self.jogo.draw(self.window)
            self.jogo.update()

        elif not self.gameover.change_scene:
            self.gameover.draw(self.window)

        elif not self.vitoria.change_scene:
            self.vitoria.draw(self.window)

        else :
            self.menu.change_scene = False
            self.jogo.change_scene = False
            self.gameover.change_scene = False
            self.vitoria.change_scene = False
            self.jogo.abelha.life = 5
            self.jogo.abelha.pontos = 0

    def events(self) :
        for events in pygame.event.get() :
            if events.type == pygame.QUIT :
                self.loop = False
            if not self.menu.change_scene :
                self.menu.events(events)
            elif not self.jogo.change_scene :
                self.jogo.abelha.move_abelha(events)

            else :
                self.gameover.events(events)

    def update(self) :
        while self.loop :
            self.fps.tick(30)
            self.draw()
            self.events()
            pygame.display.update()

game = Main(360, 640, "BEE")
#asyncio.run(game.update())
game.update()
