class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def _calculate_total_and_count(self):
        total = sum(self.data)
        count = len(self.data)
        return total, count

    def calculate_total(self):
        total, _ = self._calculate_total_and_count()
        return total

    def calculate_average(self):
        total, count = self._calculate_total_and_count()
        return total / count if count != 0 else 0

    def _calculate_extreme_value(self, func):
        if self.data:
            return func(self.data)
        else:
            return None

    def calculate_minimum(self):
        return self._calculate_extreme_value(min)

    def calculate_maximum(self):
        return self._calculate_extreme_value(max)
