

'''
    A logs parser for my node app:
    * Parse logs to yield state and datetime elements.
    * Calculate request average execution time.
'''

# ================================================================================
# Imports

from datetime import datetime


# ================================================================================
# Raw logs

logs = '''5/20/2020, 8:04:28 AM: 8cae9336-4f9d-471e-85ab-311bc937dab0 - User RNO requested for resource
5/20/2020, 8:04:35 AM: 8cae9336-4f9d-471e-85ab-311bc937dab0 - Finished processing request for RNO
5/20/2020, 8:08:06 AM: 069d3948-a0a5-4dee-8e4b-b153b3f131f1 - User RNO requested for resource
5/20/2020, 8:08:07 AM: d37df622-4bd1-4e32-9591-7b30d92e154c - User RNO requested for resource
5/20/2020, 8:08:08 AM: 39050a8d-1d14-4136-9988-0409e80fba29 - User RNO requested for resource
5/20/2020, 8:08:09 AM: 1211cca9-a7c6-459b-9840-b0f44fe8559b - User RNO requested for resource
5/20/2020, 8:08:11 AM: 069d3948-a0a5-4dee-8e4b-b153b3f131f1 - Finished processing request for RNO
5/20/2020, 8:08:13 AM: 1211cca9-a7c6-459b-9840-b0f44fe8559b - Finished processing request for RNO
5/20/2020, 8:08:14 AM: 39050a8d-1d14-4136-9988-0409e80fba29 - Finished processing request for RNO
5/20/2020, 8:08:16 AM: d37df622-4bd1-4e32-9591-7b30d92e154c - Finished processing request for RNO'''


# ================================================================================
# Functions

def parse_logs(logs):

    lines = logs.split('\n')

    for line in lines:

        date_time_raw, data_rest = line.split(': ')

        date_time = datetime.strptime(date_time_raw, '%m/%d/%Y, %H:%M:%S %p')

        id, state = data_rest.strip().split(' - ')
        id, state = id.strip(), state.strip()
        clear_state = "start" if "requested" in state else "end"

        if not request_data.get(id):
            request_data[id] = dict(start=0, end=0)

        if clear_state == "start":
            request_data[id]["start"] = date_time
        if clear_state == "end":
            request_data[id]["end"] = date_time

    return request_data


def calculate_avg_req_time(request_data):

    exec_times = [(request_data[request]["end"] - request_data[request]["start"]).total_seconds() for request in request_data]
    return sum(exec_times) / len(exec_times)


# ================================================================================
# Main

if __name__ == "__main__":

    request_data = {}
    request_data = parse_logs(logs)

    avg_req_time = calculate_avg_req_time(request_data)
    print("The average execution time for the requests is of {s} seconds.".format(s=avg_req_time))
