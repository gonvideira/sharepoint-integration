import os
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

TENANT_NAME = os.environ['TENANT_NAME']
USER_NAME = os.environ['USER_NAME']
PASSWORD = os.environ['PASSWORD']

def access():
    """Function that accesses Sharepoint"""
    site_url = f"https://{TENANT_NAME}.sharepoint.com/teams/ARREIOUStoreOrders"
    ctx = ClientContext(site_url).with_credentials(UserCredential(f"{USER_NAME}", f"{PASSWORD}"))
    web = ctx.web
    ctx.load(web)
    ctx.execute_query()
    print("Web title: {0}\n".format(web.properties['Title']))
    return ctx

def get_files(client_context):
    """Function to get all files in folder"""
    lib_title = "OrderFilesSAP"
    lib = client_context.web.lists.get_by_title(lib_title)
    items_list = lib.items.order_by("Created desc").select(["ID", "FileRef"]).get().execute_query()
    for item in items_list:  # type: ListItem
        file_url = item.properties.get("FileRef")
        file_name = os.path.basename(file_url)
        download_file(client_context, file_url)
  return print('All files downloaded!')

def download_file(ctx, file_url):
    """Function that downloads file bu url"""
    file_name = os.path.basename(file_url)
    download_folder = 'outputs/'
    download_path = download_folder + file_name
    with open(download_path, "wb") as local_file:
        file = ctx.web.get_file_by_server_relative_url(file_url).download(local_file).execute_query()
    print(f'[Ok] file has been downloaded into: {download_path}\n')

if __name__ == "__main__":
    ctx = access()
    get_files(ctx)
