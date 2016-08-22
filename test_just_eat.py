from unittest import TestCase

from just_eat import query_outcode, _get_request, _map_response, _format_data


class UnitTests(TestCase):
    def test_that_request_headers_are_set(self):
        resp = _get_request('A')

        self.assertEqual(resp.request.headers['accept-tenant'], 'uk')
        self.assertEqual(resp.request.headers['accept-language'], 'en-GB')
        self.assertEqual(resp.request.headers['authorization'], 'Basic VGVjaFRlc3RBUEk6dXNlcjI=')
        self.assertEqual(resp.request.headers['host'], 'public.je-apis.com')

    def test_that_response_data_mapped_correctly(self):
        data = _map_response("""
        {
        "Metadata": "Blah",
        "Restaurants": [{
            "Address": "107 Church Road",
            "City": "London",
            "CuisineTypes": [{
                "Id": 31,
                "Name": "Indian",
                "SeoName": "indian"},
                {"Id": 85,
                "Name": "Curry",
                "SeoName": "curry"}],
        "Name": "Yak & Yeti",
        "RatingAverage": 5.04}]
        }
        """)

        self.assertDictEqual(data[0],
            {'Name': u'Yak & Yeti', 'CuisineTypes': [u'Indian', u'Curry'], 'RatingAverage': 5.04}
        )

    def test_that_output_is_formatted_tabularly(self):
        data = [
            {'Name': u'Yak & Yeti', 'CuisineTypes': [u'Indian', u'Curry'], 'RatingAverage': 5.04},
            {'Name': u'Blah', 'CuisineTypes': [u'Thai'], 'RatingAverage': 5.04}
        ]

        self.assertEqual(_format_data(data), """
Name                                              Rating              Cuisines
Yak & Yeti                                        5.04                Indian, Curry
Blah                                              5.04                Thai""")

    def test_that_output_is_sorted_by_rating(self):
        data = _map_response("""
        {
        "Restaurants": [
            {"Name": "Yak & Yeti",
            "RatingAverage": 5.04},
            {"Name": "Thai",
            "RatingAverage": 5.5},
            {"Name": "Best",
            "RatingAverage": 5.99}]
        }
        """)

        self.assertListEqual([r['Name'] for r in data], ['Best', 'Thai', 'Yak & Yeti'])


class AcceptanceTests(TestCase):

    def test_acceptance_test(self):

        self._as_a_user_running_the_application()

        restaurants = self._i_can_view_a_list_of_restaurants_in_a_user_submitted_outcode()

        self._so_that_i_can_know_which_restaurants_are_currently_available(restaurants)

    def _as_a_user_running_the_application(self):
        # import already happened
        pass

    def _i_can_view_a_list_of_restaurants_in_a_user_submitted_outcode(self):
        return query_outcode('SE19')

    def _so_that_i_can_know_which_restaurants_are_currently_available(self, restaurants):
        self.assertTrue(restaurants)

        def has_data(d):
            return all(k in d for k in ['Name', 'CuisineTypes', 'RatingAverage'])

        # test the structure of the data, rather than std out for the purposes of this exercise
        self.assertTrue(all([has_data(r) for r in restaurants]))