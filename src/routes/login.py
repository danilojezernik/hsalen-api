from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from src.domain.user import User
from src.api.token import Token
from src.services.security import authenticate_user, create_access_token, get_current_active_user

# Create a new APIRouter instance for this module
router = APIRouter()


# Route for user authentication and obtaining an access token
@router.post("/", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """
    This route handles user authentication by validating the provided credentials (username and password).
    If the credentials are correct, it generates an access token and returns it to the client.

    Args:
        form_data (OAuth2PasswordRequestForm): The user's credentials.

    Returns:
        dict: A dictionary containing the access token and its type.
    """

    # Authenticate the user using the provided username and password
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        # Raise an exception if the authentication fails
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Set the expiration time for the access token to 30 minutes
    access_token_expires = timedelta(minutes=30)

    # Create an access token for the authenticated user
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    # Return the access token and token type
    return {"access_token": access_token, "token_type": "bearer"}


# Route to get the current user
@router.get("/user", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    """
    This route defines an HTTP GET endpoint to retrieve details of the currently authenticated user.

    Behavior:
    - It expects the client to provide an authentication token (Bearer token) in the request header.
    - The `Depends(get_current_active_user)` dependency verifies and extracts the current authenticated user based on the provided token.
    - If the user is active (not disabled), it responds with the details of the current authenticated user in the specified JSON format.
    - If the user is inactive (disabled), it raises a `HTTPException` with a status code of 400, indicating an inactive user.

    Response:
    - Upon successful authentication and an active user, the response will contain the user details in JSON format as specified by the response model.
    - In case of an inactive user, the response will include an error message indicating the user's inactive status, and the status code will be 400.
    """
    return current_user
