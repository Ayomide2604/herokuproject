from django_unicorn.components import UnicornView, QuerySetType
from pages.models import UserItem
from django.contrib.auth.models import User
from django.db.models import F


class ProductView(UnicornView):
    user_products: QuerySetType[UserItem] = None
    user_pk: int
    total: int = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        self.user_products = UserItem.objects.filter(user=self.user_pk)

    def add_item(self, product_pk):
        item, created = UserItem.objects.get_or_create(
            user_id=self.user_pk, product_id=product_pk)
        if not created:
            item.quantity = F('quantity') + 1
            item.save()
        self.user_products = UserItem.objects.filter(user=self.user_pk)
