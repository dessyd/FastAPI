from fastapi import  Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm.session import Session
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from .. import schemas, database, models,oauth2

router = APIRouter(
    prefix="/votes",
    tags=['Votes']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def cast_vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {vote.id} does not exist")

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, 
    models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()

    if (vote.dir == 1): 
        if found_vote:
            raise HTTPException(status_code=HTTP_409_CONFLICT, detail=f"user {current_user.id} has already voted on post {vote.post_id}")
        new_vote = models.Vote(post_id = vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return{"message": "successfully added vote"}

    elif (vote.dir == 0): 
        if not found_vote:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"post {vote.post_id} has no vote yet")

        vote_query.delete(synchronize_session=False)
        db.commit()
        return{"message": "successfully removed vote"}

    else:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f"invalid vote direction {vote.dir}")
