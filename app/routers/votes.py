from fastapi import  Response, status, HTTPException, Depends, APIRouter

router = APIRouter(
    prefix="/votes"
    tags=['Votes']
)

