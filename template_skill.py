from pytlas import training, translations, intent, meta

@training('en')
def en_training(): return """
%[TEMPLATE_LAUCH_SKILL]
  LAUNCH TEMPLATE SKILL
"""

@training('fr')
def fr_training(): return """
%[TEMPLATE_LAUCH_SKILL]
  LANCE LA COMPETENCE TEMPLATE  
"""

@meta()
def help_meta(_): return {
  'name': _('TEMPLATE_SKILL_NAME'),
  'description': _('TEMPLATE_SKILL_SHORT_DSCRIPTION'),
  'author': 'TEMPLATE_AUTHOR_NAME',
  'version': 'TEMPLATE_VERSION',
  'homepage': 'TEMPLATE_SKILL_GIT_URL',
}

@translations('fr')
def fr_translations(): return {
  'TEMPLATE_ANSWER': 'TEMPLATE_REPONSE',
}

@intent('TEMPLATE_LAUCH_SKILL')
def on_TEMPLATE_LAUCH_SKILL(req):
  req.agent.answer(req._('TEMPLATE_ANSWER'))
  return req.agent.done()