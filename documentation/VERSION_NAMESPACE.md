# Versions and namespaces

## Versions
Currently we have "two" different version: `dev` and the current `"live"`.
### `dev`
The `dev` version is for development.
This is always the latest version and can contains some bugs and not well tested features.
These version got **no** automatic traffic. Only dev clients have to use it.
### `live`
The `live` version is the latest stable and isn't called `live` :)
Instead the latest and well tested version have a increased number for each release.

### Example:
The current release is `1`. That means we have `dev` and `1`.
In the development we have to push always to `dev`.
When we want to release a new version and decide to mark `dev` as stable we change the version from `dev` to `2`.

> **Note:** Before we get life we have to change the `namespace` too. More about that later.

After uploading to the Cloud Backend we have to set the new version (`2`) to 100% traffic. Now every user have access to version `2`!

The version `1` should not deleted. We can use them for a rollback for example.

## Namespace
Currently we have two namespaces: `dev` and `live`.
And yes, this time I mean `live` ;)
### `dev`
This namespace is only for development.
All data are persistent (like the `live` version) but because it is in development its never guaranteed that they will be exist on the next time.
You can delete or change data like you want.
### `live`
The `live` namespace is the latest stable namespace.
You are not allowed to delete or change data from this datastore!

## FAQ
> **Q:** We have different versions. Why a namespace too?

> **A:** If we don't change the namespace in the dev-environment the datastore gets mixed. Every new user (or timetrack) goes into the same table. <br>
To split the datastore we have to set the namespace.

> **Q:** So I need to change both version and namespace with a new release?

> **A:** You got it! You have to increase the version and change the namespace from `dev` to `live`.
