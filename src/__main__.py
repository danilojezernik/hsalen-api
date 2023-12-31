"""
This script starts a FastAPI application using Uvicorn server.

Steps:
1. Imports necessary modules and libraries.
2. Configures FastAPI application with a base path and openapi tags.
3. Adds CORS middleware for handling Cross-Origin Resource Sharing.
4. Sets the secret key for the FastAPI application.
5. Includes various routers for different functionalities (blog, login, admin, mediji).
6. If the script is run directly (not imported), it drops the database and seeds it, then starts the Uvicorn server.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import env
from src.routes import mediji, admin, login, blog, email, events, subscriber, newsletter, review, index, hipnotherapy, \
    selfhypnosis, clairvoyance, regression, mediumship
# from src.services import db
from src.tags_metadata import tags_metadata

app = FastAPI(openapi_tags=tags_metadata)

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set the secret key for the FastAPI application
app.secret_key = env.SECRET_KEY

# Include various routers for different functionalities
app.include_router(blog.router, prefix="/blog", tags=['Blog'])
app.include_router(login.router, prefix="/login", tags=['LogIn'])
app.include_router(admin.router, prefix="/admin", tags=['Admin'])
app.include_router(mediji.router, prefix="/mediji", tags=['Mediji'])
app.include_router(events.router, prefix="/events", tags=['Events'])
app.include_router(email.router, prefix="/email", tags=['Contact'])
app.include_router(review.router, prefix="/review", tags=['Review'])
app.include_router(subscriber.router, prefix="/subscribers", tags=['Subscriber'])
app.include_router(newsletter.router, prefix="/newsletter", tags=['Newsletter'])

# Routes that insert logs only
app.include_router(index.router, prefix="/index", tags=['Index'])
app.include_router(hipnotherapy.router, prefix="/hipnoterapija", tags=['Hipnoterapija'])
app.include_router(selfhypnosis.router, prefix="/samohipnoza", tags=['Samo-hipnoza'])
app.include_router(clairvoyance.router, prefix="/jasnovidnost", tags=['Jasnovidnost'])
app.include_router(regression.router, prefix="/regresija", tags=['Regresija'])
app.include_router(mediumship.router, prefix="/medijstvo", tags=['Medijstvo'])

if __name__ == '__main__':
    # Drop the database and seed it
    # db.drop()
    # db.seed()

    # Run the FastAPI application using Uvicorn server
    uvicorn.run(app, host="0.0.0.0", port=env.PORT)
