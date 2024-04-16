import subprocess

commands = [
    'python /home/quanghuy20nd/web_app/blog/backend/django/manage.py runserver',
    'python /home/quanghuy20nd/web_app/blog/backend/flask/app.py',
    'python /home/quanghuy20nd/web_app/blog/backend/django/consumer.py',
]

processes = []

for command in commands:
    processes.append(subprocess.Popen(command, shell=True))

for process in processes:
    process.wait()
