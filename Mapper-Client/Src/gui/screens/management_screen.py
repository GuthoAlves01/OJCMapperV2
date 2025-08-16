from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string('''
<ManagementScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Tela de Gerenciamento'
            font_size: 24
        Button:
            text: 'Voltar'
            size_hint_y: None
            height: 50
            on_press: root.manager.current = 'projects'
''')

class ManagementScreen(Screen):
    pass