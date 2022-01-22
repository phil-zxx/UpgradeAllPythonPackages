import subprocess as sp
import sys


def print_python_vesion():
    py_version = '.'.join([str(x) for x in sys.version_info])
    print(f'>> Python version = {py_version}', flush=True)
    print('-' * 41, flush=True)
    

def filter_out_requ_already_satisfied(stdout):
    filtered_lines = [line for line in stdout.split('\n') if 'Requirement already satisfied' not in line]
    return '\n'.join(filtered_lines)


def run_command(command):
    p = sp.Popen(command, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    stdout, stderr = p.communicate()
    return stdout.decode()


def upgrade_pip():
    print('>> Upgrading pip', end=' ... ', flush=True)
    stdout = run_command('python -m pip install --upgrade pip')
    print(stdout + ('-' * 41), flush=True)


def upgrade_packages(packages):
    if len(packages) > 0:
        for i, package in enumerate(packages):
            print(f'>> Upgrading {i+1}/{len(packages)}: \'{package}\'\n' + ('- ' * 21), flush=True)
            stdout = run_command(f'pip install --upgrade {package}')
            print(filter_out_requ_already_satisfied(stdout) + ('-' * 41), flush=True)
    else:
        print('>> Nothing to upgrade', flush=True)

def collect_outdated_packages():
    print('>> Collecting outdated Python packages', end=' ... ', flush=True)
    stdout       = run_command('pip list --outdated')
    packages_all = [p.split(' ')[0] for p in stdout.split('\n')]
    packages     = [p for p in packages_all if '----' not in p and 'Package' not in p and p != '']
    print(f'found {len(packages)}', flush=True)
    return packages


def main():
    print_python_vesion()
    upgrade_pip()
    packages = collect_outdated_packages()
    upgrade_packages(packages)


if __name__ == '__main__':
    main()
