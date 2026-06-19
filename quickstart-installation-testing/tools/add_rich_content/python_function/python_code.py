from typing import Any

def add_rich_content(
    url: str,
    title: str = "",
    accessibilityText: str = "",
) -> dict[str, Any]:

    return {
        "type": "image",
        "rawUrl": url,
        "accessibilityText": accessibilityText or title
    }