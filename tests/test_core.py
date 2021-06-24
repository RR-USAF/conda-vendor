import subprocess
from unittest.mock import Mock

import pytest
import requests
from requests import Response

from conda_vendor.core import (
    conda_vendor_artifacts_from_specs,
    fetch_repodata,
    parse_environment,
    CondaChannel,
)
from tests.repodata_fixture import (
    vendor_manifest_dict,
    dot_conda_and_tar_list,
    python_395_pkg_list,
)


def expected_repodata_response():
    return {
        "info": {"subdir": "linux-64"},
        "packages": {
            "python-3.9.5-h12debd9_4.tar.bz2": {
                "build": "h12debd9_4",
                "build_number": 4,
                "depends": [
                    "ld_impl_linux-64",
                    "libffi >=3.3,<3.4.0a0",
                    "libgcc-ng >=7.5.0",
                    "libstdcxx-ng >=7.5.0",
                    "ncurses >=6.2,<7.0a0",
                    "openssl >=1.1.1k,<1.1.2a",
                    "readline >=8.0,<9.0a0",
                    "sqlite >=3.35.4,<4.0a0",
                    "tk >=8.6.10,<8.7.0a0",
                    "tzdata",
                    "xz >=5.2.5,<6.0a0",
                    "zlib >=1.2.11,<1.3.0a0",
                ],
                "license": "Python-2.0",
                "md5": "eb1bc6ccb2cbb43adb5a09e5802efef8",
                "name": "python",
                "sha256": "7fc98fe684cb716a8d19cf20a77ccce3cda3f6da968abaade63edbe006d8f3ba",
                "size": 23740654,
                "subdir": "linux-64",
                "timestamp": 1622828217909,
                "version": "3.9.5",
            },
            "_openmp_mutex-4.5-1_gnu.tar.bz2": {
                "build": "1_gnu",
                "build_number": 17,
                "constrains": ["openmp_impl 9999"],
                "depends": ["_libgcc_mutex 0.1 main", "libgomp >=7.5.0"],
                "license": "BSD-3-Clause",
                "md5": "84414b0edb0a36bd7e25fc4936c1abb5",
                "name": "_openmp_mutex",
                "sha256": "2c269ff2e33d3c158b4744485b7fe11ee132814c55a70b33b3e68d588375d465",
                "size": 22165,
                "subdir": "linux-64",
                "timestamp": 1612961522265,
                "version": "4.5",
            },
        },
        "packages.conda": {
            "tk-8.6.10-hbc83047_0.conda": {
                "build": "hbc83047_0",
                "build_number": 0,
                "depends": ["libgcc-ng >=7.3.0", "zlib >=1.2.11,<1.3.0a0"],
                "license": "Tcl/Tk",
                "license_family": "BSD",
                "md5": "9ba14aaba4818a66c820f85f5bf34ca0",
                "name": "tk",
                "sha256": "99fba40357115be361759731fc5a19b7833b4884310f2851f3faadbf33484991",
                "size": 3108365,
                "subdir": "linux-64",
                "timestamp": 1592503345885,
                "version": "8.6.10",
            },
            "xz-5.2.5-h7b6447c_0.conda": {
                "build": "h7b6447c_0",
                "build_number": 0,
                "depends": ["libgcc-ng >=7.3.0"],
                "license": "LGPL-2.1 and GPL-2.0",
                "md5": "73a16ea8ba890175a1ce94a3a87c8f68",
                "name": "xz",
                "sha256": "58045af0e1f23ea72b6759c4f5aac3e2fb98da9585758853d09961126d66f9ce",
                "size": 349481,
                "subdir": "linux-64",
                "timestamp": 1587011767250,
                "version": "5.2.5",
            },
        },
    }


@pytest.fixture
def mock_requests_repodata():
    requests_mock = Mock(spec=requests)
    actual_result_mock = Mock(Response)
    requests_mock.get.return_value = actual_result_mock
    actual_result_mock.json.return_value = expected_repodata_response()
    return requests_mock


def test_fetch_repodata_for_a_list_of_packages(mock_requests_repodata):
    input_packages = ["python-3.9.5-h12debd9_4.tar.bz2", "tk-8.6.10-hbc83047_0.conda"]
    result = fetch_repodata(input_packages, requests=mock_requests_repodata)
    assert result == {
        "info": {"subdir": "linux-64"},
        "packages": {
            "python-3.9.5-h12debd9_4.tar.bz2": {
                "build": "h12debd9_4",
                "build_number": 4,
                "depends": [
                    "ld_impl_linux-64",
                    "libffi >=3.3,<3.4.0a0",
                    "libgcc-ng >=7.5.0",
                    "libstdcxx-ng >=7.5.0",
                    "ncurses >=6.2,<7.0a0",
                    "openssl >=1.1.1k,<1.1.2a",
                    "readline >=8.0,<9.0a0",
                    "sqlite >=3.35.4,<4.0a0",
                    "tk >=8.6.10,<8.7.0a0",
                    "tzdata",
                    "xz >=5.2.5,<6.0a0",
                    "zlib >=1.2.11,<1.3.0a0",
                ],
                "license": "Python-2.0",
                "md5": "eb1bc6ccb2cbb43adb5a09e5802efef8",
                "name": "python",
                "sha256": "7fc98fe684cb716a8d19cf20a77ccce3cda3f6da968abaade63edbe006d8f3ba",
                "size": 23740654,
                "subdir": "linux-64",
                "timestamp": 1622828217909,
                "version": "3.9.5",
            },
        },
        "packages.conda": {
            "tk-8.6.10-hbc83047_0.conda": {
                "build": "hbc83047_0",
                "build_number": 0,
                "depends": ["libgcc-ng >=7.3.0", "zlib >=1.2.11,<1.3.0a0"],
                "license": "Tcl/Tk",
                "license_family": "BSD",
                "md5": "9ba14aaba4818a66c820f85f5bf34ca0",
                "name": "tk",
                "sha256": "99fba40357115be361759731fc5a19b7833b4884310f2851f3faadbf33484991",
                "size": 3108365,
                "subdir": "linux-64",
                "timestamp": 1592503345885,
                "version": "8.6.10",
            },
        },
    }


@pytest.fixture()
def minimal_environment(tmpdir_factory):
    content = """name: minimal_env
channels:
- defaults
dependencies:
- python=3.9.5"""
    fn = tmpdir_factory.mktemp("minimal_env").join("env.yml")
    fn.write(content)
    return fn


def test_parse_environment_file(minimal_environment):
    expected_output = ["python=3.9.5"]
    actual_output = parse_environment(minimal_environment)
    assert actual_output == expected_output


def test_create_dot_conda_and_tar_pkg_list():
    conda_channel = CondaChannel()
    conda_channel.fetch()
    actual_result = conda_channel.create_dot_conda_and_tar_pkg_list(
        python_395_pkg_list()
    )

    expected_result = dot_conda_and_tar_list()

    assert set(actual_result) == set(expected_result)


def test_format_manifest():
    conda_channel = CondaChannel()
    conda_channel.fetch()

    actual_result = conda_channel.format_manifest(
        ["python-3.9.5-h12debd9_4.tar.bz2"],
        base_url="https://repo.anaconda.com/pkgs/main",
        platform="linux-64",
    )

    expected_result = [
        {
            "url": "https://repo.anaconda.com/pkgs/main/linux-64/python-3.9.5-h12debd9_4.tar.bz2",
            "name": "python-3.9.5-h12debd9_4.tar.bz2",
            "validation": {
                "type": "sha256",
                "value": "7fc98fe684cb716a8d19cf20a77ccce3cda3f6da968abaade63edbe006d8f3ba",
            },
        }
    ]

    assert actual_result == expected_result


def test_conda_vendor_artifacts_from_specs():
    specs = ["python=3.9.5"]
    actual_result = vendor_artifacts_from_specs(specs)
    expected_result = vendor_manifest_dict()
    assert len(actual_result["resources"]) == len(expected_result["resources"])


#  assert actual_result["resources"][0] == expected_result["resources"][6]
