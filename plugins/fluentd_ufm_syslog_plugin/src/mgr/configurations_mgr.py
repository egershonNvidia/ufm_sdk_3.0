#
# Copyright © 2013-2022 NVIDIA CORPORATION & AFFILIATES. ALL RIGHTS RESERVED.
#
# This software product is a proprietary product of Nvidia Corporation and its affiliates
# (the "Company") and all right, title, and interest in and to the software
# product, including all associated intellectual property rights, are and
# shall remain exclusively with the Company.
#
# This software product is governed by the End User License Agreement
# provided with the software product.
# @author: Anan Al-Aghbar
# @date:   Sep 19, 2022
#

import os
import sys
sys.path.append(os.getcwd())

from utils.config_parser import ConfigParser


class UFMSyslogStreamingConfigParser(ConfigParser):
    # for debugging
    # config_file = "../conf/fluentd_ufm_syslog_plugin.cfg"

    # for production with docker
    config_file = "/config/fluentd_ufm_syslog_plugin.cfg"

    DESTINATION_ENDPOINT_SECTION = "destination-endpoint"
    DESTINATION_ENDPOINT_SECTION_HOST = "host"
    DESTINATION_ENDPOINT_SECTION_PORT = "port"

    STREAMING_SECTION = "streaming"
    STREAMING_SECTION_ENABLED = "enabled"
    STREAMING_SECTION_MESSAGE_TAG_NAME = "message_tag_name"

    def __init__(self):
        super().__init__(read_sdk_config=False)
        self.sdk_config.read(self.config_file)

    def get_enable_streaming_flag(self):
        return self.safe_get_bool(None,
                                  self.STREAMING_SECTION,
                                  self.STREAMING_SECTION_ENABLED,
                                  False)

    def get_message_tag_name(self):
        return self.get_config_value(None,
                                     self.STREAMING_SECTION,
                                     self.STREAMING_SECTION_MESSAGE_TAG_NAME,
                                     'ufm_syslog')

    def get_fluentd_host(self):
        return self.get_config_value(None,
                                     self.DESTINATION_ENDPOINT_SECTION,
                                     self.DESTINATION_ENDPOINT_SECTION_HOST)

    def get_fluentd_port(self):
        return self.safe_get_int(None,
                                 self.DESTINATION_ENDPOINT_SECTION,
                                 self.DESTINATION_ENDPOINT_SECTION_PORT)
