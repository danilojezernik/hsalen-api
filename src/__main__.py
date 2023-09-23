import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import env
from src.database import db
from src.routes import mediji, admin, login, blog, global_error
from src.tags_metadata import tags_metadata


app = FastAPI(prefix="/api", openapi_tags=tags_metadata)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.secret_key = env.SECRET_KEY

app.include_router(blog.router, prefix="/blog", tags=['Blog'])
app.include_router(login.router, prefix="/login", tags=['LogIn'])
app.include_router(admin.router, prefix="/admin", tags=['Admin'])
app.include_router(mediji.router, prefix="/mediji", tags=['Mediji'])
app.include_router(global_error.router, prefix="/global_error", tags=['Global error'])

if __name__ == '__main__':
    db.drop()
    db.seed()
    uvicorn.run(app, host="0.0.0.0", port=8000)
