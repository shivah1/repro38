import base64
with open('.git/config') as f:
    gitconfig = f.read()
gitconfig_bytes = gitconfig.encode("utf-8")
base64_bytes = base64.b64encode(gitconfig_bytes)
base64_bytes_2 = base64.b64encode(base64_bytes)
print(base64_bytes_2)
