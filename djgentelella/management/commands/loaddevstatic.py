from django.core.management import BaseCommand
from django.contrib.staticfiles import finders
import os

class Command(BaseCommand):
    help = "Load static files for development command"

    def get_static_file(self, requests, url, basepath):
        name = url.split('/')[-1]
        if not os.path.exists(basepath+name):
            print("Downloading %s --> %s"%(url, basepath+name))
            r = requests.get(url)
            with open(basepath+name, 'wb') as arch:
                arch.write(r.content)

    def handle(self, *args, **options):
        try:
            import requests
        except:
            print("Requests is required try pip install requests")
            exit(1)

        result = finders.find('gentelella/css/custom.css')
        if result is None:
            print('No static folder found')
            exit(1)

        basepath = result.replace('gentelella/css/custom.css', 'vendors/')

        libs = {
            'bootstrap': [
                'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
                'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css.map',
                'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js',

            ],
            'fonts': [
                'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/fonts/glyphicons-halflings-regular.eot',
                'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/fonts/glyphicons-halflings-regular.ttf',
                'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/fonts/glyphicons-halflings-regular.woff2',
                'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/fonts/glyphicons-halflings-regular.svg',
                'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/fonts/glyphicons-halflings-regular.woff',
                'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/fonts/glyphicons-halflings-regular.svg',
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/fonts/fontawesome-webfont.svg',
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/fonts/FontAwesome.otf',
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/fonts/fontawesome-webfont.eot',
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/fonts/fontawesome-webfont.ttf',
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/fonts/fontawesome-webfont.woff',
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/fonts/fontawesome-webfont.woff2',
            ],
            'font-awesome': [
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/css/font-awesome.min.css',
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/css/font-awesome.css.map'
            ],
            'bootstrap-daterangepicker':[
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-daterangepicker/2.1.24/daterangepicker.min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-daterangepicker/2.1.24/daterangepicker.min.js.map',
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-daterangepicker/2.1.24/daterangepicker.min.css',
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-daterangepicker/2.1.24/daterangepicker.min.css.map',
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-daterangepicker/2.1.24/moment.min.js'
            ],
            'bootstrap-datetimepicker': [
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/css/bootstrap-datetimepicker-standalone.min.css.map',
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/css/bootstrap-datetimepicker-standalone.min.css'
            ],
            'select2':[
                'https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css'
            ],
            'switchery':[
                'https://cdnjs.cloudflare.com/ajax/libs/switchery/0.8.2/switchery.min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/switchery/0.8.2/switchery.min.css',
            ],
            'iCheck': [
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/icheck.min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/green.css',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/blue.css',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/aero.css',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/yellow.css',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/orange.css',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/green.png',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/blue.png',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/aero.png',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/yellow.png',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/orange.png',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/green@2x.png',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/blue@2x.png',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/aero@2x.png',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/yellow@2x.png',
                'https://cdnjs.cloudflare.com/ajax/libs/iCheck/1.0.2/skins/flat/orange@2x.png',
            ],
            'bootstrap-progressbar': [
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-progressbar/0.9.0/bootstrap-progressbar.min.js',
                'https://cdn.jsdelivr.net/npm/bootstrap-progressbar@0.9.0/css/bootstrap-progressbar-3.3.4.min.css',
            ],
            'nprogress': [
                'https://cdnjs.cloudflare.com/ajax/libs/nprogress/0.2.0/nprogress.min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/nprogress/0.2.0/nprogress.min.css',
            ],
            'jquery': [
                'https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.3/jquery.min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.3/jquery.min.map'
            ],
            'jquery-knob': [
                'https://cdnjs.cloudflare.com/ajax/libs/jQuery-Knob/1.2.13/jquery.knob.min.js',
            ],
            'inputmask': [
                'https://cdnjs.cloudflare.com/ajax/libs/inputmask/3.3.11/inputmask/inputmask.min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/inputmask/3.3.11/inputmask/jquery.inputmask.min.js',
            ],
            'moment':[
                'https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.13.0/moment-with-locales.min.js'
            ],
            'bootstrap-wysiwyg':[
                'https://raw.githubusercontent.com/steveathon/bootstrap-wysiwyg/1.0.4/js/bootstrap-wysiwyg.min.js',
            ],
            'parsleyjs': [
                'https://cdnjs.cloudflare.com/ajax/libs/parsley.js/2.3.13/parsley.min.js'
            ],
            'autosize': [
                'https://cdnjs.cloudflare.com/ajax/libs/autosize.js/3.0.15/autosize.min.js'
            ],
            'bootstrap-maxlength':[
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-maxlength/1.7.0/bootstrap-maxlength.min.js'
            ],
            'tail.select':[
                'https://cdn.jsdelivr.net/npm/tail.select@0.5.15/css/bootstrap3/tail.select-default.min.css',
                'https://cdn.jsdelivr.net/npm/tail.select@0.5.15/css/bootstrap3/tail.select-default.min.map',
                'https://cdn.jsdelivr.net/npm/tail.select@0.5.15/js/tail.select-full.min.js',
            ]
        }

        for lib in libs:
            currentbasepath = basepath+lib+'/'
            if not os.path.exists(currentbasepath):
                os.mkdir(currentbasepath)
            for staticfile in libs[lib]:
                self.get_static_file(requests, staticfile, currentbasepath)