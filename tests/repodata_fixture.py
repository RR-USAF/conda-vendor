import yaml


def repodata_output():
    return {
        "info": {"subdir": "linux-64"},
        "packages": {
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
            "_libgcc_mutex-0.1-main.conda": {
                "build": "main",
                "build_number": 0,
                "depends": [],
                "md5": "c3473ff8bdb3d124ed5ff11ec380d6f9",
                "name": "_libgcc_mutex",
                "sha256": "476626712f60e5ef0fe04c354727152b1ee5285d57ccd3575c7be930122bd051",
                "size": 3473,
                "subdir": "linux-64",
                "timestamp": 1562011674792,
                "version": "0.1",
            },
            "ca-certificates-2021.5.25-h06a4308_1.conda": {
                "build": "h06a4308_1",
                "build_number": 1,
                "depends": [],
                "license": "MPL 2.0",
                "md5": "3a2f8a1a5c82296693933f8c3f236fcb",
                "name": "ca-certificates",
                "sha256": "6f88ed7629479ae99fb8b75a64aaf46a12a445e981f2c9353a8f3128b944ee1a",
                "size": 114222,
                "subdir": "linux-64",
                "timestamp": 1621995548182,
                "version": "2021.5.25",
            },
            "ld_impl_linux-64-2.35.1-h7274673_9.conda": {
                "build": "h7274673_9",
                "build_number": 9,
                "constrains": ["binutils_impl_linux-64 2.35.1"],
                "depends": [],
                "license": "GPL-3.0-only",
                "md5": "dec20f7c8f9d5f1b293abd97b0f518ed",
                "name": "ld_impl_linux-64",
                "sha256": "cc5b453d585754bb9d52bac9e2045f32eb0fc43d74ec3eee21e44604cf1a6485",
                "size": 600155,
                "subdir": "linux-64",
                "timestamp": 1622698544714,
                "version": "2.35.1",
            },
            "libffi-3.3-he6710b0_2.conda": {
                "build": "he6710b0_2",
                "build_number": 2,
                "depends": ["libgcc-ng >=7.3.0", "libstdcxx-ng >=7.3.0"],
                "license": "Custom",
                "md5": "88a54b8f50e351c650e16f4ee781440c",
                "name": "libffi",
                "sha256": "2cef7c80db19e83a38b6e02110f0e9828d3ef4045c38791d5b01006c44529093",
                "size": 51543,
                "subdir": "linux-64",
                "timestamp": 1594054267890,
                "version": "3.3",
            },
            "libgcc-ng-9.3.0-h5101ec6_17.conda": {
                "build": "h5101ec6_17",
                "build_number": 17,
                "constrains": ["libgomp 9.3.0 h5101ec6_17"],
                "depends": ["_libgcc_mutex 0.1 main", "_openmp_mutex >=4.5"],
                "license": "GPL-3.0-only WITH GCC-exception-3.1",
                "md5": "e9cbabbfb9e8a430f6a7660fe8dd77a7",
                "name": "libgcc-ng",
                "sha256": "49a808720a51c107241a42ac3641cce3d8451ef7cfaf3d68b6e4a3fec2da0676",
                "size": 5035441,
                "subdir": "linux-64",
                "timestamp": 1622663350853,
                "version": "9.3.0",
            },
            "libgomp-9.3.0-h5101ec6_17.conda": {
                "build": "h5101ec6_17",
                "build_number": 17,
                "depends": ["_libgcc_mutex 0.1 main"],
                "license": "GPL-3.0-only WITH GCC-exception-3.1",
                "md5": "fb19b69bac6d819c7f3d1126b05461e1",
                "name": "libgomp",
                "sha256": "b53f7b4d5a1a3a3d61ad86b043f91a0ca9ee16b77194021383185d34eb592e56",
                "size": 318078,
                "subdir": "linux-64",
                "timestamp": 1622663306647,
                "version": "9.3.0",
            },
            "libstdcxx-ng-9.3.0-hd4cf53a_17.conda": {
                "build": "hd4cf53a_17",
                "build_number": 17,
                "depends": [],
                "license": "GPL-3.0-only WITH GCC-exception-3.1",
                "md5": "47744aca0f5e63c4672d117c3596d937",
                "name": "libstdcxx-ng",
                "sha256": "0cdad37s21336fe93f626289dd45e864eb4a0659ff2094670af01e7eacad28d9c",
                "size": 3248965,
                "subdir": "linux-64",
                "timestamp": 1622663335295,
                "version": "9.3.0",
            },
            "ncurses-6.2-he6710b0_1.conda": {
                "build": "he6710b0_1",
                "build_number": 1,
                "depends": ["libgcc-ng >=7.3.0", "libstdcxx-ng >=7.3.0"],
                "license": "Free software (MIT-like)",
                "md5": "b7ddf5ee3934b7f54620e8f6c0ee8a95",
                "name": "ncurses",
                "sha256": "b06808e9d147ff7d56f37d64eb55f09bfc1108ef0af22cb461e7ad20810bc236",
                "size": 836147,
                "subdir": "linux-64",
                "timestamp": 1588170439381,
                "version": "6.2",
            },
            "openssl-1.1.1k-h27cfd23_0.conda": {
                "build": "h27cfd23_0",
                "build_number": 0,
                "depends": ["ca-certificates", "libgcc-ng >=7.3.0"],
                "license": "OpenSSL",
                "license_family": "Apache",
                "md5": "9c1822b18564cdc68c493366da6f46f4",
                "name": "openssl",
                "sha256": "dd9ff7c11ee7690256772eeae1cfebb63d8643c8329ff489ec93f64863e7b421",
                "size": 2657446,
                "subdir": "linux-64",
                "timestamp": 1616684152302,
                "version": "1.1.1k",
            },
            "readline-8.1-h27cfd23_0.conda": {
                "build": "h27cfd23_0",
                "build_number": 0,
                "depends": ["libgcc-ng >=7.3.0", "ncurses >=6.2,<7.0a0"],
                "license": "GPL-3.0",
                "md5": "715789a38d447bc0cccc936209ac78c0",
                "name": "readline",
                "sha256": "5fe35471214d5fc544fa4c37808a6ffbd294d8f6d3ef5c484f2f72d7493e8d1d",
                "size": 371059,
                "subdir": "linux-64",
                "timestamp": 1611868595060,
                "version": "8.1",
            },
            "sqlite-3.35.4-hdfb4753_0.conda": {
                "build": "hdfb4753_0",
                "build_number": 0,
                "depends": [
                    "libgcc-ng >=7.3.0",
                    "readline >=8.0,<9.0a0",
                    "zlib >=1.2.11,<1.3.0a0",
                ],
                "license": "Public-Domain (http://www.sqlite.org/copyright.html)",
                "md5": "390226b113ecaf216cc7a18aa11d7297",
                "name": "sqlite",
                "sha256": "8bc771ab36bf15127491998ea0108267bd136eb378d59114d103713ed0eec4a8",
                "size": 1004674,
                "subdir": "linux-64",
                "timestamp": 1617396741975,
                "version": "3.35.4",
            },
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
            "tzdata-2020f-h52ac0ba_0.conda": {
                "build": "h52ac0ba_0",
                "build_number": 0,
                "depends": [],
                "license": "LicenseRef-Public-Domain",
                "md5": "e968a3b568f386342fceebca8c8e6af9",
                "name": "tzdata",
                "noarch": "generic",
                "sha256": "6635dd74510ab7c399d43781e866c977d7d715147e942f10a21aed4f00251f80",
                "size": 115710,
                "subdir": "noarch",
                "timestamp": 1611086516621,
                "version": "2020f",
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
            "zlib-1.2.11-h7b6447c_3.conda": {
                "build": "h7b6447c_3",
                "build_number": 3,
                "depends": ["libgcc-ng >=7.3.0"],
                "license": "zlib",
                "license_family": "Other",
                "md5": "50aa4407424985d56ec8ae2f94626aa9",
                "name": "zlib",
                "sha256": "5c5346ca7da14d7e11e15a8cc5e695d805ecb79c0e59d7043bea5843ffc493e5",
                "size": 104994,
                "subdir": "linux-64",
                "timestamp": 1542814864621,
                "version": "1.2.11",
            },
        },
        "removed": [],
        "repodata_version": 1,
    }


def vendor_manifest_dict():
    return {
        "resources": [
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/_libgcc_mutex-0.1-main.conda",
                "name": "_libgcc_mutex-0.1-main.conda",
                "validation": {
                    "type": "sha256",
                    "value": "476626712f60e5ef0fe04c354727152b1ee5285d57ccd3575c7be930122bd051",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/ca-certificates-2021.5.25-h06a4308_1.conda",
                "name": "ca-certificates-2021.5.25-h06a4308_1.conda",
                "validation": {
                    "type": "sha256",
                    "value": "6f88ed7629479ae99fb8b75a64aaf46a12a445e981f2c9353a8f3128b944ee1a",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/ld_impl_linux-64-2.35.1-h7274673_9.conda",
                "name": "ld_impl_linux-64-2.35.1-h7274673_9.conda",
                "validation": {
                    "type": "sha256",
                    "value": "cc5b453d585754bb9d52bac9e2045f32eb0fc43d74ec3eee21e44604cf1a6485",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/libstdcxx-ng-9.3.0-hd4cf53a_17.conda",
                "name": "libstdcxx-ng-9.3.0-hd4cf53a_17.conda",
                "validation": {
                    "type": "sha256",
                    "value": "0cdad3721336fe93f626289dd45e864eb4a0659ff2094670af01e7eacad28d9c",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/noarch/tzdata-2020f-h52ac0ba_0.conda",
                "name": "tzdata-2020f-h52ac0ba_0.conda",
                "validation": {
                    "type": "sha256",
                    "value": "6635dd74510ab7c399d43781e866c977d7d715147e942f10a21aed4f00251f80",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/libgomp-9.3.0-h5101ec6_17.conda",
                "name": "libgomp-9.3.0-h5101ec6_17.conda",
                "validation": {
                    "type": "sha256",
                    "value": "b53f7b4d5a1a3a3d61ad86b043f91a0ca9ee16b77194021383185d34eb592e56",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/_openmp_mutex-4.5-1_gnu.tar.bz2",
                "name": "_openmp_mutex-4.5-1_gnu.tar.bz2",
                "validation": {
                    "type": "sha256",
                    "value": "2c269ff2e33d3c158b4744485b7fe11ee132814c55a70b33b3e68d588375d465",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/libgcc-ng-9.3.0-h5101ec6_17.conda",
                "name": "libgcc-ng-9.3.0-h5101ec6_17.conda",
                "validation": {
                    "type": "sha256",
                    "value": "49a808720a51c107241a42ac3641cce3d8451ef7cfaf3d68b6e4a3fec2da0676",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/libffi-3.3-he6710b0_2.conda",
                "name": "libffi-3.3-he6710b0_2.conda",
                "validation": {
                    "type": "sha256",
                    "value": "2cef7c80db19e83a38b6e02110f0e9828d3ef4045c38791d5b01006c44529093",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/ncurses-6.2-he6710b0_1.conda",
                "name": "ncurses-6.2-he6710b0_1.conda",
                "validation": {
                    "type": "sha256",
                    "value": "b06808e9d147ff7d56f37d64eb55f09bfc1108ef0af22cb461e7ad20810bc236",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/openssl-1.1.1k-h27cfd23_0.conda",
                "name": "openssl-1.1.1k-h27cfd23_0.conda",
                "validation": {
                    "type": "sha256",
                    "value": "dd9ff7c11ee7690256772eeae1cfebb63d8643c8329ff489ec93f64863e7b421",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/xz-5.2.5-h7b6447c_0.conda",
                "name": "xz-5.2.5-h7b6447c_0.conda",
                "validation": {
                    "type": "sha256",
                    "value": "58045af0e1f23ea72b6759c4f5aac3e2fb98da9585758853d09961126d66f9ce",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/zlib-1.2.11-h7b6447c_3.conda",
                "name": "zlib-1.2.11-h7b6447c_3.conda",
                "validation": {
                    "type": "sha256",
                    "value": "5c5346ca7da14d7e11e15a8cc5e695d805ecb79c0e59d7043bea5843ffc493e5",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/readline-8.1-h27cfd23_0.conda",
                "name": "readline-8.1-h27cfd23_0.conda",
                "validation": {
                    "type": "sha256",
                    "value": "5fe35471214d5fc544fa4c37808a6ffbd294d8f6d3ef5c484f2f72d7493e8d1d",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/tk-8.6.10-hbc83047_0.conda",
                "name": "tk-8.6.10-hbc83047_0.conda",
                "validation": {
                    "type": "sha256",
                    "value": "99fba40357115be361759731fc5a19b7833b4884310f2851f3faadbf33484991",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/sqlite-3.35.4-hdfb4753_0.conda",
                "name": "sqlite-3.35.4-hdfb4753_0.conda",
                "validation": {
                    "type": "sha256",
                    "value": "8bc771ab36bf15127491998ea0108267bd136eb378d59114d103713ed0eec4a8",
                },
            },
            {
                "url": "https://repo.anaconda.com/pkgs/main/linux-64/python-3.9.5-h12debd9_4.tar.bz2",
                "name": "python-3.9.5-h12debd9_4.tar.bz2",
                "validation": {
                    "type": "sha256",
                    "value": "7fc98fe684cb716a8d19cf20a77ccce3cda3f6da968abaade63edbe006d8f3ba",
                },
            },
        ]
    }


def vendor_manifest():
    return yaml.dump(vendor_manifest_dict())


def conda_solve_output():
    return {
        "actions": {
            "FETCH": [],
            "LINK": [
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 0,
                    "build_string": "main",
                    "channel": "pkgs/main",
                    "dist_name": "_libgcc_mutex-0.1-main",
                    "name": "_libgcc_mutex",
                    "platform": "linux-64",
                    "version": "0.1",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 1,
                    "build_string": "h06a4308_1",
                    "channel": "pkgs/main",
                    "dist_name": "ca-certificates-2021.5.25-h06a4308_1",
                    "name": "ca-certificates",
                    "platform": "linux-64",
                    "version": "2021.5.25",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 9,
                    "build_string": "h7274673_9",
                    "channel": "pkgs/main",
                    "dist_name": "ld_impl_linux-64-2.35.1-h7274673_9",
                    "name": "ld_impl_linux-64",
                    "platform": "linux-64",
                    "version": "2.35.1",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 17,
                    "build_string": "hd4cf53a_17",
                    "channel": "pkgs/main",
                    "dist_name": "libstdcxx-ng-9.3.0-hd4cf53a_17",
                    "name": "libstdcxx-ng",
                    "platform": "linux-64",
                    "version": "9.3.0",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 0,
                    "build_string": "h52ac0ba_0",
                    "channel": "pkgs/main",
                    "dist_name": "tzdata-2020f-h52ac0ba_0",
                    "name": "tzdata",
                    "platform": "noarch",
                    "version": "2020f",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 17,
                    "build_string": "h5101ec6_17",
                    "channel": "pkgs/main",
                    "dist_name": "libgomp-9.3.0-h5101ec6_17",
                    "name": "libgomp",
                    "platform": "linux-64",
                    "version": "9.3.0",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 17,
                    "build_string": "1_gnu",
                    "channel": "pkgs/main",
                    "dist_name": "_openmp_mutex-4.5-1_gnu",
                    "name": "_openmp_mutex",
                    "platform": "linux-64",
                    "version": "4.5",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 17,
                    "build_string": "h5101ec6_17",
                    "channel": "pkgs/main",
                    "dist_name": "libgcc-ng-9.3.0-h5101ec6_17",
                    "name": "libgcc-ng",
                    "platform": "linux-64",
                    "version": "9.3.0",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 2,
                    "build_string": "he6710b0_2",
                    "channel": "pkgs/main",
                    "dist_name": "libffi-3.3-he6710b0_2",
                    "name": "libffi",
                    "platform": "linux-64",
                    "version": "3.3",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 1,
                    "build_string": "he6710b0_1",
                    "channel": "pkgs/main",
                    "dist_name": "ncurses-6.2-he6710b0_1",
                    "name": "ncurses",
                    "platform": "linux-64",
                    "version": "6.2",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 0,
                    "build_string": "h27cfd23_0",
                    "channel": "pkgs/main",
                    "dist_name": "openssl-1.1.1k-h27cfd23_0",
                    "name": "openssl",
                    "platform": "linux-64",
                    "version": "1.1.1k",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 0,
                    "build_string": "h7b6447c_0",
                    "channel": "pkgs/main",
                    "dist_name": "xz-5.2.5-h7b6447c_0",
                    "name": "xz",
                    "platform": "linux-64",
                    "version": "5.2.5",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 3,
                    "build_string": "h7b6447c_3",
                    "channel": "pkgs/main",
                    "dist_name": "zlib-1.2.11-h7b6447c_3",
                    "name": "zlib",
                    "platform": "linux-64",
                    "version": "1.2.11",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 0,
                    "build_string": "h27cfd23_0",
                    "channel": "pkgs/main",
                    "dist_name": "readline-8.1-h27cfd23_0",
                    "name": "readline",
                    "platform": "linux-64",
                    "version": "8.1",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 0,
                    "build_string": "hbc83047_0",
                    "channel": "pkgs/main",
                    "dist_name": "tk-8.6.10-hbc83047_0",
                    "name": "tk",
                    "platform": "linux-64",
                    "version": "8.6.10",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 0,
                    "build_string": "hdfb4753_0",
                    "channel": "pkgs/main",
                    "dist_name": "sqlite-3.35.4-hdfb4753_0",
                    "name": "sqlite",
                    "platform": "linux-64",
                    "version": "3.35.4",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 4,
                    "build_string": "h12debd9_4",
                    "channel": "pkgs/main",
                    "dist_name": "python-3.9.5-h12debd9_4",
                    "name": "python",
                    "platform": "linux-64",
                    "version": "3.9.5",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 0,
                    "build_string": "py39h06a4308_0",
                    "channel": "pkgs/main",
                    "dist_name": "certifi-2021.5.30-py39h06a4308_0",
                    "name": "certifi",
                    "platform": "linux-64",
                    "version": "2021.5.30",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 0,
                    "build_string": "pyhd3eb1b0_0",
                    "channel": "pkgs/main",
                    "dist_name": "wheel-0.36.2-pyhd3eb1b0_0",
                    "name": "wheel",
                    "platform": "noarch",
                    "version": "0.36.2",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 0,
                    "build_string": "py39h06a4308_0",
                    "channel": "pkgs/main",
                    "dist_name": "setuptools-52.0.0-py39h06a4308_0",
                    "name": "setuptools",
                    "platform": "linux-64",
                    "version": "52.0.0",
                },
                {
                    "base_url": "https://repo.anaconda.com/pkgs/main",
                    "build_number": 0,
                    "build_string": "py39h06a4308_0",
                    "channel": "pkgs/main",
                    "dist_name": "pip-21.1.2-py39h06a4308_0",
                    "name": "pip",
                    "platform": "linux-64",
                    "version": "21.1.2",
                },
            ],
            "PREFIX": "/home/hussainsultan/miniconda3/envs/testtt",
        },
        "dry_run": true,
        "prefix": "/home/hussainsultan/miniconda3/envs/testtt",
        "success": true,
    }


def python_395_pkg_list():
    return [
        "_libgcc_mutex-0.1-main",
        "ca-certificates-2021.5.25-h06a4308_1",
        "ld_impl_linux-64-2.35.1-h7274673_9",
        "libstdcxx-ng-9.3.0-hd4cf53a_17",
        "libgomp-9.3.0-h5101ec6_17",
        "_openmp_mutex-4.5-1_gnu",
        "libgcc-ng-9.3.0-h5101ec6_17",
        "libffi-3.3-he6710b0_2",
        "ncurses-6.2-he6710b0_1",
        "openssl-1.1.1k-h27cfd23_0",
        "xz-5.2.5-h7b6447c_0",
        "zlib-1.2.11-h7b6447c_3",
        "readline-8.1-h27cfd23_0",
        "tk-8.6.10-hbc83047_0",
        "sqlite-3.35.4-hdfb4753_0",
        "python-3.9.5-h12debd9_4",
    ]


def dot_conda_and_tar_list():
    return [
        "_libgcc_mutex-0.1-main.conda",
        "ca-certificates-2021.5.25-h06a4308_1.conda",
        "ld_impl_linux-64-2.35.1-h7274673_9.conda",
        "libffi-3.3-he6710b0_2.conda",
        "libgcc-ng-9.3.0-h5101ec6_17.conda",
        "libgomp-9.3.0-h5101ec6_17.conda",
        "libstdcxx-ng-9.3.0-hd4cf53a_17.conda",
        "ncurses-6.2-he6710b0_1.conda",
        "openssl-1.1.1k-h27cfd23_0.conda",
        "readline-8.1-h27cfd23_0.conda",
        "sqlite-3.35.4-hdfb4753_0.conda",
        "tk-8.6.10-hbc83047_0.conda",
        "xz-5.2.5-h7b6447c_0.conda",
        "zlib-1.2.11-h7b6447c_3.conda",
        "_openmp_mutex-4.5-1_gnu.tar.bz2",
        "python-3.9.5-h12debd9_4.tar.bz2",
    ]
