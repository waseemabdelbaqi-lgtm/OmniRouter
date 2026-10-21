import sys; sys.path.insert(0,'/home/user/OmniRouter/apes_project/tools')
from s4s_docx import *
b=Book("Test","/tmp")
b.new_section("AP Environmental Science · Test","Success4Sure Academy",first=True)
b.add_markdown('/home/user/OmniRouter/apes_project/build/test/t.md')
for _ in range(3): b.add_markdown('/home/user/OmniRouter/apes_project/build/test/t.md')
b.save('/home/user/OmniRouter/apes_project/build/test/t.docx')
