import os
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
# import tempfile

TENANT_NAME = os.environ['TENANT_NAME']
USER_NAME = os.environ['USER_NAME']
PASSWORD = os.environ['PASSWORD']

def access():
  site_url = f"https://{TENANT_NAME}.sharepoint.com/teams/ARREIOUStoreOrders"
  ctx = ClientContext(site_url).with_credentials(UserCredential(f"{USER_NAME}", f"{PASSWORD}"))
  web = ctx.web
  ctx.load(web)
  ctx.execute_query()
  print("Web title: {0}".format(web.properties['Title']))

def download_file(ctx_365):
  file_url = 'OrderFilesSAP/StoreOrder_A026_2023-07-29.csv'
  # download_path = os.path.join(tempfile.mkdtemp(), os.path.basename(file_url))
  download_path = 'test.csv'
  with open(download_path, "wb") as local_file:
    file = ctx_365.web.get_file_by_server_relative_url(file_url).download(local_file).execute_query()
  print("[Ok] file has been downloaded into: {0}".format(download_path))

if __name__ == "__main__":
  access()
