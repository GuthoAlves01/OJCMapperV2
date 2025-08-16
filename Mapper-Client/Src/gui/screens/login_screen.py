from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App

Builder.load_string('''
<LoginScreen>:
    BoxLayout:
        orientation: 'horizontal'
        padding: 0
        spacing: 0
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1  # Fundo branco
            Rectangle:
                pos: self.pos
                size: self.size

        # Lado esquerdo - Branding do aplicativo
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.5
            padding: 40
            spacing: 20
            canvas.before:
                Color:
                    rgba: 0.95, 0.95, 0.95, 1  # Fundo cinza claro
                Rectangle:
                    pos: self.pos
                    size: self.size

            Label:
                text: 'Mapper Client'
                font_size: 36
                bold: True
                color: 0, 0, 0, 1
                size_hint_y: None
                height: 60
                
            Label:
                text: '(Modo Demo)'
                font_size: 24
                color: 0.4, 0.4, 0.4, 1
                size_hint_y: None
                height: 40
                
            Label:
                text: 'Sistema de mapeamento\\ne integração de projetos'
                font_size: 18
                color: 0.2, 0.2, 0.2, 1
                halign: 'center'
                valign: 'middle'
                text_size: self.width, None
                size_hint_y: 0.8

        # Lado direito - Área de login
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.5
            padding: [40, 60, 40, 40]
            spacing: 30

            Label:
                text: 'LOGIN'
                font_size: 28
                bold: True
                color: 0, 0, 0, 1
                size_hint_y: None
                height: 60
                
            # Campo de usuário
            TextInput:
                id: username
                hint_text: 'Usuário'
                size_hint_y: None
                height: 50
                multiline: False
                background_color: 0.95, 0.95, 0.95, 1
                foreground_color: 0, 0, 0, 1
                hint_text_color: 0.6, 0.6, 0.6, 1
                font_size: 16
                padding: [15, 10]
                
            # Campo de senha
            TextInput:
                id: password
                hint_text: 'Senha'
                password: True
                size_hint_y: None
                height: 50
                multiline: False
                background_color: 0.95, 0.95, 0.95, 1
                foreground_color: 0, 0, 0, 1
                hint_text_color: 0.6, 0.6, 0.6, 1
                font_size: 16
                padding: [15, 10]

            # Botão de login
            Button:
                text: 'ENTRAR'
                size_hint_y: None
                height: 50
                on_press: root.do_login()
                background_normal: ''
                background_color: 0, 0, 0, 1
                color: 1, 1, 1, 1
                bold: True
                font_size: 16

            # Mensagem de status
            Label:
                id: status
                text: ''
                color: 0.8, 0.2, 0.2, 1
                size_hint_y: None
                height: 30
                font_size: 14
''')

class LoginScreen(Screen):
    # Dados mockados de usuários válidos
    VALID_USERS = {
        'admin': 'admin123',  # usuário: senha
        'user1': '123456',
        'demo': 'demo'
    }

    def do_login(self):
        """Verificação mockada de credenciais"""
        username = self.ids.username.text
        password = self.ids.password.text
        
        if not username or not password:
            self.ids.status.text = "Digite usuário e senha"
            return
            
        self.ids.status.text = "Verificando..."
        
        # Verifica contra os dados mockados
        if username in self.VALID_USERS and password == self.VALID_USERS[username]:
            self.ids.status.text = "Login bem-sucedido!"
            
            # Armazena o usuário mockado no app
            app = App.get_running_app()
            app.current_user = username
            
            # Navega para a tela principal
            self.manager.current = 'projects'
        else:
            self.ids.status.text = "Usuário ou senha inválidos"