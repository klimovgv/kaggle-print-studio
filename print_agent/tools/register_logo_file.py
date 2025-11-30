import os

ALLOWED_LOGO_EXTENSIONS = {".png", ".jpg", ".jpeg", ".svg"}

def register_logo_file(path: str) -> dict:
    """Validate a provided logo path and describe the detected format."""

    if not path:
        return {
            "status": "error",
            "path": path,
            "format": None,
            "reason": "Empty path provided."
        }

    ext = os.path.splitext(path)[1].lower()
    if ext not in ALLOWED_LOGO_EXTENSIONS:
        return {
            "status": "error",
            "path": path,
            "format": None,
            "reason": "Unsupported format. Allowed formats: PNG, JPG, JPEG, SVG."
        }

    return {
        "status": "success",
        "path": path,
        "format": ext.lstrip("."),
        "reason": None
    }