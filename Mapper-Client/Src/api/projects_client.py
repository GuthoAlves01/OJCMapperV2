import requests
from config.settings import APP_CONFIG

class ProjectsClient:
    def __init__(self, auth_token):
        self.base_url = APP_CONFIG['api_url']
        self.auth_token = auth_token
        
    def get_projects(self, search=None):
        """Obtém lista de projetos do servidor"""
        try:
            headers = {'Authorization': f"Bearer {self.auth_token}"}
            params = {'search': search} if search else None
            
            response = requests.get(
                f"{self.base_url}/projects",
                headers=headers,
                params=params
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'success': False, 'message': str(e)}
    
    def mount_project(self, project_id):
        """Obtém informações para montar um projeto"""
        try:
            headers = {'Authorization': f"Bearer {self.auth_token}"}
            
            response = requests.get(
                f"{self.base_url}/projects/{project_id}/mount",
                headers=headers
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'success': False, 'message': str(e)}