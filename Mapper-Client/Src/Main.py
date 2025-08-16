import os
import sys
from pathlib import Path
from gui.screens import SkillsetDashboard
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

# Adiciona o diretório Src ao path do Python
src_path = Path(__file__).parent
sys.path.append(str(src_path))

# Importações das telas
from gui.screens.login_screen import LoginScreen
from gui.screens.projects_screen import ProjectsScreen
from gui.screens.management_screen import ManagementScreen
from gui.screens.config_screen import ConfigScreen
from config.settings import APP_CONFIG

class MapperClient(App):
    def build(self):
        self.title = "Mapper - Gerenciador de Unidades"
        self.screen_manager = ScreenManager()
        
        # Adiciona todas as telas
        self.screen_manager.add_widget(LoginScreen(name='login'))
        self.screen_manager.add_widget(ProjectsScreen(name='projects'))
        self.screen_manager.add_widget(ManagementScreen(name='management'))
        self.screen_manager.add_widget(ConfigScreen(name='config'))
        self.screen_manager.add_widget(SkillsetDashboard(name='dashboard'))
        return self.screen_manager

    def on_start(self):
        if APP_CONFIG.get('auth_token'):
            self.screen_manager.current = 'projects'
        else:
            self.screen_manager.current = 'login'

if __name__ == '__main__':
    MapperClient().run()