# BDPackages

Welcome to the official repository that stores all custom package installers.

## Installing Packages

Using eval commands, run the following code below, replacing `ADD YOUR PACKAGE HERE` with the package you want to install in lowercase, excluding everything after the dash.

```py
# Add the package you want to install inside of the empty quotes.
PACKAGE = "ADD YOUR PACKAGE HERE"


import base64, requests
r = requests.get(f"https://api.github.com/repos/Dotsian/BDPackages/contents/installers/{PACKAGE}.py")

if r.status_code == requests.codes.ok:
  await ctx.invoke(bot.get_command("eval"), body=base64.b64decode(r.json()["content"]).decode("UTF-8"))
else:
  await ctx.send(f"Failed to fetch package.\n`ERROR CODE: {r.status_code}`")
```

### Loading Packages

Packages will not be loaded upon starting your bot. This is due to how Ballsdex packages are loaded. To solve this, open up the `bot.py` file in `ballsdex/core` and search for a line that starts with `PACKAGES`. At the end of the line, add a comma and quotation marks before the square bracket. 

Add the package name inside the quotation marks, like this `, "battle"`. The line should look similar to this: `PACKAGES = ["battle", "merge", "boss"]`

## Packages

### [Battle - xen64](https://github.com/XEN486/BallsDex-Fork)
The battle package adds battle commands to your Ballsdex bot. The battle system follows a similar approach to the standard Ballsdex battle system. It has seven commands, each with its unique functionality.

### [Boss - moofficial](https://github.com/MoOfficial0000/BossPackageBD)

The boss package adds unique boss commands to your Balsdex bot. It implements a manual boss-battle system that allows admins to interact with it via the provided admin commands. Players can join boss battles and receive a special boss ball when they win.

This package requires a special called `Boss` for the rewards system.

### [Merge - xen64](https://github.com/XEN486/BallsDex-Fork)

The merge package adds commands that allow you to merge countryballs. Merging a countryball will merge its statistics and card art, splitting the card art in half. However, it will only generate a card image, similar to how the `/balls info` command functions.
