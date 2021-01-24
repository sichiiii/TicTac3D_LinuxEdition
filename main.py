from ursina import *

app = Ursina()

#tutorial
Text(text='Каждая цифра на нампаде соотвествует клетке \nСменить вид:Q\W', y=.25, z=-1, scale=1, origin=(0,0))

#access 
acc = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
arr = ['1','2', '3', '4', '5','6', '7', '8', '9']
access = True

#textures
md = 'sphere'
torvalds = load_texture('assest/torvalds.jpg')
jobs = load_texture('assets/jobs.jpg')
gates = load_texture('assets/gates.jpg')
sky_texture   = load_texture('assets/skybox.png')
linus = load_texture('assets/linus.jpg')

#map
MAP_SIZE = 3
camera.position = (MAP_SIZE // 2, -10.5, -10)
camera.rotation_x = -50
Entity(model='quad', scale=MAP_SIZE, position=(MAP_SIZE // 2, MAP_SIZE // 2, 0), texture ='torvalds')
Entity(model=Grid(MAP_SIZE, MAP_SIZE), scale=MAP_SIZE,
       position=(MAP_SIZE // 2, MAP_SIZE // 2, -0.01), color=color.white) 
Entity(parent = scene, model = 'sphere', texture = sky_texture, scale = 150, double_sided = True)

#check access
def check(st):
    if st in acc:
        acc.remove(st)
        return True
    else:
        return False

#change texture
def change_texture(md):
    if md == 'sphere':
        return 'gates'
    else:   
        return 'jobs'

#change model
def change(hod):
    if hod == 'sphere':
        return 'cube'
    else:
        return 'sphere'

def input(key):
    #change view
    if key == 'q':
        camera.rotation_x = 0
        camera.position = (MAP_SIZE // 2, MAP_SIZE // 2, -15)
    elif key == 'w':
        camera.position = (MAP_SIZE // 2, -10.5, -10)
        camera.rotation_x = -50
    global access
    if access == True:
        #press key
        global md
        global tx
        if key == '1':
            if check(key):
                md = change(md)
                player1 = Entity(model=md, texture=change_texture(md), scale_y=0.85, scale_x=0.85, y=0, x=0)
                arr[0] = md
        if key == '2':
            if check(key):
                md = change(md)
                player2 = Entity(model=md, texture=change_texture(md), scale_y=0.85, scale_x=0.85, y=0, x=1)
                arr[1] = md
        if key == '3':
            if check(key):
                md = change(md)
                player3 = Entity(model=md, texture=change_texture(md), scale_y=0.85, scale_x=0.85, y=0, x=2)
                arr[2] = md
        if key == '4':
            if check(key):
                md = change(md)
                player4 = Entity(model=md, texture=change_texture(md), scale_y=0.85, scale_x=0.85, y=1, x=0)
                arr[3] = md
        if key == '5':
            if check(key):
                md = change(md)
                player5 = Entity(model=md, texture=change_texture(md), scale_y=0.85, scale_x=0.85, y=1, x=1)
                arr[4] = md
        if key == '6':
            if check(key):
                md = change(md)
                player6 = Entity(model=md, texture=change_texture(md), scale_y=0.85, scale_x=0.85, y=1, x=2)
                arr[5] = md
        if key == '7':
            if check(key):
                md = change(md)
                player7 = Entity(model=md, texture=change_texture(md), scale_y=0.85, scale_x=0.85, y=2, x=0)
                arr[6] = md
        if key == '8':
            if check(key):
                md = change(md)
                player8 = Entity(model=md, texture=change_texture(md), scale_y=0.85, scale_x=0.85, y=2, x=1)
                arr[7] = md
        if key == '9':
            if check(key):
                md = change(md)
                player9 = Entity(model=md, texture=change_texture(md), scale_y=0.85, scale_x=0.85, y=2, x=2)
                arr[8] = md
        #check winner
        try:
            if arr[0] == arr[1] == arr[2]:
                counter = Text(text= 'Linus Torvalds wins', y=.15, z=-1, scale=2, origin=(0,0))
                Entity(model=md, texture='linus', scale_y=5, scale_x=5, scale_z=0.1, y=1, x=1)
                access = False
            elif arr[3] == arr[4] == arr[5]:
                counter = Text(text= 'Linus Torvalds wins', y=.15, z=-1, scale=2, origin=(0,0))
                Entity(model=md, texture='linus', scale_y=5, scale_x=5, scale_z=0.1, y=1, x=1)
                access = False
            elif arr[6] == arr[7] == arr[8]:
                counter = Text(text= 'Linus Torvalds wins', y=.15, z=-1, scale=2, origin=(0,0))
                Entity(model=md, texture='linus', scale_y=5, scale_x=5, scale_z=0.1, y=1, x=1)
                access = False
            elif arr[0] == arr[4] == arr[8]:
                counter = Text(text= 'Linus Torvalds wins', y=.15, z=-1, scale=2, origin=(0,0))
                Entity(model=md, texture='linus', scale_y=5, scale_x=5, scale_z=0.1, y=1, x=1)
                access = False
            elif arr[2] == arr[4] == arr[6]:
                counter = Text(text= 'Linus Torvalds wins', y=.15, z=-1, scale=2, origin=(0,0))
                Entity(model=md, texture='linus', scale_y=5, scale_x=5, scale_z=0.1, y=1, x=1)
                access = False
        except:
            return 0

#start running the game
app.run()
