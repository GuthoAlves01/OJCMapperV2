import subprocess
import platform
import logging
from config.settings import APP_CONFIG

logger = logging.getLogger(__name__)

class NetworkService:
    @staticmethod
    def mount_network_drive(letter, path, username=None, password=None):
        """Monta uma unidade de rede no Windows"""
        try:
            if platform.system() != 'Windows':
                raise Exception("Este comando só funciona no Windows")
            
            # Monta a unidade de rede
            cmd = f"net use {letter}: {path}"
            if username and password:
                cmd += f" /user:{username} {password}"
            
            result = subprocess.run(
                cmd, 
                shell=True, 
                check=True,
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE
            )
            
            logger.info(f"Unidade {letter}: montada em {path}")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Falha ao montar unidade: {e.stderr.decode()}")
            return False
        except Exception as e:
            logger.error(f"Erro inesperado: {str(e)}")
            return False
    
    @staticmethod
    def unmount_network_drive(letter):
        """Desmonta uma unidade de rede"""
        try:
            if platform.system() != 'Windows':
                raise Exception("Este comando só funciona no Windows")
            
            result = subprocess.run(
                f"net use {letter}: /delete /y",
                shell=True, 
                check=True,
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE
            )
            
            logger.info(f"Unidade {letter}: desmontada")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Falha ao desmontar unidade: {e.stderr.decode()}")
            return False
        except Exception as e:
            logger.error(f"Erro inesperado: {str(e)}")
            return False