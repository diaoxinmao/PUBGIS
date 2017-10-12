from os.path import join, dirname

from pubgis.json_output.json_output import output_json

JSON_TEST_DIR = join(dirname(__file__), "json")


def test_json_write():
    actual_file = join(JSON_TEST_DIR, 'actual', 'actual_out.json')
    expected_file = join(JSON_TEST_DIR, 'expected', 'expected_out.json')

    coords = ((3079, 4034), (3095, 4061), (3108, 4082), (3123, 4108), (3140, 4138), (3160, 4170),
              (3178, 4201), (3194, 4228), (3208, 4251), (3228, 4285), (3247, 4318), (3265, 4348),
              (3281, 4374), (3298, 4402), (3314, 4429), (3330, 4459), (3350, 4491), (3371, 4525),
              (3387, 4551), (3400, 4574), (3413, 4598))

    output_json(actual_file, "username", coords)

    expected_read = open(expected_file, 'r').read()
    actual_read = open(actual_file, 'r').read()

    assert actual_read == expected_read