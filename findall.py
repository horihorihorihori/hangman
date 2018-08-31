import re

message = "Agent Alice gave Agent Bou"

greedy_Ha_regex = re.compile(r'Agent (\w)\w*', re.I )

mo2 = greedy_Ha_regex.sub(r'\1***',message)

print(mo2)


