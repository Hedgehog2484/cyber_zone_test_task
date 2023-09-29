from fastapi import FastAPI, Request, Depends


async def add_user(request: Request, db=Depends()):
    user = await db.add_user(request["username"], request["password"])  # Ну тут типа надо добавить хэширование пароля.
    return {"user_id": user.id}


async def delete_user(request: Request, ):
    pass


async def add_booking(request: Request, db=Depends()):
    pass


async def delete_booking(request: Request, db=Depends()):
    pass


async def get_all_user_bookings(request: Request, db=Depends()):
    pass


async def get_all_bookings(request: Request, db=Depends()):
    pass


def setup_handlers(app: FastAPI) -> None:
    app.router.get('/user/add')(add_user)
    app.router.get('/user/delete')(delete_user)
    app.router.get('/booking/add')(add_booking)
    app.router.get('/booking/delete')(delete_booking)
    app.router.get('/user/bookings')(get_all_user_bookings)
    app.router.get('/booking/get_all')(get_all_bookings)

