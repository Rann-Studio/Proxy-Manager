# Proxy Manager Documentation
This documentation provides information about the ProxyManager class and how to use it for managing and checking proxies in Python.

## Introduction
The ProxyManager class is a Python script that enables users to retrieve and manage proxies from the website https://free-proxy-list.net/. It allows users to filter proxies based on the protocol (HTTP or HTTPS) and also perform a check on proxy status.

## Prerequisites
To use the ProxyManager class, you need the following:
- Python 3.x installed on your system.
- Required Python packages: requests, bs4 (BeautifulSoup).

You can install the required packages using pip:
```shell
pip install requests beautifulsoup4
```

## Getting Started
To use the ProxyManager class, follow the steps below:
1. Import the ProxyManager class into your Python script.
2. Create an instance of the ProxyManager class.
3. Call the `setup()` method with an optional protocol parameter (to filter proxies based on protocol).
4. Use the available methods to get the proxy list, retrieve a random proxy, and check the status of a proxy.

## Usage
**Importing ProxyManager**
```python
from ProxyManager import ProxyManager
```

**Initializing ProxyManager**
```python
proxy_manager = ProxyManager()
```

**Setting Up Proxy List**\
Before using proxies, you need to fetch and set up the proxy list. Use the setup() method to fetch and store the list of proxies based on the specified protocol (HTTP or HTTPS). If you don't provide the protocol parameter, the method will fetch and store all the available proxies (both HTTP and HTTPS).
```python
proxy_manager.setup(protocol='http')  # Fetch and store HTTP proxies
```

**Getting the List of Proxies**\
You can get the list of proxies that have been fetched and stored using the `get_proxies()` method. The method returns a list of proxy information dictionaries, each containing details such as IP address, port number, anonymity level, and the proxy protocol.
```python
proxies = proxy_manager.get_proxies()
print('Proxies:', proxies)
```

**Getting a Random Proxy**\
You can retrieve a random proxy from the fetched list using the `get_random_proxy()` method. The method returns a randomly chosen proxy information dictionary.
```python
random_proxy = proxy_manager.get_random_proxy()
print('Random Proxy:', random_proxy)
```

**Checking Proxy Status**\
You can check the status of a specific proxy using the `check_proxy()` method. This method takes the proxy URL as an argument and returns a boolean value (True or False)
```python
proxy_status = proxy_manager.check_proxy(random_proxy['proxy_url'])
print('Proxy status:', 'Up!' if proxy_status else 'Down')
```

**Example Usage**
```python
# Import the ProxyManager class
from ProxyManager import ProxyManager

# Create an instance of ProxyManager
proxy_manager = ProxyManager()

# Fetch and store HTTPS proxies
proxy_manager.setup(protocol='https')

# Get the list of proxies
proxies = proxy_manager.get_proxies()
print('Proxies:', proxies)

# Get a random proxy
random_proxy = proxy_manager.get_random_proxy()
print('Random Proxy:', random_proxy)

# Check the status of the random proxy
proxy_status = proxy_manager.check_proxy(random_proxy['proxy_url'])
print('Proxy status:', 'Up!' if proxy_status else 'Down')
```
