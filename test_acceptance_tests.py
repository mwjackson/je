from unittest import TestCase


class AcceptanceTests(TestCase):

    def test_acceptance_test(self):
        # as a user running the application
        self._as_a_user_running_the_application()
        # i can view a list of restaurants in a user submitted outcode
        self._i_can_view_a_list_of_restaurants_in_a_user_submitted_outcode()
        # so that I can know which restuarants are currently available
        self._so_that_i_can_know_which_restaurants_are_currently_available()

        self.fail('todo')

    def _as_a_user_running_the_application(self):
        pass

    def _i_can_view_a_list_of_restaurants_in_a_user_submitted_outcode(self):
        pass

    def _so_that_i_can_know_which_restaurants_are_currently_available(self):
        pass