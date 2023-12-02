from invokeai.app.invocations.baseinvocation import (
    invocation,
    BaseInvocation,
    InputField,
    InvocationContext
)
from invokeai.app.invocations.primitives import (
    StringOutput
)

from lib_unprompted.shared import Unprompted

Unprompted = Unprompted()

@invocation(
    "unprompted",
    title="Unprompted",
    tags=["string", "prompt" ],
    category="image",
    version="1.0.0"
)
class UnpromptedInvocation(BaseInvocation):
    """Processes an Unprompted template"""

    template: str = InputField(description="The Unprompted template to process", title="Template")
    
    def invoke(self, context: InvocationContext) -> StringOutput:
        Unprompted.shortcode_user_vars = {}
        result: str = Unprompted.start(self.template)
        Unprompted.cleanup()
        return StringOutput(value=(result))