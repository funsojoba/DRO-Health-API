from datetime import date, datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from period_cycle_api.serializers import CycleSerializer


class EstimateCycleView(APIView):
    serializer_class = CycleSerializer
    date_format = "%d/%m/%Y"

    def format_date(self, date):
        initial_date = date.split('-')
        return "/".join(initial_date[::-1])

    def calculate_cycle(self, cycle_average, period_average, date_difference):
        if (cycle_average + period_average) < date_difference:
            return date_difference/(cycle_average + period_average)
        return 1

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        initial_start_date = data.get('start_date', '')
        initial_end_date = data.get('end_date', '')
        period_average = data.get('period_average', '')
        cycle_average = data.get('cycle_average', '')

        if serializer.is_valid():
            start_date = self.format_date(initial_start_date)
            end_date = self.format_date(initial_end_date)

            start_date_time_obj = datetime.strptime(
                start_date, self.date_format)
            end_date_time_obj = datetime.strptime(end_date, self.date_format)

            date_difference = end_date_time_obj - start_date_time_obj

            cycle = self.calculate_cycle(cycle_average=int(cycle_average), period_average=int(
                period_average), date_difference=date_difference.days)

            return Response({"data": serializer.data, "total_created_cycles": cycle})
        return Response(serializer.errors)
