from sure import expect
from pytlas.testing import create_skill_agent
import os

class Test_TEMPLATE_SKILL:

  def test_TEMPLATE_LAUNCH_SKILL(self):
    agent = create_skill_agent(os.path.dirname(__file__), lang='en')
    agent.parse('LAUNCH TEMPLATE SKILL')
    call = agent.model.on_answer.get_call()
    expect(call.text).to.equal('TEMPLATE_ANSWER')
