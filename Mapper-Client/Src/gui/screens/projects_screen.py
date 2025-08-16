from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.properties import ListProperty, BooleanProperty, NumericProperty, ObjectProperty
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from api.projects_client import ProjectsClient
from config.settings import APP_CONFIG

# Corrigido: Expressões condicionais simplificadas no KV
Builder.load_string('''
<ProjectCard@ButtonBehavior+BoxLayout>:
    orientation: 'horizontal'
    size_hint_y: None
    height: dp(60)
    padding: dp(10)
    spacing: dp(15)
    project_data: None
    
    canvas.before:
        Color:
            rgba: (0.95, 0.95, 0.95, 1) if self.state == 'normal' else (0.9, 0.9, 0.9, 1)
        Rectangle:
            pos: self.pos
            size: self.size
            radius: [dp(5),]
    
    Label:
        text: root.project_data['name'] if root.project_data else ''
        size_hint_x: 0.7
        halign: 'left'
        text_size: self.width, None
        color: 0, 0, 0, 1
    
    Button:
        id: mount_btn
        text: 'Montar' if not root.project_data.get('mounted', False) else 'Desmontar'
        size_hint_x: 0.3
        on_press: root.mount_project()
        background_normal: ''
        background_color: 
            (0.2, 0.8, 0.2, 1) if not root.project_data.get('mounted', False) else (0.8, 0.2, 0.2, 1)
        color: 1, 1, 1, 1

<ProjectsScreen>:
    loading: False
    spinner_angle: 0
    projects_data: []
    
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            spacing: dp(10)
            
            TextInput:
                id: search_input
                hint_text: 'Pesquisar projetos...'
                multiline: False
                size_hint_x: 0.7
                on_text_validate: root.search_projects()
                background_color: 1, 1, 1, 1
                foreground_color: 0, 0, 0, 1
                cursor_color: 0, 0, 1, 1
                write_tab: False
            
            Button:
                id: refresh_btn
                text: 'Atualizar'
                size_hint_x: 0.3
                on_press: root.search_projects()
                background_normal: ''
                background_color: (0.2, 0.6, 0.8, 1)
                color: 1, 1, 1, 1
        
        RecycleView:
            id: projects_rv
            viewclass: 'ProjectCard'
            scroll_type: ['bars', 'content']
            scroll_wheel_distance: dp(100)
            
            RecycleBoxLayout:
                default_size: None, dp(60)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
                spacing: dp(5)
                padding: dp(5)
        
        BoxLayout:
            size_hint_y: None
            height: dp(50)
            spacing: dp(10)
            
            Button:
                text: 'Gerenciar'
                on_press: root.manager.current = 'management'
                background_normal: ''
                background_color: (0.2, 0.6, 0.8, 1)
                color: 1, 1, 1, 1
            
            Button:
                text: 'Configurações'
                on_press: root.manager.current = 'config'
                background_normal: ''
                background_color: (0.2, 0.6, 0.8, 1)
                color: 1, 1, 1, 1
            
            Button:
                text: 'Sair'
                on_press: root.logout()
                background_normal: ''
                background_color: (0.8, 0.2, 0.2, 1)
                color: 1, 1, 1, 1
        
        LoadingOverlay:
            active: root.loading
            spinner_angle: root.spinner_angle
''')

class LoadingOverlay(BoxLayout):
    active = BooleanProperty(False)
    spinner_angle = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.animation = None
        self.bind(active=self._on_active_change)
    
    def _on_active_change(self, instance, value):
        if value:
            self._start_animation()
        else:
            self._stop_animation()
    
    def _start_animation(self):
        if self.animation:
            self.animation.cancel(self)
        
        self.animation = Animation(spinner_angle=360, duration=1.5)
        self.animation += Animation(spinner_angle=0, duration=0)
        self.animation.repeat = True
        self.animation.start(self)
    
    def _stop_animation(self):
        if self.animation:
            self.animation.cancel(self)
            self.animation = None
        self.spinner_angle = 0

class ProjectsScreen(Screen):
    projects_data = ListProperty([])
    loading = BooleanProperty(False)
    spinner_angle = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._projects_client = None
        self._first_load = True
    
    @property
    def projects_client(self):
        if not self._projects_client:
            self._projects_client = ProjectsClient(APP_CONFIG['auth_token'])
        return self._projects_client
    
    def on_enter(self):
        """Carrega os projetos quando a tela é exibida pela primeira vez"""
        if self._first_load:
            self.search_projects()
            self._first_load = False
    
    def search_projects(self, *args):
        """Busca projetos no servidor"""
        if self.loading:
            return
            
        self.loading = True
        search_term = self.ids.search_input.text
        
        Clock.schedule_once(
            lambda dt: self._perform_search(search_term), 0.1)
    
    def _perform_search(self, search_term):
        """Executa a busca real dos projetos"""
        try:
            response = self.projects_client.get_projects(search=search_term)
            
            if response.get('success'):
                self.projects_data = response['projects']
                self._update_projects_list()
        except Exception as e:
            print(f"Erro na busca: {str(e)}")
        finally:
            self.loading = False
    
    def _update_projects_list(self):
        """Atualiza a lista de projetos no RecycleView"""
        self.ids.projects_rv.data = [
            {
                'project_data': project,
                'mount_project': lambda x=project: self._mount_project(x)
            }
            for project in self.projects_data
        ]
    
    def _mount_project(self, project_data):
        """Monta/desmonta um projeto específico"""
        print(f"Montando projeto: {project_data['name']}")
        # Atualiza o estado visual
        self._update_projects_list()
    
    def logout(self):
        """Realiza logout do usuário"""
        APP_CONFIG['auth_token'] = None
        APP_CONFIG['current_user'] = None
        self.manager.current = 'login'
        self.manager.transition.direction = 'right'