from fastapi import APIRouter

router = APIRouter()


@router.get("/admin", tags=["users"])
async def read_admin():
    """
    Get admin.
    
    -returns: admin
    """
    return {"username": "admin"}


@router.get("/admin/me", tags=["users"])
async def read_admin_me():
    """
    Get current admin.
    
    -returns: current admin
    """
    return {"username": "fakecurrentadmin"}


@router.post('/')
async def update_admin():
    """
    Update admin.
    
    -returns: admin
    """
    return {"message": "Admin getting schwifty"}
