"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import qaseio
from qaseio.api.results_api import ResultsApi  # noqa: E501


class TestResultsApi(unittest.TestCase):
    """ResultsApi unit test stubs"""

    def setUp(self):
        self.api = ResultsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_result(self):
        """Test case for create_result

        Create test run result.  # noqa: E501
        """
        pass

    def test_create_result_bulk(self):
        """Test case for create_result_bulk

        Bulk create test run result.  # noqa: E501
        """
        pass

    def test_delete_result(self):
        """Test case for delete_result

        Delete test run result.  # noqa: E501
        """
        pass

    def test_get_result(self):
        """Test case for get_result

        Get test run result by code.  # noqa: E501
        """
        pass

    def test_get_results(self):
        """Test case for get_results

        Get all test run results.  # noqa: E501
        """
        pass

    def test_update_result(self):
        """Test case for update_result

        Update test run result.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
