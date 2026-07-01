from fastapi import FastAPI

from api.routes import router


app = FastAPI(
    title="Olist Recommendation System",
    version="1.0.0",
    description=(
        "Multi-model recommendation system "
        "built on the Olist dataset."
    )
)


app.include_router(router)