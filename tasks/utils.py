import io
import sys
from contextlib import redirect_stdout

def capture_output(func_to_run, *args, **kwargs):
    """
    Captures the print output of a function.
    Returns the captured output as a string.
    """
    captured_output = io.StringIO()
    original_stdout = sys.stdout
    try:
        sys.stdout = captured_output
        func_to_run(*args, **kwargs)
    finally:
        sys.stdout = original_stdout # Ensure stdout is restored even if an error occurs
    return captured_output.getvalue()

# Optional: Define input parameter types (if you added this from the later suggestion)
class ParamType:
    TEXT = "text_input"
    NUMBER = "number_input"
    SELECTBOX = "selectbox"
    # Add more as needed (slider, checkbox, etc.)