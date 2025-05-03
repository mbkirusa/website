import http.server
import socketserver
import os

# Define the port to run the server on
PORT = 8000

# Set the directory to serve files from (current directory)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create a handler for serving files
Handler = http.server.SimpleHTTPRequestHandler

# Create the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print(f"Access the homepage at: http://localhost:{PORT}/html/homepage.html")
    print("Press Ctrl+C to stop the server.")
    
    # Start the server and keep it running until interrupted
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()