import os
import re
import subprocess

def setup_install():
  print('installing pip and virtualenv so we can give django its own version of python')
  os.system('yum -y install python-pip && pip install --upgrade pip')
  os.system('pip install virtualenv')
  os.chdir('/opt')
  os.mkdir('/opt/django')
  os.chdir('/opt/django')
  os.system('virutalenv django-env')
  os.system('chown -R londuso /opt/django') # We're using shell, because the python builtin chown doesn't work as well
  
def django_install():
  print('activating virtualenv and installing django after pre-requirements have been met') # You must activate the virtualenv shell every time
                                                                                            # perform a command in order for it to work from python
  os.system('source /opt/django/django-env/bin/activate && pip install django')  # confirm install and start a django project
  os.chdir('/opt/django')
  os.system('source /opt/django/django-env/bin/activate ' + \
       '&& django-admin --version ' + \
       '&& django-admin startproject project1')
  os. system('adduser -M django3')
  os. system('chown -R django3 /opt/django')
  os. system('usermod -L django3')
 
 
def django_start():
  print('starting django')
  os.system('chown -R londuso /opt/django')
  os.chdir('opt/django/project1')
  os.system('source /opt/django/django-env/bin/activate ' + \
      '&& python manage.py migrate')
  os.system('source /opt/django/django-env/bin/activate && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(\'admin\', \'admin@newproject.com\', \P@$$w0rd1\')" | python manage.py shell')
  outputwithnewline = subprocess.check_output('curl -s checkip.dyndns.org | sed -e \'s/.*Current IP Address: //\' -e \'s/<.*$//\' ', shell=True)
  print outputwithnewline
  output = outputwithnewline.replace("\n", "")
  old_string = "ALLOWED_HOSTS = []"
  new_string = 'ALLOWED_HOSTS = [\'{}\']'.format(output)
  print (new_string)
  print (old_string)
    
  with open('project1/settings.py') as f:
    newText=f.read().replace(old_string, new_string)
  with open('project1/settings.py', "w") as f:
    f.write(newText)
      
    os.system('sudo -u londuso sh -c "source /opt/django/django-env/bin/activate && python manage.py runserver 0.0.0.0:8000&"')
    
setup_install()
django_install()
django_start()

adduser -M django3
chown -R django3 /opt/django
usermod -L django3

