from jinja2 import (
    Environment,
    FileSystemLoader
)

env = Environment(
    loader=FileSystemLoader(
        "backend/templates"
    )
)


def render_monthly_email(data):

    template = env.get_template(
        "monthly_email.html"
    )

    return template.render(**data)