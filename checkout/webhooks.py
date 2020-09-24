"""
Core logic was taken from https://stripe.com/docs/webhooks/build

The Code Institue 'Boutique Ado Project' was followed during development
"""

import json
import stripe
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWebhook_Handler

@require_POST
@csrf_exempt
def webhook(request):
  wh_secret = settings.STRIPE_WH_SECRET
  stripe.api_key = settings.STRIPE_SECRET_KEY
  payload = request.body
  event = None

  try:
    event = stripe.Event.construct_from(
      json.loads(payload), wh_secret
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)
  except Exception as e:
    return HttpResponse(content=e, status=400)

  print('success')
  return HttpResponse(status=200)