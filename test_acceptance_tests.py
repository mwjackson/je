from unittest import TestCase

from just_eat import query_outcode, _get_request


class UnitTests(TestCase):
    def test_that_request_headers_are_set(self):
        resp = _get_request('A')

        self.assertEqual(resp.request.headers['accept-tenant'], 'uk')
        self.assertEqual(resp.request.headers['accept-language'], 'en-GB')
        self.assertEqual(resp.request.headers['authorization'], 'Basic VGVjaFRlc3RBUEk6dXNlcjI=')
        self.assertEqual(resp.request.headers['host'], 'public.je-apis.com')


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

        # assume 3-tuple is sufficient for name/cuisine/rating
        self.assertTrue(all([len(r) == 3 for r in restaurants]))