from fastapi import FastAPI
from database import engine, Base
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from routers.alunos import alunos_router
from routers.cursos import cursos_router
from routers.matriculas import matriculas_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código a ser executado na inicialização
    Base.metadata.create_all(bind=engine)
    yield
    # Código a ser executado no encerramento (se necessário)

app = FastAPI(
    title="API de Gestão Escolar", 
    description="""
        Esta API fornece endpoints para gerenciar alunos, cursos e turmas, em uma instituição de ensino.  
        
        Permite realizar diferentes operações em cada uma dessas entidades.
    """, 
    version="1.0.1",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

app.include_router(alunos_router, tags=["alunos"])
app.include_router(cursos_router, tags=["cursos"])
app.include_router(matriculas_router, tags=["matriculas"])
