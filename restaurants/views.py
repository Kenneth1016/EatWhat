from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from restaurants.models import Restaurant, OrderMain, OrderDetail, Food
from restaurants.forms import CreateOrderMainForm
from django.http import HttpResponse

from django.utils.timezone import utc
import calendar
import datetime
import time

def order(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')


    if request.POST:
        f = CreateOrderMainForm(request.POST)
        if f.is_valid():
            orderDate = f.cleaned_data['orderDate']
            r = f.cleaned_data['restaurant']
            memo = f.cleaned_data['memo']
            createId = request.user
            createAt = datetime.datetime.now()
            restaurant = Restaurant.objects.get(id=r)
            orderDueDate = f.cleaned_data['orderDueDate']
            c = OrderMain.objects.create(
                orderDate=orderDate,
                createId=createId,
                createAt=createAt,
                restaurant=restaurant,
                valid=True,
                orderable=True,
                memo=memo,
                orderDueDate=orderDueDate)
            f = CreateOrderMainForm()
    else:
        f = CreateOrderMainForm(initial={'orderDate':str(datetime.date.today()),
                                         'orderDueDate':str(datetime.datetime.now()+datetime.timedelta(hours=3))})

    todayDatetime = datetime.datetime.now()
    restaurants = Restaurant.objects.all()

    return render_to_response('order.html', RequestContext(request, locals()))

def follow(request):
    todayDate = datetime.date.today()
    orderMains = OrderMain.objects.order_by('-orderDate').filter(orderDate__gte=todayDate)
    return render_to_response('follow.html', RequestContext(request, locals()))

def followDetail(request,orderId):
    orderMain = OrderMain.objects.get(id=orderId)
    orders = orderMain.orderdetail_set.filter(valid=True)
    foods = orderMain.restaurant.food_set.all

    todayDatetime = datetime.datetime.utcnow().replace(tzinfo=utc).strftime("%Y/%m/%d %H:%M")
    dueDate = orderMain.orderDueDate.strftime("%Y/%m/%d %H:%M")
    #start = calendar.timegm(datetime.datetime.utcnow().replace(tzinfo=utc).timetuple())
    #due = calendar.timegm(orderMain.orderDueDate.timetuple())

    startStamp = time.mktime(datetime.datetime.utcnow().replace(tzinfo=utc).timetuple())
    dueStamp = time.mktime(orderMain.orderDueDate.timetuple())

    if orderMain.valid == True and dueStamp > startStamp:
        isOrderAble = True
    else:
        isOrderAble = False

    return render_to_response('followDetail.html', RequestContext(request, locals()))

def saveOrderDetail(request):
    OrderMainId = request.POST.get('orderMainId', '')
    FoodId = request.POST.get('foodId', '')
    TxtMemo = request.POST.get('txtMemo', '')
    food = Food.objects.get(id=FoodId)
    orderMain = OrderMain.objects.get(id=OrderMainId)

    o = OrderDetail.objects.create(
        orderMain=orderMain,
        createId=request.user,
        createAt=datetime.datetime.now(),
        valid=True,
        food=food,
        memo=TxtMemo,
        isPaid=False,
        money=food.price)


    orders = orderMain.orderdetail_set.filter(valid=True)



    return render_to_response('includeFollowList.html', RequestContext(request, locals()))
    #return HttpResponse(OrderMainId + FoodId + TxtMemo + str(food.price))

def cancelOrderDetail(request):
    OrderMainId = request.POST.get('orderMainId', '')
    orderDetailId = request.POST.get('orderDetailId', '')

    oDetail = OrderDetail.objects.get(id=orderDetailId)
    oDetail.valid=False
    oDetail.save()
    orderMain = OrderMain.objects.get(id=OrderMainId)
    orders = orderMain.orderdetail_set.filter(valid=True)
    return render_to_response('includeFollowList.html', RequestContext(request, locals()))
    #return HttpResponse(OrderMainId + orderDetailId)