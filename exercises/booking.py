from datetime import date


class Booking():
    def __init__(self):
        self.dates = []

    def book(self, begin, end):
        new_begin = date.fromisoformat(begin)
        new_end = date.fromisoformat(end)
        if self._can_book(new_begin, new_end):
            self.dates.append((new_begin, new_end))
            return True
        return False

    def _can_book(self, begin, end):
        if begin >= end:
            return False
        for booked_begin, booked_end in self.dates:
            if begin < booked_end and end > booked_begin:
                return False
        return True
