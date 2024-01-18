from django.urls import path
from .views import UserViews,UsergetUpdateDelete
urlpatterns = [
    path('user',UserViews.as_view(), name='User Create and get'),
    path('user/<int:pk>',UsergetUpdateDelete.as_view(), name='User update'),

]


    # path('role', UserRoleImplementation.as_view(
    #     {'post': 'addRole', 'get': 'getAllRole'}), name='Role'),
    # path('role/<int:pk>', UserRoleImplementation.as_view(
    #     {'put': 'updateRoleById', 'delete': 'deleteRoleById',
    #         'get': 'getRoleById'}), name='Role_detail'),