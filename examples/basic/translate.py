from jinja2 import Environment

env = Environment(extensions=["jinja2.ext.i18n"], autoescape=True)
env.globals["gettext"] = {"Hello %(user)s!": "Hallo %(user)s!"}.__getitem__
env.globals["ngettext"] = lambda s, p, n: {
    "%(count)s user": "%(count)d Benutzer",
    "%(count)s users": "%(count)d Benutzer",
}[s if n == 1 else p]
print(
    env.from_string(
        """\
{% trans %}Hello {{ user }}!{% endtrans %}
{% trans count=users|count -%}
{{ count }} user{% pluralize %}{{ count }} users
{% endtrans %}
"""
    ).render(user="someone", users=[1, 2, 3])
)
