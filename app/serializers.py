from rest_framework import serializers
from .models import *

class poorvika_serializer(serializers.ModelSerializer):
    class Meta:
        model = Poorvika
        fields = "__all__"
        #  (

        #  'product_id',
        # 'item_code',
        # 'brand',
        # 'model_name',
        # 'poorvika',
        # 'flipkart',
        # 'amazon',
        # 'croma',
        # 'reliance',
        # 'vijaysales',
        # 'date'
        # )
 
class home_appliance_serializer(serializers.ModelSerializer):
    class Meta:
        models = HomeApplainces
        fields = "__all__"

        