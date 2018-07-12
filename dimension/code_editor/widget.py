import pdb

from kivy.uix.widget import Widget
# from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from dimension.code_block.widget import CodeBlock


class CodeEditor(Widget):
    selected_block = ObjectProperty(None, allownone=True)

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            block = CodeBlock(name="Block {}".format(len(self.children)+1))
            block.scale_factor = self.width / 10
            block.center = touch.pos
            self.add_widget(block)

        for child in self.children:
            if child.on_touch_down(touch):
                self.selected_block = child
                break

    def on_touch_up(self, touch):
        # Prevent intersection/blocks can't stop on top of each other?
        for child in self.children:
            if self.selected_block and self.selected_block is not child and self.selected_block.collide_widget(child):
                print(child.name)
                # Decide whether to nudge both or just the selected or child?

        for child in self.children:
            if child.on_touch_up(touch):
                break

        self.selected_block = None