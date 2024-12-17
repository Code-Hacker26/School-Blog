from fastapi import APIRouter, HTTPException
from app.models import Blog
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

router = APIRouter()
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.school_blog_api
blog_collection = db.blogs


@router.post("/", status_code=201)
async def create_blog(blog: Blog):
    blog_data = blog.dict()
    blog_data["published_at"] = blog_data["published_at"] or datetime.utcnow()
    result = await blog_collection.insert_one(blog_data)
    return {"message": "Blog created successfully", "id": str(result.inserted_id)}


@router.get("/", status_code=200)
async def get_all_blogs():
    blogs = await blog_collection.find().to_list(100)
    for blog in blogs:
        blog["_id"] = str(blog["_id"])
    return blogs
