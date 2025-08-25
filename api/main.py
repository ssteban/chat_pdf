from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .routes import user_routes, admin_routes, auth_routes
from api.utils.auth import verify_token

app = FastAPI()


app.add_middleware(CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])

app.include_router(user_routes.router, prefix="/users", dependencies=[Depends(verify_token)], tags=["users"])
app.include_router(admin_routes.router, prefix="/admin", dependencies=[Depends(verify_token)], tags=["admin"])



