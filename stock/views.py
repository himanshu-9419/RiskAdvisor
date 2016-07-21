from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from stock.models import Stock
from stock.serializers import StockSerializer

class JSONResponse(HttpResponse):
    
    #An HttpResponse that renders its content into JSON.
    
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def stock_list(request):
    
#List all code snippets, or create a new snippet.
    
    if request.method == 'GET':
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def stock_detail(request, pk):
        
    #Retrieve, update or delete a code snippet.
        
    try:
        stock = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StockSerializer(stock)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StockSerializer(stock, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Stock.delete()
        return HttpResponse(status=204)    