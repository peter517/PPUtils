import sys

import os
import web

reload(sys)
sys.setdefaultencoding('utf8')

render = web.template.render('templates/')

urls = (
    '/', 'index'
)

class index:
    def __init__(self):
        self.registerForm = web.form.Form(
                web.form.Textarea('crash_log', web.form.notnull, rows=30, cols=150,
                                  description='submit crash log to left area'),
                web.form.Textbox('so_build_date', description='mmpc so build date'),
                web.form.Button('create stack'),
                # validators = [web.form.Validator("submit crash log too long", lambda i: len(i.crash_log) < 10000 )]
        )

    def GET(self):
        form = self.registerForm()
        return render.form(content=form)

    def POST(self):
        form = self.registerForm()
        if (not form.validates()):
            return render.form(form)
        else:
            crash_log = form.d.crash_log

            crash_log_file = "crash.log"
            f = open(crash_log_file, "w")
            f.write(crash_log)

            so_build_date = form.d.so_build_date
            symbol_path = ("/var/www/xtrunk/symbol/" + so_build_date + "/")
            crash_stack = os.popen(
                "cat '%s' | ndk-stack -sym %s | head -n 30" % (crash_log_file, symbol_path)).read()

            session_so_path = (symbol_path + "libsessionvc.so")
            so_version = os.popen("strings %s | grep mmpc_version " % (session_so_path)).read()

            return "\nServer %s \n\n %s" % (so_version, crash_stack)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
