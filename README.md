# DuckDuckC2
A proof-of-concept C2 channel through DuckDuckGo's image proxy service. The provided example can be extended multiple ways to achieve different deployments.

For more information see my accompanying article: [Using DuckDuckGo's Image Proxy as a C2 Channel](https://nopcorn.github.io/2023/09/25/duckduckgo-as-c2).

*Disclaimer: This is a tool meant for red teaming and penetration testing and the author does not condone it being used in other ways*

## Demo

A modified `server.py` is hosted on [PythonAnywhere](https://pdxkmdcepvahysnnxe.pythonanywhere.com/image.jpg) for you to play with. Instead of executing the contents of the `cmd` parameter, it just reflects it back to the user embedded in the image (I didn't think providing a remote taskable shell to the world was in line with PythonAnywhere's terms of service).

The demo will eventually expire and you'll have to host it yourself to test it out.

Clone the repo, and use the client to connect through DuckDuckGo and onwards towards the server:

```
git clone https://github.com/nopcorn/DuckDuckC2
cd DuckDuckC2
python3 client.py
```

## Server

*Note: you'll have to deploy this somewhere internet-facing to use it. If you just want a quick way to try this, see the demo section above*

The provided server-side is a basic [Flask](https://flask.palletsprojects.com/en/) app which will accept requests for `/image.jpg`. It returns the `innocent-cat-pic.jpg` file. If a `cmd` parameter containing a shell command is provided to the endpoint, it will execute the command and return the result embedded in the image. Make the required changes to `server.py` before using.

```
cd server
pip install -r requirements  # flask
flask --app server run       # listening on tcp/5000
```

## Client

The client is a simple pseudo-shell that will make requests to the configured endpoint via DuckDuckGo's image proxy. Make the required changes to `client.py` before using.

```
cd client && python client.py
```