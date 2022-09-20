import glob
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('action', choices=['push', 'pull'])
args = parser.parse_args()
print(args)


def do_copy(path):
    if args.action == 'push':
        source = path
        target = os.path.join('..', 'tps-actions', path)
    elif args.action == 'pull':
        source = path
        target = os.path.join('..', 'tps-actions-test', path)
    print(source, target)
    content = open(source, 'r', encoding='utf8').read()

    if args.action == 'push':
        content = content.replace('XiPlus-Test/tps-actions-test/', 'TNFSH-Programming-Contest/tps-actions/')
    elif args.action == 'pull':
        content = content.replace('TNFSH-Programming-Contest/tps-actions/', 'XiPlus-Test/tps-actions-test/')

    os.makedirs(os.path.dirname(target), exist_ok=True)
    open(target, 'w', encoding='utf8').write(content)


if args.action == 'push':
    for path in glob.glob('.github/actions/**/*', recursive=True):
        if os.path.isfile(path):
            do_copy(path)
    for path in glob.glob('.github/workflows/**/*', recursive=True):
        if os.path.isfile(path):
            do_copy(path)
elif args.action == 'pull':
    os.chdir('../tps-actions')
    for path in glob.glob('.github/actions/**/*', recursive=True):
        if os.path.isfile(path):
            do_copy(path)
    for path in glob.glob('.github/workflows/**/*', recursive=True):
        if os.path.isfile(path):
            do_copy(path)
