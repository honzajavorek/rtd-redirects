import click
import yaml
import requests
from lxml import html


@click.command()
@click.argument('project-name')
@click.argument('redirects-filename', type=click.File())
@click.option('--username', prompt=True,
              help='ReadTheDocs username')
@click.option('--password', prompt=True, hide_input=True,
              help='ReadTheDocs password')
def main(project_name, redirects_filename, username, password):
    session = requests.Session()
    login(session, username, password)

    url = f'https://readthedocs.org/dashboard/{project_name}/redirects/'
    res = session.get(url)
    res.raise_for_status()
    html_tree = html.fromstring(res.content)
    html_tree.make_links_absolute(res.url)

    redirects = yaml.load(redirects_filename.read()).get('redirects')
    for src_path, dst_path in redirects.items():
        remove_existing(session, html_tree, src_path)
        create(session, html_tree, src_path, dst_path)


def login(session, username, password):
    login_url = 'https://readthedocs.org/accounts/login/'
    session.headers.update({'referer': login_url})

    res = session.get(login_url)
    res.raise_for_status()
    html_tree = html.fromstring(res.content)
    html_tree.make_links_absolute(res.url)

    form = html_tree.cssselect('form.login')[0]

    fields = dict(form.fields)
    fields['login'] = username
    fields['password'] = password
    del fields['remember']

    res = session.post(form.get('action'), data=fields)
    res.raise_for_status()

    if 'readthedocs.org/dashboard' not in res.url:
        raise ValueError('Invalid username or password')


def remove_existing(session, html_tree, src_path):
    for li in html_tree.cssselect('li'):
        text = (li.text_content() or '').strip()
        if f'Page Redirect: {src_path} ->' in text:
            original_redirect = text.replace('Page Redirect: ', '')
            print(f'[remove] {original_redirect}')
            form = li.cssselect('form')[0]
            res = session.post(form.get('action'), data=dict(form.fields))
            res.raise_for_status()


def create(session, html_tree, src_path, dst_path):
    print(f'[create] {src_path} -> {dst_path}')
    form = find_redirect_form(html_tree)

    fields = dict(form.fields)
    fields['redirect_type'] = 'page'
    fields['from_url'] = src_path
    fields['to_url'] = dst_path

    res = session.post(form.get('action'), data=fields)
    res.raise_for_status()


def find_redirect_form(html_tree):
    element = html_tree.cssselect('[name="redirect_type"]')[0]
    while element.tag != 'form':
        element = element.getparent()
    return element


if __name__ == '__main__':
    main()
