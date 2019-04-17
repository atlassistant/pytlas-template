from pytlas import training, translations, intent, meta

# Hey there o/
# Glad you're taking some times to make a skill for the pytlas assistant!
# Here is all you have to know to make your own skills, let's go!

# Start by defining training data used to trigger your skill.
# Here we are defining the TEMPLATE_SKILL_INTENT with some training data.
# In english:

@training('en')
def en_training(): return """
%[TEMPLATE_SKILL_INTENT]
  launch template skill
  activate template skill
"""

# And in other supported languages, we define the same TEMPLATE_SKILL_INTENT with
# appropriate data:

@training('fr')
def fr_training(): return """
%[TEMPLATE_SKILL_INTENT]
  lance la compétence modèle
  active la compétence modèle
"""

# Let's define some metadata for this skill. This step is optional but enables
# pytlas to list loaded skills with more informations:

@meta()
def template_skill_meta(_): return {
  'name': _('Template skill'),
  'description': _('Tiny template to get you started'),
  'author': 'atlassistant',
  'version': '1.0.0',
  'homepage': 'https://github.com/atlassistant/pytlas-template',
}

# Now, adds some translations for supported languages:

@translations('fr')
def fr_translations(): return {
  'Template skill': 'Compétence modèle',
  'Tiny template to get you started': 'Simple squelette pour créer vos propres compétences',
  'Hello from the template skill': 'Bonjour depuis la compétence modèle',
}

# The final part is your handler registered to be called upon TEMPLATE_SKILL_INTENT
# recognition by the pytlas interpreter.

@intent('TEMPLATE_SKILL_INTENT')
def on_TEMPLATE_SKILL_INTENT(req):

  # Using the pytlas API to communicate with the user: https://pytlas.readthedocs.io/en/latest/writing_skills/handler.html
 
  req.agent.answer(req._('Hello from the template skill'))

  return req.agent.done()
