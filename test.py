from lib_unprompted.shared import Unprompted

Unprompted = Unprompted()

Unprompted.shortcode_user_vars = {}
result: str = Unprompted.start("[choose]one|two|three[/choose]")
Unprompted.cleanup()

print(result)