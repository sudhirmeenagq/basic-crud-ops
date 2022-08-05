import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from sqlalchemy import select
from basiccruds.models import Employee
# from basiccruds.serializers import EmployeeSerializer
from rest_framework.versioning import NamespaceVersioning
from rest_framework import status
# from sqlalchemy.orm import Session
from basiccrudops.settings import DB_SESSION as session


class EmployeeView(APIView):
    """
        Employee View Class
    """
    def get(self, request, format=None):
        # snippets = Employee
        # serializer = EmployeeSerializer(snippets, many=True)
        stmt = select(Employee)
        data = []
        res = session.scalars(stmt)
        for emp in session.scalars(stmt):
            data.append({"name": emp.name, "mobile": emp.mobile})
        return Response(data)

    def post(self, request):
        newEmp = Employee(name=request.data["name"], mobile=request.data["mobile"])
        session.add(newEmp)
        session.commit()
        return Response({"message": "success"})
        

    def put(self, request, pk, format=None):
        # snippet = self.get_object(pk)
        stmt = select(Employee).where(Employee.name == "test")
        employee = session.scalars(stmt).one()
        employee.name = request.data["name"]
        employee.mobile = request.data["mobile"]
        session.commit()
        return Response({"message": "success"})

    def delete(self, request, pk, format=None):
        employee_to_delete = session.get(Employee, pk)
        session.flush()
        session.delete(employee_to_delete)
        session.commit()
        return Response({"message": "success"})