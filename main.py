import ursina as ur


app = ur.Ursina()

ur.window.borderless = False
ur.window.title = 'Solar system'
ur.window.exit_button.visible = True

ost = ur.Audio(sound_file_name='misc/ost.mp3', autoplay=True, auto_destroy=False)

sun = ur.Entity(model='sphere', color=ur.color.yellow, scale=(2,2,2), texture='misc/2k_sun')

def update():
    sun.rotation_y += ur.time.dt * 10

app.run()

def main():
    pass

if __name__ == '__main__':
    main()

