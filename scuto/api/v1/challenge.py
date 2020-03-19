from scuto.models import Challenge, Flag
from scuto.docker import search_image
from scuto.util.decorators import jsonify
from .router import routes


load = 0

@routes('/challenge/search', methods=['GET'])
@jsonify()
async def search(request):
    term, page, page_size = request.query.get('q'), request.query.get('page'), request.query.get('page_size')
    if term:
        return await search_image(term, page, page_size)
    else:
        return {
            'status': 'failed',
            'error': 'Missing query'
        }

@routes('/challenge/get', methods=['GET'])
@jsonify()
async def get_challenge(request):
    challenge = Challenge.objects(id=request.query['id']).first().to_mongo()
    return challenge

@routes('/challenge/list', methods=['GET'])
@jsonify()
async def list_challenges(request):
    return list(Challenge.objects()
                .only('title', 'description', 'tags', 'file')
                .as_pymongo())

@routes('/admin/challenge/list', methods=['GET'])
@jsonify()
async def list_challenges(request):
    return list(Challenge.objects().only('title', 'image', 'tags').as_pymongo())

@routes('/challenge/edit', methods=['POST'])
@jsonify()
async def edit_challenge(request):
    updated = await request.json()
    if updated.get('_id'):
        challenge = Challenge.objects(id=updated['_id']).first()
        del updated['_id']
        for k in updated:
            challenge[k] = updated[k]
        challenge.save()
    else:
        del updated['_id']
        challenge = Challenge(**updated)
        challenge.save(force_insert=True)
    return {
        'status': 'success',
    }
