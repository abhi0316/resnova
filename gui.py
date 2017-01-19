
#!usr/bin/env python
import pyglet
window = pyglet.window.Window(1400,900)
label1 = pyglet.text.Label('screen1',
                          font_name='Arial',
                          font_size=36,
                          x=0, y=800
                          )

label2 = pyglet.text.Label('screen2',font_name='Arial',font_size=36,x=700,y=500)
                                                           

label3 =pyglet.text.Label('screen3',font_name='Arial',font_size=36,x=0,y=100)
label4 =pyglet.text.Label('screen4',font_name='Arial',font_size=36,x=700,y=100 )                                

@window.event
def on_draw():
    window.clear()
    label1.draw()
    label2.draw()
    label3.draw()
    label4.draw()
pyglet.app.run()
