from django.http import Http404, JsonResponse
from ..order.models import Order
from ..payment.models import Payment
from ..payment import ChargeStatus

def fullfill(request, order_id):
    requester_ip = request.META['REMOTE_ADDR']
    if not requester_ip == '127.0.0.1' and not requester_ip == '80.211.72.95':
        raise Http404

    if not order_id:
        raise Http404

    order = Order.objects.get(id=order_id)
    if order.is_fully_paid:
        raise Http404

    if not order:
        raise Http404

    order.payments.create(charge_status=ChargeStatus.FULLY_CHARGED, total=order.total.gross.amount)
    return JsonResponse({'status': 'OK'})

def getInfo(request, order_id):
    requester_ip = request.META['REMOTE_ADDR']

    # if not requester_ip == '127.0.0.1' and not requester_ip == '80.211.72.95':
    #     raise Http404


    if not order_id:
        raise Http404

    order = Order.objects.get(id=order_id)

    if not order:
        raise Http404

    # if order.is_fully_paid:
    #     raise Http404


    return JsonResponse({'amount': order.total.gross.amount, 'currency': order.total.gross.currency, ip: requester_ip});