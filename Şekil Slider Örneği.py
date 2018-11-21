from kivy.app import App
from kivy.uix.effectwidget import AdvancedEffectBase
from kivy.lang import Builder
from kivy.properties import NumericProperty

KV = '''
#:import Scanlines kivy.uix.effectwidget.ScanlinesEffect
#:import VerticalBlur kivy.uix.effectwidget.VerticalBlurEffect
#:import HorizontalBlur kivy.uix.effectwidget.HorizontalBlurEffect
#:import FXAA kivy.uix.effectwidget.FXAAEffect
#:import Pixelate kivy.uix.effectwidget.PixelateEffect
<SLabel@Label,SButton@Button>:
    size_hint_y: None
    height: 100
    font_size: '26dp'
BoxLayout:
    ScrollView:
        id: scrollview
        old_y: [1, ] * 10
        speed: app.speed
        on_speed: app.speed = self.speed
        on_scroll_y:
            self.old_y.append(self.scroll_y)
            self.old_y.pop(0)
            #self.speed = self.old_y[0] - self.old_y[-1]
            self.speed = sum(((self.old_y[x + 1] - self.old_y[x]) for x in range(9))) / 9.
        EffectWidget:
            size_hint_y: None
            height: grid.minimum_height
            effects:
                [
                #HorizontalBlur(),
                #Scanlines(),
                #FXAA(),
                #Pixelate(pixel_size=4),
                app.scrollflex,
                ]
            #on_touch_move: self.speed = args[1].dy
            GridLayout:
                id: grid
                cols: 1
                SLabel:
                    text: '1'
                SButton:
                    text: '1'
                SLabel:
                    text: '2'
                SButton:
                    text: '2'
                SLabel:
                    text: '3'
                SButton:
                    text: '3'
                SLabel:
                    text: '4'
                SButton:
                    text: '4'
                SLabel:
                    text: '5'
                SButton:
                    text: '5'
                SLabel:
                    text: '6'
                SButton:
                    text: '6'
                SLabel:
                    text: '7'
                SButton:
                    text: '7'
    ScrollView:
        GridLayout:
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            SLabel:
                text: '1'
            SButton:
                text: '1'
            SLabel:
                text: '2'
            SButton:
                text: '2'
            SLabel:
                text: '3'
            SButton:
                text: '3'
            SLabel:
                text: '4'
            SButton:
                text: '4'
            SLabel:
                text: '5'
            SButton:
                text: '5'
            SLabel:
                text: '6'
            SButton:
                text: '6'
            SLabel:
                text: '7'
            SButton:
                text: '7'
'''


effect_flex_scroll = '''
uniform float speed;
vec4 effect(vec4 color, sampler2D texture, vec2 tex_coords, vec2 coords)
{
    return texture2D(
        texture,
        vec2(tex_coords.x, tex_coords.y + sin(
            tex_coords.x * 3.1416 / 2. + 3.1416 / 4.
        ) * speed * 2.));
}
'''


class MyScrollApp(App):
    speed = NumericProperty(0)

    def build(self):
        self.scrollflex = AdvancedEffectBase(
            glsl=effect_flex_scroll,
            uniforms={'speed': self.speed}
        )
        return Builder.load_string(KV)

    def on_speed(self, *args):
        self.scrollflex.uniforms['speed'] = self.speed


MyScrollApp().run()
