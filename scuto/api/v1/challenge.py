from scuto.models import Challenge, Flag
from scuto.docker import search_image
from scuto.util.decorators import jsonify
from .router import routes


load = 0

@routes('/challenge/search')
@jsonify()
async def search(request):
    return search_image(**(await request.json()))

