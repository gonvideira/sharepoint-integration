import os
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

TENANT_NAME = os.environ['TENANT_NAME']
USER_NAME = os.environ['USER_NAME']
PASSWORD = os.environ['PASSWORD']

def access():
  site_url = f"https://{TENANT_NAME}.sharepoint.com/teams/ARREIOUStoreOrders"
  ctx = ClientContext(site_url).with_credentials(UserCredential(f"{USER_NAME}", f"{PASSWORD}"))
  web = ctx.web
  ctx.load(web)
  ctx.execute_query()
  print("Web title: {0}\n".format(web.properties['Title']))
  return ctx

def get_files(ctx_365):
  """Function to get all files in folder"""
  lib_title = "OrderFilesSAP"
  lib = ctx_365.web.lists.get_by_title(lib_title)
  recent_items = lib.items.order_by("Created desc").select(["ID", "FileRef"]).get().execute_query()
  for item in recent_items:  # type: ListItem
    file_url = item.properties.get("FileRef")
    file_name = os.path.basename(file_url)
    download_path = 'outputs/'
    print(f'File URL: {file_url}\n')
    print(f'File Name: {file_name}\n')
    
    #with open(download_path, "wb") as local_file:
    #    item.file.download(local_file).execute_query()
    #print("[Ok] file has been downloaded into: {0}".format(download_path))
  return None

def download_file(ctx_365):
  file_url = 'OrderFilesSAP/StoreOrder_A026_2023-07-29.csv'
  download_path = 'outputs/test.csv'
  with open(download_path, "wb") as local_file:
    file = ctx_365.web.get_file_by_server_relative_url(file_url).download(local_file).execute_query()
  print("[Ok] file has been downloaded into: {0}".format(download_path))

if __name__ == "__main__":
  ctx = access()
  get_files(ctx)
