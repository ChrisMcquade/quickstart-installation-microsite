from typing import Any

def get_knowledge_article(category: str, item: str, sub_item: str | None = None) -> dict[str, Any]:
    """
    Retrieves specific installation steps or information from a simulated knowledge base.

    Args:
        category (str): The main category of the knowledge article (e.g., "Hub Setup", "WiFi Pods").
        item (str): The specific item within the category (e.g., "Hub 5 Install", "Black Pod Steps").
        sub_item (str | None, optional): A more granular detail or sub-section (e.g., "Uninstall Old Hub", "Video Guide"). Defaults to None.

    Returns:
        dict[str, Any]: A dictionary containing the retrieved content or an error message.
    """
    # MOCK: This mock simulates fetching content from a knowledge base.
    # It uses a hardcoded dictionary to represent available articles.
    # In a real scenario, this would query a CMS or knowledge management system.

    knowledge_base = {
        "Acquire": {
            "Wall Socket Check": {
                "info": "The wall socket should be securely fixed, within 3 metres of the TV box and WiFi Hub, and have visible silver connectors. If it doesn't, you might need an engineer.",
                "url": "https://www.virginmedia.com/help/check-wall-socket"
            }
        },
        "Hub Setup": {
            "Hub 5 Install": {
                "Uninstall Old Hub": "To uninstall your old Hub, carefully remove all cables from its back. IMPORTANT: DO NOT remove the connector cable from the wall socket, as it will be reused for your new Hub.",
                "Install New Hub": "1. Connect the white coaxial cable from your wall socket to the 'Cable' port on your Hub 5. 2. Plug the power cable into your Hub 5 and then into a wall socket. 3. Wait for the white light on your Hub 5 to become solid. This can take up to 10 minutes.",
                "Online Steps": "https://www.virginmedia.com/help/guides/quick-start/hub-5/old-kit",
                "Video Guide": "https://www.youtube.com/watch?v=7XJqitIIlrg",
                "PDF Guide": "PDF guide is available on the online steps page."
            },
            "Hub 4 Install": {
                "Uninstall Old Hub": "To uninstall your old Hub, carefully remove all cables from its back. IMPORTANT: DO NOT remove the connector cable from the wall socket, as it will be reused for your new Hub.",
                "Install New Hub": "1. Connect the white coaxial cable from your wall socket to the 'Cable' port on your Hub 4. 2. Plug the power cable into your Hub 4 and then into a wall socket. 3. Wait for the white light on your Hub 4 to become solid. This can take up to 10 minutes.",
                "Online Steps": "https://www.virginmedia.com/help/guides/quick-start/hub-4/old-kit",
                "Video Guide": "https://www.youtube.com/watch?v=7XJqitIIlrg"
            },
            "Hub 3 Install": {
                "Uninstall Old Hub": "To uninstall your old Hub, carefully remove all cables from its back. IMPORTANT: DO NOT remove the connector cable from the wall socket, as it will be reused for your new Hub.",
                "Install New Hub": "1. Connect the white coaxial cable from your wall socket to the 'Cable' port on your Hub 3. 2. Plug the power cable into your Hub 3 and then into a wall socket. 3. Wait for the white light on your Hub 3 to become solid. This can take up to 10 minutes.",
                "Online Steps": "https://www.virginmedia.com/help/guides/quick-start/hub-3/old-kit",
                "Video Guide": "https://www.youtube.com/watch?v=7XJqitIIlrg",
                "PDF Guide": "PDF guide is available on the online steps page."
            },
            "Old Hub Return": {
                "info": "You must return your old Hub if asked to (or risk a charge). If not asked to return it, please recycle it responsibly.",
                "url": "https://www.virginmedia.com/help/return-or-recycle-equipment"
            }
        },
        "TV Box Setup": {
            "Stream": "Stream TV box setup steps: 1. Connect the HDMI cable from your Stream box to your TV. 2. Plug in the power cable. 3. Follow the on-screen instructions.",
            "Virgin TV 360": "Virgin TV 360 box setup steps: 1. Connect the coaxial cable from the wall to your TV box. 2. Connect the HDMI cable to your TV. 3. Plug in the power cable. 4. Follow the on-screen instructions."
        },
        "Landline Setup": {
            "info": "To set up your landline, plug your phone into the TEL 1 port on the back of your WiFi Hub. If you have an older phone, you might need an adapter."
        },
        "WiFi Pods": {
            "Black Pod Steps": {
                "info": "Black WiFi Pod setup: 1. Plug the Pod into a power socket halfway between your Hub and the area with poor WiFi. 2. Wait for the light to turn solid white. This can take a few minutes. If the light pulses green for more than 10 minutes, try moving it closer to the Hub.",
                "url": "https://www.virginmedia.com/help/check/status/guide/black-pods/advice",
                "video_url": "https://www.youtube.com/watch?v=asn4h2O-WNw"
            },
            "White Pod Steps": {
                "info": "White WiFi Pod setup: 1. Plug the Pod into a power socket halfway between your Hub and the area with poor WiFi. 2. Wait for the light to turn solid white. This can take a few minutes. If the light pulses green for more than 10 minutes, try moving it closer to the Hub.",
                "url": "https://www.virginmedia.com/help/check/status/guide/black-pods/advice" # Same URL as black pod
            },
            "Booster Info": "A WiFi Booster is an older device. If you have a Booster, the setup steps are different from a WiFi Pod. Please clarify if you have a black Pod, white Pod, or a Booster."
        },
        "Diagnosis": {
            "Service Status Page": {
                "info": "To help diagnose issues, please visit our service status page.",
                "url": "https://www.virginmedia.com/help/check/status/identification/identify"
            }
        },
        "General": {
            "Order Tracking": {
                "info": "You can track your order online.",
                "url": "https://www.virginmedia.com/help/track-my-order"
            },
            "Refer a Friend": {
                "info": "Refer a friend and get rewarded!",
                "url": "https://virginmedia.aklamio.com/"
            },
            "Installation Page": {
                "info": "Find out more about QuickStart installation.",
                "url": "https://www.virginmedia.com/broadband/installation"
            },
            "Engineer Booking Info": {
                "info": "If you need an engineer, you can request one during checkout. Note that this may incur a £30 cost for pre-order customers.",
                "url": "https://www.virginmedia.com/help/check-wall-socket/check-postcode"
            }
        }
    }

    # Navigate through the knowledge base
    if category in knowledge_base:
        if item in knowledge_base[category]:
            if sub_item and isinstance(knowledge_base[category][item], dict) and sub_item in knowledge_base[category][item]:
                return {"content": knowledge_base[category][item][sub_item]}
            elif not sub_item and isinstance(knowledge_base[category][item], str):
                return {"content": knowledge_base[category][item]}
            elif not sub_item and isinstance(knowledge_base[category][item], dict) and "info" in knowledge_base[category][item]:
                return {"content": knowledge_base[category][item]["info"]}
            elif not sub_item and isinstance(knowledge_base[category][item], dict) and "url" in knowledge_base[category][item]:
                return {"content": knowledge_base[category][item]["url"]}
            else:
                return {"error": f"Could not find specific sub-item '{sub_item}' for '{item}' in '{category}'."}
        else:
            return {"error": f"Could not find item '{item}' in category '{category}'."}
    else:
        return {"error": f"Could not find category '{category}' in the knowledge base."}