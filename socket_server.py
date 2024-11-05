import socket

def send_custom_http_request():
    host = "10.0.2.2"
    port = 8000

    # 创建一个 TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # 构造 HTTP GET 请求
    request = (
        "GET /api_root/Post/ HTTP/1.1\r\n"
        "Authorization: Token bf46b8f9337d1d27b4ef2511514c798be1a954b8\r\n"
        "User-Agent: Dalvik/2.1.0 (Linux; U; Android 13; sdk_gphone64_arm64 Build/TPB4.220624.004)\r\n"
        "Host: 10.0.2.2:8000\r\n"
        "Connection: Keep-Alive\r\n"
        "Accept-Encoding: gzip\r\n"
        "\r\n"
    )

    # 发送请求
    client_socket.sendall(request.encode())

    # 接收服务器响应
    response = client_socket.recv(4096)
    print("Response from server:")
    print(response.decode(errors='ignore'))

    # 关闭连接
    client_socket.close()

if __name__ == "__main__":
    send_custom_http_request()
