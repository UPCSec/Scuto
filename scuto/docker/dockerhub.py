from scuto.util.decorators import asynchronos
import aiohttp


async def search_image(repo, page=1, page_size=25, **kwargs):
    async with aiohttp.ClientSession() as session:
        url = 'https://hub.docker.com/api/content/v1/products/search'
        params = {
            'q': repo,
            'type': 'image',
            'page': page,
            'page_size': page_size
        }
        headers = {
            'Search-Version': 'v3'
        }
        async with session.get(url, params=params, headers=headers) as resp:
            result = await resp.json()
            return result