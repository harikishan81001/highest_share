import sys
import unittest

from company_share import CompanyShare


class TestCompanyShare(unittest.TestCase):
    """
    Description:
        UnitTest cases for testing heighest share price
    """
    EXPECTED = {
        'Company-A': {'month': 'Mar', 'share': '1000', 'year': '2000'},
        'Company-B': {'month': 'Mar', 'share': '986', 'year': '2007'},
        'Company-C': {'month': 'Jun', 'share': '995', 'year': '1993'},
        'Company-D': {'month': 'Apr', 'share': '999', 'year': '2002'},
        'Company-E': {'month': 'Oct', 'share': '997', 'year': '2008'}}
    csv_file_path = "test_shares_data.csv"

    def test_company_share(self):
        """
        Description:
            testing main working module for different-2 companies
        """
        obj = CompanyShare(self.csv_file_path)
        highest_share = obj.highest_share_price()
        self.assert_companyA(highest_share)
        self.assert_companyB(highest_share)
        self.assert_companyC(highest_share)
        self.assert_companyD(highest_share)
        self.assert_companyE(highest_share)

    def assert_companyA(self, hightest_price):
        """
        Test the company0
        """
        self.assertEqual(
            hightest_price['Company-A']['year'],
            self.EXPECTED['Company-A']['year'])

        self.assertEqual(
            hightest_price['Company-A']['month'],
            self.EXPECTED['Company-A']['month'])

        self.assertEqual(
            hightest_price['Company-A']['share'],
            self.EXPECTED['Company-A']['share'])

    def assert_companyB(self, hightest_price):
        """
        Test the company1
        """
        self.assertEqual(
            hightest_price['Company-B']['year'],
            self.EXPECTED['Company-B']['year'])

        self.assertEqual(
            hightest_price['Company-B']['month'],
            self.EXPECTED['Company-B']['month'])

        self.assertEqual(
            hightest_price['Company-B']['share'],
            self.EXPECTED['Company-B']['share'])

    def assert_companyC(self, hightest_price):
        """
        Test the company2
        """
        self.assertEqual(
            hightest_price['Company-C']['year'],
            self.EXPECTED['Company-C']['year'])

        self.assertEqual(
            hightest_price['Company-C']['month'],
            self.EXPECTED['Company-C']['month'])

        self.assertEqual(
            hightest_price['Company-C']['share'],
            self.EXPECTED['Company-C']['share'])

    def assert_companyD(self, hightest_price):
        """
        Test the company3
        """
        self.assertEqual(
            hightest_price['Company-D']['year'],
            self.EXPECTED['Company-D']['year'])

        self.assertEqual(
            hightest_price['Company-D']['month'],
            self.EXPECTED['Company-D']['month'])

        self.assertEqual(
            hightest_price['Company-D']['share'],
            self.EXPECTED['Company-D']['share'])

    def assert_companyE(self, hightest_price):
        """
        Test the company4
        """
        self.assertEqual(
            hightest_price['Company-E']['year'],
            self.EXPECTED['Company-E']['year'])

        self.assertEqual(
            hightest_price['Company-E']['month'],
            self.EXPECTED['Company-E']['month'])

        self.assertEqual(
            hightest_price['Company-E']['share'],
            self.EXPECTED['Company-E']['share'])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCompanyShare)
    unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit()
