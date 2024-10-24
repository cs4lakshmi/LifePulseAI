from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.links_heading.text = "Below are a few additional resources."
    self.links_heading.visible = False

    self.help_avail.visible = False
    self.lifeline.visible = False
    
    self.link_1.text = "https://www.988california.org/"
    self.link_1.url = "https://www.988california.org/"
    self.link_1.visible = False

    self.link_2.text = "https://www.heardalliance.org/help-hotlines/"
    self.link_2.url = "https://www.heardalliance.org/help-hotlines/"
    self.link_2.visible = False

    self.link_3.text = "https://dmh.lacounty.gov/resources/suicide-prevention/"
    self.link_3.url = "https://dmh.lacounty.gov/resources/suicide-prevention/"
    self.link_3.visible = False

    self.link_4.text = "https://www.nimh.nih.gov/get-involved/digital-shareables/shareable-resources-on-suicide-prevention"
    self.link_4.url = "https://www.nimh.nih.gov/get-involved/digital-shareables/shareable-resources-on-suicide-prevention"
    self.link_4.visible = False
    
    # Any code you write here will run before the form opens.

  def detect_button_click(self, **event_args):
    
    """This method is called when the button is clicked"""
    suicide_category = anvil.server.call('predict_suicide',
                                          self.user_text.text)
    
    if suicide_category:
      self.output_label.visible = True
      self.output_label.text = suicide_category

      if suicide_category == "Suicide":
        self.help_avail.visible = True
        self.lifeline.visible = True
        self.links_heading.visible = True
        self.link_1.visible = True
        self.link_2.visible = True
        self.link_3.visible = True
        self.link_4.visible = True
      else:
        self.help_avail.visible = False
        self.lifeline.visible = False
        self.links_heading.visible = False
        self.link_1.visible = False
        self.link_2.visible = False
        self.link_3.visible = False
        self.link_4.visible = False

