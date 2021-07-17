import math
from datetime import datetime, timedelta

from rest_framework.views import APIView
from rest_framework.response import Response

from period_cycle_api.models import PeriodCylceModel
from period_cycle_api.serializers.event_serializer import EventSerializer
from period_cycle_api.lib.date_format import format_date


class CycleEvent(APIView):
    serializer_class = EventSerializer
    db_data = PeriodCylceModel.objects.get(id=1)

    last_period_date = db_data.last_period_date
    start_date = db_data.start_date
    end_date = db_data.end_date
    cycle_average = db_data.cycle_average
    period_average = db_data.period_average
    total_created_cycle = db_data.total_created_cycle

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            date = data.get('event_date', '')
            date_obj = datetime.strptime(format_date(date), "%d/%m/%Y")

            days_range = self.end_date - self.start_date
            period_start_date = datetime.strptime(self.last_period_date, "%d/%m/%Y") 
            # period_end_date = period_start_date + self.period_average

            numbers_list = list(range(1, days_range.days + 1))

            ovulation_list = [numbers_list[i:self.cycle_average]
                              for i in range(0, len(numbers_list), self.period_average)]

            return Response({"date_obj": date_obj, "period_start_date": period_start_date})
        return Response({"Info": "something else"})
