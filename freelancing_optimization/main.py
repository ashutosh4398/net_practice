# each job has a deadline ie NO PAY AFTER EXCEEDING DEADLINE
# EACH JOB HAS A PAYMENT
# MAX PROFIT IN 7 DAY PERIOD
# NOTE: EACH JOB REQUIRES 1 DAY TO COMPLETE
# NOTE: NUMBER OF DAYS IS 7

from typing import Dict, List
from enum import Enum

class Constants(Enum):
    PAYMENT = "payment"
    DEADLINE = "deadline"
    MAX_DAYS = 7


def optimalFreelancing(jobs: List[Dict[str, int]]) -> int:
    # Write your code here.
    # sort the jobs based on profits,deadline in descending order
    max_number_of_days: int = 7
    payment_on_each_day : List[int] = [ 0 for _ in range(max_number_of_days)]
    jobs_sorted_in_max_payment_order: List[Dict[str, int]] = (
        sorted(
            jobs, 
            key=lambda x: (x[Constants.PAYMENT.value], x[Constants.DEADLINE.value]), 
            reverse=True
        )
    )

    for jobs in jobs_sorted_in_max_payment_order:
        payment, deadline = jobs[Constants.PAYMENT.value], jobs[Constants.DEADLINE.value]
        deadline = deadline - 1
        if deadline >= max_number_of_days:
            deadline = max_number_of_days - 1
        for i in range(deadline, -1, -1):
            if payment_on_each_day[i] == 0:
                payment_on_each_day[i] = payment
                break
            
    return sum(payment_on_each_day)


jobs = [
    {
      "deadline": 1,
      "payment": 1
    },
    {
      "deadline": 24,
      "payment": 2
    },
    {
      "deadline": 2,
      "payment": 1
    }
]

print(optimalFreelancing(jobs))