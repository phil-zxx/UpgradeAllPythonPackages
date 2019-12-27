import subprocess as sp


def run_command(command):
    p = sp.Popen(command, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    stdout, stderr = p.communicate()
    return stdout.decode()


def upgrade_package(package):
    print('Upgrading \'{}\' ...'.format(package))
    stdout = run_command('pip install --upgrade {}'.format(package))
    print(stdout, '\n-----------------------')


def collect_packages():
    stdout   = run_command('pip list --outdated')
    packages = [p.split(' ')[0] for p in stdout.split('\n')]
    return [p for p in packages if '----' not in p and 'Package' not in p and p != '']


if __name__ == '__main__':
    print('Upgrading all outdated Python packages ...\n')
    packages = collect_packages()

    if len(packages) > 0:
        for package in packages:
            upgrade_package(package)
    else:
        print('Nothing to upgrade')
