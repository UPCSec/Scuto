import docker
from scuto.config import config
from .dockerhub import search_image


client = docker.DockerClient(**config['Docker'])

async def pull_image(repo, tag='latest'):
    client.images.pull(name, tag)
