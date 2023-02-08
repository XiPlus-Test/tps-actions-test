import json
import os

requests = os.environ.get('REQUESTS')
problems = json.loads(os.environ.get('PROBLEMS'))

print('requests:', requests)

result = []
for pro in problems:
    if pro in requests:
        result.append(pro)

print('result:', result)
os.environ['GITHUB_OUTPUT'] = os.environ.get('GITHUB_OUTPUT', '') \
    + '\nproblemsjson={}'.format(json.dumps(result)) \
    + '\nproblems={}'.format(' '.join(result)) \
    + '\nlastproblem={}'.format(problems[-1])
