"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qaseio
from qaseio.model.attachment_get import AttachmentGet
from qaseio.model.attachment_response_all_of import AttachmentResponseAllOf
from qaseio.model.response import Response
globals()['AttachmentGet'] = AttachmentGet
globals()['AttachmentResponseAllOf'] = AttachmentResponseAllOf
globals()['Response'] = Response
from qaseio.model.attachment_response import AttachmentResponse


class TestAttachmentResponse(unittest.TestCase):
    """AttachmentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAttachmentResponse(self):
        """Test AttachmentResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AttachmentResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
