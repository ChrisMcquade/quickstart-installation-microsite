from urllib.parse import urlparse
from typing import Any


def add_rich_content(
    url: str,
    title: str = "",
    accessibilityText: str = "",
) -> dict[str, Any]:
    """
    Returns a native richContent payload that the chat-messenger widget renders.
    - Image/GIF URLs (.gif/.png/.jpg/.jpeg/.svg/.webp) -> native "image" type (inline).
    - Web page URLs -> native "info" type with actionLink (tappable link card).
    - MP4s are treated as link cards (the widget cannot render video inline).
    """
    image_exts = (".gif", ".png", ".jpg", ".jpeg", ".svg", ".webp")
    path = urlparse(url).path.lower()
    is_image = path.endswith(image_exts)

    if is_image:
        block = {
            "type": "image",
            "rawUrl": url,
            "accessibilityText": accessibilityText or title or "image",
        }
    else:
        block = {
            "type": "info",
            "title": title or "Open link",
            "subtitle": "Tap to open",
            "actionLink": url,
        }

    return {"richContent": [[block]]}