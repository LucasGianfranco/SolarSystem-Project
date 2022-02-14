import random
import ursina as ur
import numpy as np

class OrbitalInfo:
    def __init__(self):
        self.orbitalTheta = random.randint(0, 360)
        self.orbitalVel = 0.01
        self.solarDist = 5

    def set_orbital_theta(self, x):
        self.orbitalTheta = x

    def get_orbital_theta(self):
        return self.orbitalTheta

    def get_orbital_vel(self):
        return self.orbitalVel

    def get_solar_dist(self):
        return self.solarDist

app = ur.Ursina()

orbital_info = OrbitalInfo()

ur.window.borderless = False
ur.window.title = 'Solar system'
ur.window.exit_button.visible = True

ost = ur.Audio(sound_file_name='misc/ost.mp3', autoplay=True, auto_destroy=False)

earth = ur.Entity(model='sphere', scale=(2,2,2), texture='misc/8k_earth')
moon = ur.Entity(model='sphere', scale=(1,1,1), texture='misc/2k_moon')

earth.position = ur.Vec3(0,0,0)

moon.position = ur.Vec3(3,3,3)

def update():

    t = orbital_info.get_orbital_theta() 
    s = orbital_info.get_solar_dist()
    ov = orbital_info.get_orbital_vel()

    # print(t, s, ov)

    moon.position = ur.Vec3(s * np.cos(t) * 1.4, moon.Y, s * np.sin(t))

    # moon.X = s * np.cos(t) * 1.4
    # moon.Z = s * np.sin(t)
    orbital_info.set_orbital_theta(t + ov)

    print(moon.X, moon.Z)

    moon.rotation_y += ur.time.dt * 10
    earth.rotation_y += ur.time.dt * 10
    if ur.held_keys['space']:
        ur.camera.position += (0, ur.time.dt, 0)
    if ur.held_keys['left control']:
        ur.camera.position -= (0, ur.time.dt, 0)
    if ur.held_keys['d']:
        ur.camera.position += (ur.time.dt, 0, 0)
    if ur.held_keys['a']:
        ur.camera.position -= (ur.time.dt, 0, 0)
    if ur.held_keys['w']:
        ur.camera.position += (0, 0, ur.time.dt)
    if ur.held_keys['s']:
        ur.camera.position -= (0, 0, ur.time.dt)

app.run()

def main():
    pass

if __name__ == '__main__':
    main()

