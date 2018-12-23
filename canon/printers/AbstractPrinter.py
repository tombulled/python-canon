from .WrappedPrinter import WrappedPrinter

"""
Imports:
    .WrappedPrinter.WrappedPrinter

Contains:
    <AbstractPrinter>
"""

class AbstractPrinter(WrappedPrinter):
    """
    Inherits from: <WrappedPrinter>

    Renames methods to use a 'get_*', 'set_*', 'call_*
    ... naming scheme
    """

    def __init__(self, *args, **kwargs):
        """
        Initialise self and super
        """

        super().__init__(*args, **kwargs)

    def call_ijcpc_del(self):
        """
        Wrapper for: super().ijcpc_del
        """

        data = super().ijcpc_del()

        return data

    def set_tls_create_cert(self, **kwargs):
        """
        Wrapper for: super().tls_create_cert(set_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'set_info': 0,
            }
        )

        data = super().tls_create_cert(**kwargs)

        return data

    def get_prninfo_data(self, **kwargs):
        """
        Wrapper for: super().prninfo_data(get_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'get_info': 0,
            }
        )

        data = super().prninfo_data(**kwargs)

        return data

    def get_model(self, **kwargs):
        """
        Wrapper for: super().model(version='2.040-178E-026', **kwargs)
        """

        kwargs.update \
        (
            {
                'version': '2.040-178E-026',
            }
        )

        data = super().model(**kwargs)

        return data

    def get_lan_set_lan_if(self, **kwargs):
        """
        Wrapper for: super().lan_set_lan_if(get_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'get_info': 0,
            }
        )

        data = super().lan_set_lan_if(**kwargs)

        return data

    def get_index(self, **kwargs):
        """
        Wrapper for: super().index(**kwargs)
        """

        data = super().index(**kwargs)

        return data

    def get_firm_version(self, **kwargs):
        """
        Wrapper for: super().firm_version(**kwargs)
        """

        data = super().firm_version(**kwargs)

        return data

    def get_firm_verify(self, **kwargs):
        """
        Wrapper for: super().firm_verify(**kwargs)
        """

        data = super().firm_verify(**kwargs)

        return data

    def get_job_status(self, **kwargs):
        """
        Wrapper for: super().get_job_status(**kwargs)
        """

        data = super().get_job_status(**kwargs)

        return data

    def get_lan_setting_info(self, **kwargs):
        """
        Wrapper for: super().get_lan_setting_info(get_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'get_info': 0,
            }
        )

        data = super().get_lan_setting_info(**kwargs)

        return data

    def get_sysinfo_data(self, **kwargs):
        """
        Wrapper for: super().sysinfo_data(get_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'get_info': 0,
            }
        )

        data = super().sysinfo_data(**kwargs)

        return data

    def get_tls_cert_info(self, **kwargs):
        """
        Wrapper for: super().tls_get_cert_info(get_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'get_info': 0,
            }
        )

        data = super().tls_get_cert_info(**kwargs)

        return data

    def get_lan_ipv4_data(self, **kwargs):
        """
        Wrapper for: super().lan_ipv4_data(get_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'get_info': 0,
            }
        )

        data = super().lan_ipv4_data(**kwargs)

        return data

    def set_lan_ipv4_data(self, **kwargs):
        """
        Wrapper for: super().lan_ipv4_data(set_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'set_info': 0,
            }
        )

        data = super().lan_ipv4_data(**kwargs)

        return data

    def call_lan_data_print(self, **kwargs):
        """
        Wrapper for: super().lan_data_print(**kwargs)
        """

        data = super().lan_data_print(**kwargs)

        return data

    def get_tls_is_found_cert(self, **kwargs):
        """
        Wrapper for: super().tls_is_found_cert(get_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'get_info': 0,
            }
        )

        data = super().tls_is_found_cert(**kwargs)

        return data

    def get_tls_is_created_csr(self, **kwargs):
        """
        Wrapper for: super().tls_is_created_csr(get_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'get_info': 0,
            }
        )

        data = super().tls_is_created_csr(**kwargs)

        return data

    def set_tls_create_csr(self, **kwargs):
        """
        Wrapper for: super().tls_create_csr(set_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'set_info': 0,
            }
        )

        data = super().tls_create_csr(**kwargs)

        return data

    def call_tls_download_csr(self, **kwargs):
        """
        Wrapper for: super().tls_download_csr(**kwargs)
        """

        data = super().tls_download_csr(**kwargs)

        return data

    def get_tls_pre_download_csr(self, **kwargs):
        """
        Wrapper for: super().tls_pre_download_csr(get_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'get_info': 0,
            }
        )

        data = super().tls_pre_download_csr(**kwargs)

        return data

    def call_tls_exec_lan_restart(self, **kwargs):
        """
        Wrapper for: super().tls_exec_lan_restart(**kwargs)
        """

        data = super().tls_exec_lan_restart(**kwargs)

        return data

    def call_tls_delete_cert(self, **kwargs):
        """
        Wrapper for: super().tls_delete_cert(**kwargs)
        """

        data = super().tls_delete_cert(**kwargs)

        return data

    def set_se_setting_restriction(self, **kwargs):
        """
        Wrapper for: super().se_setting_restriction(set_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'set_info': 0,
            }
        )

        data = super().se_setting_restriction(**kwargs)

        return data

    def get_se_setting_restriction(self, **kwargs):
        """
        Wrapper for: super().se_setting_restriction(get_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'get_info': 0,
            }
        )

        data = super().se_setting_restriction(**kwargs)

        return data

    def get_ijcpc_is_already(self, **kwargs):
        """
        Wrapper for: super().ijcpc_is_already(get_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'get_info': 0,
            }
        )

        data = super().ijcpc_is_already(**kwargs)

        return data

    def call_ijcpc_printer_regi(self, **kwargs):
        """
        Wrapper for: super().ijcpc_printer_regi(**kwargs)
        """

        data = super().ijcpc_printer_regi(**kwargs)

        return data

    def call_err_recover(self, **kwargs):
        """
        Wrapper for: super().err_recover(**kwargs)
        """

        data = super().err_recover(**kwargs)

        return data

    def get_gcp_is_gcp(self, **kwargs):
        """
        Wrapper for: super().gcp_is_gcp(get_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'get_info': 0,
            }
        )

        data = super().gcp_is_gcp(**kwargs)

        return data

    def call_gcp_regi(self, **kwargs):
        """
        Wrapper for: super().gcp_regi(**kwargs)
        """

        data = super().gcp_regi(**kwargs)

        return data

    def get_app_data(self, **kwargs):
        """
        Wrapper for: super().app_data(get_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'get_info': 0,
            }
        )

        data = super().app_data(**kwargs)

        return data

    def set_app_data(self, **kwargs):
        """
        Wrapper for: super().app_data(set_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'set_info': 0,
            }
        )

        data = super().app_data(**kwargs)

        return data

    def get_machininfo_data(self, **kwargs):
        """
        Wrapper for: super().machininfo_data(get_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'get_info': 0,
            }
        )

        data = super().machininfo_data(**kwargs)

        return data

    def set_machininfo_data(self, **kwargs):
        """
        Wrapper for: super().machininfo_data(set_info=0, **kwargs)
        """

        kwargs.update \
        (
            {
                'set_info': 0,
            }
        )

        data = super().machininfo_data(**kwargs)

        return data

    def call_silent_mode(self, **kwargs):
        """
        Wrapper for: super().silent_mode(**kwargs)
        """

        data = super().silent_mode(**kwargs)

        return data

    def call_ut_nozzle_check(self, **kwargs):
        """
        Wrapper for: super().ut_nozzle_check(**kwargs)
        """

        data = super().ut_nozzle_check(**kwargs)

        return data

    def call_ut_regi_print(self, **kwargs):
        """
        Wrapper for: super().ut_regi_print(**kwargs)
        """

        data = super().ut_regi_print(**kwargs)

        return data

    def call_sendpw(self, **kwargs):
        """
        Wrapper for: super().sendpw(**kwargs)
        """

        data = super().sendpw(**kwargs)

        return data
