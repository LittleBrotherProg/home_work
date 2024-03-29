from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']

    def create(self, validated_data):
        return super().create(validated_data)


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['id','product', 'quantity', 'price']



class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    
    class Meta:
        model = Stock
        fields = ['id','address', 'positions']
    # настройте сериализатор для склада
    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        for position in positions:
            StockProduct.objects.create(stock = stock,  **position)
        

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        for position in positions:
            StockProduct.objects.update_or_create(
                                                    stock=stock.pk,
                                                    product = position['product'].pk,
                                                    defaults={
                                                                'price': position['price'],
                                                                'quantity': position['quantity']
                                                    }
            )
            
        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock
