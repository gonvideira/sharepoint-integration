import os
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

TENANT_NAME = os.environ['secrets.TENANT_NAME']
USER_NAME = os.environ['secrets.USER_NAME']
PASSWORD = os.environ['secrets.PASSWORD']

def access():
  site_url = f"https://{TENANT_NAME}.sharepoint.com"
  ctx = ClientContext(site_url).with_credentials(UserCredential(f"{USER_NAME}", f"{PASSWORD}"))
  web = ctx.web
  ctx.load(web)
  ctx.execute_query()
  print("Web title: {0}".format(web.properties['Title']))

if __name__ == "__main__":
  access()
