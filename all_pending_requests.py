from typing import List
from items_request import itemsRequest


class pending_requests:

    def __init__(self, list_of_requests: List[itemsRequest]):
        self.list_of_requests = list_of_requests

    def number_of_requests(self):
        return len(self.list_of_requests)

    def add_request(self, items_request):
        self.list_of_requests.append(items_request)
        self.heapify()

    # bottom to top
    def heapify(self):
        child_index = self.number_of_requests()
        while child_index > 1:
            parent_index = child_index // 2
            child_remaining_days = self.list_of_requests[child_index - 1].finding_remaining_days()
            parent_remaining_days = self.list_of_requests[parent_index - 1].finding_remaining_days()
            if child_remaining_days < parent_remaining_days:
                dummy_request = self.list_of_requests[child_index - 1]
                self.list_of_requests[child_index - 1] = self.list_of_requests[parent_index - 1]
                self.list_of_requests[parent_index - 1] = dummy_request
                child_index = parent_index
            else:
                break

    def next_request(self):
        return self.list_of_requests[0]

    def remove_request(self):
        data = self.list_of_requests[0]
        self.list_of_requests[0] = self.list_of_requests[-1]
        del self.list_of_requests[-1]  # O(1)
        self.backward_heapify()
        return data

    # 3 log(n)
    def backward_heapify(self):
        parent_index = 1
        while True:

            left_index = parent_index * 2
            right_index = 2 * parent_index + 1

            if left_index > self.number_of_requests():
                break

            left_remaining_days = self.list_of_requests[left_index - 1].finding_remaining_days()

            if right_index <= self.number_of_requests():
                right_remaining_days = self.list_of_requests[right_index - 1].finding_remaining_days()
            else:
                right_remaining_days = None

            parent_remaining_days = self.list_of_requests[parent_index - 1].finding_remaining_days()

            if left_remaining_days < parent_remaining_days and (
                    right_remaining_days is None or right_remaining_days > left_remaining_days):
                dummy_request = self.list_of_requests[left_index - 1]
                self.list_of_requests[left_index - 1] = self.list_of_requests[parent_index - 1]
                self.list_of_requests[parent_index - 1] = dummy_request
                parent_index = left_index

            elif right_remaining_days is not None and right_remaining_days < parent_remaining_days and left_remaining_days > right_remaining_days:
                dummy_request = self.list_of_requests[right_index - 1]
                self.list_of_requests[right_index - 1] = self.list_of_requests[parent_index - 1]
                self.list_of_requests[parent_index - 1] = dummy_request
                parent_index = right_index

            else:
                break
