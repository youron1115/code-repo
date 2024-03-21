# WaterOff Query web crawler and notification

It's a WaterOff Query web crawler (adapt [WaterOff Query web crawler and notification](https://github.com/youron1115/Code-repo/tree/main/%E8%87%AA%E4%BE%86%E6%B0%B4%E4%BE%9B%E6%87%89%E9%80%9A%E7%9F%A5) for container run)

### Usage
1. Build a image
```powershell
docker build -t <image name> .
```
2. Run a container(If you do not input the environment variable, it will use the default address)
```powershell
docker run --name=<container name> -e "ADDRESS=<your address>" <image name>
```