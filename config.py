import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = 'HPHo@3Y4S!q5Pzf'

SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:root@localhost/vk_sms'

# CSRF_ENABLED = True
# CSRF_SESSION_KEY = "somethingimpossibletoguess"

# RECAPTCHA_USE_SSL = False
# RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
# RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
# RECAPTCHA_OPTIONS = {'theme': 'white'}
