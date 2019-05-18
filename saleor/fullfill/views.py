from django.http import Http404, JsonResponse
from ..order.models import Order
from ..payment.models import Payment
from ..payment import ChargeStatus

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def fullfill(request, order_id):
    requester_ip = get_client_ip(request)
    if not requester_ip == '127.0.0.1' and not requester_ip == '80.211.72.95':
        raise Http404

    if not order_id:
        return JsonResponse({ 'status': 'MISSING' })

    order = Order.objects.get(id=order_id)

    if not order:
        return JsonResponse({ 'status': 'NO' })

    charge_status = order.get_payment_status()

    if charge_status == ChargeStatus.FULLY_CHARGED:
        return JsonResponse({ 'status': 'ALREADY' })


    order.payments.create(charge_status=ChargeStatus.FULLY_CHARGED, total=order.total.gross.amount)
    return JsonResponse({'status': 'OK'})

def getInfo(request, order_id):
    requester_ip = get_client_ip(request)

    if not requester_ip == '127.0.0.1' and not requester_ip == '80.211.72.95':
        raise Http404

    if not order_id:
        return JsonResponse({ 'status': 'MISSING' })

    order = Order.objects.get(id=order_id)

    if not order:
        return JsonResponse({ 'status': 'NO' })

    charge_status = order.get_payment_status()

    if charge_status == ChargeStatus.FULLY_CHARGED:
        return JsonResponse({ 'status': 'ALREADY' })


    return JsonResponse({'amount': order.total.gross.amount, 'currency': order.total.gross.currency, 'status': 'OK'});