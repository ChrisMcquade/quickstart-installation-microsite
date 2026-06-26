from typing import Any, Optional

def fake_tool_call(tool, input, callback_context) -> Optional[dict[str, Any]]:
    # Test/simulator only. The real tool runs in the browser via registerClientSideFunction.
    return {"status": "OK"}