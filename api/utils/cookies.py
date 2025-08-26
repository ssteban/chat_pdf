from fastapi import Response



def set_cookie(response: Response, value: str):
    try:
        response.set_cookie(
            key="access_token_cookie", 
            value=value, 
            max_age=3600, 
            httponly=True, 
            secure=False, 
            samesite="Lax"
            )
    except Exception as e:
        print(f"Error setting cookie: {e}")

    

def delete_cookie(response: Response):
    response.delete_cookie(key="access_token_cookie")
