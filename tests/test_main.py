import pytest
import requests

from courses import sort_by_duration, get_min_max_course, get_unique_mentors
from ya_api import create_folder
from tests.test_data import mentors_list_test, wrong_mentors_list, courses_list, duration_list
from tests.test_data import wrong_duration_list, wrong_courses_list
from tests.test_data import wrong_token, wrong_folder_name

class TestSortByDuration:

    def test_equal_len(self):
        assert len(courses_list) == len(duration_list)

    def test_output_type(self):
        assert type(sort_by_duration(courses_list, duration_list)) == list

    def test_correct_output(self):
        assert sort_by_duration(courses_list, duration_list) == \
               ['course3 - 12 месяцев', 'course1 - 14 месяцев', 'course2 - 20 месяцев']

    @pytest.mark.xfail
    def test_wrong_list(self):
        assert sort_by_duration(wrong_courses_list, duration_list)

class TestMinMaxCourse:

    def test_correct_output(self):
        assert get_min_max_course(courses_list, duration_list) == \
               "Самый короткий курс(ы): course3 - 12 месяца(ев) " \
               "\nСамый длинный курс(ы): course2 - 20 месяца(ев)"

    def test_output_type(self):
        assert type(get_min_max_course(courses_list, duration_list)) == str

    def test_equal_len(self):
        assert len(courses_list) == len(duration_list)

    def test_int_type_duration_list(self):
        assert sum(duration_list)

    @pytest.mark.xfail
    def test_wrong_list(self):
        assert get_min_max_course(courses_list, wrong_duration_list)


class TestUniqueNames:

    def test_correct_output(self):
        assert get_unique_mentors(mentors_list_test) == \
               "Уникальные имена преподавателей: Владимир, Евгений, Филипп"

    def test_list_len(self):
        assert len(get_unique_mentors(mentors_list_test)) > 0

    def test_output_type(self):
        assert type(get_unique_mentors(mentors_list_test)) == str

    @pytest.mark.xfail
    def test_wrong_list(self):
        assert get_unique_mentors(wrong_mentors_list)

class TestCreateFolder:

    def test_correct_request(self):
        assert create_folder(ya_url, ya_token, ya_params) == 201

    def test_folder_created(self):
        headers = {'Authorization': f'OAuth {ya_token}'}
        params = {'path': f'/'}
        response = requests.get(ya_url, headers=headers, params=params).json()
        flag = False
        for item in response.get('_embedded').get('items'):
            if item.get('name') == folder_name:
                flag = True
        assert flag is True

    def test_folder_created_1(self):
        headers = {'Authorization': f'OAuth {ya_token}'}
        params = {'path': f'/{folder_name}'}
        assert requests.get(ya_url, headers=headers, params=params).status_code == 200

    @pytest.mark.xfail
    def test_wrong_token(self):
        assert create_folder(ya_url, wrong_token, ya_params) == 201

    @pytest.mark.xfail
    def test_wrong_folder_name(self):
        headers = {'Authorization': f'OAuth {ya_token}'}
        params = {'path': f'/{wrong_folder_name}'}
        assert requests.get(ya_url, headers=headers, params=params).status_code == 200