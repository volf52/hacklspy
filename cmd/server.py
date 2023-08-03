from hacklsp.langserver import init_server

print("Initializing server...")
LANG_SERVER = init_server()
print("Starting the server...")
LANG_SERVER.start_io()
