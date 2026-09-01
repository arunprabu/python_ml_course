mkdir products_rest_api
cd products_rest_api

uv init
uv venv
.venv\Scripts\activate

code .

uv add fastapi uvicorn

# To start the server try the following command

uv run uvicorn app.main:app --reload
