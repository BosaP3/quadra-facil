from fastapi import FastAPI

# Cria a instância da aplicação FastAPI
app = FastAPI(
    title="Quadra Fácil API",
    description="API para o sistema de agendamento de quadras esportivas.",
    version="1.0.0"
)

# Uma rota de exemplo para testar se a API está no ar
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API do Quadra Fácil!"}

# Futuramente, você irá incluir os routers aqui. Ex:
# from .routers import auth
# app.include_router(auth.router)