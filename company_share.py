import csv
from pprint import pprint


class CompanyShare(object):
    """
    Description:
        Main class which calculates maximum share
        for N number of companies
    """

    def __init__(self, file_path):
        """
        Description:
            Initializing data by reading all
            the rows from csv
        """
        self.data = self._read_csv(file_path)

    def _read_csv(self, file_path):
        """
        Description:
            Reading csv file
        Args:
            file_path - path of csv file
        Returns:
            data set
        Raises:
            IOError in case file path is invalid
        """
        data = []
        try:
            f = open(file_path, 'rb')
            reader = csv.reader(f)
            data = [line for line in reader]
        except IOError:
            raise IOError("Not a valid file path !")
        return data

    def rows_count(self):
        """
        Description:
            calculates count as total number of
            rows in csv file
        Returns:
            count of rows
        """
        return len(self.data)

    def column_count(self):
        """
        Description:
            calculates total number of columns in csv
        Returns:
            count of columns
        """
        return len(self.data[0])

    def highest_share_price(self):
        """
        Description:
            function which calculates year of maximum share
            price for a company
        Algorithm:
            Assigning given first year company A has maximum
            share and performing comparisions till end of the
            rows and if larger value from assigned found
            new assigned value will be changes with larger one
            and process is being repeated for all N other companies
        Complexity:
            O(N*M)
            where N - number of companies, M - number of rows
        Returns:
            Details of all those companies having maximum share
            price with detail of year, month and share price
        """
        company_details = {}
        rows = self.rows_count()
        columns = self.column_count()

        # Index value is set to 2 because company
        # details starts from second index
        index = 2

        while index < columns:

            # starting scaning for highest share company
            row = 1
            highest_share = row

            while row < rows:
                if int(
                    self.data[highest_share][index]) <= int(
                        self.data[row][index]):
                    highest_share = row
                row += 1

            # Updating details for highest share company
            company_details[str(self.data[0][index])] = {}
            company_details[str(self.data[0][index])]['year'] = str(
                self.data[highest_share][0])
            company_details[str(self.data[0][index])]['month'] = str(
                self.data[highest_share][1])
            company_details[str(self.data[0][index])]['share'] = str(
                self.data[highest_share][index])

            index += 1
        return company_details


if __name__ == "__main__":
    obj = CompanyShare("test_shares_data.csv")
    pprint(obj.highest_share_price())
