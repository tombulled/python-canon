from .Printer import Printer
from .. import utils

"""
Imports:
    .Printer.Printer
    ..utils

Contains:
    <MG5700>
"""

class MG5700(object):
    """
    Highest Level Printer
    """

    def __init__(self, *args, **kwargs):
        """
        Initialise self
        """

        self._init_attrs()

        self.Printer = Printer(*args, **kwargs)
        self.host = self.Printer.host

        self._init()

    def _init(self):
        """
        Construct self
        """

        inherit_attrs = \
        (
            'unregister_ij_printing',
            'create_tls_certificate',
            'get_printer_info',
            'get_model',
            'get_lan_setting',
            'set_display_language',
            'get_firmware_version',
            'verify_firmware',
            'get_job_status',
            'get_lan_settings',
            'get_system_data',
            'get_tls_certificate_info',
            'get_ipv4_data',
            'set_ipv4_data',
            'print_lan_data',
            'tls_certificate_exists',
            'tls_csr_exists',
            'create_tls_csr',
            'download_tls_csr',
            'pre_download_tls_csr',
            'restart_lan',
            'delete_tls_certificate',
            'get_security_settings',
            'set_admin_password',
            'delete_admin_password',
            'register_ij_printing',
            'ij_printing_registered',
            'recover_from_error',
            'google_printing_registered',
            'register_google_printing',
            'get_app_data',
            'set_app_data',
            'get_machine_data',
            'set_machine_data',
            'enable_silent_mode',
            'print_nozzle_check',
            'print_head_alignment',
            'login',
        )

        utils.selectively_inherit \
        (
            dst = self,
            src = self.Printer,
            attrs = inherit_attrs,
        )

    def __repr__(self):
        """
        Return a string representation of the class
        ... in the form: '<Canon-{self.__class__.__name__}({self.host})>'
        """

        data = f'<Canon-{self.__class__.__name__}({self.host})>'

        return data

    def _init_attrs(self):
        """
        Initialise class attributes
        """

        self.Printer = None
        self.host = None

    def _super(self):
        """
        Returns the indirect super class: self.Printer
        """

        return self.Printer
