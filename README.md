[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cYbEVSqo)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17894035)

# I PEE PYTHON
The simplest subnet pinger.

## Features
- **Custom subnets.** Using CIDR notation, you can ping all of the IP addresses in any subnet you want.
- **Get comprehensive data.** For each IP address you ping, you will get a lot of data, including the host status (UP, DOWN, ERROR), and details about the response (response time, error details).
- **Beautiful output.** The response data is ouput to a table in the console, allowing you to quickly and easily determine the status of all of the IPs in your subnet.

## How to use
- Clone the git repository.
- Make sure you have python installed.
- Run `python3 ipeepython.py [IP address/subnet mask]` from the directory containing `ipeepython.py`, making sure to format your IP address using CIDR notation for your subnet mask.
- *I Pee Python* will iterate over each host IP address in the subnet, pinging each one and recording the response details in a table in your console.

## Notes
- **DO NOT** run *I Pee Python* on a subnet that you do not have permission to. Some networks consider this kind of scanning to be malicious.
- All reponses will time out after 5 seconds.