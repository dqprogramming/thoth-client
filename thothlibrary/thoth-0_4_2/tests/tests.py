"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import json
import unittest

import requests_mock
from thothlibrary import ThothClient


class Thoth042Tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # we set this fake endpoint to ensure that the tests are definitely
        # running against the local objects, rather than the remote server
        self.endpoint = "https://api.test042.thoth.pub"
        self.version = "0.4.2"

    def test_works(self):
        """
        Tests that good input to works produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('works', m)
            self.pickle_tester('works', thoth_client.works)
        return None

    def test_works_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('works_bad', m)
            self.pickle_tester('works', thoth_client.works, negative=True)
        return None

    def test_works_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('works', m)
            self.raw_tester(mock_response, thoth_client.works)
        return None

    def test_work_by_doi(self):
        """
        Tests that good input to work_by_doi produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('workByDoi', m)
            self.pickle_tester('workByDoi',
                               lambda:
                               thoth_client.work_by_doi(doi='https://doi.org/'
                                                            '10.21983/P3.0314.1'
                                                            '.00'))
        return None

    def test_work_by_doi_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('workByDoi_bad', m)
            self.pickle_tester('work',
                               lambda: thoth_client.work_by_doi(doi='https://'
                                                                    'doi.org/10'
                                                                    '.21983/P3'
                                                                    '.0314.1.'
                                                                    '00'),
                               negative=True)
        return None

    def test_work_by_doi_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('workByDoi', m)
            self.raw_tester(mock_response,
                            lambda: thoth_client.work_by_doi(doi='https://doi.'
                                                                 'org/10.21983'
                                                                 '/P3.0314.1.'
                                                                 '00',
                                                             raw=True),
                            lambda_mode=True)
        return None

    def test_work_by_id(self):
        """
        Tests that good input to work_by_id produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('work', m)
            self.pickle_tester('work',
                               lambda:
                               thoth_client.work_by_id(work_id='e0f748b2-984f-'
                                                               '45cc-8b9e-'
                                                               '13989c31dda4'))
        return None

    def test_work_by_id_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('work_bad', m)
            self.pickle_tester('work',
                               lambda: thoth_client.work_by_id(
                                   work_id='e0f748b2'
                                           '-'
                                           '984f-'
                                           '45cc-'
                                           '8b9e-'
                                           '13989c31'
                                           'dda4'),
                               negative=True)
        return None

    def test_work_by_id_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('work', m)
            self.raw_tester(mock_response,
                            lambda: thoth_client.work_by_id(work_id='e0f748b2'
                                                                    '-'
                                                                    '984f-'
                                                                    '45cc-'
                                                                    '8b9e-'
                                                                    '13989c31'
                                                                    'dda4',
                                                            raw=True),
                            lambda_mode=True)
        return None

    def test_publication(self):
        """
        Tests that good input to publication produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publication', m)
            self.pickle_tester('publication',
                               lambda:
                               thoth_client.publication(publication_id=
                                                        '34712b75'
                                                        '-dcdd'
                                                        '-408b'
                                                        '-8d0c'
                                                        '-cf29a35'
                                                        'be2e5'))
        return None

    def test_publication_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publication_bad',
                                                            m)
            self.pickle_tester('publication',
                               lambda: thoth_client.publication(
                                   publication_id='34712b75-dcdd-408b-8d0c-'
                                                  'cf29a35be2e5'),
                               negative=True)
        return None

    def test_publication_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publication', m)
            self.raw_tester(mock_response,
                            lambda: thoth_client.publication(publication_id=
                                                             '34712b75'
                                                             '-dcdd'
                                                             '-408b'
                                                             '-8d0c'
                                                             '-cf29a'
                                                             '35be2e5',
                                                             raw=True),
                            lambda_mode=True)
        return None

    def test_publications(self):
        """
        Tests that good input to publications produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publications', m)
            self.pickle_tester('publications', thoth_client.publications)
        return None

    def test_publications_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publications_bad',
                                                            m)
            self.pickle_tester('publications', thoth_client.publications,
                               negative=True)
        return None

    def test_publications_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publications', m)
            self.raw_tester(mock_response, thoth_client.publications)
        return None

    def test_publisher(self):
        """
        Tests that good input to publisher produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publisher', m)
            self.pickle_tester('publisher',
                               lambda:
                               thoth_client.publisher(
                                   publisher_id='85fd969a-a16c-480b-b641-cb9adf979c3b'))
        return None

    def test_publisher_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publisher_bad', m)
            self.pickle_tester('publisher',
                               lambda: thoth_client.publisher(
                                   publisher_id='85fd969a-a16c-480b-b641-'
                                                'cb9adf979c3b'),
                               negative=True)
        return None

    def test_publisher_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publisher', m)
            self.raw_tester(mock_response,
                            lambda: thoth_client.publisher(
                                publisher_id='85fd969a-a16c-480b-b641-'
                                             'cb9adf979c3b',
                                raw=True),
                            lambda_mode=True)
        return None

    def test_publishers(self):
        """
        Tests that good input to publishers produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publishers', m)
            self.pickle_tester('publishers', thoth_client.publishers)
        return None

    def test_publishers_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publishers_bad', m)
            self.pickle_tester('publishers', thoth_client.publishers,
                               negative=True)

    def test_publishers_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publishers', m)
            self.raw_tester(mock_response, thoth_client.publishers)
        return None

    def test_imprint(self):
        """
        Tests that good input to imprint produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('imprint', m)
            self.pickle_tester('imprint',
                               lambda:
                               thoth_client.imprint(
                                   imprint_id='78b0a283-9be3-4fed-a811-'
                                              'a7d4b9df7b25'))
        return None

    def test_imprint_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('imprint_bad', m)
            self.pickle_tester('imprint',
                               lambda: thoth_client.imprint(
                                   imprint_id='78b0a283-9be3-4fed-a811-'
                                              'a7d4b9df7b25'),
                               negative=True)
        return None

    def test_imprint_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('imprint', m)
            self.raw_tester(mock_response,
                            lambda: thoth_client.imprint(
                                imprint_id='78b0a283-9be3-4fed-a811-'
                                           'a7d4b9df7b25',
                                raw=True),
                            lambda_mode=True)
        return None

    def test_imprints(self):
        """
        Tests that good input to publishers produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('imprints', m)
            self.pickle_tester('imprints', thoth_client.imprints)
        return None

    def test_imprints_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('imprints_bad', m)
            self.pickle_tester('imprints', thoth_client.imprints,
                               negative=True)

    def test_imprints_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('imprints', m)
            self.raw_tester(mock_response, thoth_client.imprints)
        return None

    def test_contributions(self):
        """
        Tests that good input to contributions produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('contributions', m)
            self.pickle_tester('contributions', thoth_client.contributions)
        return None

    def test_contributions_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('contributions_bad',
                                                            m)
            self.pickle_tester('contributions', thoth_client.contributions,
                               negative=True)

    def test_contributions_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('contributions', m)
            self.raw_tester(mock_response, thoth_client.contributions)
        return None

    def test_contributor(self):
        """
        Tests that good input to contributor produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('contributor', m)
            self.pickle_tester('contributor',
                               lambda:
                               thoth_client.contributor(
                                   contributor_id='e8def8cf-0dfe-4da9-b7fa-'
                                                  'f77e7aec7524'))
        return None

    def test_contributor_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('contributor_bad',
                                                            m)
            self.pickle_tester('contributor',
                               lambda: thoth_client.contributor(
                                   contributor_id='e8def8cf-0dfe-4da9-b7fa-'
                                                  'f77e7aec7524'),
                               negative=True)
        return None

    def test_contributor_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('contributor', m)
            self.raw_tester(mock_response,
                            lambda: thoth_client.contributor(
                                contributor_id='e8def8cf-0dfe-4da9-b7fa-'
                                               'f77e7aec7524',
                                raw=True),
                            lambda_mode=True)
        return None

    def test_contributors(self):
        """
        Tests that good input to contributors produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('contributors', m)
            self.pickle_tester('contributors', thoth_client.contributors)
        return None

    def test_contributors_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('contributors_bad',
                                                            m)
            self.pickle_tester('contributors', thoth_client.contributors,
                               negative=True)

    def test_contributors_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('contributors', m)
            self.raw_tester(mock_response, thoth_client.contributors)
        return None

    def raw_tester(self, mock_response, method_to_call, lambda_mode=False):
        """
        An echo test that ensures the client returns accurate raw responses
        @param lambda_mode: whether the passed function is a complete lambda
        @param mock_response: the mock response
        @param method_to_call: the method to call
        @return: None or an assertion
        """
        if not lambda_mode:
            response = method_to_call(raw=True)
        else:
            response = method_to_call()

        self.assertEqual(mock_response, response,
                         'Raw response was not echoed back correctly.')

    def pickle_tester(self, pickle_name, endpoint, negative=False):
        """
        A test of a function's output against a stored pickle (JSON)
        @param pickle_name: the .pickle file in the fixtures directory
        @param endpoint: the method to call
        @param negative: whether to assert equal (True) or unequal (False)
        @return: None or an assertion
        """
        with open("fixtures/{0}.pickle".format(pickle_name),
                  "rb") as pickle_file:
            loaded_response = json.load(pickle_file)
            response = json.loads(json.dumps(endpoint()))

            if not negative:
                self.assertEqual(loaded_response, response)
            else:
                self.assertNotEqual(loaded_response, response)

    def setup_mocker(self, endpoint, m):
        """
        Sets up a mocker object by reading a json fixture
        @param endpoint: the file to read in the fixtures dir (no extension)
        @param m: the requests Mocker object
        @return: the mock string, a Thoth client for this version
        """
        with open("fixtures/{0}.json".format(endpoint), "r") as input_file:
            mock_response = input_file.read()

        m.register_uri('POST', '{}/graphql'.format(self.endpoint),
                       text=mock_response)

        thoth_client = ThothClient(version=self.version,
                                   thoth_endpoint=self.endpoint)

        return mock_response, thoth_client


if __name__ == '__main__':
    unittest.main()
