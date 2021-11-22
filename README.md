## Training References:

- YouTube link: https://www.youtube.com/watch?v=0sOvCWFmrtA
- Repo: https://github.com/Sanjeev-Thiyagarajan/fastapi-course.git

## Packages Used

- FastAPI doc: https://fastapi.tiangolo.com/tutorial/ and: https://fastapi.tiangolo.com/tutorial/sql-databases/
- SQLAlchemy doc: https://docs.sqlalchemy.org/en/14/
- JWT Decoder: [https://jwt.io](https://jwt.io/)

## Local Setup

```
# Create virtual environment
python3 -m venv venv
# Activate it
source venv/bin/activate
# make sure pip is up to date
pip install --upgrade pip
# install project's requirements
pip install -r requirements.txt
# Start Web server: 
uvicorn app.main:app --reload


```