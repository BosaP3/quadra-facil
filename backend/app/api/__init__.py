import pkgutil
import importlib
from fastapi import APIRouter

def get_routers():
    """
    Verifica o pacote 'api', importa módulos dinamicamente 
    e coleta instâncias do APIRouter.
    """
    routers = []
    # O prefixo do pacote onde as rotas estão localizadas
    package_prefix = "app.api"

    # Itera sobre todos os módulos dentro do pacote 'app.api'
    for _, name, _ in pkgutil.walk_packages(__path__, prefix=f"{package_prefix}."):
        try:
            # Importa o módulo dinamicamente
            module = importlib.import_module(name)
            
            # Procura por instâncias de APIRouter dentro do módulo
            for item_name in dir(module):
                item = getattr(module, item_name)
                if isinstance(item, APIRouter):
                    routers.append(item)
        except Exception as e:
            print(f"Could not import router from {name}: {e}")

    return routers