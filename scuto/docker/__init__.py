from scuto.config import config
from scuto.util.decorators import asynchronos
from .dockerhub import search_image
import docker


client = docker.DockerClient(**config['Docker'])

@asynchronos
def pull_image(repo: str, tag='latest'):
    return client.images.pull(name, tag)

@asynchronos
def start_container(repo: str, environment={}, ports={}):
    return client.containers.run()