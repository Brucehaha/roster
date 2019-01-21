from datetime import timedelta, date
from core import models


class ShiftFilter:
    """
            The minimum set of rules that the external algorithm would consider are:
            - Minimum of 10hr overnight rest
            - Maximum of 5 days working out of 7 any rolling 7 day window
            - Maximum of 5 days working in a row
    """
    def __init__(self, serializers, *args, **kwargs):
        self.serializers = serializers
        self.date = self.serializers.validated_data['date']
        self.employee = self.serializers.validated_data['employee']
        self.shift_type = self.serializers.validated_data['shift_type']
        self.array_list = list()

    def respond(self):
        response = self.rest_10hrs()
        if response['status']:
            response = self.five_day_max()
            if response['status']:
                response = self.five_day_in_row()

        return response

    def rest_10hrs(self):
        """
        Minimum of 10hr overnight rest:
        Minimum wait one day for next shift,e.g bruce take 5AM to 1:30PM, the minimum gap is
        take the next day 5AM to 1:30PM
        """
        response = {'error_message': "%s must have 10hrs rest"
                                     % self.serializers.validated_data['employee'],
                    'status': False
                    }
        response1 = {'error_message': "%s can not work more than 1 shift in the same time"
                                      % self.serializers.validated_data['employee'],
                     'status': False
                     }

        yesterday = self.date + timedelta(days=1)
        tomorrow = self.date - timedelta(days=1)
        date_list = [self.date, tomorrow, yesterday]

        data_list = models.Shift.objects. \
            filter(employee=self.employee, date__in=date_list). \
            values("date", "employee", "shift_type")
        data_list = list(data_list)

        if self.shift_type == 1:
            if {"date": self.date, "employee": self.employee.id, "shift_type": 1} in data_list:
                return response1
            if {"date": self.date, "employee": self.employee.id, "shift_type": 2} in data_list:
                return response
            if {"date": self.date, "employee": self.employee.id, "shift_type": 3} in data_list:
                return response
            if {"date": yesterday, "employee": self.employee.id, "shift_type": 2} in data_list \
                    or {"date": yesterday, "employee": self.employee, "shift_type": 3} in data_list:
                return response1
        if self.shift_type == 3:
            if {"date": self.date, "employee": self.employee.id, "shift_type": 3} in data_list:
                return response1
            if {"date": self.date, "employee": self.employee.id, "shift_type": 1} in data_list:
                return response
            if {"date": self.date, "employee": self.employee.id, "shift_type": 2} in data_list:
                return response
            if {"date": tomorrow, "employee": self.employee.id, "shift_type": 1} in data_list \
                    or {"date": yesterday, "employee": self.employee.id, "shift_type": 2} in data_list:
                return response
        if self.shift_type == 2:
            if {"date": self.date, "employee": self.employee.id, "shift_type": 2} in data_list:
                return response1
            if {"date": self.date, "employee": self.employee.id, "shift_type": 1} in data_list:
                return response
            if {"date": self.date, "employee": self.employee.id, "shift_type": 3} in data_list:
                return response
            if {"date": yesterday, "employee": self.employee.id, "shift_type": 3} in data_list \
                    or {"date": tomorrow, "employee": self.employee.id, "shift_type": 1} in data_list:
                return response
        response['status'] = True
        return response

    def five_day_max(self):
        """
        Maximum of 5 days working out of 7 any rolling 7 day window
        7 different date range to check, e.g. if new shift date is day 12,  ranges are:
        12-18
        11-17
        10-16
        .....
        6-12
        :return: response
        """
        response = {'error_message': "%s can only work 5 days in a any 7 days"
                                     % self.serializers.validated_data['employee'],
                    'status': False
                    }
        # day 6-18 range
        start_date = self.date-timedelta(days=6)
        end_date = self.date + timedelta(days=6)
        queryset = models.Shift.objects.\
            filter(employee=self.employee, date__range=(start_date, end_date)).\
            values_list('date')
        if queryset:
            query_list = [[*x] for x in zip(*queryset)]
            self.array_list.append(self.date)
            # date list that employee Bruce work between day 6-18
            self.array_list.extend(query_list[0])
        return self.days_work_check(self.date, end_date, response)

    def five_day_in_row(self):
        """
        employee cannot work 5 days in a row,if today is day 12, need to check
        the shift between day 7-17, if get 5 consecutive date in it
        :return: response
        """
        array_list = list()
        array_list.append(self.date)
        start_date = self.date - timedelta(days=5)
        end_date = self.date + timedelta(days=5)
        queryset = models.Shift.objects.\
            filter(employee=self.employee, date__range=(start_date, end_date)).\
            values_list('date')
        if queryset:
            query_list = [[*x] for x in zip(*queryset)]
            array_list.extend(query_list[0])
            array_list = sorted(array_list, reverse=True)
            print(array_list)
        return self.is_consecutive(array_list, 5)

    def is_consecutive(self, a, c):
        """
         accept a reversed date list and if, eg. 2019.1.7 - 2019.1.17 == timedelta
          then the dates above is consecutive, the number of consecutive date equal to 'c',
          then assign value to result, then break. if not consecutive, but the left number of date in list
          is less than 'c', then break, return default 'result'. else, recursive execute the left date in list
         :param a: sorted reverse date list
         :param c: required consecutive date in list
         :return: dictionary
         """
        n = 2
        response = {'error_message': "%s cannot work 5 days in row"
                                     % self.serializers.validated_data['employee'],
                    'status': True
                    }

        while len(a) > 1:
            current = a.pop()
            next_date = a.pop()
            if next_date - current == timedelta(1):
                print("n", n)
                if n == c+1:
                    response['status'] = False
                    return response
                a.append(next_date)
                n += 1
                print("a", len(a))
            # the left data in a < 6, the maximum of a is 5 then
            elif len(a) < c+1:
                break
            else:
                a.append(next_date)
                return self.is_consecutive(a, c)
        return response

    def days_work_check(self, start_date, end_date, response):
        """ recursive loop start from day 12-18"""
        delta = end_date-start_date
        print(delta)
        date_list = [start_date + timedelta(i) for i in range(delta.days + 1)]
        print("12-18", date_list)
        count = 0
        for i in self.array_list:
            if i in date_list:
                count += 1
        print('count', count)
        if count == 6:
            return response
        else:
            if end_date > self.date:
                # if during day 12 to day 18, employee bruce work less than 6 days, check day 11 to 17
                return self.days_work_check(start_date-timedelta(1), end_date-timedelta(1), response)
            else:
                response['status'] = True
                return response
