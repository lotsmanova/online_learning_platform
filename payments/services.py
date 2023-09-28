import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY

def get_session(instance):
    """ Функция возвращает сессию для оплаты """

    title_product = f"{instance.lesson}" if instance.lesson else ''

    product = stripe.Product.create(name=f'{title_product}')
    price = stripe.Price.create(
        unit_amount=instance.payment_amount,
        currency='rub',
        product=f'{product.id}',
    )

    session = stripe.checkout.Session.create(
        success_url="http://example.com/success",
        line_items=[
            {
                'price': f'{price.id}',
                'quantity': 1,
            }
        ],
        mode='payment',
        customer_email=f'{instance.user.email}'

    )
    return session


def retrieve_session(session):
    """ Функция возвращает объект сессии по API """

    return stripe.checkout.Session.retrieve(session)

