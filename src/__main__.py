import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import env
from src.database import db
from src.routes import blog
from src.routes import global_error
from src.routes import samohipnoza


app = FastAPI(prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.secret_key = env.SECRET_KEY

app.include_router(blog.router, prefix="/blog", tags=['blog'])
app.include_router(samohipnoza.router, prefix="/samohipnoza", tags=['samohipnoza'])
app.include_router(global_error.router, prefix="/global_error", tags=['global_error'])

if __name__ == '__main__':
    db.drop()
    db.seed()
    uvicorn.run(app, host="0.0.0.0", port=8000)
