from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.blogs import router as blog_router

app = FastAPI()

# Mount static files for frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Register routes
app.include_router(blog_router, prefix="/api/blogs", tags=["Blogs"])
