from django.urls import path

from basiccruds.api_views.employee_view import EmployeeView


urlpatterns = [
    path('emp', EmployeeView.as_view(), name='employee'),
    path('delete-emp/<int:pk>', EmployeeView.as_view(), name='employee-delete')
]