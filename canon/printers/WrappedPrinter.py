from .BasePrinter import BasePrinter
from .. import utils

"""
Imports:
    .BasePrinter.BasePrinter
    ..utils

Contains:
    <WrappedPrinter>
"""

class WrappedPrinter(BasePrinter):
    """
    Wrapper for <BasePrinter>

    Re-Writes variable names to be more human-readable
    Applies basic type-casting
    """

    def __init__(self, *args, **kwargs):
        """
        Initialise self and super
        """

        super().__init__(*args, **kwargs)

    def ijcpc_del(self):
        """
        Human Wrapper for: super().ijcpc_del()

        Applies map (from -> (type) to):
            job_num -> (int) job_number
            result -> result
            err_disp_state -> error_display_state
            warning_id -> warning_id
            bst_state -> (int) bst_state

        Return keys:
            job_number: ...
            result: ...
            error_display_state: ...
            warning_id: ...
            bst_state: ...
        """

        raw = super().ijcpc_del()

        page_ijcpc = raw.get('page_ijcpc', {})

        job_number = page_ijcpc.get('job_num', None)
        result = page_ijcpc.get('result', None)
        error_display_state = page_ijcpc.get('err_disp_state', None)
        warning_id = page_ijcpc.get('warning_id', None)
        bst_state = page_ijcpc.get('bst_state', None)

        if job_number is not None:
            job_number = int(job_number)
        if bst_state is not None:
            bst_state = int(bst_state)

        data = \
        {
            'job_number': job_number,
            'result': result,
            'error_display_state': error_display_state,
            'warning_id': warning_id,
            'bst_state': bst_state,
        }

        return data

    def tls_create_cert \
            (
                self,
                set_info = None,
                dsa = None,
                key_bit = None,
                start_date = None,
                start_year = None,
                start_month = None,
                start_day = None,
                end_date = None,
                end_year = None,
                end_month = None,
                end_day = None,
                common_name = None,
                country = None,
                prefecture = None,
                municipality = None,
                organization = None,
                organization_unit = None,
            ):
        """
        Human Wrapper for: super().tls_create_cert

        Applies arg map (from -> to):
            set_info -> setinfo
            start_year -> st_year
            start_month -> st_month
            start_day -> st_day
            organization_unit -> org_unit

        Applies key map (from -> (type) to):
            bst_state -> (int) bst_state
            err_disp_state -> error_display_state
            result -> result
            warning_id -> warning_id

        Return keys:
            bst_state: ...
            error_display_state: ...
            result: ...
            warning_id: ...
        """

        kwargs = \
        {
            'setinfo': set_info,
            'dsa': dsa,
            'key_bit': key_bit,
            'start_date': start_date,
            'st_year': start_year,
            'st_month': start_month,
            'st_day': start_day,
            'end_date': end_date,
            'end_year': end_year,
            'end_month': end_month,
            'end_day': end_day,
            'common_name': common_name,
            'country': country,
            'prefecture': prefecture,
            'municipality': municipality,
            'organization': organization,
            'org_unit': organization_unit,
        }

        raw = super().tls_create_cert(**kwargs)

        # sess_err_url = ...
        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def prninfo_data(self, get_info=None):
        """
        Human Wrapper for: super().prninfo_data
        """

        kwargs = \
        {
            'getinfo': get_info,
        }

        raw = super().prninfo_data(**kwargs)

        page_prninfo = raw.get('page_prninfo', {})
        page_rdlink_eid = raw.get('page_rdlink_eid', {})
        page_rdlink_ink = raw.get('page_rdlink_ink', {})
        page_rdlink_err = raw.get('page_rdlink_err', {})
        page_rdlink_sup = raw.get('page_rdlink_sup', {})

        result = raw.get('result', None)
        battery_rest = page_prninfo.get('batteryrest', None)
        bst_state = page_prninfo.get('bst_state', None)
        error_display_state = page_prninfo.get('err_disp_state', None)
        lan_setting = page_prninfo.get('lan_setting', None)
        link_quality = page_prninfo.get('link_quality', None)
        mode = page_prninfo.get('mode', None)
        signal_strength = page_prninfo.get('signal_strength', None)
        warning_id = page_prninfo.get('warning_id', None)
        eid_url = page_rdlink_eid.get('eid_url', None)
        error_url = page_rdlink_err.get('err_url', None)
        ink_url = page_rdlink_ink.get('ink_url', None)
        support_url = page_rdlink_sup.get('sup_url', None)
        ink_rest_0 = page_prninfo.get('inkrest0', None)
        ink_rest_1 = page_prninfo.get('inkrest1', None)
        ink_rest_2 = page_prninfo.get('inkrest2', None)
        ink_rest_3 = page_prninfo.get('inkrest3', None)
        ink_rest_4 = page_prninfo.get('inkrest4', None)
        prn_doc = page_prninfo.get('prndoc', None)

        if bst_state is not None:
            bst_state = int(bst_state)
        if link_quality is not None:
            link_quality = int(link_quality)
        if signal_strength is not None:
            signal_strength = int(signal_strength)
        if prn_doc is not None:
            prn_doc = int(prn_doc)
        if ink_rest_0 is not None:
            ink_rest_0 = [int(index.strip()) for index in ink_rest_0.split(',')]
        if ink_rest_1 is not None:
            ink_rest_1 = [int(index.strip()) for index in ink_rest_1.split(',')]
        if ink_rest_2 is not None:
            ink_rest_2 = [int(index.strip()) for index in ink_rest_2.split(',')]
        if ink_rest_3 is not None:
            ink_rest_3 = [int(index.strip()) for index in ink_rest_3.split(',')]
        if ink_rest_4 is not None:
            ink_rest_4 = [int(index.strip()) for index in ink_rest_4.split(',')]

        ink_rests = \
        [
            ink_rest_0,
            ink_rest_1,
            ink_rest_2,
            ink_rest_3,
            ink_rest_4,
        ]

        urls = \
        {
            'eid': eid_url,
            'error': error_url,
            'ink': ink_url,
            'support': support_url,
        }

        data = \
        {
            'battery_rest': battery_rest,
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'lan_setting': lan_setting,
            'link_quality': link_quality,
            'mode': mode,
            'signal_strength': signal_strength,
            'warning_id': warning_id,
            'urls': urls,
            'result': result,
            'prn_doc': prn_doc,
            'ink_rests': ink_rests,
        }

        return data

    def model(self, version=None):
        """
        Human Wrapper for: super().model
        """

        kwargs = \
        {
            'ver': version,
        }

        raw = super().model(**kwargs)

        aap_paper_width_enabled = raw.get('g_AAP_PAPERWIDTH_ENABLE', None)
        administrator = raw.get('g_Administrator', None)
        adf = raw.get('g_adf', None)
        battery_level = raw.get('g_battery_lv', None)
        bst_state = raw.get('g_bst_st', None)
        data_aap_batch_set = raw.get('g_data_aap_batchset', None)
        data_aap_paper_width = raw.get('g_data_aap_paperwidth', None)
        data_bon_name = raw.get('g_data_bonname', None)
        data_bon_name_conflict = raw.get('g_data_bonname_conflict', None)
        data_bon_note = raw.get('g_data_bonnote', None)
        data_geo_1_min = raw.get('g_data_geo_1_min', None)
        data_geo_1_ns = raw.get('g_data_geo_1_ns', None)
        data_geo_1_sec1 = raw.get('g_data_geo_1_sec1', None)
        data_geo_1_sec2 = raw.get('g_data_geo_1_sec2', None)
        data_geo_1_time = raw.get('g_data_geo_1_time', None)
        data_geo_2_ew = raw.get('g_data_geo_2_ew', None)
        data_geo_2_min = raw.get('g_data_geo_2_min', None)
        data_geo_2_sec1 = raw.get('g_data_geo_2_sec1', None)
        data_geo_2_sec2 = raw.get('g_data_geo_2_sec2', None)
        data_geo_2_time = raw.get('g_data_geo_2_time', None)
        data_geo_3 = raw.get('g_data_geo_3', None)
        eid_url = raw.get('g_eid_url', None)
        error_message_id = raw.get('g_err_msg_id', None)
        error_url = raw.get('g_err_url', None)
        fax_model = raw.get('g_fax_model', None)
        firmware_update = raw.get('g_firm_up_date', None)
        help_url = raw.get('g_help_url', None)
        ink_url = raw.get('g_ink_url', None)
        ipp_over_usb = raw.get('g_ipp_over_usb', None)
        job_auth_number = raw.get('g_job_auth_num', None)
        lan_if = raw.get('g_lan_if', None)
        link_quality = raw.get('g_link_quality', None)
        logon_screen = raw.get('g_logon_screen', None)
        micro_ap = raw.get('g_micro_ap', None)
        mobile = raw.get('g_mobile', None)
        network_mode = raw.get('g_network_mode', None)
        nfc_mode = raw.get('g_nfc_mode', None)
        pass_url = raw.get('g_pass_url', None)
        password_enabled = raw.get('g_password_enable', None)
        prn_doc = raw.get('g_prndoc', None)
        scanner = raw.get('g_scanner', None)
        scan_to_folder = raw.get('g_scanto_folder', None)
        signal_strength = raw.get('g_signal_strength', None)
        ssl_cert_end_year = raw.get('g_ssl_cert_end_year', None)
        ssl_cert_start_year = raw.get('g_ssl_cert_start_year', None)
        support_url = raw.get('g_sup_url', None)
        wifi_direct = raw.get('g_wifi_direct', None)
        ink_tank = raw.get('inktank', None)

        if bst_state is not None:
            bst_state = bool(int(bst_state))

        aap = \
        {
            'paper_width_enabled': aap_paper_width_enabled,
            'batch_set': data_aap_batch_set,
            'paper_width': data_aap_paper_width,
        }
        bon = \
        {
            'name': data_bon_name,
            'name_conflict': data_bon_name_conflict,
            'note': data_bon_note,
        }
        geo_1 = \
        {
            'min': data_geo_1_min,
            'ns': data_geo_1_ns,
            'sec1': data_geo_1_sec1,
            'sec2': data_geo_1_sec2,
            'time': data_geo_1_time,
        }
        geo_2 = \
        {
            'ew': data_geo_2_ew,
            'min': data_geo_2_min,
            'sec1': data_geo_2_sec1,
            'sec2': data_geo_2_sec2,
            'time': data_geo_2_time,
        }
        geo_3 = \
        {
        }
        geo = \
        {
            1: geo_1,
            2: geo_2,
            #3: geo_3, # geo_alti?
        }

        if job_auth_number is not None:
            job_auth_number = int(job_auth_number)
        if link_quality is not None:
            link_quality = int(link_quality)
        if logon_screen is not None:
            logon_screen = int(logon_screen)
        if prn_doc is not None:
            prn_doc = int(prn_doc)
        if signal_strength is not None:
            signal_strength = int(signal_strength)
        if ink_tank is not None:
            ink_tank = utils.list_from_dict(ink_tank)

        url = \
        {
            'eid': eid_url,
            'error': error_url,
            'help': help_url,
            'ink': ink_url,
            'pass': pass_url,
            'support': support_url,
        }

        if administrator is not None:
            administrator = bool(administrator)
        if adf is not None:
            adf = bool(adf)
        if fax_model is not None:
            fax_model = bool(fax_model)
        if firmware_update is not None:
            firmware_update = bool(firmware_update)
        if ipp_over_usb is not None:
            ipp_over_usb = bool(ipp_over_usb)
        if micro_ap is not None:
            micro_ap = bool(micro_ap)
        if mobile is not None:
            mobile = bool(mobile)
        if nfc_mode is not None:
            nfc_mode = bool(nfc_mode)
        if password_enabled is not None:
            password_enabled = bool(password_enabled)
        if scanner is not None:
            scanner = bool(scanner)
        if scan_to_folder is not None:
            scan_to_folder = bool(scan_to_folder)
        if wifi_direct is not None:
            wifi_direct = bool(wifi_direct)

        ssl_cert = \
        {
            'end_year': ssl_cert_end_year,
            'start_year': ssl_cert_start_year,
        }

        data = \
        {
            'aap': aap,
            'administrator': administrator,
            'adf': adf,
            'battery_level': battery_level,
            'bst_state': bst_state,
            'bon': bon,
            'geo': geo,
            'url': url,
            'error_message_id': error_message_id,
            'fax_model': fax_model,
            'firmware_update': firmware_update,
            'ipp_over_usb': ipp_over_usb,
            'job_auth_number': job_auth_number,
            'lan_if': lan_if,
            'link_quality': link_quality,
            'logon_screen': logon_screen,
            'micro_ap': micro_ap,
            'mobile': mobile,
            'network_mode': network_mode,
            'nfc_mode': nfc_mode,
            'password_enabled': password_enabled,
            'prn_doc': prn_doc,
            'scanner': scanner,
            'scan_to_folder': scan_to_folder,
            'signal_strength': signal_strength,
            'ssl_cert': ssl_cert,
            'wifi_direct': wifi_direct,
            'ink_tank': ink_tank,
        }

        return data

    def lan_set_lan_if(self, get_info=None):
        """
        Human Wrapper for: super().lan_set_lan_if
        """

        kwargs = \
        {
            'getinfo': get_info,
        }

        raw = super().lan_set_lan_if(**kwargs)

        page_systeminfo = raw.get('page_systeminfo', {})

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        lan_setting = page_systeminfo.get('lan_setting', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)

        lsli_data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'lan_setting': lan_setting,
            'result': result,
            'warning_id': warning_id,
        }

        return lsli_data

    def index(self, language_index=None):
        """
        Human Wrapper for: super().index
        """

        kwargs = \
        {
            'lang': language_index,
        }

        raw = super().index(**kwargs)

        return raw

    def firm_version(self):
        """
        Human Wrapper for: super().firm_version
        """

        raw = super().firm_version()

        page_firmupinfo = raw.get('page_firmupinfo', {})

        firmware_current_version = page_firmupinfo.get('firm_current_ver', None)
        firmware_latest_version = page_firmupinfo.get('firm_latest_ver', None)
        result = raw.get('result', None)

        version = \
        {
            'current': firmware_current_version,
            'latest': firmware_latest_version,
        }

        data = \
        {
            'version': version,
            'result': result,
        }

        return data

    def firm_verify(self):
        """
        Human Wrapper for: super().firm_verify
        """

        raw = super().firm_verify()

        page_firmup = raw.get('page_firmup', {})

        bst_state = raw.get('bst_state', None)
        detail = raw.get('detail', None)
        error_display_state = raw.get('err_disp_state', None)
        job_number = raw.get('job_num', None)
        lan_setting = page_firmup.get('lan_setting', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)
        if lan_setting is not None:
            lan_setting = int(lan_setting)

        if job_number is not None:
            job_number = int(job_number)

        data = \
        {
            'bst_state': bst_state,
            'detail': detail,
            'error_display_state': error_display_state,
            'job_number': job_number,
            'lan_setting': lan_setting,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def get_job_status(self, job_number=None):
        """
        Human Wrapper for: super().get_job_status
        """

        kwargs = \
        {
            'job_num': job_number,
        }

        raw = super().get_job_status(**kwargs)

        update = raw.get('update', {})

        bon_conflict = raw.get('bonconflict', None)
        bon_name = raw.get('bonname', None)
        bon_note = raw.get('bonnote', None)
        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        get_job_state = raw.get('getjobstate', None)
        get_firm_up_state = update.get('getfirmupstate', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)
        if get_job_state is not None:
            get_job_state = int(get_job_state)
        if get_firm_up_state is not None:
            get_firm_up_state = int(get_firm_up_state)

        bon = \
        {
            'conflict': bon_conflict,
            'name': bon_name,
            'note': bon_note,
        }
        get_state = \
        {
            'job': get_job_state,
            'firm_up': get_firm_up_state,
        }

        data = \
        {
            'bon': bon,
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'get_state': get_state,
            'warning_id': warning_id,
        }

        return data

    def get_lan_setting_info(self, get_info=None):
        """
        Human Wrapper for: super().get_lan_setting_info
        """

        kwargs = \
        {
            'getinfo': get_info,
        }

        raw = super().get_lan_setting_info(**kwargs)

        confirm_lan_settings = raw.get('confirm_lan_settings', {})

        bst_state = raw.get('bst_state', None)
        com_mode = confirm_lan_settings.get('com_mode', None)
        connection_type = confirm_lan_settings.get('connect_type', None)
        ip_sec = confirm_lan_settings.get('ipsec', None)
        ipv4_address = confirm_lan_settings.get('ipv4_add', None)
        ipv4_gateway = confirm_lan_settings.get('ipv4_gateway', None)
        ipv4_mask = confirm_lan_settings.get('ipv4_mask', None)
        ipv4_mode = confirm_lan_settings.get('ipv4_mode', None)
        ipv6_address = confirm_lan_settings.get('ipv6_add', None)
        ipv6_gateway = confirm_lan_settings.get('ipv6_gateway', None)
        ipv6_length = confirm_lan_settings.get('ipv6_length', None)
        lan_security = confirm_lan_settings.get('lan_security', None)
        link_quality = confirm_lan_settings.get('link_quality', None)
        mac_address = confirm_lan_settings.get('mac_add', None)
        signal_strength = confirm_lan_settings.get('signal_strength', None)
        ssid = confirm_lan_settings.get('ssid', None)
        transmission = confirm_lan_settings.get('transmission', None)
        error_display_state = raw.get('err_disp_state', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)
        if ipv4_mode is not None:
            ipv4_mode = int(ipv4_mode)
        if ipv6_length is not None:
            ipv6_length = int(ipv6_length)
        if link_quality is not None:
            link_quality = int(link_quality)
        if signal_strength is not None:
            signal_strength = int(signal_strength)
        if transmission is not None:
            transmission = float(transmission)

        ipv4 = \
        {
            'address': ipv4_address,
            'gateway': ipv4_gateway,
            'mask': ipv4_mask,
            'mode': ipv4_mode,
        }
        ipv6 = \
        {
            'address': ipv6_address,
            'gateway': ipv6_gateway,
            'length': ipv6_length,
        }

        data = \
        {
            'bst_state': bst_state,
            'com_mode': com_mode,
            'connection_type': connection_type,
            'ip_sec': ip_sec,
            'ipv4': ipv4,
            'ipv6': ipv6,
            'lan_security': lan_security,
            'link_quality': link_quality,
            'mac_address': mac_address,
            'signal_strength': signal_strength,
            'ssid': ssid,
            'transmission': transmission,
            'error_display_state': error_display_state,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def sysinfo_data(self, get_info=None):
        """
        Human Wrapper for: super().sysinfo_data
        """

        kwargs = \
        {
            'getinfo': get_info
        }

        raw = super().sysinfo_data(**kwargs)

        page_systeminfo = raw.get('page_systeminfo', {})

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        device_name = page_systeminfo.get('device_name', None)
        mac_address = page_systeminfo.get('mac_add', None)
        rom_version = page_systeminfo.get('rom_ver', None)
        serial_number = page_systeminfo.get('serial_num', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'device_name': device_name,
            'mac_address': mac_address,
            'rom_version': rom_version,
            'serial_number': serial_number,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def tls_get_cert_info(self, get_info=None):
        """
        Human Wrapper for: super().tls_get_cert_info
        """

        kwargs = \
        {
            'getinfo': get_info,
        }

        raw = super().tls_get_cert_info(**kwargs)

        page_tls = raw.get('page_tls', {})

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        dsa = page_tls.get('dsa', None)
        end_date = page_tls.get('end_date', None)
        hash = page_tls.get('hash', None)
        hash_algorithm = page_tls.get('hash_alg', None)
        issuer = page_tls.get('issuer', None)
        key_algorithm = page_tls.get('key_alg', None)
        key_bit = page_tls.get('key_bit', None)
        serial_number = page_tls.get('number', None)
        result = page_tls.get('result', None)
        start_date = page_tls.get('start_date', None)
        subject = page_tls.get('subject', None)
        version = page_tls.get('version', None)
        warning_id = raw.get('warning_id', None)

        if dsa is not None:
            dsa = bool(int(dsa))
        if hash_algorithm is not None:
            hash_algorithm = int(hash_algorithm)
        if key_algorithm is not None:
            key_algorithm = int(key_algorithm)
        if version is not None:
            version = int(version)
        if bst_state is not None:
            bst_state = int(bst_state)
        if key_bit is not None:
            key_bit = int(key_bit)
        if hash is not None:
            hash = hash.strip()
        if serial_number is not None:
            serial_number = serial_number.strip()

        date = \
        {
            'start': start_date,
            'end': end_date,
        }

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'dsa': dsa,
            'date': date,
            'hash': hash,
            'hash_algorithm': hash_algorithm,
            'issuer': issuer,
            'key_algorithm': key_algorithm,
            'key_bit': key_bit,
            'serial_number': serial_number,
            'result': result,
            'subject': subject,
            'version': version,
            'warning_id': warning_id,
        }

        return data

    def lan_ipv4_data \
            (
                self,
                set_info = None,
                get_info = None,
                proxy_use = None,
                dns_auto = None,
            ):
        """
        Human Wrapper for: super().lan_ipv4_data
        """

        kwargs = \
        {
            'setinfo': set_info,
            'getinfo': get_info,
            'prx_use': proxy_use,
            'dns_auto': dns_auto,
        }

        raw = super().lan_ipv4_data(**kwargs)

        page_systeminfo = raw.get('page_systeminfo', {})

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        job_number = raw.get('job_num', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)
        dns_auto = page_systeminfo.get('dns_auto', None)
        dns_primary = page_systeminfo.get('dns_prim', None)
        dns_secondary = page_systeminfo.get('dns_scnd', None)
        ipv4_address = page_systeminfo.get('ipv4_add', None)
        ipv4_gateway = page_systeminfo.get('ipv4_gateway', None)
        ipv4_mask = page_systeminfo.get('ipv4_mask', None)
        ipv4_mode = page_systeminfo.get('ipv4_mode', None)
        proxy_address = page_systeminfo.get('prx_addr', None)
        proxy_port = page_systeminfo.get('prx_port', None)
        proxy_use = page_systeminfo.get('prx_use', None)
        proxy_user_auth_mode = page_systeminfo.get('prx_user_authmode', None)
        proxy_user_name = page_systeminfo.get('prx_user_name', None)
        proxy_user_password =  page_systeminfo.get('prx_user_pass', None)

        if bst_state is not None:
            bst_state = int(bst_state)
        if dns_auto is not None:
            dns_auto = bool(int(dns_auto))
        if ipv4_mode is not None:
            ipv4_mode = int(ipv4_mode)
        if proxy_port is not None:
            if not proxy_port:
                proxy_port = None
            else:
                proxy_port = int(proxy_port)
        if proxy_use is not None:
            proxy_use = bool(int(proxy_use))
        if proxy_user_auth_mode is not None:
            proxy_user_auth_mode = int(proxy_user_auth_mode)
        if proxy_address is not None:
            if not proxy_address:
                proxy_address = None

        if job_number is not None:
            job_number = int(job_number)

        dns = \
        {
            'auto': dns_auto,
            'primary': dns_primary,
            'secondary': dns_secondary,
        }
        ipv4 = \
        {
            'address': ipv4_address,
            'gateway': ipv4_gateway,
            'mask': ipv4_mask,
            'mode': ipv4_mode,
        }
        proxy = \
        {
            'address': proxy_address,
            'port': proxy_port,
            'use': proxy_use,
            'user': \
            {
                'auth_mode': proxy_user_auth_mode,
                'username': proxy_user_name,
                'password': proxy_user_password,
            },
        }

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'job_number': job_number,
            'dns': dns,
            'ipv4': ipv4,
            'proxy': proxy,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def lan_data_print(self):
        """
        Human Wrapper for: super().lan_data_print
        """

        raw = super().lan_data_print()

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        job_number = raw.get('job_num', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)

        if job_number is not None:
            job_number = int(job_number)

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'job_number': job_number,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def tls_is_found_cert(self, get_info=None):
        """
        Human Wrapper for: super().tls_is_found_cert
        """

        kwargs = \
        {
            'getinfo': get_info,
        }

        raw = super().tls_is_found_cert(**kwargs)

        page_tls = raw.get('page_tls', {})

        certificate_found = page_tls.get('cert_found', None)
        result = page_tls.get('result', None)

        if certificate_found is not None:
            certificate_found = bool(int(certificate_found))

        data = \
        {
            'certificate_found': certificate_found,
            'result': result,
        }

        return data

    def tls_is_created_csr(self, get_info=None):
        """
        Human Wrapper for: super().tls_is_created_csr
        """

        kwargs = \
        {
            'getinfo': get_info,
        }

        raw = super().tls_is_created_csr(**kwargs)

        page_tls = raw.get('page_tls', {})

        csr_created = page_tls.get('csr_created', None)
        result = page_tls.get('result', None)

        if csr_created is not None:
            csr_created = bool(int(csr_created))

        data = \
        {
            'csr_created': csr_created,
            'result': result,
        }

        return data

    def tls_create_csr \
            (
                self,
                set_info = None,
                dsa = None,
                key_bit = None,
                common_name = None,
                country = None,
                prefecture = None,
                municipality = None,
                organization = None,
                organization_unit = None,
            ):
        """
        Human Wrapper for: super().tls_create_csr
        """

        kwargs = \
        {
            'setinfo': set_info,
            'dsa': dsa,
            'key_bit': key_bit,
            'common_name': common_name,
            'country': country,
            'prefecture': prefecture,
            'municipality': municipality,
            'organization': organization,
            'org_unit': organization_unit,
        }

        raw = super().tls_create_csr(**kwargs)

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def tls_download_csr(self):
        """
        Human Wrapper for: super().tls_download_csr
        """

        raw = super().tls_download_csr()

        return raw

    def tls_pre_download_csr(self, get_info=None):
        """
        Human Wrapper for: super().tls_pre_download_csr
        """

        kwargs = \
        {
            'getinfo': get_info,
        }

        raw = super().tls_pre_download_csr(**kwargs)

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def tls_exec_lan_restart(self):
        """
        Human Wrapper for: super().tls_exec_lan_restart
        """

        raw = super().tls_exec_lan_restart()

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        job_number = raw.get('job_num', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)
        if job_number is not None:
            job_number = int(job_number)

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'job_number': job_number,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def tls_delete_cert(self):
        """
        Human Wrapper for: super().tls_delete_cert
        """

        raw = super().tls_delete_cert()

        page_tls = raw.get('page_tls', None)

        result = page_tls.get('result', None)
        error_display_state = raw.get('err_disp_state', None)
        warning_id = raw.get('warning_id', None)
        bst_state = raw.get('bst_state', None)

        if bst_state is not None:
            bst_state = int(bst_state)

        data = \
        {
            'result': result,
            'error_display_state': error_display_state,
            'warning_id': warning_id,
            'bst_state': bst_state,
        }

        return data

    def se_setting_restriction \
            (
                self,
                get_info = None,
                set_info = None,
                admin_password = None,
                scope = None,
                password = None,
            ):
        """
        Human Wrapper for: super().se_setting_restriction
        """

        kwargs = \
        {
            'getinfo': get_info,
            'setinfo': set_info,
            'admin_pw': admin_password,
            'scope': scope,
            'password': password,
        }

        raw = super().se_setting_restriction(**kwargs)

        page_security = raw.get('page_security', {})

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        admin_password = page_security.get('admin_pw', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'admin_password': admin_password,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def ijcpc_is_already(self, get_info=None):
        """
        Human Wrapper for: super().ijcpc_is_already
        """

        kwargs = \
        {
            'getinfo': get_info,
        }

        raw = super().ijcpc_is_already(**kwargs)

        page_ijcpc = raw.get('page_ijcpc', {})

        registered = page_ijcpc.get('registerd', None)
        result = page_ijcpc.get('result', None)

        if registered is not None:
            registered = bool(int(registered))

        data = \
        {
            'registered': registered,
            'result': result,
        }

        return data

    def ijcpc_printer_regi(self):
        """
        Human Wrapper for: super().ijcpc_printer_regi
        """

        raw = super().ijcpc_printer_regi()

        page_ijcpc = raw.get('page_ijcpc', {})

        bst_state = page_ijcpc.get('bst_state', None)
        error_display_state = page_ijcpc.get('err_disp_state', None)
        job_number = page_ijcpc.get('job_num', None)
        registered = page_ijcpc.get('registerd', None)
        result = page_ijcpc.get('result', None)
        warning_id = page_ijcpc.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)
        if job_number is not None:
            job_number = int(job_number)
        if registered is not None:
            registered = bool(int(registered))

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'job_number': job_number,
            'registered': registered,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def err_recover(self, warning_id=None):
        """
        Human Wrapper for: super().err_recover
        """

        kwargs = \
        {
            'warning_id': warning_id,
        }

        raw = super().err_recover(**kwargs)

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def gcp_is_gcp(self, get_info=None):
        """
        Human Wrapper for: super().gcp_is_gcp
        """

        kwargs = \
        {
            'getinfo': get_info,
        }

        raw = super().gcp_is_gcp(**kwargs)

        page_gcp = raw.get('page_gcp', {})

        cgp_registered = page_gcp.get('gcp_registerd', None)
        result = page_gcp.get('result', None)

        if cgp_registered is not None:
            cgp_registered = bool(int(cgp_registered))

        data = \
        {
            'cgp_registered': cgp_registered,
            'result': result,
        }

        return data

    def gcp_regi(self, auth_job_number=None):
        """
        Human Wrapper for: super().gcp_regi
        """

        kwargs = \
        {
            'auth_job_num': auth_job_number,
        }

        raw = super().gcp_regi(**kwargs)

        page_gcp = raw.get('page_gcp', {})

        bst_state = page_gcp.get('bst_state', None)
        error_display_state = page_gcp.get('err_disp_state', None)
        job_number = page_ijcpc.get('job_num', None)
        result = page_gcp.get('result', None)
        warning_id = page_gcp.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)
        if job_number is not None:
            job_number = int(job_number)

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'result': result,
            'warning_id': warning_id,
            'job_number': job_number,
        }

        return data

    def app_data \
            (
                self,
                set_info = None,
                get_info = None,
                bon_name = None,
                bon_note = None,
                geo_loc_1_ns = None,
                geo_loc_1_time = None,
                geo_loc_1_min = None,
                geo_loc_1_sec_1 = None,
                geo_loc_1_sec_2 = None,
                geo_loc_2_ew = None,
                geo_loc_2_time = None,
                geo_loc_2_min = None,
                geo_loc_2_sec_1 = None,
                geo_loc_2_sec_2 = None,
                geo_alti = None,
                aap_batch_set = None,
                detect_paper_width = None,
            ):
        """
        Human Wrapper for: super().app_data
        """

        kwargs = \
        {
            'setinfo': set_info,
            'getinfo': get_info,
            'bonname': bon_name,
            'bonnote': bon_note,
            'geoloc1_ns': geo_loc_1_ns,
            'geoloc1_time': geo_loc_1_time,
            'geoloc1_min': geo_loc_1_min,
            'geoloc1_sec1': geo_loc_1_sec_1,
            'geoloc1_sec2': geo_loc_1_sec_2,
            'geoloc2_ew': geo_loc_2_ew,
            'geoloc2_time': geo_loc_2_time,
            'geoloc2_min': geo_loc_2_min,
            'geoloc2_sec1': geo_loc_2_sec_1,
            'geoloc2_sec2': geo_loc_2_sec_2,
            'geoalti': geo_alti,
            'aapbatchset': aap_batch_set,
            'detect_paper_width': detect_paper_width,
        }

        raw = super().app_data(**kwargs)

        page_app = raw.get('page_app', {})

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)
        job_number = raw.get('job_num', None)
        aap_batch_set = page_app.get('aapbatchset', None)
        bon_conflict = page_app.get('bonconflict', None)
        bon_name = page_app.get('bonname', None)
        bon_note = page_app.get('bonnote', None)
        detect_paper_width = page_app.get('detect_paper_width', None)
        geo_alti = page_app.get('geoalti', None)
        geo_loc_1_min = page_app.get('geoloc1_min', None)
        geo_loc_1_ns = page_app.get('geoloc1_ns', None)
        geo_loc_1_sec1 = page_app.get('geoloc1_sec1', None)
        geo_loc_1_sec2 = page_app.get('geoloc1_sec2', None)
        geo_loc_1_time = page_app.get('geoloc1_time', None)
        geo_loc_2_ew = page_app.get('geoloc2_ew', None)
        geo_loc_2_min = page_app.get('geoloc2_min', None)
        geo_loc_2_sec1 = page_app.get('geoloc2_sec1', None)
        geo_loc_2_sec2 = page_app.get('geoloc2_sec2', None)
        geo_loc_2_time = page_app.get('geoloc2_time', None)

        if bst_state is not None:
            bst_state = int(bst_state)
        if aap_batch_set is not None:
            aap_batch_set = bool(int(aap_batch_set))
        if detect_paper_width is not None:
            detect_paper_width = bool(int(detect_paper_width))
        if geo_alti is not None:
            geo_alti = int(geo_alti)
        if geo_loc_1_min is not None:
            geo_loc_1_min = int(geo_loc_1_min)
        if geo_loc_1_ns is not None:
            geo_loc_1_ns = int(geo_loc_1_ns)
        if geo_loc_1_sec1 is not None:
            geo_loc_1_sec1 = int(geo_loc_1_sec1)
        if geo_loc_1_sec2 is not None:
            geo_loc_1_sec2 = int(geo_loc_1_sec2)
        if geo_loc_1_time is not None:
            geo_loc_1_time = int(geo_loc_1_time)
        if geo_loc_2_ew is not None:
            geo_loc_2_ew = int(geo_loc_2_ew)
        if geo_loc_2_min is not None:
            geo_loc_2_min = int(geo_loc_2_min)
        if geo_loc_2_sec1 is not None:
            geo_loc_2_sec1 = int(geo_loc_2_sec1)
        if geo_loc_2_sec2 is not None:
            geo_loc_2_sec2geo_loc_2_sec2 = int(geo_loc_2_sec2)
        if geo_loc_2_time is not None:
            geo_loc_2_time = int(geo_loc_2_time)
        if job_number is not None:
            job_number = int(job_number)

        bon = \
        {
            'conflict': bon_conflict,
            'name': bon_name,
            'note': bon_note,
        }
        geo = \
        {
            'alti': geo_alti,
            1: \
            {
                'min': geo_loc_1_min,
                'ns': geo_loc_1_ns,
                'sec': \
                {
                    1: geo_loc_1_sec1,
                    2: geo_loc_1_sec2,
                },
                'time': geo_loc_1_time,
            },
            2: \
            {
                'ew': geo_loc_2_ew,
                'min': geo_loc_2_min,
                'sec': \
                {
                    1: geo_loc_2_sec1,
                    2: geo_loc_2_sec2,
                },
                'time': geo_loc_2_time,
            },
        }

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'result': result,
            'warning_id': warning_id,
            'job_number': job_number,
            'aap_batch_set': aap_batch_set,
            'bon': bon,
            'detect_paper_width': detect_paper_width,
            'geo': geo,
        }

        return data

    def machininfo_data \
            (
                self,
                set_info = None,
                get_info = None,
                dry_level = None,
                detect_paper_width = None,
                left_margin_cassette_1 = None,
                paper_gap = None,
                power_save_off = None,
                power_save_time = None,
                power_save_on = None,
            ):
        """
        Human Wrapper for: super().machininfo_data
        """

        kwargs = \
        {
            'setinfo': set_info,
            'getinfo': get_info,
            'dry_level': dry_level,
            'detect_paper_width': detect_paper_width,
            'left_margin_ca1': left_margin_cassette_1,
            'paper_gap': paper_gap,
            'power_save_off': power_save_off,
            'power_save_time': power_save_time,
            'power_save_on': power_save_on,
        }

        raw = super().machininfo_data(**kwargs)

        page_hardinfo = raw.get('page_hardinfo', {})

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        auto_agitation = page_hardinfo.get('auto_agitation', None)
        detect_paper_width = page_hardinfo.get('detect_paper_width', None)
        dry_level = page_hardinfo.get('dry_level', None)
        left_margin_cassette_1 = page_hardinfo.get('left_margin_ca1', None)
        paper_gap = page_hardinfo.get('paper_gap', None)
        power_save_off = page_hardinfo.get('power_save_off', None)
        power_save_on = page_hardinfo.get('power_save_on', None)
        power_save_time = page_hardinfo.get('power_save_time', None)
        silent_mode = page_hardinfo.get('silent_mode', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)
        if auto_agitation is not None:
            auto_agitation = bool(int(auto_agitation))
        if detect_paper_width is not None:
            detect_paper_width = bool(int(detect_paper_width))
        if dry_level is not None:
            dry_level = int(dry_level)
        if left_margin_cassette_1 is not None:
            left_margin_cassette_1 = int(left_margin_cassette_1)
        if paper_gap is not None:
            paper_gap = int(paper_gap)
        if power_save_off is not None:
            power_save_off = bool(int(power_save_off))
        if power_save_on is not None:
            power_save_on = bool(int(power_save_on))
        if power_save_time is not None:
            power_save_time = int(power_save_time)

        power_save = \
        {
            'on': power_save_on,
            'off': power_save_off,
            'time': power_save_time,
        }

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'auto_agitation': auto_agitation,
            'detect_paper_width': detect_paper_width,
            'dry_level': dry_level,
            'left_margin_cassette_1': left_margin_cassette_1,
            'paper_gap': paper_gap,
            'power_save': power_save,
            'silent_mode': silent_mode,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def silent_mode(self, silent_mode=None):
        """
        Human Wrapper for: super().silent_mode
        """

        kwargs = \
        {
            'silent_mode': silent_mode,
        }

        raw = super().silent_mode(**kwargs)

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def ut_nozzle_check(self):
        """
        Human Wrapper for: super().ut_nozzle_check
        """

        raw = super().ut_nozzle_check()

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        job_number = raw.get('job_num', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)
        if job_number is not None:
            job_number = int(job_number)

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'job_number': job_number,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def ut_regi_print(self):
        """
        Human Wrapper for: super().ut_regi_print
        """

        raw = super().ut_regi_print()

        bst_state = raw.get('bst_state', None)
        error_display_state = raw.get('err_disp_state', None)
        job_number = raw.get('job_num', None)
        result = raw.get('result', None)
        warning_id = raw.get('warning_id', None)

        if bst_state is not None:
            bst_state = int(bst_state)
        if job_number is not None:
            job_number = int(job_number)

        data = \
        {
            'bst_state': bst_state,
            'error_display_state': error_display_state,
            'job_number': job_number,
            'result': result,
            'warning_id': warning_id,
        }

        return data

    def sendpw(self, password_hash=None, id_type=None):
        """
        Human Wrapper for: super().sendpw
        """

        kwargs = \
        {
            'namae': password_hash,
            'idtype': id_type,
        }

        raw = super().sendpw(**kwargs)

        return raw
