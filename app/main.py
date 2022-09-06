from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth, posts, users, votes

# Needed if Alembic is not used to create / upgrade the structure
# models.Base.metadata.create_all(bind=engine)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
]

description = """
FastAPI tutorial API helps you do awesome stuff. 🚀

## Posts

You can **read, create, update  and delete posts**.

## Users

You will be able to:

* **Create users** (_implemented_).
* **Read users** (_implemented_).

## Authentication

This is the main login module

## Votes

Here you can cast a vote for a post
"""

tags_metadata = [
    {
        "name": "Users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "Posts",
        "description": "Manage posts. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Posts external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(
    title="FastAPI tutorial",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Domenico",
        "url": "http://x-force.example.com/contact/",
        "email": "dom.do@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/")
def root():
    return {"message": "Hello Root"}
