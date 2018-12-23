# python-canon

## Python 3 HTTP(S) API for Canon PIXMA MG5700 Series Printers

![PIXMA MG5700/MG5720](https://www.usa.canon.com/internet/wcm/connect/us/aac839e7-a603-4b01-b611-199fd896abc7/pixma-mg-5720-wireless+inkjet-all-in-one-3q-output-d.jpg?MOD=AJPERES&CACHEID=ROOTWORKSPACE.Z18_P1KGHJ01L85180AUEPQQJ53034-aac839e7-a603-4b01-b611-199fd896abc7-k-Uv37)


-----------------------------------

### Getting started:

```python
>>> # Import libraries
>>> from canon import MG5700
>>> from pprint import pprint
>>> 
>>> # Printer constants
>>> HOST = '192.168.1.223'
>>> ADMIN_PASSWORD = 'admin'
>>> 
>>> # Create printer instance
>>> printer = MG5700(HOST)
>>> printer
<Canon-MG5700(192.168.1.223)>
>>> 
>>> # Log-in as an Administrator
>>> logged_in = printer.login(ADMIN_PASSWORD)
>>> 
>>> # Check the log-in was successful
>>> assert logged_in, 'Admin log-in failed!'
>>> 
>>> # Get some parameters
>>> lan_settings = printer.get_lan_settings()
>>> 
>>> # Then, display them
>>> pprint(lan_settings)
{'bst_state': 0,
 'com_mode': 'INFRA',
 'connection_type': 'WIRELESS_IPV4V6',
 'error_display_state': 'HTTP_ERR_DISP_IDLE',
 'ip_sec': 'INACTIVE',
 'ipv4': {'address': '192.168.1.223',
          'gateway': '192.168.1.254',
          'mask': '255.255.255.0',
          'mode': 1},
 'ipv6': {'address': 'FFAA:BBCC:DDEE:0000:1324:88FF:FFAA:44EE',
          'gateway': 'EE88:0000:0000:0000:99DD:44FF:FF00:EE99',
          'length': 64},
 'lan_security': 'WPA2_AES',
 'link_quality': 84,
 'mac_address': '66-11-88-AA-CC-EE',
 'result': 'RD_PAGE_SYS',
 'signal_strength': 68,
 'ssid': 'BTHub4-MM33',
 'transmission': 72.2,
 'warning_id': 'NO_ERR'}
>>> 
```

-----------------------------------

### Python libraries that were of great help:

Name | Link
---- | ----
Requests | https://github.com/requests/requests
Beautiful Soup | https://www.crummy.com/software/BeautifulSoup/

-----------------------------------

### Software that was of great help:

Software | Link
-------- | ----
Firefox Quantum: Developer Edition | https://www.mozilla.org/en-GB/firefox/developer/
Atom | https://atom.io/
Python | https://www.python.org/

-----------------------------------

Total printers harmed in the making of this code: **0**
