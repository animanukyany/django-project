
def product_serializer(obj):
    data = {
        "id": obj.id,
        "name": obj.name,
        "description": obj.description,
        "price": float(obj.price),
        "is_available": obj.is_available
    }
    return data