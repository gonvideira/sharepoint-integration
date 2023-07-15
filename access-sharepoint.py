from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

site_url = "https://{your-tenant-prefix}.sharepoint.com"
ctx = ClientContext(site_url).with_credentials(UserCredential("{username}", "{password}"))
web = ctx.web
ctx.load(web)
ctx.execute_query()
print("Web title: {0}".format(web.properties['Title']))
