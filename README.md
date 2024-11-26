# BDPackages

Welcome to the official repository that stores of all custom package installers.
To install a package, type the following command below:

b.eval

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

Replace `ADD YOUR PACKAGE HERE` with the package you want to install.

## Packages

* battle
* boss
* merge

### [Battle - xen64](https://github.com/XEN486/BallsDex-Fork)

The battle package adds battle commands to your Ballsdex bot. The battle system follows a similiar approach to the standard Ballsdex battle system. It has seven commands, each with its own unique functionality.

### [Boss - moofficial](https://github.com/MoOfficial0000/BossPackageBD)

The boss package adds unique boss commands to your Balsdex bot. It implements a manual boss-battle system that allows admins to interact with it via the provided admin commands. Players will have the ability to join boss battles, allowing them to receive a special boss ball when they win.

This package requires a special named `Boss` for the rewards system to function.

### [Merge - xen64](https://github.com/XEN486/BallsDex-Fork)

The merge package adds commands that allows you to merge countryballs together. Merging a countryball will merge their statistics, along with their card art, splitting the card art in half. It will only generate a card image, similiar to how the `/balls info` command functions.
