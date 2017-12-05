import sys

import os
import web

reload(sys)
sys.setdefaultencoding('utf8')

currnt_path = os.path.dirname(os.path.abspath(__file__))
render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/crash_stack', 'crash_stack'
)

import time

DATE_FORMAT = "%Y/%m/%d %H:%M:%S"

class index:
    def GET(self):
        return render.index()

    def POST(self):

        client_request_log = "client_request.log"
        with open(client_request_log, "a") as f:
            f.write(time.strftime(DATE_FORMAT) + " recv create crash log request from: " + web.ctx.ip + "\n")

        input_data = web.input()

        so_build_date = input_data.build_date
        crash_log = input_data.crash_log

        crash_log_file = "crash.log"
        with open(crash_log_file, "w") as f:
            f.write(crash_log)

        symbol_path = ("/var/www/xtrunk/symbol/" + so_build_date + "/")
        session_so_path = (symbol_path + "libsessionvc.so")
        so_version = os.popen("strings %s | grep mmpc_version " % (session_so_path)).read()

        crash_stack = os.popen(
            "cat '%s' | ndk-stack -sym '%s' | head -n 30" % (crash_log_file, symbol_path)).read()
        if crash_stack == "":
            return "\nServer %s \n\nNo crash found!" % (so_version)

        if "com.yunos.tv.videochat" not in crash_stack and "com.yunos.videochat.phone" not in crash_stack:
            return "\nServer %s \n\nThe crash log is not from videochat!" % (so_version)

        # find bug hander

        bug_hanlder = self.getBugHandler(crash_stack)
        if bug_hanlder == "":
            return "\nServer %s \n\n%s \n\nbug hanlder not found, please contact xiaocheng" % (
            so_version, crash_stack)

        return "\nServer %s \n\n%s \n\nplease contact the bug handler: %s" % (
        so_version, crash_stack, bug_hanlder)

    # 	return render.crash_stack("\nServer %s \n\n %s" % (so_version, crash_stack))

    def getBugHandler(self, crash_stack):

        crash_stack_content = ""
        for line in crash_stack:
            if "videochat" not in line:
                crash_stack_content += line

        video_keyword = ["openh264", "video"]
        ado_keyword = ["ado"]
        audio_keyword = ["opensles", "audio", "decoder"]
        session_keyword = ["session", "jxcore"]
        transport_keyword = ["transport"]

        bug_hanlder = ""
        if any(keyword in crash_stack_content for keyword in video_keyword):
            bug_hanlder = "tiantu"
        if any(keyword in crash_stack_content for keyword in audio_keyword):
            bug_hanlder = "mafeng"
        if any(keyword in crash_stack_content for keyword in session_keyword):
            bug_hanlder = "xiaocheng"
        if any(keyword in crash_stack_content for keyword in ado_keyword):
            bug_hanlder = "xizhu"
        if any(keyword in crash_stack_content for keyword in transport_keyword):
            bug_hanlder = "mishao"

        return bug_hanlder

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
