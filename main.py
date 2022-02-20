import decimal as dec
import random
from turtle import color
from xml.dom.minidom import Entity
import ursina as ur
import numpy as np
from ursina.prefabs.first_person_controller import FirstPersonController

class OrbitalInfo:
    def __init__(self):
        self.orbitalTheta = random.randint(0, 360)
        self.orbitalVel = 0.01
        self.solarDist = 3

    def get_theta(self):
        return self.orbitalTheta

    def set_theta(self, x):
        self.orbitalTheta = x

    def get_orbital_vel(self):
        return self.orbitalVel

    def get_dist(self):
        return self.solarDist

    def set_dist(self, x):
        self.solarDist = x

app = ur.Ursina()

orbital_info = OrbitalInfo()

global switch

switch = True

ur.window.borderless = False
ur.window.title = 'Solar system'
ur.window.exit_button.visible = True

ost = ur.Audio(sound_file_name='misc/ost.mp3', autoplay=True, auto_destroy=False)

sun = ur.Entity(model='sphere', scale=(5,5,5), texture='misc/2k_sun')
earth = ur.Entity(model='sphere', scale=(2,2,2), texture='misc/8k_earth')
moon = ur.Entity(model='sphere', scale=(0.1,0.1,0.1), texture='misc/2k_moon')

sun.position = ur.Vec3(0, 0, 0)
earth.position = ur.Vec3(10,0,10)
moon.position = ur.Vec3(3,3,3)

orbital_info.set_dist(earth.x)

player = FirstPersonController()
player.gravity = 0
# ur.camera.fov = 90

lista = []

def input(key):
    if key == 'escape':
        if player.enabled:
            player.disable()
        else:
            player.enable()

def update():

    t = orbital_info.get_theta()
    s = orbital_info.get_dist()
    ov = orbital_info.get_orbital_vel()

    moon.position = ur.Vec3(s * np.cos(t) * 1.4, 0, s * np.sin(t))

    trace = ur.Entity(model='cube', scale=(0.01,0.01,0.01), color=ur.color.white, texture=None)

    trace.position = moon.position

    lista.append(trace)

    index = int(ur.time.time() % 100)

    if len(lista) > 500:
        ur.destroy(lista.pop(0))


    # print(trace.position, lista)

    # moon.X = s * np.cos(t) * 1.4
    # moon.Z = s * np.sin(t)
    orbital_info.set_theta(t + ov)

    moon.rotation_y += ur.time.dt * 10
    sun.rotation_y += ur.time.dt * 10
    earth.rotation_y += ur.time.dt * 50

    player.position =  ur.Vec3(player.position.x , player.position.y + ur.held_keys['space'] * ur.time.dt * 8, player.position.z)
    player.position =  ur.Vec3(player.position.x , player.position.y - ur.held_keys['left control'] * ur.time.dt * 8, player.position.z)
    

app.run()

def main():
    pass

if __name__ == '__main__':
    main()

