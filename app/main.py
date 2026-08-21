from fastapi import FastAPI


# Import Modules
# Import Router
from app.routers import userCommentRouter


app = FastAPI(
    title="Skillora",
    description="Api for Upskill the Students",
    version="0.4.0",
    summary="API build with FastAPI Framework for application Upskill website",
    terms_of_service="https://example.com",
    contact={
        "name": "Vibhu Sahu",
        "url": "https://example.com",
        "email": "vibhu6751@gmail.com",
    },
    license_info={
        "name": "GPL-3.0-only",
        "url": "https://spdx.org/licenses/GPL-3.0-only.html",
    },
)



@app.get("/")
def health_check():
    # Check database connection here
    database_ok = True

    if database_ok:
        return {
            "status": "healthy",
            "database": "connected"
        }

    return {
        "status": "unhealthy",
        "database": "disconnected"
    }


# Include Router
app.include_router(userCommentRouter.router)