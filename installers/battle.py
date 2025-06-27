import os
import shutil
import base64
import requests


async def load_extension(package):
    try:
        await bot.reload_extension(package)
    except commands.ExtensionNotLoaded:
        await bot.load_extension(package)
    except Exception:
        pass

async def install_package(path, link, files):
    path = f"ballsdex/packages/{path}"

    if os.path.exists(path):
        await ctx.send("Uninstalling current version...")
        shutil.rmtree(path)

    await ctx.send("Starting installation process...")
    os.mkdir(path)

    for index, file in enumerate(files, start=1):
        request = requests.get(f"{link}/{file}")

        if request.status_code != requests.codes.ok:
            await ctx.send(f"Failed to install {file}. `({request.status_code})`")
            break

        with open(f"{path}/{file}", "w") as opened_file:
            content = base64.b64decode(request.json()["content"])
            opened_file.write(content.decode("UTF-8"))

        await ctx.send(f"Installed `{file}` ({index}/{len(files)})")

    await load_extension(path.replace("/", "."))
    await ctx.send("Finished installing everything!")


await install_package( # type: ignore
    "battle",
    "https://api.github.com/repos/XEN486/BallsDex-Packages/contents/packages/battle",
    [
        "__init__.py",
        "cog.py",
        "xe_battle_lib.py",
    ]
)
