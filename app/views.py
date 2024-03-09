from django.shortcuts import render

# Create your views here.
def home(request):
    # Fetching data (adjust according to your data source)
    # stock_data = StockData.objects.order_by('time')  
    # data = [
    #     {'time': item.time.strftime('%Y-%m-%d'), 'value': item.price}
    #     for item in stock_data
    # ]
    data = [
        {'time': '2023-03-06', 'value': 123.45},
        {'time': '2023-03-07', 'value': 115.80},
        {'time': '2023-03-08', 'value': 130.00},
        # ... add more data points if you want
    ]

    context = {'chart_data': data}
    return render(request, 'home.html',context)


def home2(request):
    return render(request, 'home2.html')

# urlpatterns = [
#     path('quote/<str:stock>/', views.quote, name='quote'),
# ]
# write the view function for the quote URL

def quote(request, asset='BTC'):
    return render(request, 'quote.html', {'asset': asset})

