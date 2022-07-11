from fastapi import APIRouter

from app.api.endpoints import user_router, recipe_router, auth_router, admin_router


main_router = APIRouter()
main_router.include_router(auth_router)
main_router.include_router(
    admin_router, prefix='/user', tags=['Admin']
)
main_router.include_router(
    recipe_router, prefix='/recipe', tags=['Recipes']
)
main_router.include_router(
    user_router, prefix='/user', tags=['Users']
)
