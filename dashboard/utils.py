from django.core.serializers.python import Serializer
import matplotlib.pyplot as plt
import base64
from io import BytesIO

class LazyDashboardEncoder(Serializer):
    def get_dump_object(self, obj):
        dump_object = {}
        dump_object.update({'contact_us_message': str(obj.message)})
        dump_object.update({'user_name': str(obj.user_name)})
        return dump_object


def get_graph():
    # Create buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    # convert from base64 to utf-8 format
    graph = graph.decode('utf-8')
    # free buffer
    buffer.close()
    return graph


def get_plot(x, y):

    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title('Energy Cost')
    plt.plot(x, y)
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_usage_plot(x, y):

    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title('Energy Usage')
    plt.plot(x, y)
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Usage')
    plt.tight_layout()
    graph = get_graph()
    return graph

