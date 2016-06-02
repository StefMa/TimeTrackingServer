from google.appengine.api import namespace_manager

dev_namespace = "dev"
live_namespace = "live"

namespace = live_namespace

def namespace_manager_default_namespace_for_request():
    return namespace
