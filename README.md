# Encrypt on python 

This is my project, which provides the functionality of encrypting and decrypting files and text using various algorithms such as 3DES, AES, Blowfish,Cast5 and Grasshopper.

## Installation

### Using Docker

1. Clone the repository:

```
    git clone https://github.com/sl4sh73r/BlockCryptoPrac
```

2. Navigate to the project directory:

```
    cd directory-name
```

3. Build the Docker image:

```
    docker build -t kunin .
```

4. Run the Docker container:

```
    docker run -it --name kunin-container -p 3000:3000 kunin
```

The application is now available at `http://localhost:3000`.

### Manual Installation

1. Clone the repository:

```
    git clone https://github.com/sl4sh73r/BlockCryptoPrac
```

2. Navigate to the project directory:

```
    cd directory-name
```

3. Install Node.js dependencies:

```
    npm install
```

4. Install Python dependencies:

```
    pip install -r backend/algorithms/requirements.txt
```

5. Start the server:

```
    node backend/server.js
```

The application is now available at `http://localhost:3000`.

---


这是我的项目，它提供了使用各种算法（如3DES、AES、Cast、5Blowfish和Grasshopper）加密和解密文件和文本的功能。

## 安装

### 使用 Docker

1. 克隆仓库：

```
    git clone https://github.com/sl4sh73r/BlockCryptoPrac
```

2. 导航到项目目录：

```
    cd directory-name
```

3. 构建 Docker 镜像：

```
    docker build -t kunin .
```

4. 运行 Docker 容器：

```
    docker run -it --name kunin-container -p 3000:3000 kunin
```

应用程序现在可以在 `http://localhost:3000` 上使用。

### 手动安装

1. 克隆仓库：

```
    git clone https://github.com/sl4sh73r/BlockCryptoPrac
```

2. 导航到项目目录：

```
    cd directory-name
```

3. 安装 Node.js 依赖项：

```
    npm install
```

4. 安装 Python 依赖项：

```
    pip install -r backend/algorithms/requirements.txt
```

5. 启动服务器：
```

    node backend/server.js
```

应用程序现在可以在 `http://localhost:3000` 上使用。
