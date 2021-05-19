# conf.py to run tests

master_doc = 'index'
extensions = [
    'notfound.extension',
]

templates_path = ['_templates']


def setup(app):
    app.add_css_file('css_added_by_extension.css')
    app.add_js_file('js_added_by_extension.js')
