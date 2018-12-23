from .. import sessions
from .. import utils
from .. import parsers
import bs4

"""
Imports:
    ..sessions
    ..utils
    ..parsers
    bs4

Contains:
    <BasePrinter>
"""

class BasePrinter(object):
    """
    Base-most printer

    Interacts with the HTTP Session
    """

    def __init__(self, host):
        """
        Initialise self
        """

        self._init_attrs()

        self.host = host
        self.HTTPSession = sessions.HTTPSession()
        self.SBID = None

    def ijcpc_del(self):
        """
        Make a HTTP POST request to endpoint: rui/ijcpc_del.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
        }

        endpoint = 'rui/ijcpc_del.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def tls_create_cert \
            (
                self,
                setinfo = None,
                dsa = None,
                key_bit = None,
                start_date = None,
                st_year = None,
                st_month = None,
                st_day = None,
                end_date = None,
                end_year = None,
                end_month = None,
                end_day = None,
                common_name = None,
                country = None,
                prefecture = None,
                municipality = None,
                organization = None,
                org_unit = None,
            ):
        """
        Make a HTTP POST request to endpoint: rui/tls_create_cert.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'SETINFO': setinfo,
            'DSA': dsa,
            'KEY_BIT': key_bit,
            'START_DATE': start_date,
            'ST_YEAR': st_year,
            'ST_MONTH': st_month,
            'ST_DAY': st_day,
            'END_DATE': end_date,
            'END_YEAR': end_year,
            'END_MONTH': end_month,
            'END_DAY': end_day,
            'COMMON_NAME': common_name,
            'COUNTRY': country,
            'PREFECTURE': prefecture,
            'MUNICIPALITY': municipality,
            'ORGANIZATION': organization,
            'ORG_UNIT': org_unit,
        }

        endpoint = 'rui/tls_create_cert.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def prninfo_data(self, getinfo=None):
        """
        Make a HTTP POST request to endpoint: rui/prninfo_data.cgi
        """

        post_data = \
        {
            'GETINFO': getinfo,
            'SBID': self.SBID,
        }

        endpoint = 'rui/prninfo_data.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def model(self, ver=None):
        """
        Make a HTTP GET request to endpoint: rui/JS_MDL/model.js?ver={ver}
        """

        get_params = \
        {
            'ver': ver,
        }

        endpoint = 'rui/JS_MDL/model.js'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(get_params, value = None)

        http_resp = self.HTTPSession.get(url, params = get_params)

        data = parsers.parse_js(http_resp.text)

        return data

    def lan_set_lan_if(self, getinfo=None):
        """
        Make a HTTP POST request to endpoint: rui/lan_set_lan_if.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'GETINFO': getinfo,
        }

        endpoint = 'rui/lan_set_lan_if.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def index(self, lang=None):
        """
        Make a HTTP GET request to endpoint: index.html?lang={lang}
        """

        get_params = \
        {
            'lang': lang,
        }

        utils.dict_skim(get_params, value = None)

        endpoint = 'index.html'

        url = self._make_url(endpoint = endpoint)

        http_resp = self.HTTPSession.get(url, params = get_params)

        data = http_resp.text

        return data

    def firm_version(self):
        """
        Make a HTTP POST request to endpoint: rui/firm_version.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
        }

        endpoint = 'rui/firm_version.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def firm_verify(self):
        """
        Make a HTTP POST request to endpoint: rui/firm_verify.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
        }

        endpoint = 'rui/firm_verify.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def get_job_status(self, job_num=None):
        """
        Make a HTTP POST request to endpoint: rui/get_job_status.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'JOB_NUM': job_num,
        }

        endpoint = 'rui/get_job_status.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def get_lan_setting_info(self, getinfo=None):
        """
        Make a HTTP POST request to endpoint: rui/get_lan_setting_info.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'GETINFO': getinfo,
        }

        endpoint = 'rui/get_lan_setting_info.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def sysinfo_data(self, getinfo=None):
        """
        Make a HTTP POST request to endpoint: rui/sysinfo_data.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'GETINFO': getinfo,
        }

        endpoint = 'rui/sysinfo_data.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def tls_get_cert_info(self, getinfo=None):
        """
        Make a HTTP POST request to endpoint: rui/tls_get_cert_info.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'GETINFO': getinfo,
        }

        endpoint = 'rui/tls_get_cert_info.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def lan_ipv4_data \
            (
                self,
                setinfo = None,
                getinfo = None,
                prx_use = None,
                dns_auto = None,
            ):
        """
        Make a HTTP POST request to endpoint: rui/lan_ipv4_data.cgi
        """

        if prx_use is not None:
            prx_use = int(bool(prx_use))
        if dns_auto is not None:
            dns_auto = int(bool(dns_auto))

        post_data = \
        {
            'SBID': self.SBID,
            'SETINFO': setinfo,
            'GETINFO': getinfo,
            'PRX_USE': prx_use,
            'DNS_AUTO': dns_auto,
        }

        endpoint = 'rui/lan_ipv4_data.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def lan_data_print(self):
        """
        Make a HTTP POST request to endpoint: rui/lan_data_print.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
        }

        endpoint = 'rui/lan_data_print.cgi'

        url = self._make_url(endpoint = endpoint)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def tls_is_found_cert(self, getinfo=None):
        """
        Make a HTTP POST request to endpoint: rui/tls_is_found_cert.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'GETINFO': getinfo,
        }

        endpoint = 'rui/tls_is_found_cert.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def tls_is_created_csr(self, getinfo=None):
        """
        Make a HTTP POST request to endpoint: rui/tls_create_cert.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'GETINFO': getinfo,
        }

        endpoint = 'rui/tls_is_created_csr.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def tls_create_csr \
            (
                self,
                setinfo = None,
                dsa = None,
                key_bit = None,
                common_name = None,
                country = None,
                prefecture = None,
                municipality = None,
                organization = None,
                org_unit = None,
            ):
        """
        Make a HTTP POST request to endpoint: rui/tls_create_csr.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'SETINFO': setinfo,
            'DSA': dsa,
            'KEY_BIT': key_bit,
            'COMMON_NAME': common_name,
            'COUNTRY': country,
            'PREFECTURE': prefecture,
            'MUNICIPALITY': municipality,
            'ORGANIZATION': organization,
            'ORG_UNIT': org_unit,
        }

        endpoint = 'rui/tls_create_csr.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def tls_download_csr(self):
        """
        Make a HTTP GET request to endpoint: rui/tls_download_csr.bin
        """

        endpoint = 'rui/tls_download_csr.bin'

        url = self._make_url(endpoint = endpoint)

        http_resp = self.HTTPSession.get(url)

        data = http_resp.text

        return data

    def tls_pre_download_csr(self, getinfo=None):
        """
        Make a HTTP POST request to endpoint: rui/tls_pre_download_csr.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'GETINFO': getinfo,
        }

        endpoint = 'rui/tls_pre_download_csr.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def tls_exec_lan_restart(self):
        """
        Make a HTTP POST request to endpoint: rui/tls_exec_lan_restart.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
        }

        endpoint = 'rui/tls_exec_lan_restart.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def tls_delete_cert(self):
        """
        Make a HTTP POST request to endpoint: rui/tls_delete_cert.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
        }

        endpoint = 'rui/tls_delete_cert.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def se_setting_restriction \
            (
                self,
                setinfo = None,
                getinfo = None,
                admin_pw = None,
                scope = None,
                password = None,
            ):
        """
        Make a HTTP POST request to endpoint: rui/se_setting_restriction.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'SETINFO': setinfo,
            'GETINFO': getinfo,
            'ADMIN_PW': admin_pw,
            'SCOPE': scope,
            'PASSWORD': password,
        }

        endpoint = 'rui/se_setting_restriction.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def ijcpc_is_already(self, getinfo=None):
        """
        Make a HTTP POST request to endpoint: rui/ijcpc_is_already.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'GETINFO': getinfo,
        }

        endpoint = 'rui/ijcpc_is_already.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def ijcpc_printer_regi(self):
        """
        Make a HTTP POST request to endpoint: rui/ijcpc_printer_regi.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
        }

        endpoint = 'rui/ijcpc_printer_regi.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def err_recover(self, warning_id=None):
        """
        Make a HTTP POST request to endpoint: rui/err_recover.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'WARNING_ID': warning_id,
        }

        endpoint = 'rui/err_recover.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def gcp_is_gcp(self, getinfo=None):
        """
        Make a HTTP POST request to endpoint: rui/gcp_is_gcp.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'GETINFO': getinfo,
        }

        endpoint = 'rui/gcp_is_gcp.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def gcp_regi(self, auth_job_num=None):
        """
        Make a HTTP POST request to endpoint: rui/gcp_regi.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'AUTH_JOB_NUM': auth_job_num,
        }

        endpoint = 'rui/gcp_regi.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def app_data \
            (
                self,
                setinfo = None,
                getinfo = None,
                bonname = None,
                bonnote = None,
                geoloc1_ns = None,
                geoloc1_time = None,
                geoloc1_min = None,
                geoloc1_sec1 = None,
                geoloc1_sec2 = None,
                geoloc2_ew = None,
                geoloc2_time = None,
                geoloc2_min = None,
                geoloc2_sec1 = None,
                geoloc2_sec2 = None,
                geoalti = None,
                aapbatchset = None,
                detect_paper_width = None,
            ):
        """
        Make a HTTP POST request to endpoint: rui/app_data.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'SETINFO': setinfo,
            'GETINFO': getinfo,
            'BONNAME': bonname,
            'BONNOTE': bonnote,
            'GEOLOC1_NS': geoloc1_ns,
            'GEOLOC1_TIME': geoloc1_time,
            'GEOLOC1_MIN': geoloc1_min,
            'GEOLOC1_SEC1': geoloc1_sec1,
            'GEOLOC1_SEC2': geoloc1_sec2,
            'GEOLOC2_TIME': geoloc2_time,
            'GEOLOC2_MIN': geoloc2_min,
            'GEOLOC2_SEC1': geoloc2_sec1,
            'GEOLOC2_SEC2': geoloc2_sec2,
            'GEOALTI': geoalti,
            'AAPBATCHSET': aapbatchset,
            'DETECT_PAPER_WIDTH': detect_paper_width,
        }

        endpoint = 'rui/app_data.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def machininfo_data \
            (
                self,
                setinfo = None,
                getinfo = None,
                dry_level = None,
                detect_paper_width = None,
                left_margin_ca1 = None,
                paper_gap = None,
                power_save_off = None,
                power_save_time = None,
                power_save_on = None,
            ):
        """
        Make a HTTP POST request to endpoint: rui/machininfo_data.cgi
        """

        if detect_paper_width is not None:
            detect_paper_width = int(bool(detect_paper_width))
        if power_save_on is not None:
            power_save_on = int(bool(power_save_on))
        if power_save_off is not None:
            power_save_off = int(bool(power_save_off))

        post_data = \
        {
            'SBID': self.SBID,
            'SETINFO': setinfo,
            'GETINFO': getinfo,
            'DRY_LEVEL': dry_level,
            'DETECT_PAPER_WIDTH': detect_paper_width,
            'LEFT_MARGIN_CA1': left_margin_ca1,
            'PAPER_GAP': paper_gap,
            'POWER_SAVE_OFF': power_save_off,
            'POWER_SAVE_TIME': power_save_time,
            'POWER_SAVE_ON': power_save_on,
        }

        endpoint = 'rui/machininfo_data.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def silent_mode(self, silent_mode=None):
        """
        Make a HTTP POST request to endpoint: rui/silent_mode.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
            'SILENT_MODE': silent_mode,
        }

        endpoint = 'rui/silent_mode.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def ut_nozzle_check(self):
        """
        Make a HTTP POST request to endpoint: rui/ut_nozzle_check.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
        }

        endpoint = 'rui/ut_nozzle_check.cgi'

        url = self._make_url(endpoint = endpoint)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def ut_regi_print(self):
        """
        Make a HTTP POST request to endpoint: rui/ut_regi_print.cgi
        """

        post_data = \
        {
            'SBID': self.SBID,
        }

        endpoint = 'rui/ut_regi_print.cgi'

        url = self._make_url(endpoint = endpoint)

        http_resp = self.HTTPSession.post(url, data = post_data)

        data = parsers.parse_xml(http_resp.text)

        return data

    def sendpw(self, namae=None, idtype=None):
        """
        Make a HTTP POST request to endpoint: rui/sendpw.cgi
        """

        post_data = \
        {
            'NAMAE': namae,
            'IDTYPE': idtype,
        }

        endpoint = 'rui/sendpw.cgi'

        url = self._make_url(endpoint = endpoint)

        utils.dict_skim(post_data, value = None)

        http_resp = self.HTTPSession.post(url, data = post_data)

        html_soup = bs4.BeautifulSoup(http_resp.text, 'html.parser')

        tag_input = html_soup.find('input')

        if tag_input is None:
            SBID = None
        else:
            SBID = tag_input['value']

        self.SBID = SBID

        data = \
        {
            'SBID': SBID,
        }

        return data

    def _make_url(self, endpoint='', protocol='https'):
        """
        Make a HTTP URL in the form:
            {protocol}://{self.host}/{endpoint}
        """

        host = self.host

        url = f'{protocol}://{host}/{endpoint}'

        return url

    def _init_attrs(self):
        """
        Initialise class attributes
        """

        self.host = None
        self.HTTPSession = None
        self.SBID = None
