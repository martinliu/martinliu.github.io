"""An Azure RM Python Pulumi program"""

import pulumi
from pulumi_azure_native import storage, resources
import os

# 读取配置参数
config = pulumi.Config()
resource_group_name = config.require("resourceGroupName")
location = config.require("location")
storage_account_name = config.require("storageAccountName")
container_name = config.require("containerName")


# 创建资源组
resource_group = resources.ResourceGroup(
    resource_group_name,
    resource_group_name=resource_group_name,
    location=location,
)

# 创建 Azure 存储账户 (Storage Account)
account = storage.StorageAccount(
    storage_account_name,
    resource_group_name=resource_group.name,
    sku={
        "name": storage.SkuName.STANDARD_LRS,
    },
    kind=storage.Kind.STORAGE_V2,
    location=resource_group.location,
    enable_https_traffic_only=True,
    encryption=storage.EncryptionArgs(
        key_source=storage.KeySource.MICROSOFT_STORAGE,
        services=storage.EncryptionServicesArgs(
            blob=storage.EncryptionServiceArgs(
                enabled=True,
            ),
            file=storage.EncryptionServiceArgs(
                enabled=True,
            ),
        ),
    ),
    network_rule_set=storage.NetworkRuleSetArgs(
        bypass=storage.Bypass.AZURE_SERVICES,
        default_action=storage.DefaultAction.ALLOW,
    ),
)

# 启用静态网站
static_website = storage.StorageAccountStaticWebsite(
    "mblogsa-website",
    resource_group_name=resource_group.name,
    account_name=account.name,
    index_document="index.html",
    error404_document="404.html",
)

# 上传静态网站文件

def upload_directory_to_blob(directory_path, container_name):
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            blob_name = os.path.relpath(file_path, directory_path)
            storage.Blob(
                blob_name,
                resource_group_name=resource_group.name,
                account_name=account.name,
                container_name=static_website.container_name,
                source=pulumi.FileAsset(file_path),
                content_type="text/html",
            )

upload_directory_to_blob("../../public", static_website.container_name)


# Export the primary key of the Storage Account
primary_key = (
    pulumi.Output.all(resource_group.name, account.name)
    .apply(
        lambda args: storage.list_storage_account_keys(
            resource_group_name=args[0], account_name=args[1]
        )
    )
    .apply(lambda accountKeys: accountKeys.keys[0].value)
)

pulumi.export("primary_storage_key", primary_key)

pulumi.export("staticEndpoint", account.primary_endpoints.web)