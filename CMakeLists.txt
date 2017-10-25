cmake_minimum_required(VERSION 3.6)
project(PPUtils)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    lajiao/love_of_father_and_mother.py
    lajiao/love_of_father_and_mother_other.py
    math/max_common_divisor.py
    net/build.log
    net/build_error.log
    net/httpclient_get.py
    net/mail_to.txt
    net/stmp_email_sender.py
    net/tcp_attack.py
    net/tcp_client.py
    net/tcp_port_scan.py
    test/newspapter_test.py
    test/test.py
    test/time_test.py
    webpy/create_mmpc_stack/static/css/style.css
    webpy/create_mmpc_stack/static/images/user.png
    webpy/create_mmpc_stack/templates/crash_stack.html
    webpy/create_mmpc_stack/templates/index.html
    webpy/create_mmpc_stack/mmpccs_main.py
    webpy/create_mmpc_stack/mmpccs_main_no_html.py
    1.txt
    2.txt
    3.txt
    4.txt
    PPUtils.iml
    README.md)

add_executable(PPUtils ${SOURCE_FILES})