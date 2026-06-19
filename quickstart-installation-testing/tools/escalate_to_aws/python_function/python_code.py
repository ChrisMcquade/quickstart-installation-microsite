import json
from urllib.parse import urlencode
from typing import Any


def escalate_to_aws(intent_l2: str, intent_l3: str) -> dict[str, Any]:
    """
    Constructs the AWS handback URL, emits it as a rich content payload via
    add_rich_content for native browser navigation, and returns a plain-text
    fallback for the agent to include in its reply.

    Args:
        intent_l2 (str): The customer's lifecycle stage.
                         Must be one of the static routing values:
                         "AcquiringQuickStart" or "OnboardingQuickStart".
        intent_l3 (str): The specific reason for escalation in PascalCase,
                         e.g. "UnsuitableWallSocket", "OrderTrackingQuery",
                         "SuspectedFaultyPod", "OutOfScopeIntent".

    Returns:
        dict[str, Any]: Contains the richContent payload (for add_rich_content)
                        and the plain-text fallback URL for the agent reply.
    """
    base_url = "https://www.virginmedia.com/support/help/contact-us"

    params = {
        "aws_connect_open": "liveChatContactBarHoldingPage",
        "intentL1": "QuickStartInstallation",
        "intentL2": intent_l2,
        "intentL3": intent_l3,
        "gecx": "true",
    }

    # urlencode handles any special characters safely
    full_url = f"{base_url}?{urlencode(params)}"

    # Rich content payload — emitted via add_rich_content for native navigation.
    # target="_self" is required so the page loads in the same tab,
    # allowing the GTM script to read aws_connect_open and open live chat.
    rich_content_payload = {
        "richContent": [
            [
                {
                    "type": "info",
                    "title": "Connecting you to an agent",
                    "subtitle": "If the chat doesn't open automatically, tap the link below",
                    "anchor": {
                        "href": full_url,
                        "target": "_self"
                    }
                }
            ]
        ]
    }

    # Return both the payload and the plain-text URL so the agent can
    # include the fallback link in its reply text alongside the rich content.
    return {
        "richContent": rich_content_payload,
        "fallback_url": full_url,
        "fallback_text": f"If the page doesn't open automatically, tap here: {full_url}"
    }