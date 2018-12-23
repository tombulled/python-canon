from .AbstractPrinter import AbstractPrinter
from .. import utils

"""
Imports:
    .AbstractPrinter.AbstractPrinter
    ..utils
"""

class Printer(AbstractPrinter):
    """
    Base printer once its already gone through:
        <AbstractPrinter> (super)
        <WrappedPrinter>
        <BasePrinter>
    """

    def __init__(self, *args, **kwargs):
        """
        Initialise self and super
        """

        super().__init__(*args, **kwargs)

    def unregister_ij_printing(self):
        """
        Wrapper for: super().call_ijcpc_del()
        """

        data = super().call_ijcpc_del()

        return data

    def create_tls_certificate \
            (
                self,
                dsa = 0,
                key_bit = 2048,
                start_date = 0,
                end_date = 0,
                **kwargs,
            ):
        """
        Wrapper for: super().set_tls_create_cert(**kwargs)

        Defaults:
            dsa -> 0
            key_bit -> 2048
            start_date -> 0
            end_date -> 0
        """

        kwargs.update \
        (
            {
                'dsa': dsa,
                'key_bit': key_bit,
                'start_date': start_date,
                'end_date': end_date,
            }
        )

        data = super().set_tls_create_cert(**kwargs)

        return data

    def get_printer_info(self):
        """
        Wrapper for: super().get_prninfo_data()
        """

        data = super().get_prninfo_data()

        return data

    def get_model(self):
        """
        Wrapper for: super().get_model()
        """

        data = super().get_model()

        return data

    def get_lan_setting(self):
        """
        Wrapper for: super().get_lan_set_lan_if()
        """

        data = super().get_lan_set_lan_if()

        return data

    def set_display_language(self, language_index): # pointless?
        """
        Wrapper for: super().get_index(language_index=language_index)
        """

        kwargs = \
        {
            'language_index': language_index,
        }

        data = super().get_index(**kwargs)

    def get_firmware_version(self):
        """
        Wrapper for: super().get_firm_version()
        """

        data = super().get_firm_version()

        return data

    def verify_firmware(self):
        """
        Wrapper for: super().get_firm_verify()
        """

        data = super().get_firm_verify()

        return data

    def get_job_status(self, job_number):
        """
        Wrapper for: super().get_job_status(job_number=job_number)
        """

        kwargs = \
        {
            'job_number': job_number,
        }

        data = super().get_job_status(**kwargs)

        return data

    def get_lan_settings(self):
        """
        Wrapper for: super().get_lan_setting_info()
        """

        data = super().get_lan_setting_info()

        return data

    def get_system_data(self):
        """
        Wrapper for: super().get_sysinfo_data()
        """

        data = super().get_sysinfo_data()

        return data

    def get_tls_certificate_info(self):
        """
        Wrapper for: super().get_tls_cert_info()
        """

        data = super().get_tls_cert_info()

        return data

    def get_ipv4_data(self):
        """
        Wrapper for: super().get_lan_ipv4_data()
        """

        data = super().get_lan_ipv4_data()

        return data

    def set_ipv4_data(self, **kwargs): # starts job
        """
        Wrapper for: super().set_lan_ipv4_data(**kwargs)
        """

        data = super().set_lan_ipv4_data(**kwargs)

        return data

    def print_lan_data(self):
        """
        Wrapper for: super().call_lan_data_print()
        """

        data = super().call_lan_data_print()

        return data

    def tls_certificate_exists(self):
        """
        Wrapper for: super().get_tls_is_found_cert()
        """

        data = super().get_tls_is_found_cert()

        return data

    def tls_csr_exists(self):
        """
        Wrapper for: super().get_tls_is_created_csr()
        """

        data = super().get_tls_is_created_csr()

        return data

    def create_tls_csr \
            (
                self,
                dsa = 0,
                key_bit = 2048,
                **kwargs,
            ):
        """
        Wrapper for: super().set_tls_create_csr(**kwargs)

        Defaults:
            dsa -> 0
            key_bit -> 2048
        """

        kwargs.update \
        (
            {
                'dsa': dsa,
                'key_bit': key_bit,
            }
        )

        data = super().set_tls_create_csr(**kwargs)

        return data

    def download_tls_csr(self):
        """
        Wrapper for: super().call_tls_download_csr()
        """

        data = super().call_tls_download_csr()

        return data

    def pre_download_tls_csr(self):
        """
        Wrapper for: super().get_tls_pre_download_csr()
        """

        data = super().get_tls_pre_download_csr()

        return data

    def restart_lan(self):
        """
        Wrapper for: super().call_tls_exec_lan_restart()
        """

        data = super().call_tls_exec_lan_restart()

        return data

    def delete_tls_certificate(self):
        """
        Wrapper for: super().call_tls_delete_cert()
        """

        data = super().call_tls_delete_cert()

        return data

    def get_security_settings(self):
        """
        Wrapper for: super().get_se_setting_restriction()
        """

        data = super().get_se_setting_restriction()

        return data

    def set_admin_password(self, admin_password):
        """
        Wrapper for: super().set_se_setting_restriction(**kwargs)

        Sends:
            admin_password: SET
            scope: RUI_NETTOOL
            password: utils.sha256(admin_password)
        """

        password_hash = utils.sha256(admin_password)

        kwargs = \
        {
            'admin_password': 'SET',
            'scope': 'RUI_NETTOOL',
            'password': password_hash,
        }

        data = super().set_se_setting_restriction(**kwargs)

        return data

    def delete_admin_password(self):
        """
        Wrapper for: super().set_se_setting_restriction(**kwargs)

        Sends:
            admin_password: CLEAR
        """

        kwargs = \
        {
            'admin_password': 'CLEAR',
        }

        data = super().set_se_setting_restriction(**kwargs)

        return data

    def register_ij_printing(self):
        """
        Wrapper for: super().call_ijcpc_printer_regi()
        """

        data = super().call_ijcpc_printer_regi()

        return data

    def ij_printing_registered(self):
        """
        Wrapper for: super().get_ijcpc_is_already()
        """

        data = super().get_ijcpc_is_already()

        return data

    def recover_from_error(self):
        """
        Wrapper for: super().call_err_recover()
        """

        data = super().call_err_recover()

        return data

    def google_printing_registered(self):
        """
        Wrapper for: super().get_gcp_is_gcp()
        """

        data = super().get_gcp_is_gcp()

        return data

    def register_google_printing(self):
        """
        Wrapper for: super().call_gcp_regi()
        """

        data = super().call_gcp_regi()

        return data

    def get_app_data(self):
        """
        Wrapper for: super().get_app_data()
        """

        data = super().get_app_data()

        return data

    def set_app_data(self, **kwargs):
        """
        Wrapper for: super().set_app_data(**kwargs)
        """

        data = super().set_app_data(**kwargs)

        return data

    def get_machine_data(self):
        """
        Wrapper for: super().get_machininfo_data()
        """

        data = super().get_machininfo_data()

        return data

    def set_machine_data(self, **kwargs):
        """
        Wrapper for: super().set_machininfo_data(**kwargs)
        """

        data = super().set_machininfo_data(**kwargs)

        return data

    def enable_silent_mode(self, silent_mode):
        """
        Wrapper for: super().call_silent_mode(**kwargs)

        Sends:
            silent_mode: ON if silent_mode else OFF
        """

        silent_modes_map = \
        {
            True: 'ON',
            False: 'OFF',
        }

        decoded_silent_mode = silent_modes_map[bool(silent_mode)]

        kwargs = \
        {
            'silent_mode': decoded_silent_mode,
        }

        data = super().call_silent_mode(**kwargs)

        return data

    def print_nozzle_check(self):
        """
        Wrapper for: super().call_ut_nozzle_check()
        """

        data = super().call_ut_nozzle_check()

        return data

    def print_head_alignment(self):
        """
        Wrapper for: super().call_ut_regi_print()
        """

        data = super().call_ut_regi_print()

        return data

    def login(self, password):
        """
        Wrapper for: super().call_sendpw(**kwargs)

        Sends:
            password_hash: utils.sha256(password)
            id_type: 2
        """

        password_hash = utils.sha256(password)

        kwargs = \
        {
            'password_hash': password_hash,
            'id_type': 2,
        }

        data = super().call_sendpw(**kwargs)

        return data
