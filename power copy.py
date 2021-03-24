import subprocess
import docker
import click

from subprocess import Popen, PIPE

client = docker.from_env()
client.containers.run("owasp/zap2docker-stable", detach=True)


# def kill_and_remove(ctr_name):
#     for action in ('kill', 'rm'):
#         p = Popen('docker %s %s' % (action, ctr_name), shell=True,
#                   stdout=PIPE, stderr=PIPE)
#         if p.wait() != 0:
#             raise RuntimeError(p.stderr.read())
@click.command(
    short_help = "Runs ZAP Scan from a Docker image."
)
@click.option(
    '--docker_image',
    required = True,
    help = "Name of the Docker Image."
)

def execute(docker_image, *args):
    container_name = input("Enter Container Name: ")
    p = Popen(
        [

        ]
    )

run: docker run -v $(cd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py \   
           -t http://testhtml5.vulnweb.com -g gen.conf -J test_report.json

# def execute():
#     ctr_name = 'sml/tools:8' # docker image file name
#     p = Popen(['docker', 'run', '-v','/lib/modules:/lib/modules',
#                '--cap-add','NET_ADMIN','--name','o-9000','--restart',
#                'always', ctr_name ,'startup',' --base-port',
#                9000,' --orchestrator-integration-license',
#                ' --orchestrator-integration-license','jaVl7qdgLyxo6WRY5ykUTWNRl7Y8IzJxhRjEUpKCC9Q='
#                ,'--orchestrator-integration-mode'],
#               stdin=PIPE)
#     out = p.stdin.write('Something')

#     if p.wait() == -20:  # Happens on timeout

#         kill_and_remove(ctr_name)

#     return out